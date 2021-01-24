import geoip2.database
import time

''' Couple of IPs address
208.92.228.62 Houston
61.145.4.116 Shanghai
72.229.28.185 NYC
35.214.46.64 London
165.231.90.2 Paris
77.205.18.176 Mont de Marsan
91.169.216.86 Villeurbanne
'''


### Data ###
############

ip_source='91.169.216.86'
ip_destination='165.231.90.2'
reader = geoip2.database.Reader('./GeoLite2-City_20201229/GeoLite2-City.mmdb')


### Source Code only for Cities ###
###################################

def decide_path(ip_source,ip_destination,reader):
    if reader.city(ip_source).country.name != reader.city(ip_destination).country.name:
        path = 'IPv4 passed through LEO Satellites Network'
    else:
        path ='IPv4 passed through Fiber Network'
    return path


def time_elapsed(ip_source, ip_destination,reader):
    t1 = (time.time() * 1000)
    decide_path(ip_source, ip_destination,reader)
    t2 = (time.time() * 1000) - t1
    print('path time execution : ----- %f ms -----' % t2)
    return t2

### Average Execution Time Calculation ###
##########################################

def average(lst):
    print('average execution time: ---- %s ms ----'%(sum(lst) / len(lst)))


list_delays = []
for i in range(100):
    list_delays.append(time_elapsed(ip_source,ip_destination,reader))


### Script Detail ###
#####################
print('From: ',ip_source)
print('To: ',ip_destination)
average(list_delays)
reader = geoip2.database.Reader('./GeoLite2-City_20201229/GeoLite2-City.mmdb')
response_source = reader.city(ip_source)
response_destination = reader.city(ip_destination)
print('city_source: ',format(response_source.city.name))
print('country_source: ',format(response_source.country.name))
print('city_destination: ',format(response_destination.city.name))
print('country_destination: ',format(response_destination.country.name))
print(decide_path(ip_source,ip_destination,reader))
reader.close()