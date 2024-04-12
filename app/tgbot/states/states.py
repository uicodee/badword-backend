from aiogram.fsm.state import StatesGroup, State


class MenuSG(StatesGroup):

    menu = State()


class WordsSG(StatesGroup):

    words = State()


class CreateWordSG(StatesGroup):

    create_word = State()


class InfoSG(StatesGroup):

    info = State()


class AdminSG(StatesGroup):

    admin = State()
