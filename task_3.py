import requests
import json
import datetime
from functools import wraps


def logger(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        url = "https://akabab.github.io/superhero-api/api/all.json"
        resp = requests.get(url)
        if resp.status_code == 200:
            resp = resp.text
            resp = json.loads(resp)
            with open('task_3.log', 'a', encoding='utf-8') as f:
                f.write(f'{datetime.datetime.now()} - {old_function.__name__}({args}, {kwargs}) = {resp}\n')
            return resp
        else:
            message = 'Error'
            return message

    return new_function


@logger
def my_function():
    pass


if __name__ == '__main__':
    my_function()
