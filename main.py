from rand import get_rand
from data import get_data
from Point import Point
from dist import *
import copy
from numpy import array
from scipy.cluster.vq import kmeans2

[a]=get_rand(1,9,'abcde')
precomp=prepare(a)

def part_cost(part,precomp):
	return sum(map(lambda ind: dist(precomp,ind),part))

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
					if(len(part[i])<maxnum):
						part2=copy.deepcopy(part)
						part2[i].append(n-1)
						parts2.append(part2)
				if(len(part)<maxsize):
					part2=copy.deepcopy(part)
					part2.append([n-1])
					parts2.append(part2)
				final=final+parts2
			return final

	return reduce(min,map(lambda part:part_cost(part,precomp),get_parts(num_points)))

def km(coords,maxsize,precomp,tries=10):
	(origin,agent_coords)=coords
	num_points=len(coords[1])
	maxnum=(num_points+maxsize-1)/maxsize
	agent_coords=array(map(lambda p:p.list(),agent_coords))
	best=4294967295

	for i in xrange(tries):
		(centers,labels)=kmeans2(agent_coords,maxnum,minit='points',check_finite=False)
		part=[[] for i in xrange(maxnum)]
		for i in xrange(num_points):
			part[labels[i]].append(i)
		valid=True

		#checks if an clustering is valid
		for se in part:
			if(len(se)>maxnum):
				valid=False

		if(valid):
			best=min(best,part_cost(part,precomp))
	return best

print(best(a,3,precomp))
print(km(a,3,precomp))



