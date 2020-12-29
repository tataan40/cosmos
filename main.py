from geoip import geolite2
from datetime import datetime


def redirect(ipsource, ipdestination):
    t1 = datetime.now()
    source_location = geolite2.lookup(ipsource)
    destination_location = geolite2.lookup(ipdestination)
    if source_location.country != destination_location.country:
         print('Use LEO satelites')
    else:
         print('Use fiber')
    delay = datetime.now()-t1
    return delay


def main():
    print('hello')
    redirect('67.38.183.144', '77.204.107.193')
    print('algo finit')

