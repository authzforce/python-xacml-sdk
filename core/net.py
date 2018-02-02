#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# net.py
# Copyright (c) 2017 hargathor <3949704+hargathor@users.noreply.github.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -*- coding: utf-8 -*-
# File              : net.py
# Author            : hargathor <3949704+hargathor@users.noreply.github.com>
# Date              : 26.11.2017
# Last Modified Date: 26.11.2017
# Last Modified By  : hargathor <3949704+hargathor@users.noreply.github.com>

import json
import logging
import requests
import sys

from pyxacml_sdk.core.utils import Tools

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class Net(object):

    """Docstring for sdk. """

    def __init__(self, host, endpoint, domain_id, port=8080, headers=None, *args, **kwargs):
        """TODO: to be defined1. """
        logging.debug('Initializing Network client....')
        self.tcp_ip = host
        self.tcp_port = port
        self.endpoint = endpoint
        self.domain_id = domain_id

        # Optional variables
        self.headers = {}
        self.headers['Content-Type'] = 'Application/json'
        self.headers['Accept'] = 'Application/json'
        if headers:
            self.headers.update(headers)
        print(self.headers)
        self.ssl_enable = kwargs.get('ssl_enable')
        self.proxy = {}
        self.proxy_enable = kwargs.get('proxy_enable')
        self.proxy_ssl_enable = kwargs.get('proxy_ssl_enable')
        self.proxy_host = kwargs.get('proxy_host')
        self.proxy_port = kwargs.get('proxy_port')
        self.proxy_user = kwargs.get('proxy_user')
        self.proxy_password = kwargs.get('proxy_password')
        self.auth_type = kwargs.get('auth_type')
        self.user = kwargs.get('user')
        self.password = kwargs.get('password')
        self.cert_path = kwargs.get('cert_path')

        if self.proxy_enable:
            if self.proxy_user and self.proxy_password:
                self.proxy = {"http://{user}:{password}@{host}:{port}/".format(
                    user=self.proxy_user, password=self.proxy_password,
                    host=self.proxy_host, port=self.proxy_port)}

    def __parse_response__(self, request_response):
        """TODO: Docstring for __parse_response__.

        :response: TODO
        :returns: TODO

        """
        decision = request_response.get(
            'Response').get('Result').get('Decision')
        response = (decision, request_response.get('Response'))

        logging.debug('Decision is: {}'.format(decision))

        return response

    def send_request(self, xacml_request):
        """TODO: Docstring for send_request.

        :payload: TODO
        :returns: TODO

        """
        payload = json.dumps(xacml_request, default=Tools.default_serializer)
        r = requests.post(
            'http://{host}:{port}/{endpoint}/domains/{domain}/pdp'.format(
                host=self.tcp_ip, port=self.tcp_port,
                endpoint=self.endpoint, domain=self.domain_id),
            headers=self.headers,
            data=payload,
        )
        if r.status_code != 200:
            logging.error("Something went wrong: {}".format(r.reason))
        logging.debug("Response from server: {}".format(r.json()))

        return self.__parse_response__(r.json())
