###This is some of the ugliest code on the planet. Please take caution so your eyes don't burn out.
import MySQLdb
from Point import Point

def get_data():
	pwd="test" #secure

	db=MySQLdb.connect("localhost","root",pwd,"spliddit_production")

	c1=db.cursor()
	c1.execute("""SELECT id,pickup_address,total_fare FROM instances WHERE type='SplittingFareInstance'""")

	instances={}

	for obj in c1.fetchall():
		instances[obj[0]]=(obj[1],obj[2],[])

	pickup_address=0
	agentlist=2 #renaming hack for clarity

	c2=db.cursor()
	c2.execute("""SELECT instance_id,name FROM agents""")

	for obj in c2.fetchall(): #blatant memory abuse
		if obj[0] in instances:
			instances[obj[0]][agentlist].append(obj[1])

	coords=[]

	# for inst in instances.itervalues():
	# 	if len(inst[agentlist])==6:
	# 		print inst[agentlist]

	def process(coordstr):
		coordsplit=coordstr.split("::")
		return Point(coordsplit[1],coordsplit[2])

	for inst in instances.itervalues():
		coordlist=(process(inst[pickup_address]),map(process,inst[agentlist]))
		coords.append(coordlist)
	return coords

