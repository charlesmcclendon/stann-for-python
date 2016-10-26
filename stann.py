import stann_backend

DATA_TYPE_USHORT    = 1
DATA_TYPE_SHORT     = 2
DATA_TYPE_INT       = 3
DATA_TYPE_UINT      = 4
DATA_TYPE_ULONG     = 5
DATA_TYPE_LONG      = 6
DATA_TYPE_FLOAT     = 7
DATA_TYPE_DOUBLE    = 8

POINT_TYPE_DPOINT = 1

DIM = 3
DATA_TYPE = DATA_TYPE_INT
POINT_TYPE = POINT_TYPE_DPOINT

POINT_TYPES = {
    POINT_TYPE_DPOINT: "DPoint"
}

DATA_TYPES = {
    DATA_TYPE_USHORT: 	"UShort",
    DATA_TYPE_SHORT: 	"Short",
    DATA_TYPE_UINT: 	"UInt",
    DATA_TYPE_INT: 	"Int",
    DATA_TYPE_ULONG: 	"ULong",
    DATA_TYPE_LONG: 	"Long",
    DATA_TYPE_FLOAT: 	"Float",
    DATA_TYPE_DOUBLE: 	"Double",
}

def getStannFunctionName(prefix, hasPoint=False):
    if hasPoint:
        return "{0}_{1}_{2}d_{3}".format(
				prefix
				, POINT_TYPES[POINT_TYPE]
                                , DIM
				, DATA_TYPES[DATA_TYPE])
    else:
        return "{0}_{1}d_{2}".format(
                                prefix
                                , DIM
                                , DATA_TYPES[DATA_TYPE])

def getStannFunction(prefix, hasPoint=False):
    funcName = getStannFunctionName(prefix, hasPoint)
    return getattr(stann_backend, funcName)


def createPointVector():
    func = getStannFunction("Vector", True)
    return func() 

def newRandomPoint(min_val, max_val):
    func = getStannFunction("newRandomPoint", True)
    return func(min_val, max_val)

def configure(dim, data_type, point_type=POINT_TYPE_DPOINT):
    DIM = dim
    DATA_TYPE = data_type
    POINT_TYPE = POINT_TYPE_DPOINT

#stann_backend.DPoint_3d_Int.points = patch_DPoint_3d_Int_points

# To patch the DPoint_DIMd_TYPE functions with a points() func
# that returns a TYPEArray; it's a wrapper arond point_begin()
for pointKey, pointValue in POINT_TYPES.items():
    for dataTypeKey, dataTypeValue in DATA_TYPES.items():
        for d in range(5):
            pointClassName = "{0}_{1}d_{2}".format(
                                            pointValue
                                            , d+1
                                            , dataTypeValue)
            pointClass = getattr(stann_backend, pointClassName)
            arrayClassFuncName = "{0}Array_frompointer".format(dataTypeValue)
            arrayClassFunc = getattr(stann_backend, arrayClassFuncName)
            setattr(pointClass, "points"
                        , lambda self, bound_arrayClassFunc=arrayClassFunc
                            : bound_arrayClassFunc(self.point_begin()))
