from pydantic import parse_obj_as
from sqlalchemy import insert, select, delete, func, update
from sqlalchemy.ext.asyncio import AsyncSession

from app import dto
from app.infrastructure.database.dao.rdb import BaseDAO
from app.infrastructure.database.models import Word


class WordDAO(BaseDAO[Word]):
    def __init__(self, session: AsyncSession):
        self.word_sort_columns = {
            dto.WordFilterTypes.ALL: (Word.is_checked == True)
            | (Word.is_checked == False),
            dto.WordFilterTypes.CHECKED: Word.is_checked == True,
            dto.WordFilterTypes.UNCHECKED: Word.is_checked == False,
        }
        super().__init__(Word, session)

    async def add_word(self, word: str) -> dto.Word:
        result = await self.session.execute(
            insert(Word).values(word=word).returning(Word)
        )
        await self.session.commit()
        return dto.Word.from_orm(result.scalar())

    async def set_checked(self, word_id: int, is_checked: bool) -> dto.Word:
        result = await self.session.execute(
            update(Word)
            .where(Word.id == word_id)
            .values(is_checked=is_checked)
            .returning(Word)
        )
        await self.session.commit()
        return dto.Word.from_orm(result.scalar())

    async def get_word(self, word: str) -> dto.Word:
        result = await self.session.execute(
            select(Word).where(Word.word == word).order_by(Word.created_at.desc())
        )
        word = result.scalar()
        if word is not None:
            return dto.Word.from_orm(word)

    async def get_all_words(self, is_checked: bool) -> list[dto.Word]:
        result = await self.session.execute(
            select(Word).where(Word.is_checked == is_checked)
        )
        return parse_obj_as(list[dto.Word], result.scalars().all())

    async def get_words(
        self, limit: int, page: int, type_: dto.WordFilterTypes
    ) -> list[dto.Word]:
        result = await self.session.execute(
            select(Word)
            .limit(limit)
            .offset((page - 1) * limit)
            .where(self.word_sort_columns[type_])
            .order_by(Word.created_at.desc())
        )
        return parse_obj_as(list[dto.Word], result.scalars().all())

    async def get_words_count(self, type_: dto.WordFilterTypes) -> int:
        result = await self.session.execute(
            select(func.count()).where(self.word_sort_columns[type_]).select_from(Word)
        )
        return result.scalar()

    async def delete_word_by_id(self, word_id: int) -> None:
        await self.session.execute(delete(Word).where(Word.id == word_id))
        await self.session.commit()
