'''
Final test for PY110
atrange_dec - decorator
if dec_var = 'test' then print function name and arguments
gen_address - generates random address from provided data

'''

import json
import re
import random


def strange_dec(dec_var: str = 'test'):
    '''
    Decorator
    if dec_var = 'test' then print function name and arguments
    :param dec_var: strange var
    :return: wrapper
    '''
    def md(fn):
        def wrp(*ar, **kw):
            if dec_var in ar or dec_var in kw.values():
                print('Вызов функции {} с параметрами'.format(fn.__name__), ', '.join(ar), ', '.join(kw))
            else:
                return fn(*ar, **kw)
            #
            # res = fn(*ar, **kw)
            # while True:
            #     addr = next(res)
            #     if dec_var in addr:
            #         print('Вызов функции {} с параметрами'.format(fn.__name__), ', '.join(ar), ', '.join(kw))
            #     else:
            #         yield addr
        return wrp
    return md


def check_addr_item(item: str):
    '''
    Check if provided address item is valid
    :param item: address item to check
    :return: True if checked, False if Error string
    '''
    if re.search('[\n!,]', item):
        print('wrong format', item)
        return False
    return True


@strange_dec('Synopskaya')
def gen_address(source_json: str = None, source_path: str = None):
    '''
    Generates random address from provided data
    :param source_json: set to read data from json string
    :param source_path: set to read data from json file
    :return: random address as string
    '''
    if source_path is not None:
        with open(source_path, 'r') as f:
            data = json.load(f)
    if source_json is not None:
        data = json.loads(source_json)

    if data is None:
        print('set path or json source')
        return False

    if not check_addr_item(data['country']):
        return False
    if not check_addr_item(data['city']):
        return False
    for street in data['streets']:
        if not check_addr_item(street):
            return False
    while True:
        out_address = [
            data['country'],
            data['city'],
            random.choice(data['streets'])
        ]
        house_number = 'd' + str(random.randint(1, 10))
        if random.randint(1, 10) > 5:
            house_number = house_number + ' k' + str(random.randint(1, 10))
        out_address.append(house_number)
        out_address.append('kv ' + str(random.randint(1, 10)))
        yield ', '.join(out_address)


if __name__ == '__main__':
    data = {
        'country': 'Russian Federation',
        'city': 'St. Petersburg',
        'streets': [
            'Nevsky pr',
            "Synopskaya nab"
        ]
    }
    f_path = 'final.json'
    with open(f_path, 'w') as f:
        json.dump(data, f)

    # a = gen_address('test')
    a = gen_address(json.dumps(data))
    # a = gen_address(source_path=f_path)
    try:
        for _ in range(5):
            print(next(a))
    except Exception as e:
        print(e)
