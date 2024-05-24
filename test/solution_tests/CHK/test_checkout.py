from lib.solutions.CHK.checkout_solution import checkout

def test_checkout():
    result = checkout("A")
    assert result == 50