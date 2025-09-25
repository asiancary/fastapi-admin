import pytest
from fastapi import FastAPI
from starlette.testclient import TestClient
from examples.main import create_app
from starlette.middleware.cors import CORSMiddleware

@pytest.fixture
def app():
    # Create the app instance for testing
    return create_app()

@pytest.fixture
def client(app):
    return TestClient(app)

def test_create_app_returns_fastapi_instance(app):
    assert isinstance(app, FastAPI)

def test_static_files_mounted(app):
    # Check that '/static' is mounted
    assert "static" in app.routes[0].path or any(
        getattr(route, "name", None) == "static" for route in app.routes
    )

def test_admin_app_mounted(app):
    # Check that '/admin' is mounted
    assert any(route.path == "/admin" for route in app.routes)

def test_index_redirects_to_admin(client):
    response = client.get("/", allow_redirects=False)
    assert response.status_code in (302, 307)
    assert response.headers["location"] == "/admin"

def test_cors_middleware_present(app):
    # Check that CORS middleware is present
    assert any(isinstance(middleware.cls, type) and middleware.cls is CORSMiddleware for middleware in app.user_middleware)