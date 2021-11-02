import pytest 

def test_get_all_recipes_with_no_records(client):
    #Act
    response = client.get("/recipes")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_book(client, two_saved_books):

    #Act
    response = client.get("/recipes/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "fish with anchovy sauce",
        "ingredients": "fish, anchovies, butter, capers"
    }

def test_get_one_book_that_doesnt_exist(client, two_saved_books):

    #Act
    response = client.get("/recipes/3")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 404
    assert not response_body

def test_get_all_books(client, two_saved_books):

    #Act
    response = client.get("/recipes")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0] == {
        "id": 1,
        "name": "fish with anchovy sauce",
        "ingredients": "fish, anchovies, butter, capers"
    }

def test_get_one_book_with_non_int_id(client, two_saved_books):

    # Act
    response = client.get("/recipes/one")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert not response_body