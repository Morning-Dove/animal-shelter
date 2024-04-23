from pydantic import BaseModel as bm


class AnimalCounts(bm):
    cats: int
    dogs: int

class Shelter(bm):
    name: str
    address: str
    animals: AnimalCounts