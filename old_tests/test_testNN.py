import unittest
import stann

def testNN(dim, dataType, size, k, nnMin, nnMax):
    stann.configure(dim, dataType)

    data = stann.createPointVector()
    query = stann.createPointVector()
    bf_ans = stann.createAnswerVector()
    sfcnn_ans = stann.createAnswerVector()
    
    for i in range(size):
        data.push_back(stann.newRandomPoint(nnMin, nnMax))
        query.push_back(stann.newRandomPoint(nnMin, nnMax))
    
    bf = stann.bruteNN(data[0], size)
    sfc = stann.sfcnn(data[0], size)
    
    success = True
    for i in range(size):
        bf.ksearch(query[i], k, bf_ans)
        sfc.ksearch(query[i], k, sfcnn_ans)
    
        for j in range(bf.DIM):
            if bf_ans[j] != sfcnn_ans[j]:
                print("i={0}, bf[{1}] = {2}, sfcnn[{1}]={3}".format(i,j,bf_ans[j], sfcnn_ans[j]))
                success = False
    
    return success

def testKNNG(dim, dataType, size, k, nnMin, nnMax):
    stann.configure(dim, dataType)
    
    data = stann.createPointVector()
    bf_ans = stann.createAnswerVector()
    
    for i in range(size):
        data.push_back(stann.newRandomPoint(nnMin, nnMax))
    
    bf = stann.bruteNN(data[0], size)
    sfc = stann.sfcnn_knng(data[0], size, k)
    
    success = True
    for i in range(size):
        bf.ksearch(data[i], k+1, bf_ans)
    
        for j in range(1, k+1):
            if bf_ans[j] != sfc[i][j-1]:
                #print("i={0}, bf[{1}] = {2}, sfcnn[{1}]={3}".format(i,j,bf_ans[j], sfcnn_ans[j]))
                success = False
    
    
    return success


# example of sorting from the internet
# source: http://danishmujeeb.com/blog/2014/01/basic-sorting-algorithms-implemented-in-python/
# there was some trouble getting things to work with sorted(), since zorder_lt()
# returns a boolean
def bubble_sort(items):
    """ Implementation of bubble sort """
    lt = stann.zorderLT()
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if lt(items[j],  items[j+1]):
                items[j], items[j+1] = items[j+1], items[j]     # Swap!

def testSORT(dim, dataType, size, nnMin, nnMax):
    stann.configure(dim, dataType)
    points = []
    
    for i in range(size):
        points.append(stann.newRandomPoint(nnMin, nnMax))
    
    bubble_sort(points)
    points.reverse()
    success = True

    lt = stann.zorderLT()
    for i in range(size-1):
        if not lt(points[i], points[i+1]):
            success = False
            break
    
    return success

class StannTestMethods(unittest.TestCase):
    TEST_SIZE = 500
    K = 5

    def test_testNN_Short_1d(self):
        self.assertTrue(testNN(1, stann.DATA_TYPE_SHORT, TEST_SIZE, K, -(2**16-1), 2**16-1))

    def test_testNN_Short_5d(self):
        self.assertTrue(testNN(5, stann.DATA_TYPE_SHORT, TEST_SIZE, K, -1200, 1200))

    def test_testNN_Int_3d(self):
        self.assertTrue(testNN(3, stann.DATA_TYPE_INT, TEST_SIZE, K, -1000000000, 1000000000))

    def test_testNN_Int_5d(self):
        self.assertTrue(testNN(5, stann.DATA_TYPE_INT, TEST_SIZE, K, -1000000000, 1000000000))

    def test_testNN_Long_3d(self):
        self.assertTrue(testNN(3, stann.DATA_TYPE_LONG, TEST_SIZE, K, -1000000000, 1000000000))

    def test_testNN_Long_5d(self):
        self.assertTrue(testNN(5, stann.DATA_TYPE_LONG, TEST_SIZE, K, -1000000000, 1000000000))
##
    def test_testNN_UShort_3d(self):
        self.assertTrue(testNN(3, stann.DATA_TYPE_USHORT, TEST_SIZE, K, 0, 2500))

    def test_testNN_UShort_5d(self):
        self.assertTrue(testNN(5, stann.DATA_TYPE_USHORT, TEST_SIZE, K, 0, 1200))

    def test_testNN_UInt_3d(self):
        self.assertTrue(testNN(3, stann.DATA_TYPE_UINT, TEST_SIZE, K, 0, 1000000000))

    def test_testNN_UInt_5d(self):
        self.assertTrue(testNN(5, stann.DATA_TYPE_UINT, TEST_SIZE, K, 0, 1000000000))

    def test_testNN_ULong_3d(self):
        self.assertTrue(testNN(3, stann.DATA_TYPE_ULONG, TEST_SIZE, K, 0, 1000000000))

    def test_testNN_ULong_5d(self):
        self.assertTrue(testNN(5, stann.DATA_TYPE_ULONG, TEST_SIZE, K, 0, 1000000000))
##
##    def test_testNN_Long_5d(self):
##        self.assertTrue(testNN(5, stann.DATA_TYPE_LONG, TEST_SIZE, K, -1000000000, 1000000000))

##    def test_testNN_Long_5d(self):
##        self.assertTrue(testNN(5, stann.DATA_TYPE_LONG, TEST_SIZE, K, -1000000000, 1000000000))

if __name__ == "__main__":
    unittest.main()
