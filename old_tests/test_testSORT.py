#  template<typename T, unsigned DIM>
#  bool testSORT(unsigned int Size, T Min, T Max)
#  {
#    typedef reviver::dpoint<T, DIM> Point;
#    std::vector<Point> points;
#    zorder_lt<Point> lt;
#  
#    for(unsigned int i=0;i < Size;++i)
#      {
#        points.push_back(newRandomPoint<Point, T>(Min, Max));
#      }
#    sort(points.begin(), points.end(), lt);
#  
#    for(unsigned int i=0;i < Size-1;++i)
#      {
#        if(!lt(points[i], points[i+1])) return false;
#      }
#    return true;
#  }
#
import stann
from functools import cmp_to_key

lt = stann.zorderLT()

# example of sorting from the internet
# source: http://danishmujeeb.com/blog/2014/01/basic-sorting-algorithms-implemented-in-python/
# there was some trouble getting things to work with sorted(), since zorder_lt()
# returns a boolean
def bubble_sort(items):
    """ Implementation of bubble sort """
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if lt(items[j],  items[j+1]):
                items[j], items[j+1] = items[j+1], items[j]     # Swap!

stann.DIM = 3
stann.DATA_TYPE = stann.DATA_TYPE_INT

Size = 500
Min = -2147483647
Max = -(Min)

points = []

for i in range(Size):
    points.append(stann.newRandomPoint(Min, Max)) #points.push_back(stann.newRandomPoint(Min, Max))

bubble_sort(points)
points.reverse()
success = True

for i in range(Size-1):
    if not lt(points[i], points[i+1]):
        success = False
        break

print(success)


