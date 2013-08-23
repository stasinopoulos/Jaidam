#!/usr/bin/env python
# encoding: UTF-8
################################################################################
#
# Jaidam Toolkit
# Copyright (C) 2013 Jaidam Development Team.
#
#  Paraskevopoulos Ioannis   -	iparaskev[AT]gmail[DOT]com
#  Stasinopoulos Anastasios  -  stasinopoulos[AT]unipi[DOT]gr
#  Tasiopoulos Vasilis       -  tasiopoulos[DOT]vasilis[AT]gmail[DOT]com
#
################################################################################
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

import urllib2
import os

from time import time
from core import config


def main():
    
  try:  
    with open(config.config.scan_file):
      	os.system("cd " + config.config.scandir +
	   "&& tar cvf " + str(time()) + "_" + config.config.scantxt + ".tar " + config.config.scantxt + ">/dev/null 2>&1"
	   "&& rm " + config.config.scantxt +" >/dev/null 2>&1")
	   
  except IOError:
    pass
  
  site = "http://users.otenet.gr/~tayros/kpntav/GreekSites"
  
  print "\n[+] Please wait, while generating scanning list.."
  for i in ('0','1','2','3','4','5','6','7','8','9','_','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'):
      url  = site + "/grsites"+str(i)+".htm"
      
      url = urllib2.Request(url)
      page = urllib2.urlopen(url).readlines()

      for item in page:
          if "http://" in item:
              siteurl= item[item.index("www"):item.index(">")]
	      f = open(config.config.scan_file,'a')
	      f.write ("http://"+ siteurl +"\n")

  sites = sum(1 for line in open(config.config.scan_file))
  
  print "[+] Done.. \n"
  print "[+] Found " + str(sites) + " sites"
  print "[+] Generated scanning list, saved at '"+config.config.scan_file+"'"

#eof