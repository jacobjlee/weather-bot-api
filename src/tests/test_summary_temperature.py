import random

from fastapi.testclient import TestClient

from api.summary.helpers import get_temperature_results
from main import app

client: TestClient = TestClient(app)

temp_list: list = [15, -5, 30, 25, 40]
max_temp: int = 40
min_temp: int = -5


def test_summary_temperature_temp_down_and_current_temp_greater_equal_15():
    """Test get expected message when temp went down and current temp is greater or equal to 15."""

    # given
    current_temp: int = random.randint(10, 15)
    temp_24_hours_ago: int = random.randint(16, 20)
    params: dict = dict(current_temp=current_temp, temp_24_hours_ago=temp_24_hours_ago,
                        max_temp=max_temp, min_temp=min_temp)

    # when
    results: str = get_temperature_results(**params)

    # then
    assert results
    assert results == f"어제보다 {temp_24_hours_ago - current_temp}도 덜 덥습니다. " \
                      f"최고기온은 {max_temp}도, 최저기온은 {min_temp}도 입니다."


def test_summary_temperature_temp_down_and_current_temp_under_15():
    """Test get expected message when temp went down and current temp is under 15."""

    # given
    current_temp: int = random.randint(10, 14)
    temp_24_hours_ago: int = random.randint(15, 20)
    params: dict = dict(current_temp=current_temp, temp_24_hours_ago=temp_24_hours_ago,
                        max_temp=max_temp, min_temp=min_temp)

    # when
    results: str = get_temperature_results(**params)

    # then
    assert results
    assert results == f"어제보다 {temp_24_hours_ago - current_temp}도 더 춥습니다. " \
                      f"최고기온은 {max_temp}도, 최저기온은 {min_temp}도 입니다."


def test_summary_temperature_temp_up_and_current_temp_greater_equal_15():
    """Test get expected message when temp went up and current temp is greater or equal to 15."""

    # given
    current_temp: int = random.randint(15, 20)
    temp_24_hours_ago: int = random.randint(10, 14)
    params: dict = dict(current_temp=current_temp, temp_24_hours_ago=temp_24_hours_ago,
                        max_temp=max_temp, min_temp=min_temp)

    # when
    results: str = get_temperature_results(**params)

    # then
    assert results
    assert results == f"어제보다 {current_temp - temp_24_hours_ago}도 더 덥습니다. " \
                      f"최고기온은 {max_temp}도, 최저기온은 {min_temp}도 입니다."


def test_summary_temperature_temp_up_and_current_temp_under_15():
    """Test get expected message when temp went up and current temp is under 15."""

    # given
    current_temp: int = random.randint(10, 14)
    temp_24_hours_ago: int = random.randint(5, 9)
    params: dict = dict(current_temp=current_temp, temp_24_hours_ago=temp_24_hours_ago,
                        max_temp=max_temp, min_temp=min_temp)

    # when
    results: str = get_temperature_results(**params)

    # then
    assert results
    assert results == f"어제보다 {current_temp - temp_24_hours_ago}도 덜 춥습니다. " \
                      f"최고기온은 {max_temp}도, 최저기온은 {min_temp}도 입니다."


def test_summary_temperature_temp_same_and_current_temp_greater_equal_15():
    """Test get expected message when temps are same and current temp is greater or equal to 15."""

    # given
    current_temp: int = random.randint(15, 20)
    temp_24_hours_ago: current_temp = current_temp
    params: dict = dict(current_temp=current_temp, temp_24_hours_ago=temp_24_hours_ago,
                        max_temp=max_temp, min_temp=min_temp)

    # when
    results: str = get_temperature_results(**params)

    # then
    assert results
    assert results == f"어제와 비슷하게 덥습니다. " \
                      f"최고기온은 {max_temp}도, 최저기온은 {min_temp}도 입니다."


def test_summary_temperature_temp_same_and_current_temp_under_15():
    """Test get expected message when temps are same and current temp is under 15."""

    # given
    current_temp: int = random.randint(10, 14)
    temp_24_hours_ago: current_temp = current_temp
    params: dict = dict(current_temp=current_temp, temp_24_hours_ago=temp_24_hours_ago,
                        max_temp=max_temp, min_temp=min_temp)

    # when
    results: str = get_temperature_results(**params)

    # then
    assert results
    assert results == f"어제와 비슷하게 춥습니다. " \
                      f"최고기온은 {max_temp}도, 최저기온은 {min_temp}도 입니다."
