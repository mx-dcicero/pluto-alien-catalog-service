from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class Temperment(str, Enum):
    CALM = "CALM"
    CURIOUS = "CURIOUS"
    AGGRESSIVE = "AGGRESSIVE"
    UNKNOWN = "UNKNOWN"


class Location(BaseModel):
    lat: float = Field(..., description="Latitude on Pluto")
    long: float = Field(..., description="Longitude on Pluto")


class AlienRegistrationRequest(BaseModel):
    name: str
    location: Location


class AlienSightingRequest(BaseModel):
    location: Location
    notes: str


class Alien(BaseModel):
    id: str
    name: str
    discovery_latitude: float
    discovery_longitude: float
    temperment: Temperment
    discovered_on: datetime
    notes: list[str] = []
