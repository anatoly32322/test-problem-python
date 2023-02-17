"""
Main.py
"""
from exceptions import WrongFileFilling, WrongInput
from solution import solve
from utils import is_bracket_sequence, read_file


def try_to_get_sequence() -> str:
    """
    Method that ask user for input data.
    :return:
    """
    while True:
        input_type = input(
            'If you want to read input data from file write [1] otherwise write [2]: '
        )
        if input_type == '1':
            filepath = input('Write filepath: ')
            try:
                string = read_file(filepath)
                if not is_bracket_sequence(string):
                    raise WrongFileFilling
                return string
            except WrongFileFilling:
                print(
                    '''
                    File fills incorrect data.
                    Please try again.
                    '''
                )
                continue
            except FileNotFoundError:
                print(
                    '''
                    Wrote incorrect filepath.
                    Please try again.
                    '''
                )
                continue
        else:
            string = input('Write bracket sequence: ')
            try:
                if not is_bracket_sequence(string):
                    raise WrongInput
                return string
            except WrongInput:
                print(
                    '''
                    Wrote incorrect string. You should write string that containing only brackets.
                    Please try again.
                    '''
                )
                continue


def main() -> None:
    """
    Main method
    :return:
    """
    sequence = try_to_get_sequence()
    result = solve(sequence)
    print(result)


if __name__ == '__main__':
    main()
