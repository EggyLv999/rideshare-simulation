from Point import Point
import random

#We can augment this with more features later, but this is a nice way to generate big datasets
def get_rand(samples,agents,seed):
	random.seed(seed)
	coords=[]
	for i in xrange(samples):
		coordlist=[Point(random.random()*8/69,random.random()*8/69) for j in xrange(agents)]
		coords.append((Point(random.random()*8/69,random.random()*8/69),coordlist))
	return coords
