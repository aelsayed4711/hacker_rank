import os
import leap_year as ly

def test_leap_year():
    out = ly.is_leap(2000)
    #out, err = capsys.readouterr()    
    assert out == "True"
    
    
if __name__ == "__main__":
    test_leap_year()