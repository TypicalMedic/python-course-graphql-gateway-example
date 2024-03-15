import json
import os

from models.news import NewsModel, SourceModel


class NewsService:
    """
    Сервис для работы с новостями стран.
    """

    def get_news(self) -> dict:
        """
        Получение списка новостей всех стран.

        :return:
        """

        result = {}
        for filename in os.listdir("fixtures/news"):
            with open(os.path.join("fixtures/news", filename), 'r') as file: 
                if data := json.load(file):
                    articles = data.get("articles", [])
                    result[filename.split(".json")[0].upper()] = [NewsModel(
                            source=SourceModel(
                                id=news.get("source").get("id"),
                                name=news.get("source").get("name"),
                            ),
                            author=news.get("author"),
                            title=news.get("title"),
                            description=news.get("description"),
                            url=news.get("url"),
                            url_to_image=news.get("urlToImage"),
                            published_at=news.get("publishedAt"),
                            content=news.get("content")
                        ) for news in articles
                        ]
        return result

