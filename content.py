# Micropython Http Server
# Erni Tron ernitron@gmail.com
# Copyright (c) 2016

# Content Callback functions.
# They should receive parameters and return a HTML formatted string
# By convention they start with cb_

import gc
import time

from config import save_config, set_config, get_config


# Content Functions
def cb_index(title):
    with open('index.txt', 'r') as f:
        return f.readlines()
    return []


def cb_status():
    uptime = time.time()
    import os
    filesystem = os.listdir()
    chipid = get_config('chipid')
    macaddr = get_config('mac')
    address = get_config('address')
    return '<h2>Device %s</h2>' \
           '<p>MacAddr: %s' \
           '<p>Address: %s' \
           '<p>Free Mem: %d (alloc %d)' \
           '<p>Files: %s' \
           '<p>Uptime: %d"</div>' % (chipid, macaddr, address, gc.mem_free(), gc.mem_alloc(), filesystem, uptime)


def cb_help():
    with open('help.txt', 'r') as f:
        return f.readlines()
    return []


def cb_setplace(place):
    set_config('place', place)
    save_config()
    return 'Place set to %s' % place


def cb_setparam(param, value):
    if param == None:
        return '<p>Set configuration parameter<form action="/conf">' \
               'Param <input type="text" name="param"> ' \
               'Value <input type="text" name="value"> ' \
               '<input type="submit" value="Submit">' \
               '</form></p></div>'
    else:
        set_config(param, value)
        save_config()
    return 'Param set to %s' % value


def cb_setwifi(ssid, pwd):
    if len(ssid) < 3 or len(pwd) < 8:
        return '<h2>WiFi too short, try again</h2>'
    set_config('ssid', ssid)
    set_config('pwd', pwd)
    save_config()
    return '<h2>WiFi set to %s %s</h2>' % (ssid, pwd)
