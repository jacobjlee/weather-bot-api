weather = {
    'sunny': 0,
    'cloudy': 1,
    'rainy': 2,
    'snowy': 3,
}

greeting_responses = {
    0: "폭설이 내리고 있어요.",
    1: "눈이 포슬포슬 내립니다.",
    2: "폭우가 내리고 있어요.",
    3: "비가 오고 있습니다.",
    4: "날씨가 약간은 칙칙해요.",
    5: "따사로운 햇살을 맞으세요.",
    6: "날이 참 춥네요.",
    7: "날씨가 참 맑습니다.",
}

heads_up_responses = {
    0: "내일 폭설이 내릴 수도 있으니 외출 시 주의하세요.",
    1: "눈이 내릴 예정이니 외출 시 주의하세요.",
    2: "폭우가 내릴 예정이에요. 우산을 미리 챙겨두세요.",
    3: "며칠동안 비 소식이 있어요.",
    4: "날씨는 대체로 평온할 예정이에요.",
}


def get_greeting_results(timestamp: float, code: int, temp: float, rain1h: int):
    if code == weather['snowy'] and rain1h >= 100:
        return greeting_responses[0]
    elif code == weather['snowy']:
        return greeting_responses[1]
    elif code == weather['rainy'] and rain1h >= 100:
        return greeting_responses[2]
    elif code == weather['rainy']:
        return greeting_responses[3]
    elif code == weather['cloudy']:
        return greeting_responses[4]
    elif code == weather['sunny'] and temp >= 30:
        return greeting_responses[5]
    elif temp <= weather['sunny'] and temp <= 0:
        return greeting_responses[6]
    else:
        return greeting_responses[7]


def get_temperature_results(current_temp: int, temp_24_hours_ago: int, max_temp: int, min_temp: int):
    max_min_temp_sentence = f"최고기온은 {max_temp}도, 최저기온은 {min_temp}도 입니다."

    if temp_24_hours_ago > current_temp >= 15:
        return f"어제보다 {temp_24_hours_ago - current_temp}도 덜 덥습니다." + " " + max_min_temp_sentence
    elif temp_24_hours_ago > current_temp < 15:
        return f"어제보다 {temp_24_hours_ago - current_temp}도 더 춥습니다." + " " + max_min_temp_sentence
    elif temp_24_hours_ago < current_temp >= 15:
        return f"어제보다 {current_temp - temp_24_hours_ago}도 더 덥습니다." + " " + max_min_temp_sentence
    elif temp_24_hours_ago < current_temp < 15:
        return f"어제보다 {current_temp - temp_24_hours_ago}도 덜 춥습니다." + " " + max_min_temp_sentence
    elif current_temp == temp_24_hours_ago and current_temp >= 15:
        return f"어제와 비슷하게 덥습니다." + " " + max_min_temp_sentence
    elif current_temp == temp_24_hours_ago and current_temp < 15:
        return f"어제와 비슷하게 춥습니다." + " " + max_min_temp_sentence


def get_heads_up_results(forecast_code_rain_list: list):
    forecast_24_hours: dict = dict(snowy=0, rainy=0)
    forecast_48_hours: dict = dict(snowy=0, rainy=0)

    for i, forecast in enumerate(forecast_code_rain_list):
        if not forecast['rain']:
            continue
        if not forecast['code'] in [weather['snowy'], weather['rainy']]:
            continue
        if forecast['code'] == weather['snowy']:
            if i <= 3:
                forecast_24_hours['snowy'] += 1
            forecast_48_hours['snowy'] += 1
        elif forecast['code'] == weather['rainy']:
            if i <= 3:
                forecast_24_hours['rainy'] += 1
            forecast_48_hours['rainy'] += 1

    if forecast_24_hours['snowy'] >= 2:
        return heads_up_responses[0]
    elif forecast_48_hours['snowy'] >= 2:
        return heads_up_responses[1]
    elif forecast_24_hours['rainy'] >= 2:
        return heads_up_responses[2]
    elif forecast_48_hours['rainy'] >= 2:
        return heads_up_responses[3]
    else:
        return heads_up_responses[4]
