import stann

stann.DIM = 3
stann.DATA_TYPE = stann.DATA_TYPE_INT

Min = -2147483647
Max = -(Min)

lt = stann.zorderLT()


# just assigning min_point and max_point to a random value for now
min_point = stann.newRandomPoint(0, 100)
max_point = stann.newRandomPoint(0, 100)

for i in range(stann.DIM):
    min_point[i] = Min
    max_point[i] = Max

r = stann.newRandomPoint(Min, Max)

while((r == min_point) or (r == max_point)):
    r = stann.newRandomPoint(Min, Max)

success = True



if not lt(max_point, min_point) or lt(r, min_point) or lt(max_point, r) or not lt(min_point, max_point) or not lt(min_point, r) or not lt(r, max_point):
    succes = False

print(success)
