# from app.app import get_message
import app
import re

def test_message():
    result = app.get_message()
    pattern = r"Hi there! This is a message from the app\. \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]"
    assert re.match(pattern, result)

