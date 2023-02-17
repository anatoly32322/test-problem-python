"""
Solve problem
"""
from config import OPEN_BRACKETS
from utils import check_match


def solve(sequence: str) -> bool:
    """
    Solution.
    We have stack where we put all opened brackets.
    If we see closed bracket we are checking if upper stack value
    and current bracket is correct bracket sequence.
    If not we return 'False'.
    If stack size isn't 0, we also return 'False'.
    Otherwise we return 'True'.
    :param sequence:
    :return:
    """
    stack = []
    for char in sequence:
        if char in OPEN_BRACKETS:
            stack.append(char)
        else:
            if len(stack) == 0 or not check_match(stack.pop(), char):
                return False
    return len(stack) == 0
