
import re





if __name__ == '__main__':

    find_str = '83.149.9.216 - - [17/May/2015:10:05:03 +0000] "GET /presentations/logstash-monitorama-2013/images/kibana-search.png HTTP/1.1" 200 203023 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1)'

    print(re.findall(
        r'(?:(?:(?:25[0-5])|(?:2[0-4][0-9])|(?:1[0-9]{2})|(?:[0-9]{1,2}))\.){3}(?:(?:(?:25[0-5])|(?:2[0-4][0-9])|(?:1[0-9]{2})|(?:[0-9]{1,2})))',
        find_str))
    filename = 'apache_server.log'
    ip = r'[0-9]{1,3}(?:\.[0-9]{1,3}){3}'
    counts = {}
    with open(filename, 'r') as f:
        f_data = f.read()
    res = re.findall(ip, f_data)
    for i in res:
        if i in counts:
            counts[i] +=1
        else:
            counts[i] = 1
    print(counts)
    # if __name__ == '__main__':
    filename = 'apache_server.log'
    ip = '/[0-9](\.[0-9]){3}/'


    counts = {ip: 0}
    with open(filename, 'r') as f:
        for line in f:
            if re.match(ip, line):
                counts[ip] += 1
    print(counts)

    os_list = [
        'Windows NT',
        'Macintosh',
        'Linux'
    ]
    counts = {'total': 0}
    for os_name in os_list:
        with open(filename, 'r') as f:
            for line in f:
                if re.search(os_name, line):
                    counts['total'] += 1
                    if os_name in counts:
                        counts[os_name] += 1
                    else:
                        counts[os_name] = 1
    print(counts)
    for os_name in counts:
        print(counts[os_name]/counts['total'])





