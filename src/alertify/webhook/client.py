# MIT License
#
# Copyright (c) 2022 Clivern
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import requests
import logging
from alertify.exception import ApiError


class Client():
    """Client Class"""

    def __init__(self):
        self._logging = logging.getLogger(__name__)

    def post(self, url, api_key, payload={}):

        headers = {
            'Authorization': f'Bearer {api_key}',
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
        except Exception as e:
            raise ApiError("Failed to call webhook: {}".format(str(e)))

        if response.status_code // 100 == 2:
            raise ApiError("Webhook respond with error status code {}".format(response.status_code))

        return True

    def put(self, url, api_key, payload={}):

        headers = {
            'Authorization': f'Bearer {api_key}',
        }

        try:
            response = requests.put(url, json=payload, headers=headers)
        except Exception as e:
            raise ApiError("Failed to call webhook: {}".format(str(e)))

        if response.status_code // 100 == 2:
            raise ApiError("Webhook respond with error status code {}".format(response.status_code))

        return True
