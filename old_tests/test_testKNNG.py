import stann

stann.DIM = 3
stann.DATA_TYPE = stann.DATA_TYPE_DOUBLE

Size = 500
k = 5
nnMin = -(2.0**32)
nnMax =  2.0**32


data = stann.createPointVector()
bf_ans = stann.createAnswerVector()

for i in range(Size):
    data.push_back(stann.newRandomPoint(nnMin, nnMax))

bf = stann.bruteNN(data[0], Size)
sfc = stann.sfcnn_knng(data[0], Size, k)

success = True
for i in range(Size):
    bf.ksearch(data[i], k+1, bf_ans)

    for j in range(1, k+1):
        if bf_ans[j] != sfc[i][j-1]:
            #print("i={0}, bf[{1}] = {2}, sfcnn[{1}]={3}".format(i,j,bf_ans[j], sfcnn_ans[j]))
            success = False


print(success)
