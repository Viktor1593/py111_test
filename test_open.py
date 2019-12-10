import random
import itertools

import final

def gen_ip_fromstr(fn):
    def wrp(*ar, **kw):
        ip_filter = []
        for ip in ar[0]:
            if type(ip) == str:
                ip = ip.split('-')
                ip = list(range(int(ip[0]), int(ip[1]) + 1))
            ip_filter.append(ip)
        old_fun = fn(ip_filter)
        while True:
            n_f = yield next(old_fun)
            if n_f is not None:
                ip_filter = []
                for ip in n_f:
                    if type(ip) == str:
                        ip = ip.split('-')
                        ip = list(range(int(ip[0]), int(ip[1]) + 1))
                    ip_filter.append(ip)
                old_fun.send(ip_filter)
    return wrp


@final.strange_dec('test')
def gen_ip(ip_filter):
    while True:
        ips = []
        for ip in ip_filter:
            ip = list(filter(lambda x: x in range(256), ip))
            if len(ip) == 0:
                ip = range(256)
            ips.append(str(random.choice(ip)))
        new_filter = yield '.'.join(ips)
        if new_filter is not None:
            ip_filter = new_filter


if __name__ == '__main__':
    a = gen_ip([[], '25-26', [], []])
    # for _ in range(5):
    #     print(next(a))
    #
    #
    # a.send([[50], '192-224', [], []])
    # for _ in range(5):
    #     print(next(a))
    #
    # a.send([[60], '0-31', [], []])
    # for _ in range(5):
    #     print(next(a))