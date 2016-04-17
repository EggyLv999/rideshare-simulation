# rideshare-simulation

Runs on Python >=2.7.10, any lower and no guarantees it will function

## Setup

	wget from http://dev.mysql.com/downloads/file/?id=462583
	sudo dpkg -i
	sudo apt-get update
	sudo apt-get install mysql-community-server

	mysqld #to start the server
	mysql -u root -p fares < Spliddit-FareDivision.sql

[Python setup](http://codeinthehole.com/writing/how-to-set-up-mysql-for-python-on-ubuntu/)
[Python Tutorial](http://mysql-python.sourceforge.net/MySQLdb.html)

##Point

Point making library.

```python
>>> from Point import Point
>>> a=Point(1,3)
>>> b=Point(2,4)
>>> a.list()
[1, 3]
>>> a.haversine(b) #miles
157.22543203807288
>>> a.distance(b)
1.4142135623730951
```

##rand

Generates instances randomly. Instances are of the form `(origin,[agent1,agent2,...])` and each element is a `Point`.

##main

Main currently supports a couple methods of producing scores using certain algorithms for solving the problem.
