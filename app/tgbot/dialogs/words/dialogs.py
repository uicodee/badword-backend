from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import (
    Start,
    NumberedPager,
)
from aiogram_dialog.widgets.text import Const, Format, ScrollingText

from app.tgbot.states import WordsSG, MenuSG
from .getters import words_getter


dialog = Dialog(
    Window(
        Const("<b>So'zlar ro'yxati:</b>\n"),
        ScrollingText(
            text=Format("{words}"),
            id="text_scroll",
            page_size=1000,
        ),
        NumberedPager(
            scroll="text_scroll",
        ),
        Start(Const("⬅️ Ortga"), id="back", state=MenuSG.menu),
        state=WordsSG.words,
        getter=words_getter,
    )
)
