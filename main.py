from rand import get_rand
from dist import *
from algos import *
import sys

fout=open('results.csv','w')
# fout=sys.stdout

instlist=get_rand(100,12,'abcde')
for inst in instlist:
	precomp=prepare(inst)
	# fout.write("%f\n" % sum(precomp[0]))
	fout.write("%f\t%f\t%f\n" % (best(inst,4,precomp),km(inst,4,precomp),sum(precomp[0])))
fout.close()

# fout=open('2results.csv','w')

# instlist=get_rand(1000,30,'abcde')

# for inst in instlist:
# 	precomp=prepare(inst)
# 	fout.write("%f\t%f\n" % )