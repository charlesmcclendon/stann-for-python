import sys
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
MAX_DIM = 5
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

def getStannName(prefix, hasPoint=False, dim=None, dataType=None):
    dim = dim if dim else DIM
    dataType = dataType if dataType else DATA_TYPE
    if hasPoint:
        return "{0}_{1}_{2}d_{3}".format(
				prefix
				, POINT_TYPES[POINT_TYPE]
                                , dim
				, DATA_TYPES[dataType])
    else:
        return "{0}_{1}d_{2}".format(
                                prefix
                                , dim
                                , DATA_TYPES[dataType])

def getStannFunctionName(prefix, hasPoint=False, dim=None, dataType=None):
    return getStannName(prefix, hasPoint, dim, dataType)

def getStannFunction(prefix, hasPoint=False, dim=None, dataType=None):
    funcName = getStannFunctionName(prefix, hasPoint, dim, dataType)
    return getattr(stann_backend, funcName)

def getStannClassName(prefix, hasPoint=False, dim=None, dataType=None):
    return getStannName(prefix, hasPoint, dim, dataType)

def getStannClass(prefix, hasPoint=False, dim=None, dataType=None):
    className = getStannClassName(prefix, hasPoint, dim, dataType)
    return getattr(stann_backend, className)

def createPointVector():
    func = getStannFunction("Vector", hasPoint=True)
    return func() 

def createDataVector(dataType=None):
    dataType = dataType if dataType else DATA_TYPE
    className = "{0}Vector".format(DATA_TYPES[dataType])
    return getattr(stann_backend, className)()

def createAnswerVector():
    return createDataVector(dataType=DATA_TYPE_ULONG)

def bruteNN(pointVector, n):
    return getStannClass("bruteNN", hasPoint=True)(pointVector, n)

def sfcnn(pointVector, n):
    return getStannClass("sfcnn", hasPoint=True)(pointVector, n)

def newRandomPoint(min_val, max_val):
    func = getStannFunction("newRandomPoint", hasPoint=True)
    return func(min_val, max_val)

def configure(dim, data_type, point_type=POINT_TYPE_DPOINT):
    DIM = dim
    DATA_TYPE = data_type
    POINT_TYPE = POINT_TYPE_DPOINT


for dataTypeKey, dataTypeValue in DATA_TYPES.items():
    className = "{0}Vector".format(dataTypeValue)
    thisModule = sys.modules[__name__]
    setattr(thisModule, className, getattr(stann_backend, className))

# To patch the DPoint_DIMd_TYPE functions with a points() func
# that returns a TYPEArray; it's a wrapper arond point_begin()
for pointKey, pointValue in POINT_TYPES.items():
    for dataTypeKey, dataTypeValue in DATA_TYPES.items():
        for d in range(MAX_DIM):
            dim = d+1
            pointClassName = "{0}_{1}d_{2}".format(
                                            pointValue
                                            , dim
                                            , dataTypeValue)
            pointClass = getattr(stann_backend, pointClassName)
            arrayClassFuncName = "{0}Array_frompointer".format(dataTypeValue)
            arrayClassFunc = getattr(stann_backend, arrayClassFuncName)
            setattr(pointClass, "points"
                        , lambda self, bound_arrayClassFunc=arrayClassFunc
                            : bound_arrayClassFunc(self.point_begin()))

            dimAttrName = "_{0}__DIM".format(pointClassName)
            setattr(pointClass, "DIM", getattr(pointClass, dimAttrName))
            setattr(pointClass, "point_set"
                        , lambda self, 
                            : set([self.points()[i] for i in range(self.DIM)]))

            setattr(pointClass, "DATA_TYPE", dataTypeValue)

            vectorClass = getStannClass("Vector", hasPoint=True, dim=dim, dataType=dataTypeKey)
            setattr(vectorClass, "DIM", dim)
            setattr(vectorClass, "DATA_TYPE", dataTypeValue)


            algoNames = ["bruteNN", "sfcnn"]
            for algoName in algoNames:
                if dim != 3 or dataTypeValue != "Int":
                    continue

                algoClass = getStannClass(algoName, hasPoint=True, dim=dim, dataType=dataTypeKey)
                setattr(algoClass, "DIM", dim)
                setattr(algoClass, "DATA_TYPE", dataTypeValue)
                setattr(algoClass, "POINT_TYPE", pointValue)
                setattr(algoClass, "createDataVector"
                        , lambda self, bound_dataType=dataTypeKey
                            : createDataVector(dataType=bound_dataType))

