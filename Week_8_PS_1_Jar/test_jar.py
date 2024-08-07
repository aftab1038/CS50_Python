from jar import Jar

# testing __init__ 
def test_init():
    jar1 = Jar()
    assert jar1.capacity == 12
    jar2 = Jar(20)
    assert jar2.capacity == 20


# testing  __str__
def test_str():
    jar1 = Jar()
    assert str(jar1) == ""
    jar1.deposit(5)
    assert str(jar1) == "🍪🍪🍪🍪🍪"
    jar1.deposit(4)
    assert str(jar1) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪"

# testing deposit
def test_deposit():
    jar1 =Jar()
    jar1.deposit(5)
    assert jar1.size == 5
    jar1.deposit(4)
    assert jar1.size == 9
   

# testing withdraw
def test_withdraw():
    jar1 =Jar()
    jar1.deposit(5)
    jar1.withdraw(4)
    assert jar1.size == 1
    jar1.withdraw(1)
    assert jar1.size == 0