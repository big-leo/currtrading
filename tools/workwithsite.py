from socket import socket
import time
import csv


def put_curr(curr_from, curr_to, rate):
    s = socket()
    s.connect(('127.0.0.1', 8000))
    s.send(('PUT /currency/%s/%s/?rate=%s HTTP/1.1\r\n\r\n' % (curr_from, curr_to, str(rate))).encode())
    time.sleep(1)


def post_curr(curr):
    s = socket()
    s.connect(('127.0.0.1', 8000))
    s.send(('POST /currency/%s/ HTTP/1.1\r\n\r\n' % curr).encode())
    time.sleep(1)


def load_default():
    post_curr('EUR')
    post_curr('USD')
    post_curr('CNY')
    post_curr('RUB')

    put_curr('EUR', 'EUR', 1)
    put_curr('EUR', 'USD', 1.1)
    put_curr('EUR', 'CNY', 6.5)
    put_curr('EUR', 'RUB', 70)

    put_curr('USD', 'EUR', 0.9)
    put_curr('USD', 'USD', 1)
    put_curr('USD', 'CNY', 6)
    put_curr('USD', 'RUB', 65)

    put_curr('CNY', 'EUR', 0.16)
    put_curr('CNY', 'USD', 0.17)
    put_curr('CNY', 'CNY', 1)
    put_curr('CNY', 'RUB', 10.75)

    put_curr('RUB', 'EUR', 0.01)
    put_curr('RUB', 'USD', 0.02)
    put_curr('RUB', 'CNY', 0.08)
    put_curr('RUB', 'RUB', 1)


def load_csv(f_name):
    with open(f_name, 'rb') as fd:
        reader = csv.reader(fd, delimiter=' ', quotechar='\n')
        header = []
        for row in reader:
            row = [r for r in row if r != '']
            if not header:
                header = row[:]
            else:
                for i in range(len(header)):
                    print(row[0], header[i], row[i + 1])
                    put_curr(row[0], header[i], row[i + 1])


if __name__ == '__main__':
    load_default()
    # or
    # load_csv('../matrix.csv')
