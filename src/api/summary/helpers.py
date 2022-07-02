weather = {
    'sunny': 0,
    'cloudy': 1,
    'rainy': 2,
    'snowy': 3,
}

greeting_priority_mapping = {
    0: "폭설이 내리고 있어요.",
    1: "눈이 포슬포슬 내립니다.",
    2: "폭우가 내리고 있어요.",
    3: "비가 오고 있습니다.",
    4: "날씨가 약간은 칙칙해요.",
    5: "따사로운 햇살을 맞으세요.",
    6: "날이 참 춥네요.",
    7: "날씨가 참 맑습니다."
}


def get_greeting_results(timestamp: float, code: int, temp: float, rain1h: int):
    if code == weather['snowy'] and rain1h >= 100:
        return greeting_priority_mapping[0]
    elif code == weather['snowy']:
        return greeting_priority_mapping[1]
    elif code == weather['rainy'] and rain1h >= 100:
        return greeting_priority_mapping[2]
    elif code == weather['rainy']:
        return greeting_priority_mapping[3]
    elif code == weather['cloudy']:
        return greeting_priority_mapping[4]
    elif code == weather['sunny'] and temp >= 30:
        return greeting_priority_mapping[5]
    elif temp <= weather['sunny'] and temp <= 0:
        return greeting_priority_mapping[6]
    else:
        return greeting_priority_mapping[7]


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
