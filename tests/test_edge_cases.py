def test_signup_supports_url_encoded_activity_name(client):
    # Arrange
    activity_name = "Basketball Team"
    email = "newplayer@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 200



def test_signup_is_case_sensitive_for_activity_name(client):
    # Arrange
    activity_name = "chess club"
    email = "casecheck@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"



def test_signup_allows_blank_email_current_behavior(client):
    # Arrange
    activity_name = "Art Studio"
    blank_email = ""

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": blank_email},
    )

    # Assert
    assert response.status_code == 200

    activities_response = client.get("/activities")
    participants = activities_response.json()[activity_name]["participants"]
    assert blank_email in participants
