#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : model/categories.py
# Author            : hargathor <3949704+hargathor@users.noreply.github.com>
# Date              : 23.01.2018
# Last Modified Date: 23.01.2018
# Last Modified By  : hargathor <3949704+hargathor@users.noreply.github.com>

from enum import Enum
"""

"""


class Category_ID(Enum):
    ACCESS_SUBJECT = "urn:oasis:names:tc:xacml:1.0:subject-category:access-subject"
    RECIPIENT_SUBJECT = "urn:oasis:names:tc:xacml:1.0:subject-category:recipient-subject"
    INTERMEDIARY_SUBJECT = "urn:oasis:names:tc:xacml:1.0:subject-category:intermediary-subject"
    RESOURCE = "urn:oasis:names:tc:xacml:3.0:attribute-category:resource"
    ACTION = "urn:oasis:names:tc:xacml:3.0:attribute-category:action"
    ENVIRONMENT = "urn:oasis:names:tc:xacml:3.0:attribute-category:environment"
    CODEBASE = "urn:oasis:names:tc:xacml:1.0:subject-category:codebase"
    REQUESTING_MACHINE = "urn:oasis:names:tc:xacml:1.0:subject-category:requesting-machine"

    def __str__(self):
        return '{0}'.format(self.value)
