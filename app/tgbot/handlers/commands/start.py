from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from app.tgbot.states import MenuSG

router = Router()


@router.message(CommandStart())
async def on_cmd_start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MenuSG.menu, mode=StartMode.RESET_STACK)
