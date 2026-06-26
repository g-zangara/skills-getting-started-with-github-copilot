def test_unregister_success_removes_participant(client):
    # Arrange
    activity_name = "Gym Class"
    email = "john@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"

    activities_response = client.get("/activities")
    participants = activities_response.json()[activity_name]["participants"]
    assert email not in participants


def test_unregister_returns_404_for_unknown_activity(client):
    # Arrange
    activity_name = "Unknown Club"
    email = "student@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_returns_404_for_missing_participant(client):
    # Arrange
    activity_name = "Science Club"
    email = "absent@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found in this activity"


def test_unregister_twice_returns_404_second_time(client):
    # Arrange
    activity_name = "Debate Team"
    email = "isabella@mergington.edu"

    # Act
    first_response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": email},
    )
    second_response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": email},
    )

    # Assert
    assert first_response.status_code == 200
    assert second_response.status_code == 404
    assert second_response.json()["detail"] == "Participant not found in this activity"
