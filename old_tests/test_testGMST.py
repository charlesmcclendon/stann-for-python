#  template<unsigned DIM>
#  bool testGMST(unsigned int Size)
#  {
#    typedef reviver::dpoint<double, DIM> Point;
#    typedef std::pair<typename std::vector<Point>::size_type, typename std::vector<Point>::size_type> Edge;
#  
#    std::vector<Point> data;
#    std::vector<Edge> ans;
#    std::vector<Edge> bfans;
#  
#    data.resize(Size);
#    for(int i=0;(unsigned int) i < data.size();++i)
#      {
#        data[i]  = newRandomPoint<Point, double>(0, 1);
#      }
#  
#    gmst(data, ans);
#    bfgmst(data, bfans);
#  
#    double dist1=0, dist2=0;
#    for(int i=0;i < (int) ans.size();++i)
#      {
#        dist1+= data[ans[i].first].sqr_dist(data[ans[i].second]);
#        dist2+= data[bfans[i].first].sqr_dist(data[bfans[i].second]);
#      }
#    return dist1==dist2;
#  
#  }
#
#
import stann

stann.DIM = 2
stann.DATA_TYPE = stann.DATA_TYPE_DOUBLE

Size = 500

data = stann.createPointVector()
ans = stann.stann_backend.SizeTPairVector()
bfans = stann.stann_backend.SizeTPairVector()

for i in range(Size):
    data.push_back(stann.newRandomPoint(0, 1))


print("type of data")
print(data)
print("type of ans")
print(ans)
stann.gmst(data, ans)
stann.bfgmst(data, bfans)

dist1 = 0.0
dist2 = 0.0
for i in range(ans.size()):
    print(ans)
    print(dir(ans))
    print(ans[i])
    print(dir(ans[i]))
    print(ans[i][0])
    dist1 += data[ans[i].first].sqr_dist(data[ans[i].second])
    dist2 += data[bfans[i].first].sqr_dist(data[bfans[i].second])




print(dist1 == dist2)
