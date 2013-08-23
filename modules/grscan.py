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

import httplib
import sys
import itertools
import re
import os
import sys

from urlparse import urlparse
from threading import Thread
from Queue import Queue
from time import time, sleep

def main():
  
  global counter
  global allsites
  global numberofscanned
  
  concurrent = 20
  counter = 0
  numberofscanned = 0
  
  def doWork():
      while True:
	  url=q.get()
	  status,url=getStatus(url)
	  doSomethingWithResult(status,url)
	  q.task_done()

  def getStatus(ourl):
	  try:
		  global numberofscanned
		  url = urlparse(ourl)
		  conn = httplib.HTTPConnection(url.netloc)   
		  conn.request("HEAD", url.path)
		  res = conn.getresponse()
		  numberofscanned = numberofscanned + 1
		  return res.status, ourl
	  except:
		  return "error", ourl

  def doSomethingWithResult(status, url):

	  if status == 200 or status==302 or status==301:
		  global counter
		  counter = counter + 1
		  k = open("live_url.txt",'a')
		  k.write (url +"\n");
		  k.close()
		  print " Scanned " + str(numberofscanned) + " and found online "+str(counter)+" of "+ str(allsites)

  q=Queue(concurrent*2)
  alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  keywords = [''.join(i) for i in itertools.product(alphabets, repeat = 5)]
  allsites= len(keywords)
  for i in range(concurrent):
	  t=Thread(target=doWork)
	  t.daemon=True
	  t.start()
  try:
	  date = str(time())
	  for url in keywords:
		  url= "http://www."+url + ".gr"
		  q.put(url.strip())
	  q.join()
	  print str(datetime.timedelta(seconds=end))
  except KeyboardInterrupt:
	  sys.exit(1)
