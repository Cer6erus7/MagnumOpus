def city_country(city: str, country: str, population=""):
    if not population:
        return f"{city.title()}, {country.title()}"
    return  f"{city.title()}, {country.title()}. Population - {population}"