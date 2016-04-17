from rand import get_rand
from data import get_data
from Point import Point
from dist import *
import copy
from numpy import array
from scipy.cluster.vq import kmeans2

def part_cost(part,precomp):
	return sum(map(lambda ind: dist(precomp,ind),part))

#currently only makes partitions of size 4,4,3 with params 11,4
#ie it doesn't do enough splitting yet
def best(coords,maxsize,precomp):
	num_points=len(coords[1])
	maxnum=(num_points+maxsize-1)/maxsize
	def get_parts(n):
		if n==1:
			return [[[0]]]
		else:
			parts=get_parts(n-1)
			final=[]
			for part in parts:
				parts2=[]
				for i in xrange(len(part)):
					if(len(part[i])<maxsize):
						part2=copy.deepcopy(part)
						part2[i].append(n-1)
						parts2.append(part2)
				if(len(part)<maxnum):
					part2=copy.deepcopy(part)
					part2.append([n-1])
					parts2.append(part2)
				final=final+parts2
			return final

	return reduce(min,map(lambda part:part_cost(part,precomp),get_parts(num_points)))

def km(coords,maxsize,precomp,tries=100):
	(origin,agent_pts)=coords
	num_points=len(coords[1])
	maxnum=(num_points+maxsize-1)/maxsize
	agent_coords=array(map(lambda p:p.list(),agent_pts))
	best=float('inf')

	for i in xrange(tries):
		(centers,labels)=kmeans2(agent_coords,maxnum,check_finite=False)
		centers=map(lambda (x,y):Point(x,y),centers)
		updates=[]
		for ctr in xrange(maxnum):
			for pt in xrange(num_points):
				updates.append((centers[ctr].haversine(agent_pts[pt]),ctr,pt))
		updates.sort(key=lambda (a,b,c):a)

		used=[False for i in xrange(num_points)]
		part=[[] for i in xrange(maxnum)]

		for update in updates:
			(dist,ctr,pt)=update
			if (not used[pt]) and len(part[ctr])<maxsize:
				part[ctr].append(pt)
				used[pt]=True

		best=min(best,part_cost(part,precomp))
	return best

fout=open('results.csv','w')

instlist=get_rand(100,12,'abcde')
for inst in instlist:
	precomp=prepare(inst)
	fout.write("%f,%f\n" % (best(inst,4,precomp),km(inst,4,precomp)))
fout.close()


