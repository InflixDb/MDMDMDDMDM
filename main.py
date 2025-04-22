from pyrogram import Client
from handlers import user, admin
from config import BOT_TOKEN, API_ID, API_HASH

app = Client("bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# Register the user and admin handlers
user.register_handlers(app)
admin.register_handlers(app)

# Start the bot
app.run()
