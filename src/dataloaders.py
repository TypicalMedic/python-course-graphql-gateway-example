from promise import Promise
from promise.dataloader import DataLoader

from services.news import NewsService
from services.countries import CountriesService


class CountryLoader(DataLoader):
    """
    Загрузчик данных о странах.
    """

    def batch_load_fn(  # pylint: disable=method-hidden
        self, alpha2codes: list[str]
    ) -> Promise:
        """
        Функция для загрузки связанных данных по переданному множеству значений.

        :param alpha2codes: Список ISO Alpha2-кодов стран
        :return: список информации стран по ISO Alpha2-коду
        """

        countries = CountriesService().get_countries()
        countries_map = {country.alpha2code: country for country in countries}

        # формирование результата с сохранением порядка из alpha2codes
        return Promise.resolve([countries_map.get(code) for code in alpha2codes])

class NewsLoader(DataLoader):
    """
    Загрузчик данных о новостях.
    """

    def batch_load_fn(  # pylint: disable=method-hidden
        self, alpha2codes: list[str]
    ) -> Promise:
        """
        Функция для загрузки связанных данных по переданному множеству значений.

        :param alpha2codes: Список ISO Alpha2-кодов стран
        :return: список новостей стран по ISO Alpha2-коду
        """

        news = NewsService().get_news()        
        # формирование результата с сохранением порядка из alpha2codes
        return Promise.resolve([news.get(code) for code in alpha2codes])
