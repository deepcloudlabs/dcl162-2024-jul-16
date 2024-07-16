countries = [
    {"code": "tur", "name": "turkey", "continent": "asia", "population": 80_000_000},
    {"code": "fra", "name": "france", "continent": "europe", "population": 67_000_000},
    {"code": "ita", "name": "italy", "continent": "europe", "population": 60_000_000}
]


def fun_to_population(country) -> float:
    # global global_data
    # global_data += 1
    print(f"fun_to_population({country}) is running")
    return country["population"]


def fun_eu_country(country) -> bool:
    print(f"fun_eu_country({country}) is running")
    return country["continent"] == "europe"


"""
  filter/map/reduce: i. HoF ii. lazy evaluation-> generator
"""
print("Application is just started!")
for eu_country in filter(fun_eu_country, countries):
    print(f"eu country: {eu_country['name']}")
print("Application is just completed!")
