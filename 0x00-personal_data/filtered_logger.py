#!/usr/bin/env python3
"""
Regex-ing
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    returns the log message obfuscated
    """
    for field in fields:
        """ {field}=.*?; means from {field}= to ;
        .*? is non-gready copy. it copys from = and ends at ;
        """
        message = re.sub(rf'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
