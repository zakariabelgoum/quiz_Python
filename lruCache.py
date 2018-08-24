import collections
from datetime import datetime
import time

class LRUCache:

    ''' we use an OrdredDict object that is a dictionary that remembers the order in which its contents are added '''
    def __init__(self, capacity,timeExpiration):
        self.capacity = capacity 
        self.cachDictionary = collections.OrderedDict() # ordered dictionary that order items in cachDictionary
        self.timeExpiration=timeExpiration
        self.timestamp=datetime.now()

    def set(self, key, value):
        try:
            self.cachDictionary.pop(key) #remove the item from dictionary
        except KeyError:
            if len(self.cachDictionary) >= self.capacity:
                self.cachDictionary.popitem(last=False) #remove the least used item
        self.cachDictionary[key] = value
        self.timeExpiration +=1

    def get(self, key):
        try:
            value = self.cachDictionary.pop(key) #remove the item and get the value that corresponds to the key
            self.cachDictionary[key] = value
            return value
        except KeyError:
            return -1
        self.timeExpiration +=1

    #To do add function to verify time expiration for the cache
    def verifyCacheExpiration(self):
        ''' verify if the cache is used within the time of expiration time '''
        now=datetime.now()
        delta=now-self.timestamp
        if delta.seconds > self.timeExpiration:
            print('time has expired')
            cachDictionary.clear()
    
#implementing tests
lru = LRUCache(4,5)
lru.set(1,'one')
lru.set(2,'two')
lru.set(3,'three')
print(lru.get(1))
lru.set(4,'four')
lru.set(5,'five')
print(lru.get(2))




