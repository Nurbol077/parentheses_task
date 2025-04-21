import time
from main import countWellFormedParenthesis

def test_performance():
    start = time.time()
    for n in range(1, 16):
        countWellFormedParenthesis(n)
    duration = time.time() - start
    assert duration < 1.0  # должно работать быстро