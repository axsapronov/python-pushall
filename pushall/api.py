# -*- encoding: utf-8 -*-
import json
import urllib.parse
import urllib.request


def validate_data(**kwargs) -> bool:
    try:
        str_args = ['type', 'key', 'title', 'text', 'icon', 'url', 'encode']
        for x in str_args:
            if x in kwargs and kwargs[x] is not None:
                assert isinstance(kwargs[x], str), \
                    "Not valid data (arg - {}), expected 'str', got - {}".format(x, type(kwargs[x]))

        if 'type' in kwargs:
            assert kwargs['type'] in ['broadcast', 'self', 'unicast'], "Not valid 'type' in request"
        if 'hidden' in kwargs:
            assert isinstance(kwargs['hidden'], int), "Not valid 'hidden', excepted int"
            assert kwargs['hidden'] in [0, 1, 2], "Not valid 'hidden' expected (0, 1, or 2)"
        if 'priority' in kwargs:
            assert isinstance(kwargs['hidden'], int), "Not valid 'priority', excepted int"
            assert kwargs['hidden'] in [-1, 0, 1], "Not valid 'priority' expected (-1, 0, or 1)"

    except AssertionError as e:
        print(e)
        return False
    else:
        return True


def api_request(**kwargs) -> dict:
    assert 'id' in kwargs, "Not found 'id' in api request"
    assert 'key' in kwargs, "Not found 'key' in api request"
    assert validate_data(**kwargs), "Not valid data"
    url = 'https://pushall.ru/api.php'

    values = {}
    for x in ['type', 'id', 'key', 'title', 'text', 'icon', 'url', 'hidden', 'encode', 'priority']:
        if x in kwargs and kwargs[x]:
            values[x] = kwargs[x]

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as r:
        # for python 3.4
        return json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))


def is_ok(response) -> bool:
    return bool('success' in response)


def is_error(response) -> bool:
    return bool('error' in response)


def broadcast_notify(key, id, text, title, icon=None, url=None):
    data = api_request(key=key, id=id, text=text, title=title, icon=icon, url=url, type='broadcast')


def self_notify(key, id, text, title, icon=None, url=None) -> bool:
    data = api_request(key=key, id=id, text=text, title=title, icon=icon, url=url, type='self')
    print(data)
    return is_ok(data)


def main():
    subsribe_id = 123
    self_key = '123'
    # a = api_request(key=self_key, id=subsribe_id, type='self')
    b = self_notify(key=self_key, id=subsribe_id, title='Hi all', text='Hiiiii maaan')
    # print(a, is_ok(a))
    print(b)


if __name__ == '__main__':
    main()
