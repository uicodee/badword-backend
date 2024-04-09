from math import ceil

from fastapi import APIRouter, Query, Depends, Path, HTTPException, status
from app import dto
from app.api import schems
from app.api.dependencies import dao_provider, get_user
from app.dto import WordFilterTypes
from app.infrastructure.database.dao import HolderDao

router = APIRouter(prefix="/word")


@router.get(
    path="/json",
    description="Get all words",
    summary="Get all words in JSON format",
    response_model=list[dto.Word],
)
async def get_all_words(dao: HolderDao = Depends(dao_provider)) -> list[dto.Word]:
    return await dao.word.get_all_words(is_checked=True)


@router.get(
    path="/all",
    description="Get all words",
    summary="Get all words by page, limit and type",
    response_model=dto.PaginatedWord,
)
async def get_words(
    page: int = Query(default=1, gt=0),
    limit: int = Query(default=10, gt=0),
    type_: WordFilterTypes = Query(alias="type", default=WordFilterTypes.ALL),
    dao: HolderDao = Depends(dao_provider),
) -> dto.PaginatedWord:
    words = await dao.word.get_words(page=page, limit=limit, type_=type_)
    words_count = await dao.word.get_words_count(type_=type_)
    pages = ceil(words_count / limit)
    return dto.PaginatedWord(words=words, total_items=words_count, pages=pages)


@router.get(
    path="/{word}",
    description="Get word by word",
    summary="Get word by word",
    response_model=dto.Word,
)
async def get_word(
    word: str = Path(), dao: HolderDao = Depends(dao_provider)
) -> dto.Word:
    return await dao.word.get_word(word=word)


@router.post(
    path="/new",
    description="Add word",
    summary="Add new word",
    response_model=dto.Word,
)
async def add_word(
    word: schems.Word, dao: HolderDao = Depends(dao_provider)
) -> dto.Word:
    if await dao.word.get_word(word=word.word) is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Word already exists",
        )
    return await dao.word.add_word(word=word.word)


@router.put(
    path="/set-checked",
    description="Set word checked or unchecked",
    summary="Set word checked or unchecked status",
    response_model=dto.Word,
    dependencies=[Depends(get_user)],
)
async def set_checked(
    word: schems.UpdateWord,
    dao: HolderDao = Depends(dao_provider),
) -> dto.Word:
    return await dao.word.set_checked(word_id=word.word_id, is_checked=word.is_checked)


@router.delete(
    path="/delete",
    description="Delete word",
    summary="Delete word by word id",
    dependencies=[Depends(get_user)],
)
async def delete_word(
    word_id: int = Query(gt=0), dao: HolderDao = Depends(dao_provider)
):
    return await dao.word.delete_word_by_id(word_id=word_id)
