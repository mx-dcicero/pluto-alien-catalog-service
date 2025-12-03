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
3. Run the application with local development server: `fastapi dev main.py`
4. Navigate to http://127.0.0.1:8000/docs to view the API documentation and test endpoints.

## Assessment

_The following questions are meant to assess general Python knowledge, API design, and problem-solving skills. Have fun with it!_

1. Please boot up the application locally. [Hint: See above for instructions]
2. Test the healthcheck endpoint.
3. Pretend you are a scientist. POST your new alien discovery to the `/register` endpoint.
4. Update the alien's entry by POSTing to the `/sight/{name}` endpoint.
5. Users have been complaining that they have no way to get a list of all aliens. Add a new endpoint to support this.
6. Users have been complaining about the long response times when registering a new alien. Are there any strategies you could think of to improve this?
