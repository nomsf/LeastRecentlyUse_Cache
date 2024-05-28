import LeastRecentlyUsedCache as lru

def test1():
    '''
    Expected output:
    1
    2
    -1
    2
    3
    '''
    cache = lru.LeastRecentlyUsedCache(2)

    cache.put(1, 1)

    cache.put(2, 2)
    # cache.print()
    print(cache.get(1))
    print(cache.get(2))
    cache.put(3, 3)
    print(cache.get(1))
    print(cache.get(2))
    print(cache.get(3))

def test2():
    '''
    Expected output:
    1
    2
    -1
    -1
    '''
    cache = lru.LeastRecentlyUsedCache(2)

    cache.put(1, 1)

    cache.put(2, 2)
    # cache.print()
    print(cache.get(1))
    print(cache.get(2))
    print(cache.get(3))
    print(cache.get(4))

def test3():
    '''
    5
    Capacity:  10
    Cache:  {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11}
    Queue:  2,3,4,6,7,8,9,5,10,11,
    Queue Dict:  {2: 2, 3: 3, 4: 4, 6: 6, 7: 7, 8: 8, 9: 9, 5: 5, 10: 10, 11: 11}
    Queue Head:  2
    Queue Tail:  11
    '''
    length = 10
    cache = lru.LeastRecentlyUsedCache(10)
    for i in range(length):
        cache.put(i, i)
    
    print(cache.get(5))
    cache.put(10, 10)
    cache.put(11, 11)

    cache.print()

def test4():
    '''
    -1
    1
    2
    3
    Capacity:  5
    Cache:  {2: 2, 3: 3, 10: 10, 11: 11, 12: 12}
    Queue:  2,3,10,11,12,
    Queue Dict:  {2: 2, 3: 3, 10: 10, 11: 11, 12: 12}
    Queue Head:  2
    Queue Tail:  12
    '''
    cache = lru.LeastRecentlyUsedCache(5)

    for i in range(5):
        cache.put(i, i)
    
    print(cache.get(5))
    print(cache.get(1))
    print(cache.get(2))
    print(cache.get(3))

    for i in range(3):
        cache.put(i+10, i+10)
    
    cache.print()
    

test1()
test2()
test3()
test4()