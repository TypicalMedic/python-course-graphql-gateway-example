from typing import Optional

import graphene
from graphene import Int, Schema
from graphql import ResolveInfo
from promise import Promise

from context import DATA_LOADER_COUNTRIES, DATA_LOADER_NEWS
from models.countries import CountryModel
from models.places import PlaceModel
from services.places import PlacesService


class NewsSource(graphene.ObjectType):
    """
    Тип объекта источника новости.
    """

    id = graphene.String()
    name = graphene.String()


class News(graphene.ObjectType):
    """
    Тип объекта новости.
    """

    source = graphene.Field(NewsSource)
    author = graphene.String()
    title = graphene.String()
    description = graphene.String()
    url = graphene.String()
    url_to_image = graphene.String()
    published_at = graphene.String()
    content = graphene.String()


class Country(graphene.ObjectType):
    """
    Тип объекта страны.
    """

    name = graphene.String()
    alpha2code = graphene.String()
    alpha3code = graphene.String()
    capital = graphene.String()
    region = graphene.String()
    subregion = graphene.String()
    population = graphene.Int()
    latitude = graphene.Float()
    longitude = graphene.Float()
    demonym = graphene.String()
    area = graphene.Float()
    numeric_code = graphene.Int()
    flag = graphene.String()
    currencies = graphene.List(graphene.String)
    languages = graphene.List(graphene.String)
    news = graphene.List(News)

    @staticmethod
    def resolve_news(parent: CountryModel, info: ResolveInfo) -> Promise:
        """
        Получение связанной информации о новостях для объектов стран.

        :param parent: Объект страны.
        :param info: Объект с метаинформацией и данных о контексте запроса.
        :return: Новости
        """

        if info.context:
            dataloaders = info.context["dataloaders"]

            return dataloaders[DATA_LOADER_NEWS].load(str(parent.alpha2code))

        return Promise.resolve([])


class Place(graphene.ObjectType):
    """
    Тип объекта любимого места.
    """

    latitude = graphene.Float()
    longitude = graphene.Float()
    description = graphene.String()
    city = graphene.String()
    locality = graphene.String()
    country = graphene.Field(Country)

    @staticmethod
    def resolve_country(parent: PlaceModel, info: ResolveInfo) -> Promise:
        """
        Получение связанной информации о странах для объектов любимых мест.

        :param parent: Объект любимого места.
        :param info: Объект с метаинформацией и данных о контексте запроса.
        :return: Страны
        """

        if info.context:
            dataloaders = info.context["dataloaders"]

            return dataloaders[DATA_LOADER_COUNTRIES].load(str(parent.country))

        return Promise.resolve([])


class Query(graphene.ObjectType):
    """
    Общий тип для запроса получения данных.
    """

    places = graphene.List(Place)
    place = graphene.Field(Place, id=Int())

    @staticmethod
    def resolve_places(
        parent: Optional[dict], info: ResolveInfo  # pylint: disable=unused-argument
    ) -> list[PlaceModel]:
        return PlacesService().get_places()

    @staticmethod
    def resolve_place(
        parent: Optional[dict],
        info: ResolveInfo,
        placeid: int,  # pylint: disable=unused-argument
    ) -> PlaceModel:
        return PlacesService().get_place(placeid)


schema = Schema(query=Query)
