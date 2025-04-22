from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from database import users_col, channels_col, requests_col
from utils.invite import generate_invite
from datetime import datetime, timedelta
import secrets

def register_handlers(app):
    @app.on_message(filters.private & filters.text)
    async def keyword_handler(client, message: Message):
        keyword = message.text.strip().lower()
        # Check if the keyword corresponds to a registered channel
        channel = channels_col.find_one({"keyword": keyword})
        if not channel:
            return await message.reply("No such channel registered.")
        
        # Create a temporary request link
        code = "req_" + secrets.token_urlsafe(8)
        requests_col.insert_one({
            "code": code,
            "channel_id": channel["channel_id"],
            "user_id": message.from_user.id,
            "expires_at": datetime.utcnow() + timedelta(minutes=5)
        })

        link = f"https://t.me/{client.me.username}?start={code}"
        await message.reply(f"Click the button below to get access:",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Here is your link", url=link)]]))

    @app.on_message(filters.command("start") & filters.private)
    async def start(client, message):
        args = message.text.split()
        if len(args) == 2 and args[1].startswith("req_"):
            code = args[1]
            data = requests_col.find_one({"code": code})
            if not data or data["expires_at"] < datetime.utcnow():
                return await message.reply("Link expired or invalid.")
            
            # Generate the invite link and send it to the user
            invite = await generate_invite(client, data["channel_id"])
            await message.reply(
                "Here is your invite link:",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Join Channel", url=invite.invite_link)]])
            )
        else:
            await message.reply("Send a keyword to get access to a channel.")

        # Track user
        users_col.update_one({"user_id": message.from_user.id}, {"$set": {"user_id": message.from_user.id}}, upsert=True)
