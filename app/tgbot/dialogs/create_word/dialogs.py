from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Back, Start
from aiogram_dialog.widgets.text import Const

from .handlers import create_word

from app.tgbot.states import CreateWordSG, MenuSG

dialog = Dialog(
    Window(
        Const("Yangi so'zni kiriting: "),
        Start(Const("⬅️ Ortga"), id="back", state=MenuSG.menu),
        MessageInput(create_word),
        state=CreateWordSG.create_word,
    ),
)