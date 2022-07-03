import random

from fastapi.testclient import TestClient

from api.summary.helpers import get_heads_up_results
from main import app

client: TestClient = TestClient(app)


def test_summary_headsup_priority_0():
    # given
    params: list = [
        dict(code=3, rain=random.randrange(1, 10)) for _ in range(8)
    ]

    # when
    results: str = get_heads_up_results(params)

    # then
    assert results
    assert results == "내일 폭설이 내릴 수도 있으니 외출 시 주의하세요."


def test_summary_headsup_priority_1():
    # given
    params: list = [
        dict(code=3, rain=0) for _ in range(4)
    ]
    params.append(dict(code=3, rain=1))
    params.append(dict(code=3, rain=1))

    # when
    results: str = get_heads_up_results(params)

    # then
    assert results
    assert results == "눈이 내릴 예정이니 외출 시 주의하세요."


def test_summary_headsup_priority_2():
    # given
    params: list = [
        dict(code=2, rain=random.randrange(1, 10)) for _ in range(8)
    ]

    # when
    results: str = get_heads_up_results(params)

    # then
    assert results
    assert results == "폭우가 내릴 예정이에요. 우산을 미리 챙겨두세요."


def test_summary_headsup_priority_3():
    # given
    params: list = [
        dict(code=2, rain=0) for _ in range(4)
    ]
    params.append(dict(code=2, rain=1))
    params.append(dict(code=2, rain=1))

    # when
    results: str = get_heads_up_results(params)

    # then
    assert results
    assert results == "며칠동안 비 소식이 있어요."


def test_summary_headsup_priority_4():
    # given
    params: list = [
        dict(code=1, rain=0) for _ in range(8)
    ]

    # when
    results: str = get_heads_up_results(params)

    # then
    assert results
    assert results == "날씨는 대체로 평온할 예정이에요."
