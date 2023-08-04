#!/usr/bin/env python3
"""
Regex-ing
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    returns the log message obfuscated
    """
    for field in fields:
        """ {field}=.*?; means from {field}= to ;
        .*? is non-gready copy. it copys from = and ends at ;
        """
        message = re.sub(rf'{field}=.*?;',
                         f'{field}={redaction}{separator}', message)
    return message
