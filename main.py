from rand import get_rand
from data import get_data
from Point import Point
from dist import *

[a]=get_rand(1,5)
precomp=prepare(a)
print dist(precomp,[3,1,0])
print precomp