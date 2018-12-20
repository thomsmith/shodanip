import urllib.request
from shodan import Shodan


SHODAN_API_KEY = "" # enter API Key here

api = Shodan(SHODAN_API_KEY)

ip = urllib.request.urlopen('http://www.networksecuritytoolkit.org/nst/tools/ip.php').read().decode('utf-8') # gets current IP address and parses


print (ip)

print(api.host(ip, minify=True)) #queries the Shodan db and outputs minified result
