from lib.solutions.CHK.checkout_solution import checkout

def test_checkout():
    result = checkout("AAAA")
    assert result == 180
    
    result = checkout("AB")
    assert result == 80

    result = checkout("ABB")
    assert result == 95

    result = checkout("Z")
    assert result == -1

    result = checkout("ABCDABCD")
    assert result == 215

    result = checkout("EEB")
    assert result == 80

    # result = checkout("EEEEBB")
    # assert result == 160

    # result = checkout("EEBB")
    # assert result == 110