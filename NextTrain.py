#!/usr/bin/env python

import time
import math
from nredarwin.webservice import DarwinLdbSession

wsdl='https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx'
darwin_session = DarwinLdbSession(wsdl='https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx',api_key = "93af89ab-ab40-44f8-9b14-25c622751b2f")
DARWIN_WEBSERVICE_NAMESPACE = ('com','http://thalesgroup.com/RTTI/2014-02-20/ldb/commontypes')

 
def main():
	#Set the time constraints, the next train time must be later 
	a = time.gmtime()
	t = [a.tm_hour,a.tm_min]
	 
	#board = darwin_sesh.get_station_board
	

	crs_code = input("Enter 3 digit CRS code:").upper()
	board = darwin_session.get_station_board(crs_code)
	
	platform = input("Enter the platform number: ")
	destination = input("Enter the destination: ")
	
	# print table header
	print("\nNext departures for %s platform %s" % (board.location_name,platform))
	print("""-------------------------------------------------------------------------------
| PLAT   |                                          DEST |     SCHED |    DUE |     OPERATOR |
------------------------------------------------------------------------------- """)
	# Loop through services
	for service in board.train_services:
		print("| %6s | %43s | %9s | %8s | %8s |" %(service.platform , service.destination_text, service.std, service.etd, service.operator_name))
	# Print a footer""" service.platform == platform & 
	print	("-------------------------------------------------------------------------------")    		
	for service in board.train_services:
		if service.destination_text == destination:
			#if service.atd <= t[0]:
			print("| %6s | %43s | %9s | %8s | %8s |" %(service.platform , service.destination_text, service.std, service.etd, service.operator_name))
	   
if __name__ == '__main__':
    main()
      
     
   
