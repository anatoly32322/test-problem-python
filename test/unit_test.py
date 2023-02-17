"""
Unit tests
"""
import unittest
from solution import solve
from utils import check_match, is_bracket_sequence


class TestSolution(unittest.TestCase):
    """
    TestSolution class
    """
    def test_solution(self) -> None:
        """
        Test solution correctness
        :return:
        """
        correct_results = [True, False, False, True, True]
        sequences = ['()', '((', '({)}', '(()){[()]}', '']
        outputs = list(map(solve, sequences))
        self.assertEqual(correct_results, outputs)

    def test_check_match(self) -> None:
        """
        Test check_match method
        :return:
        """
        correct_results = [True, False, False, False, False, True, True, False]
        brackets = [
            ('(', ')'), ('(', ']'), ('(', '}'), ('[', ')'),
            ('[', '}'), ('[', ']'), ('{', '}'), ('{', ']'),
        ]
        outputs = list(map(lambda brck: check_match(brck[0], brck[1]), brackets))
        self.assertEqual(correct_results, outputs)

    def test_is_bracket_sequence(self) -> None:
        """
        Test is_bracket_sequence method
        :return:
        """
        correct_results = [True, True, False, False, False]
        brackets = ['())()(()', '[](){}][', '[][]34]', '()().]', 'abs']
        outputs = list(map(is_bracket_sequence, brackets))
        self.assertEqual(correct_results, outputs)
