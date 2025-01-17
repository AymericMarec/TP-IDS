import requests

url = "" # put your webhook url here


def SendWebhook(message) :
    data = {
        "username" : "IDS BOT"
    }

    data["embeds"] = [
        {
            "description" : message,
            "title" : "Y'a une erreur gros"
        }
    ]

    result = requests.post(url, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print(f"Payload delivered successfully, code {result.status_code}.")