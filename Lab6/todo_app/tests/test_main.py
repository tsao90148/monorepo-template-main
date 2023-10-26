from ..src.main import first_api, first_api2, first_api3, first_api4, first_api5, first_api6, first_api7

def test_first_api():
    response = first_api()
    assert response["msg"] == "This is Get Rest API"
    # Add more assertions if needed

def test_first_api2():
    response = first_api2("random_stuff")
    assert response["msg"] == "path used is random_stuff"
    # Add more assertions if needed

def test_first_api3():
    response = first_api3("cool_stuff")
    assert response["msg"] == "category name of stuff is cool_stuff"
    # Add more assertions if needed

def test_first_api4():
    response = first_api4("name_two", 5)
    assert response["msg"] == "path or category name used is name_two and queried by id number: 5"
    # Add more assertions if needed

