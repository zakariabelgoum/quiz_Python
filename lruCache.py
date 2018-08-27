############## Code by Zakaria Belgoum ###########
#lruCache implements a true LRU cache
#Pylru provides a cache class with a simple dict interface.
#Basic operations are get and set items


import collections
from datetime import datetime
import time

class LRUCache:
   
    def __init__(self, capacity):
        self.capacity = capacity 
        self.cacheDictionary = collections.OrderedDict() #we use an ordered dictionary that remembers the order entries were added
        
           
    def set(self, key, value):
        try:
            self.cacheDictionary.pop(key)  
        except KeyError:
            if len(self.cacheDictionary) >= self.capacity:
                self.cacheDictionary.popitem(last=False) 
        self.cacheDictionary[key] = value
        

    def get(self, key):
        try:
            value = self.cacheDictionary.pop(key) 
            self.cacheDictionary[key] = value 
            return value
        except KeyError:
            return -1
        
    #To do list
    #add function to validate expiration of the cache
    #add geo distributed architecture
    #add spacial reference
    #add replication of data
    #writing in real time


if __name__ == '__main__' :

    lru = LRUCache(4)
    lru.set(1,'one')
    lru.set(2,'two')
    lru.set(3,'three')
    lru.set(4,'four')
    lru.set(5,'five')
    print(dict(lru.cacheDictionary))
    lru.get(2)
    print(dict(lru.cacheDictionary))





