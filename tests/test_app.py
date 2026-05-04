# from app.app import get_message
import app
def test_message():
    assert app.get_message() == "Hello from app"


