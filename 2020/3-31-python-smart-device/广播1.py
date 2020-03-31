# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 22:24
# @File    : 广播1.py


"""
广播1.py:

https://stackoverflow.com/questions/12607516/python-udp-broadcast-not-sending




"""
from socket import *

cs = socket(AF_INET, SOCK_DGRAM)
cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)


def main():
    # cs.sendto(b'This is a testThis is a testThis is a testThis is a test', ('255.255.255.255', 80))
    # cs.sendto(b'000000000000000008000000e40732270d011e0300000000c0a800669cfb000095c30000000006000000000000000000', ('255.255.255.255', 80))
    # cs.sendto(b"..............2'...........f....................", ('255.255.255.255', 80))
    data="\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\xe4\x07\x32\x27" \
         "\x0d\x01\x1e\x03\x00\x00\x00\x00\xc0\xa8\x00\x66\x9c\xfb\x00\x00" \
         "\x95\xc3\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    cs.sendto(data, ('255.255.255.255', 80))
    print('发送 智能插排')
    pass


def main2():
    cs.sendto(b'This is a test', ('255.255.255.255', 8080))
    print('发送完毕')
    pass

def main3():
    data=b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\xe4\x07\x15\x0f\x02\x02\x1f\x03\x00\x00\x00\x00\xc0\xa8\x00fx\xe5\x00\x00\x1d\xc3\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    data=b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\xe4\x07\x06\x12\x02\x02\x1f\x03\x00\x00\x00\x00\xc0\xa8\x00f\x1a\xe2\x00\x00\xb0\xc2\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    data=b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\xe4\x07\t\x12\x02\x02\x1f\x03\x00\x00\x00\x00\xc0\xa8\x00f\x1a\xe2\x00\x00\xb3\xc2\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    data=b"\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\xe4\x07\x39\x27\x0d\x01\x1e\x03\x00\x00\x00\x00\xc0\xa8\x00\x66\x9c\xfb\x00\x00\x9c\xc3\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    data=b"\xff\xff\xff\xff\xff\xff\x98\x46\x0a\xc7\xe6\x39\x08\x00\x45\x00\x00\x4c\x86\x85\x00\x00\x40\x11\x33\x0f\xc0\xa8\x00\x65\xff\xff\xff\xff\xe9\x13\x00\x50\x00\x38\x5d\x2a\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\xe4\x07\x2e\x1c\x02\x02\x1f\x03\x00\x00\x00\x00\xc0\xa8\x00\x65\x13\xe9\x00\x00\xe1\xc2\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    cs.sendto(data, ('255.255.255.255', 80))
    print('发送完毕3')
    pass

def main4():
    data=b"\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\xe4\x07\x28\x1c\x02\x02\x1f\x03\x00\x00\x00\x00\xc0\xa8\x00\x65\x13\xe9\x00\x00\xdb\xc2\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    cs.sendto(data, ('224.0.0.251', 80))
    print('发送完毕')
    pass

if __name__ == '__main__':
    main3()
