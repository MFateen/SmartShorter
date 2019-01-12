from mongoframes import *
from app import Frame


class ShortLink(Frame):
    _fields = {
        'slug',
        'web',
        'android',
        'ios'
    }


class DeviceLink(SubFrame):
    _fields = {
        'primary',
        'fallback'
    }


def add_short_link(short_link):
    short_link.insert()

