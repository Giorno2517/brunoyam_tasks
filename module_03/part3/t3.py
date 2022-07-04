class smart_key(object):
    def __init__(self, obj):
        self.obj = obj

    def __lt__(self, other):
        return (other.obj + self.obj) < (self.obj + other.obj)


join_to_biggest = lambda x: ''.join(sorted(
    map(str, x),
    key=smart_key
))

print(join_to_biggest([45, 21, 12, 99]))
