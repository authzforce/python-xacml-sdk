#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : model/datatypes.py
# Author            : hargathor <3949704+hargathor@users.noreply.github.com>
# Date              : 24.01.2018
# Last Modified Date: 24.01.2018
# Last Modified By  : hargathor <3949704+hargathor@users.noreply.github.com>

from enum import Enum


class Datatype(Enum):
    STRING = "http://www.w3.org/2001/XMLSchema#string"
    BOOLEAN = "http://www.w3.org/2001/XMLSchema#boolean"
    INTEGER = "http://www.w3.org/2001/XMLSchema#integer"
    DOUBLE = "http://www.w3.org/2001/XMLSchema#double"
    TIME = "http://www.w3.org/2001/XMLSchema#time"
    DATE = "http://www.w3.org/2001/XMLSchema#date"
    DATETIME = "http://www.w3.org/2001/XMLSchema#dateTime"
    ANYURI = "http://www.w3.org/2001/XMLSchema#anyURI"
    HEXBINARY = "http://www.w3.org/2001/XMLSchema#hexBinary"
    BASE64BINARY = "http://www.w3.org/2001/XMLSchema#base64Binary"
    DAYTIMEDURATION = "http://www.w3.org/2001/XMLSchema#dayTimeDuration"
    YEARMONTHDURATION = "http://www.w3.org/2001/XMLSchema#yearMonthDuration"
    X500NAME = "urn:oasis:names:tc:xacml:1.0:data-type:x500Name"
    RFC822NAME = "urn:oasis:names:tc:xacml:1.0:data-type:rfc822Name"
    IPADDRESS = "urn:oasis:names:tc:xacml:2.0:data-type:ipAddress"
    DNSNAME = "urn:oasis:names:tc:xacml:2.0:data-type:dnsName"
    XPATHEXPRESSION = "urn:oasis:names:tc:xacml:3.0:data-type:xpathExpression"

    def __str__(self):
        return '{0}'.format(self.value)
