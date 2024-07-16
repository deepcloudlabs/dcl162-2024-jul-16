countries = [
    {"code": "tur", "name": "turkey", "continent": "asia", "population": 80_000_000},
    {"code": "fra", "name": "france", "continent": "europe", "population": 67_000_000},
    {"code": "ita", "name": "italy", "continent": "europe", "population": 60_000_000}
]

"""
  data                             -> pipeline: function composition
  list, kafka/rabbitmq, websocket               filter -> map -> reduce/sum
                                                High-order function
                                                Pure       function   
                                      lazy evaluation -> generator function             
"""

global_data: int = 42


def fun_to_population(country) -> float:
    # global global_data
    # global_data += 1
    print(f"fun_to_population({country}) is running")
    return country["population"]


def fun_eu_country(country) -> bool:
    print(f"fun_eu_country({country}) is running")
    return country["continent"] == "europe"


to_population = lambda country: country["population"]
eu_country = lambda country: country["continent"] == "europe"
# internal loop
print(f"Total population: {sum(map(to_population, filter(eu_country, countries)))}")
print(f"Total population: {sum(map(fun_to_population, filter(fun_eu_country, countries)))}")
