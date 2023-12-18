class ImmutableMap:
    def __init__(self, **kwargs):
        self._kwargs = kwargs

    def __len__(self):
        ln = 0
        for l in self._kwargs:
            ln += 1
        return ln
        # return len(self._kwargs)

    def __contains__(self, item):
        for c in self._kwargs:
            if c == item:
                return True
        return False
        # return item in self._kwargs

    def __iter__(self):
        for key in self._kwargs:
            yield key
        # return iter(self._kwargs)

    def __getitem__(self, item):
        return self._kwargs[item]

    def __setitem__(self, key, value):
        raise TypeError("Immutable Mapping type does not support item assignment")

    def __delitem__(self, key):
        raise TypeError("Immutable Mapping type does not support item deletion")

    def __repr__(self):
        return f"Immutable Mapping type({self._kwargs})"

    def keys(self):
        return tuple(key for key in self._kwargs)

    def values(self):
        return tuple(self._kwargs[value] for value in self._kwargs)

    def items(self):
        return tuple((item, self._kwargs[item]) for item in self._kwargs)


if __name__ == "__main__":
    ob = ImmutableMap(a=3, b=4)
    print((ob.items()))
    for i in ob.values():
        print(i)
    ob1 = ImmutableMap()

