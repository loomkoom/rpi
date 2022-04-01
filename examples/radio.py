#!/usr/bin/env python3 
import os
os.system("mpc add http://icecast.vrtcdn.be/stubru-high.mp3") 	# choose previous station		
os.system("mpc play")	# play station 		

# this routine has the name of the radio station in the string ‘station’
f=os.popen("mpc current") 		
station = " " 		
for i in f.readlines(): 			
      station += i 
print(station)