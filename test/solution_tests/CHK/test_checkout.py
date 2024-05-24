from lib.solutions.CHK.checkout_solution import checkout

def test_checkout():
    result = checkout("AAAA")
    assert result == 180
    
    result = checkout("AB")
    assert result == 80

    result = checkout("ABB")
    assert result == 95

    result = checkout("E")
    assert result == -1

    result = checkout("ABCDABCD")
    assert result == 215