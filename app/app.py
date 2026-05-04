from datetime import datetime


def get_message():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Hi there! This is a message from the app. [{timestamp}]"


if __name__ == "__main__":
    print(get_message())