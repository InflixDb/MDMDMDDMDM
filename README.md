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


   Deployment on Render
   
---

### **Deploying on Render**

1. **Create a New Web Service**:
   - Go to [Render](https://render.com/) and log in.
   - Click on **New** and select **Web Service**.
   - Connect your GitHub account and select the `telegram-temp-invite-bot` repository.

2. **Configure Build and Start Commands**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python main.py`

3. **Set Environment Variables**:
   - `BOT_TOKEN`: Your Telegram bot token.
   - `API_ID`: Your Telegram API ID.
   - `API_HASH`: Your Telegram API hash.
   - `MONGO_URI`: Your MongoDB connection string.
   - `OWNER_ID`: Your Telegram user ID.

4. **Deploy**:
   - Click **Create Web Service** to start the deployment process.

---

#Don't Forget To Star The Repo 🥶🥶🥶


   
