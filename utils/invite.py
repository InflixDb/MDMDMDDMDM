from datetime import datetime, timedelta

async def generate_invite(client, channel_id):
    return await client.create_chat_invite_link(
        chat_id=channel_id,
        expire_date=datetime.utcnow() + timedelta(minutes=5),
        creates_join_request=True
    )
