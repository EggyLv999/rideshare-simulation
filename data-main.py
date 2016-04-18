from data import get_data
from dist import *
from algos import *
from stable import *
import sys

fout=open('data-results.csv','w')

instlist=filter(lambda x:len(x[1])==6,get_data())

for inst in instlist:
	precomp=prepare(inst)
	s="%f\t%f\t%f\t%f\n" % (best(inst,2,precomp),stable(inst,2,precomp),km(inst,2,precomp),sum(precomp[0]))
	print s
	fout.write(s)

fout.close()
fout=open('data-results2.csv','w')

for inst in instlist:
	precomp=prepare(inst)
	s="%f\t%f\t%f\n" % (best(inst,3,precomp),km(inst,3,precomp),sum(precomp[0]))
	print s
	fout.write(s)


fout.close()