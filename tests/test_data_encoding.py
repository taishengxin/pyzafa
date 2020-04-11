# -*- coding: utf-8 -*-
from pyzafa.data_encoding import base64decode, base64encode


def test_base64_encode():
    assert base64encode('你好，世界') == '5L2g5aW977yM5LiW55WM'


def test_base64_decode():
    assert base64decode('5L2g5aW977yM5LiW55WM') == '你好，世界'
