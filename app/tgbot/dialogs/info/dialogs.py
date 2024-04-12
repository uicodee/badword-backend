from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import (
    Start,
)
from aiogram_dialog.widgets.text import Const

from app.tgbot.states import InfoSG, MenuSG

dialog = Dialog(
    Window(
        Const(
            "<b>Loyixa:</b>\n\n"
            "<b>Muallif:</b> @uicode\n"
            "<b>Frontend:</b> ReactJS, shadcn/ui, ReactQuery, Axios, orval\n"
            "<b>Backend:</b> FastAPI, PostgreSQL, SQLAlchemy, aiogram, aiogram-dialog"
        ),
        Start(Const("⬅️ Ortga"), id="back", state=MenuSG.menu),
        state=InfoSG.info,
    )
)
