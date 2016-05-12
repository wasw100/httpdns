# -*- coding: utf-8 -*-
import httpdns


def test_get_ip():
    host = 'localhost'
    ip = httpdns.get_ip(host)
    assert ip == '127.0.0.1'
