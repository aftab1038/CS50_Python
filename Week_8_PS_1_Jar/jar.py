class Jar:
    # __init__ should initialize a cookie jar with the given capacity, 
    # which represents the maximum number of cookies that can fit in the cookie jar. 
    # If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity can not be Negative!")
        self._capacity = capacity
        self._size = 0

    # __str__ should return a str with 🍪, 
    # where is the number of cookies in the cookie jar. 
    # For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
    def __str__(self):
        return self._size * "🍪"

    # deposit should add n cookies to the cookie jar. 
    # If adding that many would exceed the cookie jar’s capacity, though, deposit should instead raise a ValueError.
    def deposit(self, n):
        if n>self._capacity or self._size+n > self._capacity:
            raise ValueError("Not Enough Capacity in jar!")
        self._size+=n

    # withdraw should remove n cookies from the cookie jar. Nom nom nom. 
    # If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
    def withdraw(self, n):
        if n>self._size or self._size-n < 0:
            raise ValueError("Not Enough Cookies in jar!")
        self._size-=n

    # capacity should return the cookie jar’s capacity.
    @property
    def capacity(self):
        return self._capacity

    # size should return the number of cookies actually in the cookie jar, initially 0.
    @property
    def size(self):
        return self._size 
    
jar = Jar()