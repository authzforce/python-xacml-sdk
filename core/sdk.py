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
from array import *
from pprint import pprint

from pyxacml_sdk.core.net import Net
from pyxacml_sdk.core.utils import Tools
from pyxacml_sdk.model.categories import Category_ID
from pyxacml_sdk.model.category import Category

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class Sdk(object):

    categories = dict()
    """Docstring for sdk. """

    def __init__(self, endpoint, domain_id, port=8080, headers=None):
        """TODO: to be defined1. """
        logging.debug(
            'Initializing SDK using: [endpoint: {}, port: {}, domain_id: {}, headers: {}]'
            .format(endpoint, port, domain_id, headers))
        self.net = Net(endpoint, port, domain_id, headers)

    def add_attribute(self, category, attribute):
        """TODO: Docstring for add_attribute.

        :category: TODO
        :: TODO
        :returns: TODO

        """
        logging.debug("Adding attribute to category")
        updated_attr = attribute
        if('Category' not in self.categories):
            self.categories['Category'] = []

        else:
            cat = self.__is_category__(category)
            print(cat)
            if cat:
                attributes = self.categories['Category'].pop(cat)
                print(attributes)

            self.categories['Category'].append({
                'CategoryId': str(category), 'Attribute': updated_attr
            })

    def get_authz(self):
        """TODO: Docstring for get_authz.

        :subject: TODO
        :resource: TODO
        :action: TODO
        :environment: TODO
        :returns: TODO

        """

        # request = self.__build_request()
        # logging.debug(json.dumps(request, indent=4,
        #                          default=Tools.default_serializer))

    def update_category(self, category, attribute):
        """TODO: Docstring for update_attribute.

        :category: TODO
        :attribute: TODO
        :returns: TODO

        """
        pass

    def __is_category__(self, category):
        """
        Searching if category is inside the self.categories object

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
                return cat

        return {}

    def __build_request(self):
        data = {'Request': self.categories}

        return data

    def __build_category_from_str_attribute(self,
                                            attribute,
                                            category):
        """TODO: Docstring for function.

        :attribute: TODO
        :category: TODO
        :returns: TODO

        """
        attributes = []
        attributes.append(attribute)

        return Category(category, attributes)
