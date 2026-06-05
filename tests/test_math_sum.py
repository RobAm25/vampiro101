from math_ import sum

def test_sum_2_3_equals_5():
  assert sum(2, 3) == 5

def test_sum_3_3_equals_6():
    assert sum(3,3) == 6

def test_sum_m1_1_equals_0():
    assert sum(-1,1) == 0