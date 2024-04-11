#!/usr/bin/env python3
"""
Regex-ing
"""

import re


def filter_datum(fields, redaction, message, separator):
    """
    a function called filter_datum that returns the log message obfuscated:
    """
    """
    for field in fields:
        mesage = re.sub(f'{field}=.*?{separator}',
                        f'{field}={redaction}{separator}', message)
    return message
    """
    pattern = '|'.join(map(re.escape, fields))
    return re.sub(pattern, redaction, message).replace(f'{separator}{separator}', separator)


if __name__ == "__main__":
    main()
