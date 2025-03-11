from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.models import CrewMember
from app.schema import CrewMemberCreate, CrewMemberResponse

app = FastAPI()

crew_members = [
    {
        "id": 1,
        "name": "John Doe",
        "role": "PILOT",
        "contract_days": 10,
        "availability": 8,
    },
    {
        "id": 2,
        "name": "Jane Doe",
        "role": "PILOT",
        "contract_days": 5,
        "availability": 5,
    },
    {
        "id": 3,
        "name": "Alice",
        "role": "GROUND_STAFF",
        "contract_days": 6,
        "availability": 3,
    },
    {
        "id": 4,
        "name": "Bob",
        "role": "CABIN_CREW",
        "contract_days": 8,
        "availability": 7,
    },
    {
        "id": 5,
        "name": "Charlie",
        "role": "INSTRUCTOR",
        "contract_days": 6,
        "availability": 6,
    }
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API AirCrew"}


@app.get("/crew/", response_model=List[CrewMemberResponse])
async def get_all_crew():
    return crew_members


@app.get("/crew/{crew_id}", response_model=CrewMemberResponse)
async def get_crew_member(crew_id: int):
    return {"message": "crew with id crew_id"}  # TODO


@app.post("/crew/", response_model=CrewMemberResponse)
async def create_crew_member(crew_member: CrewMemberCreate):
    crew = CrewMember(
        id=len(crew_members) + 1,
        name=crew_member.name,
        contract_days=crew_member.contract_days,
        availability=crew_member.availability,
        role=crew_member.role
    )

    crew_members.append(crew)
    return crew


@app.delete("/crew/{crew_id}")
async def delete_crew_member(crew_id: int):
    return {"message": "crew with id crew_id"}  # TODO


@app.put("/crew/{crew_id}/update-availability")
async def update_availability(crew_id: int):
    return {"message": "Availability updated"}  # TODO


@app.get("/crew/stats")
async def get_stats():
    return {
        "PILOT": {"total": 0, "available": 0},
    }  # TODO
