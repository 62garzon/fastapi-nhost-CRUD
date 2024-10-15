tasks_prefix = f"/api/v1/tasks"


def test_forbidden_access(test_client, fake_task_service, fake_access_token):
    response = test_client.get(
        url=f"{tasks_prefix}"
    )

    assert response.status_code == 403


