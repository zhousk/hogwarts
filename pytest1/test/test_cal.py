import pytest
from pytest1.cal import Cal


class TestCal():

    def setup(self):
        self.cal = Cal()

    @pytest.mark.parametrize('a,b,c', [
        [1, 2, 2],
        [0, 1, 0],
        [-1, -1, 1],
        [-1, 1, -1],
        [100, 55, 5500],
        [1.1, 1, 1.1]
    ])
    def test_mul(self, a, b, c):
        assert self.cal.mul(a, b) == c

    @pytest.mark.parametrize('a,b,c', [
        [2, 2, 1],
        [1, 2, 0.5],
        [1.1, 1.1, 1],
        [100, 50, 2],
        [1.1, 1, 1.1],
        [0, 1, 0],
        [0, -1, 0],
        [-1, -2, 0.5]
    ])
    def test_div(self, a, b, c):
        assert self.cal.div(a, b) == c

    @pytest.mark.parametrize('a,b', [
        [2, 0],
        [-1, 0],
        [1, 0]
    ])
    def test_div_exception(self, a, b):
        with pytest.raises(ZeroDivisionError):
            assert self.cal.div(a, b)
