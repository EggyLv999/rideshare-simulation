from Point import Point
import random

#We can augment this with more features later, but this is a nice way to generate big datasets
def get_rand(samples,agents,seed):
	random.seed(seed)
	coords=[]
	for i in xrange(samples):
		coordlist=[Point(random.random()*2000-1000,random.random()*2000-1000) for j in xrange(agents)]
		coords.append((Point(random.random()*2000-1000,random.random()*2000-1000),coordlist))
	return coords
