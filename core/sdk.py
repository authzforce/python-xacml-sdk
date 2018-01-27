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
import json
import logging
import sys

import yaml
from pyxacml_sdk.core.net import Net
from pyxacml_sdk.core.utils import Tools

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class Sdk(object):

    """Docstring for sdk. """

    categories = dict()

    def __init__(self, configuration_file_path, domain_id, headers=None):
        """TODO: to be defined1. """
        self.cfg = self.__init_conf__(configuration_file_path)
        self.host = self.cfg.get('pdp').get('host')
        self.port = self.cfg.get('pdp').get('port')
        self.endpoint = self.cfg.get('pdp').get('endpoint')
        self.domain_id = domain_id
        self.headers = headers
        logging.debug(
            'Initializing SDK using: [host {}, port: {}, endpoint: {}, domain_id: {}, headers: {}]'
            .format(self.host, self.port, self.endpoint, self.domain_id, self.headers))
        self.net = Net(self.host, self.endpoint,
                       self.domain_id, self.port, self.headers)

    def add_attribute(self, category, attribute):
        """TODO: Docstring for add_attribute.

        :category: TODO
        :: TODO
        :returns: TODO

        """
        logging.debug("Adding attribute to category")
        updated_attr = attribute
        if 'Category' not in self.categories:
            self.categories['Category'] = []

        else:
            cat = self.__is_category_exists__(category)
            """
                If the category already exist we update the list of
                attributes of this category. We create the list if
                it doesn't already exist
            """
            if cat:
                updated_attr = self.__update_category__(attribute, cat)

        self.categories['Category'].append({
            'CategoryId': str(category), 'Attribute': updated_attr
        })

    def __init_conf__(self, conf_file_path):
        """TODO: Docstring for __read_conf__.

        :conf_file_path: TODO
        :returns: TODO

        """
        with open(conf_file_path, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        logging.debug("Dumping configuration")
        logging.debug(cfg)

        return cfg

    def get_authz(self):
        """TODO: Docstring for get_authz.

        :subject: TODO
        :resource: TODO
        :action: TODO
        :environment: TODO
        :returns: TODO

        """

        request = self.__build_request()
        logging.debug(json.dumps(request, default=Tools.default_serializer))
        self.net.send_request(request)

    def __update_category__(self, attribute, category):
        """TODO: Docstring for __update_category__.

        :attribute: TODO
        :category: TODO
        :returns: TODO

        """
        updated_attr = []
        updated_attr.append(category['Attribute'])
        updated_attr.append(attribute)
        self.categories['Category'].remove(category)

        return updated_attr

    def __is_category_exists__(self, category):
        """
        Search if category is inside the self.categories object

        :category: Enum Category
        :returns: return empty dict if the category is not found and the  
                    category object if found

        """
        logging.debug("Searching if {} is already present".format(category))
        for cat in self.categories['Category']:
            """
            TODO: Implement proper category comparaison in order to avoid string comparaison
            """
            if str(category) is str(cat['CategoryId']):
                logging.debug("Found it!")
                print(cat)
                return cat

        return {}

    def __build_request(self):
        data = {'Request': self.categories}

        return data
