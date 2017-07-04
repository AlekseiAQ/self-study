import pytest

from binary_search import binary_search

EXAMPLES = (
    ('args', 'expected'),
    [
        (([0, 1, 2, 8, 13, 17, 19, 32, 42], 3), False),
        (([0, 1, 2, 8, 13, 17, 19, 32, 42], 8), True),
        (([], 13), False),
        (([1], 15), False),
        (([15], 15), True),
        (([1, 2], 15), False),
        (([1, 15], 15), True),
        (([0, 1, 2, 8, 13, 17, 19, 32, 42], 0), True),
        (([0, 1, 2, 8, 13, 17, 19, 32, 42], 42), True),
        (([0, 1, 2, 8, 13, 17, 19, 19, 32, 42], 19), True),
        (([0, 1, 2, 8, 13, 17, 19, 19, 32, 42], 42), True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert binary_search(*args) == expected
