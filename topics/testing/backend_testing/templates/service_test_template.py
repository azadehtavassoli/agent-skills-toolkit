import pytest

pytestmark = pytest.mark.asyncio


class DummyRepo:
    def __init__(self):
        self.saved = []

    async def save(self, item):
        self.saved.append(item)
        return item


class DummyPolicy:
    async def can_create(self, user_id: str, workspace_id: str) -> bool:
        return True


async def test_service_create_success():
    repo = DummyRepo()
    policy = DummyPolicy()

    service = ExampleService(repo=repo, policy=policy)

    result = await service.create(
        user_id="user-1",
        workspace_id="ws-1",
        payload={"name": "Alpha"},
    )

    assert result["name"] == "Alpha"
    assert len(repo.saved) == 1


async def test_service_create_rejects_invalid_payload():
    repo = DummyRepo()
    policy = DummyPolicy()

    service = ExampleService(repo=repo, policy=policy)

    with pytest.raises(ValueError):
        await service.create(
            user_id="user-1",
            workspace_id="ws-1",
            payload={},
        )