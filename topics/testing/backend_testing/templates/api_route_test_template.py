import pytest
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio


async def test_create_resource_success(async_client: AsyncClient, auth_headers: dict, workspace_id: str):
    payload = {
        "workspace_id": workspace_id,
        "name": "Example resource",
    }

    response = await async_client.post("/api/v1/resources", json=payload, headers=auth_headers)

    assert response.status_code == 201
    body = response.json()
    assert body["name"] == "Example resource"
    assert body["workspace_id"] == workspace_id


async def test_create_resource_rejects_missing_workspace(async_client: AsyncClient, auth_headers: dict):
    payload = {"name": "Invalid"}

    response = await async_client.post("/api/v1/resources", json=payload, headers=auth_headers)

    assert response.status_code in (400, 422)


async def test_create_resource_forbidden_for_wrong_workspace(
    async_client: AsyncClient,
    auth_headers_other_user: dict,
    workspace_id: str,
):
    payload = {
        "workspace_id": workspace_id,
        "name": "Should fail",
    }

    response = await async_client.post("/api/v1/resources", json=payload, headers=auth_headers_other_user)

    assert response.status_code in (403, 404)