import stann

success = True

Size = 500
k = 5
nnMin = -1000000000
nnMax =  1000000000

dims = [x+1 for x in range(5)]

for dataType in stann.DATA_TYPES:
    for dim in dims:
                
        data = stann.createPointVector()
        query = stann.createPointVector()
        bf_ans = stann.createAnswerVector()
        sfcnn_ans = stann.createAnswerVector()
        
        
        
        for i in range(Size):
            data.push_back(stann.newRandomPoint(nnMin, nnMax))
            query.push_back(stann.newRandomPoint(nnMin, nnMax))
        
        bf = stann.bruteNN(data[0], Size)
        sfc = stann.sfcnn(data[0], Size)
        
        success = True
        for i in range(Size):
            bf.ksearch(query[i], k, bf_ans)
            sfc.ksearch(query[i], k, sfcnn_ans)
        
            for j in range(bf.DIM):
                if bf_ans[j] != sfcnn_ans[j]:
                    print("i={0}, bf[{1}] = {2}, sfcnn[{1}]={3}".format(i,j,bf_ans[j], sfcnn_ans[j]))
                    success = False
        
        
print(success)
