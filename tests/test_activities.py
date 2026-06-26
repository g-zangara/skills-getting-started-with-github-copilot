def test_get_activities_returns_expected_structure(client):
    # Arrange
    expected_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert payload

    for details in payload.values():
        assert expected_keys.issubset(details.keys())
        assert isinstance(details["participants"], list)
        assert isinstance(details["max_participants"], int)
