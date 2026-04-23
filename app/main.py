import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

router = Router(name=__name__)
load_dotenv()


@router.message(Command("start"))
async def start(message: Message) -> None:
    await message.answer(
        "TG Toolkit Bot ready.\nUse /help to see available technical commands."
    )


@router.message(Command("help"))
async def help_command(message: Message) -> None:
    await message.answer(
        "Available commands:\n"
        "/get_chat_id - current chat ID\n"
        "/get_user_id - your Telegram user ID\n"
        "/get_my_id - alias for /get_user_id\n"
        "/chat_info - technical chat metadata"
    )


@router.message(Command("get_chat_id"))
async def get_chat_id(message: Message) -> None:
    await message.answer(f"chat_id: {message.chat.id}")


@router.message(Command("get_user_id", "get_my_id"))
async def get_user_id(message: Message) -> None:
    if not message.from_user:
        await message.answer("Unable to resolve user ID for this update.")
        return

    await message.answer(f"user_id: {message.from_user.id}")


@router.message(Command("chat_info"))
async def chat_info(message: Message) -> None:
    from_user = message.from_user
    username = f"@{from_user.username}" if from_user and from_user.username else "-"
    full_name = from_user.full_name if from_user else "-"

    lines = [
        "chat_info",
        f"chat_id: {message.chat.id}",
        f"chat_type: {message.chat.type}",
        f"user_id: {from_user.id if from_user else '-'}",
        f"username: {username}",
        f"full_name: {full_name}",
    ]

    await message.answer("\n".join(lines))


async def main() -> None:
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN is not set")

    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
