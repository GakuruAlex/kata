from descending_order import descending_order

def test_descending_order_with_ascending_9_digit_number():
    
    assert descending_order(123456789) == 987654321
def test_descending_order_with_sorted_number():
      assert descending_order(987654321) == 987654321

def test_descending_order_with_2_digits():
    assert descending_order(15) == 51

def test_descending_order_with_4_digits():
    assert descending_order(8957) == 9875
    
def test_descending_order_with_1_digit():
    assert descending_order(1) == 1
