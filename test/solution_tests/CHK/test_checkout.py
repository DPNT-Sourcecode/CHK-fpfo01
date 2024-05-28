from lib.solutions.CHK.checkout_solution import checkout

def test_checkout():
    result = checkout("UUUU")
    assert result == 120

    result = checkout("UUU")
    assert result == 120

    result = checkout("NNNM")
    assert result == 120

    result = checkout("RRRQ")
    assert result == 150

    result = checkout("VV")
    assert result == 90

    result = checkout("PPPPP")
    assert result == 200
    
    result = checkout("QQQ")
    assert result == 80

    result = checkout("KK")
    assert result == 120

    result = checkout("HHHHH")
    assert result == 45

    result = checkout("HHHHHHHHHH")
    assert result == 80

    result = checkout("HHHHHHHHHHH")
    assert result == 90

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