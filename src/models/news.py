from typing import Optional

from pydantic import BaseModel, Field

from models.mixins import TimeStampMixin


class SourceModel(TimeStampMixin, BaseModel):
    """
    Модель для описания источника новости.
    """

    id: Optional[str] = Field(title="Идентификатор")
    name: Optional[str] = Field(title="Название")


class NewsModel(TimeStampMixin, BaseModel):
    """
    Модель для описания новости.
    """

    source: SourceModel = Field(title="Источник")
    author: Optional[str] = Field(title="Автор")
    title: Optional[str] = Field(title="Название")
    description: Optional[str] = Field(title="Описание")
    url: Optional[str] = Field(title="Ссылка на новость")
    url_to_image: Optional[str] = Field(title="Ссылка на изображение")
    published_at: Optional[str] = Field(title="Время публикации")
    content: Optional[str] = Field(title="Содержимое")