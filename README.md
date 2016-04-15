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