
import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')

def Is_num_or_dot(value: str) -> bool:
    return bool(NUM_OR_DOT_REGEX.search(value))

def Is_empty(value: str):
    return len(value) == 0

def Is_valid_number(value: str):
    valid = False
    try:
        float(value)
        valid = True
    except ValueError:
        ...
    return valid