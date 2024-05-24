from lib.solutions.CHK.checkout_solution import checkout

def test_checkout():
    result = checkout("AAA")
    assert result == 130