import random

from fastapi.testclient import TestClient

from api.summary.helpers import get_current_results
from main import app

client = TestClient(app)

timestamp = random.uniform(1000000000, 2000000000)
temp = random.uniform(1, 20)
rain1h = random.randrange(100, 200)


def test_summary_greeting_priority_0():
    # given
    params: dict = dict(timestamp=timestamp, code=3, temp=temp, rain1h=rain1h)

    # when
    results: str = get_current_results(**params)

    # then
    assert results
    assert results == "폭설이 내리고 있어요."


def test_summary_greeting_priority_1():
    # given
    params: dict = dict(timestamp=timestamp, code=3, temp=temp, rain1h=random.randrange(1, 99))

    # when
    results: str = get_current_results(**params)

    # then
    assert results
    assert results == "눈이 포슬포슬 내립니다."


def test_summary_greeting_priority_2():
    # given
    params: dict = dict(timestamp=timestamp, code=2, temp=temp, rain1h=rain1h)

    # when
    results: str = get_current_results(**params)

    # then
    assert results
    assert results == "폭우가 내리고 있어요."


def test_summary_greeting_priority_3():
    # given
    params: dict = dict(timestamp=timestamp, code=2, temp=temp, rain1h=random.randrange(1, 99))

    # when
    results: str = get_current_results(**params)

    # then
    assert results
    assert results == "비가 오고 있습니다."


def test_summary_greeting_priority_4():
    # given
    params: dict = dict(timestamp=timestamp, code=1, temp=temp, rain1h=rain1h)

    # when
    results: str = get_current_results(**params)

    # then
    assert results
    assert results == "날씨가 약간은 칙칙해요."


def test_summary_greeting_priority_5():
    # given
    params: dict = dict(timestamp=timestamp, code=0, temp=random.uniform(30, 40), rain1h=rain1h)

    # when
    results: str = get_current_results(**params)

    # then
    assert results
    assert results == "따사로운 햇살을 맞으세요."


def test_summary_greeting_priority_6():
    # given
    params: dict = dict(timestamp=timestamp, code=0, temp=random.uniform(-20, 0), rain1h=rain1h)

    # when
    results: str = get_current_results(**params)

    # then
    assert results
    assert results == "날이 참 춥네요."


def test_summary_greeting_priority_7():
    # given
    params: dict = dict(timestamp=timestamp, code=0, temp=temp, rain1h=rain1h)

    # when
    results: str = get_current_results(**params)

    # then
    assert results
    assert results == "날씨가 참 맑습니다."

