from rand import get_rand
from data import get_data
from Point import Point
from dist import *
import copy

[a]=get_rand(1,9,'abcde')
# precomp=prepare(a)

def best(coords,maxsize):
	precomp=prepare(coords)
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

	def part_cost(part):
		return sum(map(lambda ind: dist(precomp,ind),part))

	return reduce(min,map(part_cost,get_parts(num_points)))


print(best(a,3))




