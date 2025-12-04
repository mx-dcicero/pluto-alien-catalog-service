# Pluto Alien Catalog Service (PACS)

Astrophysicists observing Pluto discover and track intelligent alien life. Whenever they discover or spot an alien, they interact with the **Pluto Alien Catalog Service** (PACS).

## API Endpoints

PACS currently exposes a very small HTTP surface:

- `POST /register` – Register a newly discovered alien.
- `POST /sight/{name}` – Record a new sighting of an existing alien, by name.

## Getting Started

To fire up the app locally:

1. Ensure poetry is installed on local machine - https://python-poetry.org/docs/
2. Install dependencies in virtual env with `poetry install`
3. Activate virtual environment: source `$(poetry env info --path)/bin/activate`
4. Run the application with local development server: `fastapi dev main.py`
5. Navigate to http://127.0.0.1:8000/docs to view the API documentation and test endpoints.
