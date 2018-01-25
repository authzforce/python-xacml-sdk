#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : core/utils.py
# Author            : hargathor <3949704+hargathor@users.noreply.github.com>
# Date              : 25.01.2018
# Last Modified Date: 25.01.2018
# Last Modified By  : hargathor <3949704+hargathor@users.noreply.github.com>


from pyxacml_sdk.model.attribute import Attribute


class Tools(object):

    @staticmethod
    def default_serializer(o):
        """TODO: Docstring for default_serializer.
        :returns: TODO

        """
        if(isinstance(o, Attribute)):
            return o.__to_dict__()
        return o.__dict__
