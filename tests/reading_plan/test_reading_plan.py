import pytest

from tech_news.analyzer.reading_plan import ReadingPlanService
from tests.assets.news import NEWS


def test_reading_plan_group_news(mocker):
    mocker.patch(
                 'tech_news.analyzer.reading_plan.find_news',
                 return_value=NEWS)
    news = ReadingPlanService.group_news_for_available_time(3)
    assert len(news['readable']) == 4
    assert len(news['unreadable']) == 4
    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(-4)
