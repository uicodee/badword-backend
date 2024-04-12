from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Row, Start
from aiogram_dialog.widgets.markup.reply_keyboard import ReplyKeyboardFactory
from aiogram_dialog.widgets.text import Const, Format

from app.tgbot.states import MenuSG, WordsSG, CreateWordSG, InfoSG

dialog = Dialog(
    Window(
        Const("Asosiy menu\n"),
        Row(
            Start(
                Const("➕ So'z yaratish"),
                id="create_word",
                state=CreateWordSG.create_word,
            ),
        ),
        Row(
            Start(Const("🗒 So'zlar"), id="words", state=WordsSG.words),
            Start(
                Const("ℹ️ Loyiha va muallif haqida"),
                id="info",
                state=InfoSG.info,
            ),
        ),
        markup_factory=ReplyKeyboardFactory(
            input_field_placeholder=Format("@{event.from_user.username}, tanlang"),
            resize_keyboard=True,
        ),
        state=MenuSG.menu,
    ),
)
