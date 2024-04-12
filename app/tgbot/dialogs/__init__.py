from aiogram import Dispatcher
from aiogram_dialog import setup_dialogs

from app.tgbot.dialogs import menu, words, info, create_word


def setup(dp: Dispatcher):
    setup_dialogs(dp)
    menu.setup(dp)
    create_word.setup(dp)
    info.setup(dp)
    words.setup(dp)
    # upload.setup(dp)
    # folder.setup(dp)
    # files.setup(dp)
    # choose_folder.setup(dp)
    # media.setup(dp)
