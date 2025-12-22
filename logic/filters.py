def matches_weather(item, weather):
    return "all" in item["weather"] or weather in item["weather"]


def matches_occasion(item, occasion):
    return occasion in item["occasion"]

def matches_style(item, style):
    return style in item["style"]

def matches_season(item, season):
    return "all" in item["season"] or season in item["season"]

def hard_filter(items, user_input):
    filtered = []

    for item in items:
        if not matches_weather(item, user_input["weather"]):
            continue
        if not matches_occasion(item, user_input["occasion"]):
            continue
        if not matches_style(item, user_input["style"]):
            continue
        if not matches_season(item, user_input["season"]):
            continue

        filtered.append(item)

    return filtered