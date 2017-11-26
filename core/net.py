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

import logging
# import requests
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class Net(object):

    """Docstring for sdk. """

    def __init__(self, endpoint, domain_id, port=8080, headers=None):
        """TODO: to be defined1. """
        logging.debug('Initializing Network client....')
