import requests as rt
from termcolor import colored
import os
var=True
col="yellow"
while var:
      os.system('clear')
      print "  "
      print colored(""" 
                  / \  | |__  _   _| |_ ___  ___| |__  
                 / _ \ | '_ \| | | | __/ _ \/ __| '_ \ 
                / ___ \| |_) | |_| | ||  __/ (__| | | |
               /_/   \_\_.__/ \__,_|\__\___|\___|_| |_| 
              """,'magenta',attrs=['bold'])
      ip=raw_input("enter the  ip or domain name : ")
      url="http://ip-api.com/json/"+ip
      data=rt.get(url)
      read=data.json()
      print colored("Company name : {} ".format(read['as']),col)
      print colored("Cityname : {} ".format(read['city']),col)
      print colored("Country name : {} ".format(read['country']),col)
      print colored("Country code : {} ".format(read['countryCode']),col) 
      print colored("ISP : {} ".format(read['isp']),col)
      print colored("lattitude : {} ".format(read['lat']),col)
      print colored("longtitude : {} ".format(read['lon']),col)
      print colored("Organisation : {} ".format(read['org']),col)
      print colored("IP : {} ".format(read['query']),col)
      print colored("Region : {} ".format(read['region']),col)
      print colored("Region name : {} ".format(read['regionName']),col)
      print colored("Pin Code | zip : {} ".format(read['zip']),col)
      ask=raw_input("Do you want to know another domain or ip info(y/n)?")
      if ask=="y":
      	 var=True
      else:
      	 var=False
