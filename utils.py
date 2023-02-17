"""
Utils
"""
import re
from config import RE_BR_SEQ, BRACKETS_MATCHING


def read_file(filepath: str) -> str:
    """
    Read file method
    :param filepath:
    :return:
    """
    with open(filepath, 'r', encoding='utf-8') as fin:
        string = ''
        for line in fin:
            string += line.strip().replace(' ', '')
        return string


def check_match(open_bracket: str, close_bracket: str) -> bool:
    """
    Check bracket match method
    :param open_bracket:
    :param close_bracket:
    :return:
    """
    return (open_bracket, close_bracket) in BRACKETS_MATCHING


def is_bracket_sequence(string: str) -> bool:
    """
    Check if string is bracket sequence or not
    :param string:
    :return:
    """
    return bool(
        re.fullmatch(
            RE_BR_SEQ,
            string
        )
    )
