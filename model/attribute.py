#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : model/attribute.py
# Author            : hargathor <3949704+hargathor@users.noreply.github.com>
# Date              : 24.01.2018
# Last Modified Date: 24.01.2018
# Last Modified By  : hargathor <3949704+hargathor@users.noreply.github.com>
import json
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class Attribute(object):
    def __init__(self,
                 attr_id,
                 value,
                 datatype,
                 issuer="",
                 include_in_result=False):
        """
        Build an XACML attribute to be used in building the category
        :returns: TODO

        """
        self.attr_id = attr_id
        self.value = value
        self.datatype = datatype
        self.issuer = issuer
        self.include_in_result = include_in_result
        logging.debug(self.datatype)
        # logging.debug("Attribute built: {}".format(self))

    def __to_dict__(self):
        data = {}
        data['AttributeId'] = str(self.attr_id)
        data['Value'] = self.value
        if(self.issuer):
            data['Issuer'] = self.issuer
        data['DataType'] = str(self.datatype)
        data['IncludeInResult'] = self.include_in_result

        return data

    def __str__(self):
        return json.dumps(self.__dict__)
