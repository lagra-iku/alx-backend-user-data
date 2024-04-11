#!/usr/bin/env python3
"""
Regex-ing
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """a function called filter_datum that returns the log msg obfuscated"""
    for f in fields:
        message = re.sub(f'{f}=.*?{separator}',
                         f'{f}={redaction}{separator}', message)
    return message


if __name__ == "__main__":
    main()
