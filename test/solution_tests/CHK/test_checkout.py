from lib.solutions.CHK.checkout_solution import checkout

def test_checkout():
    result = checkout("FF")
    assert result == 20

    result = checkout("FFF")
    assert result == 20

    result = checkout("FFFF")
    assert result == 30

    result = checkout("FFFFFF")
    assert result == 40

    result = checkout("AAAAA")
    assert result == 200

    result = checkout("AAAAAA")
    assert result == 250

    result = checkout("AAAAAAAA")
    assert result == 330

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

    result = checkout("EEEEBB")
    assert result == 160

    result = checkout("EEBB")
    assert result == 110

    result = checkout("EEEBB")
    assert result == 150
