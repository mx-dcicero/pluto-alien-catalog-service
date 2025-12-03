import random
import time
from datetime import datetime, timezone
from typing import Dict
from uuid import uuid4

from fastapi import APIRouter, HTTPException, Request
from models.aliens import (
    Alien,
    AlienRegistrationRequest,
    AlienSightingRequest,
    Temperment,
)

router = APIRouter(tags=["aliens"])

# Very lightweight in-memory "catalog" keyed by alien name
CATALOG_BY_NAME: Dict[str, Alien] = {}


async def call_orbital_scanner(lat: float, long: float) -> Temperment | None:
    """
    Mock for the external Orbital Scanner Service.
    """

    # Orbital scanner takes time to locate the alien and characterize it.
    time.sleep(5)

    # Occasionally "fail to locate" the alien by returning None.
    # Interview candidates can change this logic.
    temperment = random.choice(
        [Temperment.CURIOUS, Temperment.CALM, Temperment.AGGRESSIVE, None]
    )

    if temperment is None:
        raise HTTPException(
            status_code=500, detail="Orbital scanner failed to locate alien"
        )

    return temperment


@router.post("/register", response_model=Alien)
async def register_alien(payload: AlienRegistrationRequest, request: Request) -> Alien:
    """
    Register a newly discovered alien.
    """
    print(f"register_alien: {request.client.host}")

    if payload.name in CATALOG_BY_NAME:
        raise HTTPException(
            status_code=409, detail="Alien with this name already exists"
        )

    alien_id = str(uuid4())
    now = datetime.now(timezone.utc)

    # Call the external Orbital Scanner Service with the sighting coordinates
    temperment = await call_orbital_scanner(
        lat=payload.location.lat,
        long=payload.location.long,
    )

    alien = Alien(
        id=alien_id,
        name=payload.name,
        discovery_latitude=payload.location.lat,
        discovery_longitude=payload.location.long,
        temperment=temperment,
        discovered_on=now,
    )
    CATALOG_BY_NAME[payload.name] = alien
    return alien


@router.post("/sight/{name}", response_model=Alien)
async def sight_alien(name: str, payload: AlienSightingRequest) -> Alien:
    """
    Record a new sighting of an existing alien and attempt to characterize its temperment.
    """
    alien = CATALOG_BY_NAME.get(name)
    if not alien:
        raise HTTPException(status_code=404, detail="Alien not found")

    # Persist the possibly-updated alien back to the catalog
    CATALOG_BY_NAME[name] = alien

    alien.notes.append(payload.notes)

    return alien
