import os
import pytest

from problems import leap_year as ly


@pytest.mark.parametrize("test_input,expected", 
                         [(2000, True), 
                          (2400, True), 
                          (1800, False), 
                          (1900, False), 
                          (2100, False), 
                          (2200, False), 
                          (2300, False), 
                          (2500, False), 
                          (1964, True), 
                          (1971, False)]
                        )
def test_leap_year(test_input: int,expected: bool):
        assert ly.is_leap(test_input) == expected


    


