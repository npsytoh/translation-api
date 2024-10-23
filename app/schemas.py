from enum import Enum

from pydantic import BaseModel


class LanguageEnum(str, Enum):
    JA = "JA"
    EN = "EN"
    KO = "KO"
    ZH = "ZH"
    FR = "FR"
    IT = "IT"
    RU = "RU"
    DE = "DE"


class TranslateParams(BaseModel):
    text: str
    source_lang: LanguageEnum
    target_lang: LanguageEnum


class UsageBase(BaseModel):
    count: int
    limit: int


class TranslateResponse(BaseModel):
    text: str
    usage: UsageBase
