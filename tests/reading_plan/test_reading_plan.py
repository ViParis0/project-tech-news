from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
from unittest.mock import MagicMock
import json
import pytest


def test_reading_plan_group_news():
    ReadingPlanService._db_news_proxy = MagicMock(
        return_value=[{"reading_time": 10, "title": "noticia incrivel de 10m"}]
    )
    readable_news = ReadingPlanService.group_news_for_available_time(10)
    assert readable_news["unreadable"] == []

    with open("tests/assets/cached_news.json") as f:
        data = json.load(f)
        ReadingPlanService._db_news_proxy = MagicMock(return_value=data)
        readable_news = ReadingPlanService.group_news_for_available_time(10)

        assert "readable" in readable_news
        assert "unreadable" in readable_news
        assert readable_news["unreadable"]
        assert readable_news["readable"][0]["unfilled_time"] == 1

    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(0)
