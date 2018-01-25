#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# samples/simple_authz_request.py
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
# File              : samples/simple_authz_request.py
# Author            : hargathor <3949704+hargathor@users.noreply.github.com>
# Date              : 28.11.2017
# Last Modified Date: 28.11.2017
# Last Modified By  : hargathor <3949704+hargathor@users.noreply.github.com>

import json
import logging
import sys

from pyxacml_sdk.core import sdk
from pyxacml_sdk.model.attribute import Attribute
from pyxacml_sdk.model.attribute_ids import Attribute_ID
from pyxacml_sdk.model.categories import Category_ID
from pyxacml_sdk.model.datatypes import Datatype

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


if __name__ == "__main__":
    logging.info("Trying to request a simple XACML authorization request")
    subject_attribute_romain = Attribute(
        Attribute_ID.SUBJECT_ID, "Romain", Datatype.STRING)
    subject_attribute_cyril = Attribute(
        Attribute_ID.SUBJECT_ID, "Cyril", Datatype.STRING)
    sdk = sdk.Sdk(
        "http://authzforce-server",
        "qsjjsfjiaohiozaqjp",
        8080,
        {"Accept": "Application/json"})
    sdk.add_attribute(Category_ID.ACCESS_SUBJECT, subject_attribute_romain)
    sdk.add_attribute(Category_ID.ACCESS_SUBJECT, subject_attribute_cyril)
    sdk.add_attribute(Category_ID.INTERMEDIARY_SUBJECT,
                      subject_attribute_cyril)
    sdk.get_authz()
