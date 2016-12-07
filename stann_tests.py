import unittest
import stann

TEST_SIZE = 500
K = 5

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


def testZorderLT(dim, dataType, nnMin, nnMax):
    stann.configure(dim, dataType)
    lt = stann.zorderLT()
    
    
    # just assigning min_point and max_point to a random value for now
    min_point = stann.newRandomPoint(0, 100)
    max_point = stann.newRandomPoint(0, 100)
    
    for i in range(stann.DIM):
        min_point[i] = nnMin
        max_point[i] = nnMax
    
    r = stann.newRandomPoint(nnMin, nnMax)
    
    while((r == min_point) or (r == max_point)):
        r = stann.newRandomPoint(nnMin, nnMax)
    
    success = True
    
    
    if not lt(max_point, min_point) or lt(r, min_point) or lt(max_point, r) or not lt(min_point,       max_point) or not lt(min_point, r) or not lt(r, max_point):
        succes = False
    
    return success



class StannTestMethods(unittest.TestCase):

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
    
    def test_testNN_UShort_3d(self):
        self.assertTrue(testNN(3, stann.DATA_TYPE_USHORT, TEST_SIZE, K, 0, 25000))

    def test_testNN_UShort_5d(self):
        self.assertTrue(testNN(5, stann.DATA_TYPE_USHORT, TEST_SIZE, K, 0, 12000))

    def test_testNN_UInt_3d(self):
        self.assertTrue(testNN(3, stann.DATA_TYPE_UINT, TEST_SIZE, K, 0, 1000000000))

    def test_testNN_UInt_5d(self):
        self.assertTrue(testNN(5, stann.DATA_TYPE_UINT, TEST_SIZE, K, 0, 1000000000))

    def test_testNN_ULong_3d(self):
        self.assertTrue(testNN(3, stann.DATA_TYPE_ULONG, TEST_SIZE, K, 0, 1000000000))

    def test_testNN_ULong_5d(self):
        self.assertTrue(testNN(5, stann.DATA_TYPE_ULONG, TEST_SIZE, K, 0, 1000000000))
    
    def test_testNN_Float_3d(self):
        self.assertTrue(testNN(3, stann.DATA_TYPE_FLOAT, TEST_SIZE, K, -(2.0**12), 2.0**12))

    def test_testNN_Double_3d(self):
        self.assertTrue(testNN(3, stann.DATA_TYPE_DOUBLE, TEST_SIZE, K, -(2.0**32), 2.0**32))

    def test_testNN_Double_3d_between_neg1_and_1(self):
        self.assertTrue(testNN(3, stann.DATA_TYPE_DOUBLE, TEST_SIZE, K, -1, 1))

    def test_testKNNG_Double_3d(self):
        self.assertTrue(testKNNG(3, stann.DATA_TYPE_DOUBLE, TEST_SIZE, K, -(2.0**32), 2.0**32))

    def test_testKNNG_Float_3d(self):
        self.assertTrue(testKNNG(3, stann.DATA_TYPE_FLOAT, TEST_SIZE, K, -(2.0**12), 2.0**12))

    def test_testKNNG_Double_3d_between_neg1_and_1(self):
        self.assertTrue(testNN(3, stann.DATA_TYPE_DOUBLE, TEST_SIZE, K, -1, 1))

    def test_zorderLT_UInt_3d(self):
        self.assertTrue(testZorderLT(3, stann.DATA_TYPE_UINT, 0, 2**32-1))

    def test_zorderLT_Int_3d(self):
        self.assertTrue(testZorderLT(3, stann.DATA_TYPE_INT, 0, 2**31-1))

    def test_zorderLT_Float_3d(self):
        self.assertTrue(testZorderLT(3, stann.DATA_TYPE_FLOAT, -(2.0**12), 2**12))

    def test_zorderLT_Float_3d_between_0_and_1(self):
        self.assertTrue(testZorderLT(3, stann.DATA_TYPE_FLOAT, 0.0, 1.0))

    def test_zorderLT_Double_3d(self):
        self.assertTrue(testZorderLT(3, stann.DATA_TYPE_DOUBLE, -(2.0**32), 2.0**32))

    def test_zorderLT_Double_3d_between_0_and_1(self):
        self.assertTrue(testZorderLT(3, stann.DATA_TYPE_DOUBLE, 0.0, 1.0))

    def test_sort_UInt_3d(self):
        self.assertTrue(testSORT(3, stann.DATA_TYPE_UINT, TEST_SIZE, 0, 2**32-1))

    def test_sort_Int_3d(self):
        self.assertTrue(testSORT(3, stann.DATA_TYPE_INT, TEST_SIZE, -(2**31-1), 2**31-1))

    def test_sort_Float_3d(self):
        self.assertTrue(testSORT(3, stann.DATA_TYPE_FLOAT, TEST_SIZE, -(2.0**20), 2**20))

    def test_sort_Float_3d_between_0_and_1(self):
        self.assertTrue(testSORT(3, stann.DATA_TYPE_FLOAT, TEST_SIZE, 0, 1))

    def test_sort_Double_3d(self):
        self.assertTrue(testSORT(3, stann.DATA_TYPE_DOUBLE, TEST_SIZE, -(2.0**32), 2.0**32))

    def test_sort_Double_3d_between_0_and_1(self):
        self.assertTrue(testSORT(3, stann.DATA_TYPE_DOUBLE, TEST_SIZE, 0, 1))




#    def test_testNN_Float_3d(self):
#        self.assertTrue(testNN(3, stann.DATA_TYPE_FLOAT, TEST_SIZE, K, -(2.0**12), 2.0**12))
#
#    def test_testNN_Float_3d(self):
#        self.assertTrue(testNN(3, stann.DATA_TYPE_FLOAT, TEST_SIZE, K, -(2.0**12), 2.0**12))
#
#    def test_testNN_Float_3d(self):
#        self.assertTrue(testNN(3, stann.DATA_TYPE_FLOAT, TEST_SIZE, K, -(2.0**12), 2.0**12))
#
#    def test_testNN_Float_3d(self):
#        self.assertTrue(testNN(3, stann.DATA_TYPE_FLOAT, TEST_SIZE, K, -(2.0**12), 2.0**12))
#
#    def test_testNN_Float_3d(self):
#        self.assertTrue(testNN(3, stann.DATA_TYPE_FLOAT, TEST_SIZE, K, -(2.0**12), 2.0**12))

##    def test_testNN_Long_5d(self):
##        self.assertTrue(testNN(5, stann.DATA_TYPE_LONG, TEST_SIZE, K, -1000000000, 1000000000))

if __name__ == "__main__":
    unittest.main()
