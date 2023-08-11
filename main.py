import os
import datetime


def logger(function):
    def new_function(*args, **kwargs):
        start = datetime.datetime.now()
        name = function.__name__
        arg = f'{args}, {kwargs}'
        result = function(*args, **kwargs)
        with open('main.log', 'a', encoding='utf-8') as file:
            res = f'{start}\n{name}\n{arg}\n{result}\n'
            file.writelines(res)
        return result

    return new_function


def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world()
    result = summator(2, 2)
    assert isinstance(result, int)
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path)

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content


if __name__ == '__main__':
    test_1()