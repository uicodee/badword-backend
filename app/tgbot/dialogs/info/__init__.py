from aiogram import Dispatcher

from .dialogs import dialog


def setup(dp: Dispatcher):
    dp.include_router(dialog)
