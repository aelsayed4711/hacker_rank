import os
from problem_006_Write_a_function import is_leap

def test_leap_year(capsys):
    is_leap(2000)
    out, err = capsys.readouterr()    
    assert out == "True"