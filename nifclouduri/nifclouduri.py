#!/bin/env python
# condig: utf-8

import hashlib
import hmac
import base64
import requests
import urllib.parse
from datetime import datetime as dt

class Signature:
    @staticmethod
    def v0(key, data):
        return base64.b64encode(hmac.new(key.encode('utf-8'), data.encode('utf-8'), hashlib.sha1).digest())


class NifCloud:
    def __init__(self, endpoint, access_key, secret_key):
        self.endpoint = endpoint
        self.access_key = access_key
        self.secret_key = secret_key

