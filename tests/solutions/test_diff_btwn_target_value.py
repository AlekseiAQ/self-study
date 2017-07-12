import pytest

from solutions.diff_btwn_target_value import some_function

EXAMPLES = (
    ('args', 'expected'),
    [
        ((7, [-4, 1, 4, 10, 18]), 4),
        ((7, [-4, 1, 5, 10, 18]), 5),
        ((-7, [-4, 1, 5, 10, 18]), -4),
        ((100, [-4, 1, 5, 10, 18]), 18),
        ((7, [5]), 5),
        ((7, []), []),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert some_function(*args) == expected
