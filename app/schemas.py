from enum import Enum

from pydantic import BaseModel


class LanguagesEnum(str, Enum):
    JA = "JA"
    EN = "EN"
    KO = "KO"
    ZH = "ZH"
    FR = "FR"
    IT = "IT"
    RU = "RU"
    DE = "DE"


class UsageResponse(BaseModel):
    count: int
    limit: int


class TranslateResponse(BaseModel):
    text: str
    usage: UsageResponse
