import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    """Create a test client for API requests."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset in-memory activities before and after each test for isolation."""
    original_state = copy.deepcopy(activities)

    # Arrange: ensure each test starts from a known state.
    activities.clear()
    activities.update(copy.deepcopy(original_state))

    yield

    # Cleanup: restore original state for the next test.
    activities.clear()
    activities.update(copy.deepcopy(original_state))
