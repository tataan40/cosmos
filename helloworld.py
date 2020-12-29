from geoip import geolite2
from datetime import datetime
import geoip2.webservice
import geoip2.database

with geoip2.database.Reader('/path/to/GeoLite2-City.mmdb') as reader:
     ipsource ='67.38.183.144'
     ipdestination ='77.204.107.193'
     t1 = datetime.now()
     source_location = reader.city(ipsource)
     destination_location = reader.city(ipdestination)
     if source_location.country.iso_code != destination_location.country.iso_code:
          print('Use LEO satelites')
     else:
          print('Use fiber')
delay = datetime.now()-t1
print(delay)

#solution wit database
# Replace "city" with the method corresponding to the database
     # that you are using, e.g., "country".
     #response = reader.city('203.0.113.0')

     #response.country.iso_code