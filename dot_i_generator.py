ctypes = [
    ('UShort', 'unsigned short'),
    ('Short', 'short'),
    ('Uint', 'unsigned int'),
    ('Int', 'int'),
    ('ULong', 'unsigned long'),
    ('Long', 'long'),
    ('Float', 'float'),
    ('Double', 'double'),
]

for i in range(1,6):
    for key, value in ctypes:
        name = "%template(bruteNN_DPoint_{}d_{})".format(i,key)
        declaration = "::bruteNN<reviver::dpoint<{0:<14}, {1}>>;".format(value, i)
        print("{0:<37}{1}".format(name, declaration))
    print()
