from pyrogram import filters
from pyrogram.types import Message
from database import channels_col, users_col
from config import OWNER_ID

def register_handlers(app):
    @app.on_message(filters.command("addchannel") & filters.user(OWNER_ID))
    async def add_channel(client, message: Message):
        try:
            _, keyword = message.text.split(maxsplit=1)
            chat_id = message.reply_to_message.forward_from_chat.id
            channels_col.update_one(
                {"keyword": keyword.lower()},
                {"$set": {"channel_id": chat_id, "keyword": keyword.lower()}},
                upsert=True
            )
            await message.reply("Channel added successfully.")
        except:
            await message.reply("Reply to a forwarded message from the channel with /addchannel <keyword>")

    @app.on_message(filters.command("users") & filters.user(OWNER_ID))
    async def users_count(client, message: Message):
        count = users_col.count_documents({})
        await message.reply(f"Total users: {count}")

    @app.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
    async def broadcast(client, message: Message):
        if not message.reply_to_message:
            return await message.reply("Reply to a message to broadcast.")
        users = users_col.find()
        for user in users:
            try:
                await client.send_message(user["user_id"], message.reply_to_message.text)
            except:
                pass
        await message.reply("Broadcast complete.")
