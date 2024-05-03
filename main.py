# Make the pydantic model `Shelter` that will represent this data, then manually
# change this list to be a list[Shelter]. You don't need to write code to convert
# this list, just manually change it by hand.
from fastapi import FastAPI

from schemas import AnimalCounts, Shelter


app = FastAPI()


shelters: list[Shelter] = [
    Shelter(
        name= "St. George Animal Shelter",
        address= "605 Waterworks Dr, St. George, UT 84770",
        animals= AnimalCounts(cats= 13,dogs= 15)
    ),
    Shelter(
        name="St. George Paws",
        address= "1125 W 1130 N, St. George, UT 84770",
        animals= AnimalCounts(cats=12, dogs=9)
    ),
    Shelter(
        name= "Animal Rescue Team",
        address= "1838 W 1020 N Ste. B, St. George, UT 84770",
        animals= AnimalCounts(cats=4,dogs= 7)
    )
]

@app.get("/shelters")
async def get_shelter() -> list[Shelter]:
    return shelters


@app.post("/shelters")
async def create_shelter(shelter: Shelter):
    shelters.append(shelter)


@app.put("/shelters/{name}")
async def update_shelter(name: str, updated_shelter: Shelter) -> None:
    for shelter in shelters:
        if name == shelter.name:
            shelter.address = updated_shelter.address
            shelter.animals = updated_shelter.animals
    shelters.append(updated_shelter)


@app.delete("/shelters/{name}")
async def delete_shelter(name: str) -> str:
    for i, shelter in enumerate(shelters):
        if name == shelter.name:
            shelters.pop(i)
            return "Shelter Deleted"
            
