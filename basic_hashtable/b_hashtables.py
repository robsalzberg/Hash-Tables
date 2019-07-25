

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for x in string:
        hash = (( hash << 5) + hash) + ord(x)
    return (hash % max)


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    i = hash(key, len(hash_table.storage))
    pair = Pair(key, value)
    stored_pair = hash_table.storage[i]

    if stored_pair is not None:
        if stored_pair.key != key:
            print("Warning, overwriting old key value pair")
    
    hash_table.storage[i] = pair


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    i = hash(key, len(hash_table.storage))

    if hash_table.storage[i].key != key or hash_table.storage[i] is None:
        print("Warning, the key you are wanting to delete is not here")
    
    hash_table.storage[i] = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    i = hash(key, len(hash_table.storage))

    if hash_table.storage[i] is not None and hash_table.storage[i].key == key:
        return hash_table.storage[i].value
    else:
        return None


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
