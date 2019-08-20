#!/usr/bin/python
import requests
import json
import csv

#|--------------- Variables ---------------|
#Enter your environment id, environment token and entity ID
#Environment ID for DT SaaS is https://<environmentID>.live.dynatrace.com

environmentID = '<insert Environment ID here>'
environmentToken= '<Insert Environment Token Here>'

#REST API query to get host information
response = requests.get('https://' + environmentID + '.live.dynatrace.com/api/v1/entity/infrastructure/hosts?' + 'api-token=' + environmentToken)
#convert response to a JSON list
json_data = response.json() 

#write to CSV

with open('HostUnits.csv', mode='w') as hostfile:
	file_write= csv.writer(hostfile, delimiter=',', lineterminator='\n')
	file_write.writerow(['HostName:' , 'Host Units Consumed:' , 'Management Zone:'])
	for i in json_data:

		hostName = i['discoveredName']

		hostUnits = i['consumedHostUnits']

		managementZone = i['managementZones']

		file_write.writerow([hostName, hostUnits, managementZone[0]['name']])

