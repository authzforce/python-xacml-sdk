#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# sdk.py
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
# File              : sdk.py
# Author            : hargathor <3949704+hargathor@users.noreply.github.com>
# Date              : 26.11.2017
# Last Modified Date: 26.11.2017
# Last Modified By  : hargathor <3949704+hargathor@users.noreply.github.com>

import logging
import sys

from pyxacml_sdk.core import net

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class Sdk(object):

    """Docstring for sdk. """

    def __init__(self, endpoint, domain_id, port=8080, headers=None):
        """TODO: to be defined1. """
        logging.debug(
                'Initializing SDK using: [endpoint: {}, port: {}, domain_id: {}, headers: {}]'
                .format(endpoint, port, domain_id, headers))
        self.net = net.Net(endpoint, port, domain_id, headers)


    def get_authz(self, subject, resource, action, environment):
        """TODO: Docstring for get_authz.

        :subject: TODO
        :resource: TODO
        :action: TODO
        :environment: TODO
        :returns: TODO

        """
        logging.error('Not implemented')
        pass

