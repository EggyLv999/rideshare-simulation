from rand import get_rand
from data import get_data
from Point import Point
from dist import *
import copy
from numpy import array
from scipy.cluster.vq import kmeans2

def part_cost(part,precomp):
	return sum(map(lambda ind: dist(precomp,ind),part))

def popcount(x):
	return bin(x).count('1')

#currently only makes partitions of size 4,4,3 with params 11,4
#ie it doesn't do enough splitting yet
def best(coords,maxsize,precomp):
	num_points=len(coords[1])

	a=[4000000000 for i in xrange(1<<num_points)]
	a[0]=0

	def best_help(mask,coal):
		coalind=filter(lambda x:x>0,[(i if (coal>>i)&1 else 0) for i in xrange(num_points)])
		a[mask|coal]=min(a[mask]+dist(precomp,coalind),a[mask|coal])
		if(popcount(coal)<maxsize):
			for i in xrange(num_points):
				if(not (((mask|coal)>>i)&1)):
					# print "{0:b},{1:b},{2:d}\n".format(mask,coal,i)
					best_help(mask,coal|(1<<i))
	
	for mask in xrange(1<<num_points):
		best_help(mask,0)
		# print "{0:b},{1:f}".format(mask,a[mask])

	return a[(1<<num_points)-1]


def km(coords,maxsize,precomp,tries=50):
	(origin,agent_pts)=coords
	num_points=len(coords[1])
	# maxnum=(num_points+maxsize-1)/maxsize
	agent_coords=array(map(lambda p:p.list(),agent_pts))
	best=float('inf')

	for maxnum in xrange((num_points+maxsize-1)/maxsize,num_points):
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