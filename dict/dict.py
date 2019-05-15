from random import randrange

class Dict:

    def __init__(self):
        # not [[]] * 5
        self._hash_table = [[] for _ in range(5)]
        self._p = 109345121 # duza liczba pierwsza
        self._a = randrange(self._p)
        self._b = randrange(self._p)
        print(self._hash_table)

    def _scale(self, key):
        h = hash(key)

        return (self._a * h + self._b) % len(self._hash_table)

    def put(self, key, value):
        index = self._scale(key)
        bucket = self._hash_table[index]
        for p in range(len(bucket)):
            if bucket[p][0] == key:
                bucket[p] = (key, value)
                return

    def get(self, key):
        index = self._scale(key)
        bucket = self._hash_table[index]

        for key1, value in bucket:
            if key1 == key:
                return value


d = Dict()
d.put("Marcin", "kowalski")
print(d.get("Marcin"))
