from app.infrastructure.database.dao import HolderDao


async def words_getter(dao: HolderDao, **kwargs):
    words = await dao.word.get_all_checked_words(is_checked=True)
    words_list = ""
    for index, word in enumerate(words, start=1):
        words_list += f"{index}. {word.word}\n"
    return {
        "words": words_list,
        "filter_types": [
            ("Barchasi", "all"),
            ("Tekshirilgan", "checked"),
            ("Tekshirilmagan", "unchecked"),
        ],
    }
