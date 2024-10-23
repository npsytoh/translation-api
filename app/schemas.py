from enum import Enum

from pydantic import BaseModel


class LanguageEnum(str, Enum):
    Japanese = "JA"
    English = "EN"
    Korean = "KO"
    Chinese = "ZH"
    French = "FR"
    Italian = "IT"
    Russian = "RU"
    German = "DE"


class UsageBase(BaseModel):
    count: int
    limit: int


class TranslateBase(BaseModel):
    text: str


class TranslateParams(TranslateBase):
    source_lang: LanguageEnum
    target_lang: LanguageEnum


class TranslateResponse(TranslateBase):
    usage: UsageBase
