import pytest
from testcases import divide
def test_divide():
    assert divide(6,2) == 3.0
    assert divide(6,0) == "Cannot divide by zero"
test_divide()