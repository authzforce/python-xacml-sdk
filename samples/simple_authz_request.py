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

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


if __name__ == "__main__":
    logging.info("Trying to request a simple XACML authorization decision")
    sdk = sdk.Sdk(
        # Path to our configuration file
        "/tmp/pyxacml_sdk/config.yml",
        # Domain ID
        "PvQkPMo-EeeHNgJCCgEAAw")

    # Building our attributes
    subject_attribute_romain = Attribute(
        Attribute_ID.SUBJECT_ID, "Romain", Datatype.STRING)
    subject_attribute_cyril = Attribute(
        Attribute_ID.SUBJECT_ID, "Cyril", Datatype.STRING)
    action_attribute = Attribute(
        Attribute_ID.ACTION_ID, "GET", Datatype.STRING)
    ressource_attribute = Attribute(
        Attribute_ID.RESOURCE_ID, "http://rootme.org", Datatype.STRING)

    # Adding attributes to our request
    sdk.add_attribute(Category_ID.ACCESS_SUBJECT, subject_attribute_romain)
    sdk.add_attribute(Category_ID.ACCESS_SUBJECT, subject_attribute_cyril)
    sdk.add_attribute(Category_ID.INTERMEDIARY_SUBJECT,
                      subject_attribute_cyril)
    sdk.add_attribute(Category_ID.RESOURCE, ressource_attribute)
    sdk.add_attribute(Category_ID.ACTION, action_attribute)

    # Asking for Authorization
    decision, raw = sdk.get_authz()
