"""
1. OOP:
class -> object
flow/algorithm/process -> states-> objects
2. Procedural Programming
global data/state -> list/tuple/set/dictionary
procedure -> flow/algorithm/process
"""
countries = [
    {"code": "tur", "name": "turkey", "continent": "asia", "population": 80_000_000},
    {"code": "fra", "name": "france", "continent": "europe", "population": 67_000_000},
    {"code": "ita", "name": "italy", "continent": "europe", "population": 60_000_000}
]
# imperative programming: pp, oop
total_eu_population: int = 0
for country in countries:  # external loop
    if country["continent"] == "europe":
        population: int = country["population"]
        total_eu_population = total_eu_population + population
print(f"Total population: {total_eu_population}")

# declarative programming: functional programming, oop
to_population = lambda country: country["population"]
eu_country = lambda country: country["continent"] == "europe"
print(f"Total population: {sum(map(to_population, filter(eu_country, countries)))}")
