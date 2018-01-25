#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : model/attribute.py
# Author            : hargathor <3949704+hargathor@users.noreply.github.com>
# Date              : 24.01.2018
# Last Modified Date: 24.01.2018
# Last Modified By  : hargathor <3949704+hargathor@users.noreply.github.com>

import logging
import sys
import json

from pyxacml_sdk.model.attribute import Attribute
from pyxacml_sdk.model.attribute_ids import Attribute_ID
from pyxacml_sdk.model.categories import Category_ID
from pyxacml_sdk.model.datatypes import Datatype

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class Category(object):

    def __init__(self,
                 category_id,
                 attributes=[],
                 id=None,
                 content=None):
        """
        Build an XACML attribute to be used in building the category
        category_id is the id defined by an enum Categories.
            It's used to identify the type of XACML category used.
            At least an subject, resource and action category
                needs to be specified in a request.
        id is optionnal. It's used as a reference when doing multirequests
            (check multi request profile)
        Content is optionnal. It's used as a blob usually filled with xml.
            The engine need to do xpath afterwards to support it
        :returns: TODO

        """
        self.category_id = category_id
        self.attributes = attributes
        self.id = id
        self.content = content

    def default(self):
        return self.__str__()

    def __str__(self):
        data = {}
        data['CategoryId'] = self.category_id.name
        if(self.id):
            data['id'] = self.id
        if(self.content):
            data['Content'] = self.content
        my_attributes = []
        for attribute in self.attributes:
            my_attributes.append(attribute.__str__())
        data['Attribute'] = my_attributes

        return json.dumps(data)
