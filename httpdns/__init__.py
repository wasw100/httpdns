# -*- coding: utf-8 -*-
import requests

_host_dict = {}


def get_ip(host, force_update=False):
    if not host:
        return

    global _host_dict
    if not force_update:
        ip = _host_dict.get(host)
        if ip:
            return ip

    url = 'http://119.29.29.29/d'
    params = {'dn': host}
    r = requests.get(url, params=params)
    body = r.text
    if body:
        ip = body.split(';')[0]
        _host_dict[host] = ip
        return ip
