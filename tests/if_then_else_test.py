import os
import pytest

from problems import if_then_else 

@pytest.mark.parametrize("test_input,expected", 
                         [
                             (1, 'Weird\n') ,
                             (3, 'Weird\n'),
                             
                             (2, 'Not Weird\n'),
                             (4, 'Not Weird\n'),
                             
                             (6, 'Weird\n'),
                             (8, 'Weird\n'),  
                             
                             (24, 'Not Weird\n'),
                             (26, 'Not Weird\n')                         
                          ]
                        )
def test_if_then_else(capsys, test_input, expected):
    if_then_else.if_then_else(test_input)
    captured = capsys.readouterr()
    assert captured.out == expected