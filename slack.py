import requests
from cred_store_local import SLACK_WEBHOOK


def send_slack_message(message: str) -> None:
    payload = {"text": message}

    try:
        requests.post(SLACK_WEBHOOK, json=payload)
    except requests.exceptions.RequestException as e:
        print(e)


if __name__ == "__main__":
    msg = "Hello World From Python!"
    send_slack_message(msg)
