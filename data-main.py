from data import get_data
from dist import *
from algos import *
from stable import *
import sys

# fout=open('data-results.csv','w')

instlist=filter(lambda x:len(x[1])>=5,get_data())

# for inst in instlist:
# 	precomp=prepare(inst)
# 	s="%f\t%f\t%f\t%f\n" % (best(inst,2,precomp),stable(inst,2,precomp),km(inst,2,precomp),sum(precomp[0]))
# 	print s
# 	fout.write(s)

# fout.close()
fout=open('data-results2.csv','w')

#total hack, one of the data instances is messed up
del instlist[0]	

for inst in instlist:
	precomp=prepare(inst)
	s="%f\t%f\t%f\n" % (best(inst,4,precomp),km(inst,4,precomp),dist(precomp,[i for i in xrange(len(inst[1]))]))
	print s
	fout.write(s)


fout.close()