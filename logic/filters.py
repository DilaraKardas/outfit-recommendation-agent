def matches_weather(item, weather):
    return "all" in item["weather"] or weather in item["weather"]

def matches_occasion(item, occasion):
    return occasion in item["occasion"]

def matches_style(item, style):
    return style in item["style"]

def matches_season(item, season):
    if season is None:
        return True
    # Eğer user "all" diyorsa, her şey uyar
    if season == "all":
        return True
    # Eğer item'ın season'ı "all" ise, her şeye uyar
    return "all" in item["season"] or season in item["season"]

def hard_filter(items, user_input):
    filtered = []

    print(f"\n=== FILTERING WITH ===")
    print(f"Weather: '{user_input['weather']}'")
    print(f"Occasion: '{user_input['occasion']}'")
    print(f"Style: '{user_input['style']}'")
    print(f"Season: '{user_input.get('season')}'")
    print(f"\n=== CHECKING {len(items)} ITEMS ===\n")


    for item in items:

        print(f"Checking: {item['name']} (category: {item['category']})")

        weather_match = matches_weather(item, user_input["weather"])
        print(f"  Weather match: {weather_match} (item weather: {item['weather']}, looking for: '{user_input['weather']}')")
        
        if not weather_match:
            print(f"  ❌ REJECTED: weather mismatch")
            continue
            
        occasion_match = matches_occasion(item, user_input["occasion"])
        print(f"  Occasion match: {occasion_match}")
        if not occasion_match:
            print(f"  ❌ REJECTED: occasion mismatch")
            continue
            
        style_match = matches_style(item, user_input["style"])
        print(f"  Style match: {style_match}")
        if not style_match:
            print(f"  ❌ REJECTED: style mismatch")
            continue
            
        season_match = matches_season(item, user_input.get("season"))
        print(f"  Season match: {season_match}")
        if not season_match:
            print(f"  ❌ REJECTED: season mismatch")
            continue

        print(f"  ✅ PASSED ALL FILTERS")
        filtered.append(item)

    print(f"\n=== FILTERED RESULT: {len(filtered)} items ===\n")
    return filtered
'''''
        if not matches_weather(item, user_input["weather"]):
            continue
        if not matches_occasion(item, user_input["occasion"]):
            continue
        if not matches_style(item, user_input["style"]):
            continue
        if not matches_season(item, user_input["season"]):
            continue

        filtered.append(item)
'''