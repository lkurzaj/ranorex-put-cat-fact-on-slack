import requests
from robot.api import logger
from robot.api.deco import keyword, library


@library(scope="GLOBAL", version='0.1')
class CatFactsService:

    def __init__(self):
        self.__base_url = "https://catfact.ninja/"
        self.__fact_url = self.__base_url + "fact"

    @keyword("Get Random Fact")
    def get_random_fact(self):
        random_fact = requests.get(self.__fact_url).json()["fact"]
        logger.info("Fact achieved ...::: %s :::..." % random_fact)
        return random_fact


if __name__ == "__main__":
    x = CatFactsService().get_random_fact()
    print(x)
