from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


_ACTIVITIES_BASELINE = deepcopy(activities)


@pytest.fixture
def client():
    activities.clear()
    activities.update(deepcopy(_ACTIVITIES_BASELINE))

    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        activities.clear()
        activities.update(deepcopy(_ACTIVITIES_BASELINE))