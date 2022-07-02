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


def get_current_results(timestamp: float, code: int, temp: float, rain1h: int):
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
