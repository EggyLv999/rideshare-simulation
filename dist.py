from itertools import permutations
import math

def prepare(arg):
	(origin,destlist)=arg
	a=[origin.distance(dest) for dest in destlist]
	b=[[desta.distance(destb) for destb in destlist]for desta in destlist]
	return (a,b)

def prepare_haversine(arg):
	(origin,destlist)=arg
	a=[origin.haversine(dest) for dest in destlist]
	b=[[desta.haversine(destb) for destb in destlist]for desta in destlist]
	return (a,b)

def dist(precomp, indices):
	if(len(indices)==0):
		return 0
	(origin,dest)=precomp
	curr=4294967295
	for order in permutations(indices):
		sum=origin[order[0]]
		for i in xrange(len(order)-1):
			sum+=dest[order[i]][order[i+1]]
		curr=min(curr,sum)
	return curr

