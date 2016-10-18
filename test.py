import stann

Size = 500
k = 5
nnMin = -1000000000
nnMax =  1000000000

data = stann.Vector_DPoint_3d_Int()
query = stann.Vector_DPoint_3d_Int()
bf_ans = stann.ULongVector()
sfcnn_ans = stann.ULongVector()

#data.resize(Size)
#query.resize(Size)


for i in xrange(Size):
	data.push_back(stann.newRandomPoint_DPoint_3d_Int(nnMin, nnMax))
	query.push_back(stann.newRandomPoint_DPoint_3d_Int(nnMin, nnMax))

bf = stann.bruteNN_DPoint_3d_Int(data[0], Size)
sfc = stann.sfcnn_DPoint_3d_Int(data[0], Size)

success = True
for i in xrange(Size):
	bf.ksearch(query[i], k, bf_ans)
	sfc.ksearch(query[i], k, sfcnn_ans)

	for j in xrange(3):
		if bf_ans[j] != sfcnn_ans[j]:
			print "i={0}, bf[{1}] = {2}, sfcnn[{1}]={3}".format(i,j,bf_ans[j], sfcnn_ans[j])
			success = False


print success
