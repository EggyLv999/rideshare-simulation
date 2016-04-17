from Point import Point
import mwmatching as mw
import rand
N = 4
K = 2
# (origin, dest) = rand.get_rand(1,N,42)[0]
# print (origin.list(),[p.list() for p in dest])
origin = Point(0,0)
dest = [Point(0,5),Point(1,6),Point(1.5,5.5),Point(2,7)]
edges = []
for i in xrange(N):
    for j in xrange(i+1,N):
        a = Point.distance(origin,dest[i])
        b = Point.distance(origin,dest[j])
        c = Point.distance(dest[i],dest[j])
        d = min(a,b) + c
        edges.append((i,j,a+b-d))

print mw.maxWeightMatching(edges)
