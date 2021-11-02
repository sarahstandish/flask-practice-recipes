import pytest
from app import create_app
from app import db
from app.recipe.Recipe import Recipe

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app
    
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()
    client.get(request_path)

@pytest.fixture
def two_saved_books(app):

    r1 = Recipe(name="fish with anchovy sauce", ingredients="fish, anchovies, butter, capers")
    r2 = Recipe(name="farro salad", ingredients="farro, olive oil, nuts, cherry tomatos")

    db.session.add_all([r1, r2])