# Telegram Temporary Invite Bot

A Telegram bot that generates temporary (5-minute expiry) invite links for private channels. Features include channel registration, user tracking, and broadcasting messages.

## Features

- Temporary Invite Links
- Channel Registration
- User Tracking
- Broadcast Messages
- Render Deployment Support

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/telegram-temp-invite-bot.git
   cd telegram-temp-invite-bot

2 . Install dependencies:
pip install -r requirements.txt

3. Configure environment variables in a .env file:
4. BOT_TOKEN=your_telegram_bot_token
API_ID=your_telegram_api_id
API_HASH=your_telegram_api_hash
MONGO_URI=your_mongodb_connection_string
OWNER_ID=your_telegram_user_id

4. Run the bot:
   python main.py
