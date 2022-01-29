from pyrogram.types import Message


async def admin_check(message: Message) -> bool:
    if not message.from_user:
        return False

    if message.chat.type not in ["supergroup", "channel"]:
        return False

    if message.from_user.id in [
        777000,  
        1087968824  
    ]:
        return True

    client = message._client
    chat_id = message.chat.id
    user_id = message.from_user.id

    check_status = await client.get_chat_member(
        chat_id=chat_id,
        user_id=user_id
    )
    admin_strings = [
        "creator",
        "administrator"
    ]
    if check_status.status not in admin_strings:
        return False
    else:
        return True
