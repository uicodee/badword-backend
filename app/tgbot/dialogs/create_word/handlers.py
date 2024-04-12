from aiogram import types
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.input import MessageInput

from app.infrastructure.database.dao import HolderDao
from app.tgbot.states import MenuSG


async def create_word(
    message: types.Message,
    message_input: MessageInput,
    manager: DialogManager,
):
    dao: HolderDao = manager.middleware_data["dao"]
    if await dao.word.get_word(word=message.text) is not None:
        await message.answer(
            text="🚫 Bu so'z allaqachon ma'lumotlar omboriga qo'shilgan, iltimos boshqa so'z kiriting"
        )
        manager.show_mode = ShowMode.EDIT
        await manager.back()
    else:
        await dao.word.add_word(word=message.text)
        await message.answer(
            text="✅ So'z yaratildi"
        )
        await manager.done()
        await manager.start(state=MenuSG.menu)
