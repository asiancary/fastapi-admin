# Copilot Instructions for fastapi-admin

## Project Overview
- **fastapi-admin** is an admin dashboard framework built on FastAPI and TortoiseORM, using Tabler UI.
- The codebase is modular, with clear separation between core admin logic (`fastapi_admin/`), example usage (`examples/`), and tests (`tests/`).
- The admin app is mounted as a sub-application at `/admin` in example projects.

## Key Components
- `fastapi_admin/app.py`: Core FastAPI app for admin features.
- `fastapi_admin/models.py`: TortoiseORM models for admin entities.
- `fastapi_admin/resources.py`: Resource definitions for admin UI.
- `fastapi_admin/providers/`: Authentication and login providers.
- `examples/main.py`: Example FastAPI app showing how to integrate and configure the admin dashboard.
- `examples/models.py`: Example models for demonstration.
- `examples/providers.py`: Example login provider.

## Developer Workflows
- **Run Example App:**
  - Use `docker-compose up -d --build` to start dependencies (MySQL, Redis).
  - Run `examples/main.py` (e.g., `uvicorn examples.main:app_ --reload`).
  - Visit `/admin/init` to create the first admin user.
- **Configuration:**
  - Set `DATABASE_URL` and `REDIS_URL` in a `.env` file at the project root.
- **Testing:**
  - Tests are in the `tests/` directory. Use `pytest` or `unittest` to run them.
- **Database:**
  - Uses TortoiseORM. Models are auto-discovered from the `models` module.

## Project Conventions
- **App Factory Pattern:**
  - Use `create_app()` (see `examples/main.py`) to instantiate the FastAPI app with all middleware, admin, and ORM setup.
- **Exception Handling:**
  - Custom exception handlers are registered for common HTTP errors in the admin app.
- **Static & Templates:**
  - Static files are served from `static/` and templates from `templates/`.
- **Providers:**
  - Authentication is pluggable via providers in `fastapi_admin/providers/` and `examples/providers.py`.

## Integration Points
- **Redis:** Used for session and cache. URL is set via `REDIS_URL`.
- **MySQL:** Default DB, set via `DATABASE_URL`.
- **TortoiseORM:** Handles all DB models and migrations.

## Example: Minimal App Setup
```python
from examples.main import create_app
app = create_app()
```

## References
- See `examples/main.py` for a full integration example.
- See https://fastapi-admin-docs.long2ice.io for detailed documentation.
