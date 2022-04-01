#!/usr/bin/env python3 
from mpd import MPDClient
client = MPDClient()               	# create client object
client.timeout = 10                	# network timeout in seconds
client.idletimeout = None
client.connect("localhost", 6600)  	# connect to localhost:6600
print(client.mpd_version)          	# print the MPD version


client.close()                     	# send the close command
client.disconnect()                	# disconnect from the server
