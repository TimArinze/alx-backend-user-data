#!/usr/bin/env python3
"""
Regex-ing
"""
import re
from typing import List
import logging


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


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: str):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """formats log record"""
        filter_data = filter_datum(list(self.fields), self.REDACTION,
                                   super().format(record), self.SEPARATOR)
        return filter_data
