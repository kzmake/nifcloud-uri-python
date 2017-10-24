#!/bin/env python
# condig: utf-8

import hashlib
import hmac
import base64

class Signature:
    @staticmethod
    def v0(key, data):
        return base64.b64encode(hmac.new(key.encode('utf-8'), data.encode('utf-8'), hashlib.sha1).digest())
