ctypes = [
    ('UShort', 'unsigned short'),
    ('Short', 'short'),
    ('UInt', 'unsigned int'),
    ('Int', 'int'),
    ('ULong', 'unsigned long'),
    ('Long', 'long'),
    ('Float', 'float'),
    ('Double', 'double'),
]

for i in range(1,6):
    for key, value in ctypes:
        name = "%template(sfcnn_knng_DPoint_{}d_{})".format(i,key)
        declaration = "::sfcnn_knng<reviver::dpoint<{0:<14}, {1}>, {1}, {0:<14}>;".format(value, i)
        print("{0:<45}{1}".format(name, declaration))
    print()
