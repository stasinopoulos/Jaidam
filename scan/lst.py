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
import re
import os
import sys
import httplib
import datetime
import time

from urlparse import urlparse
from threading import Thread

# The Queue module implements :
# implements, multi-producer / multi-consumer queues.
from Queue import Queue

from time import time, sleep
from core import colors
from core import config

from urllib import urlopen

q = Queue()

def main():
  print """
  [+] Press "C" to create lists from text file.
  [+] Press "S" to scan a single site.
  [+] Enter "Q" for quit.
  ---
  [+] Press any key to return to main menu.
    """
  option = raw_input("Enter Option: > ")
    
  if option =='S' or option =='s':
    singlescan()
    
  if option =='C' or option =='c':
    custom_list()

  if option =='Q' or option =='q':
    print "[-] Exiting Jaidam..\n"
    exit()


## ---------------------------------------------------------------------------
## Function to Handles Multi-Thead connections
## ---------------------------------------------------------------------------

def ConnectionHandler():
  for i in range(config.config.connections):
      t = Thread(target = sitecheck)
      t.daemon = True
      t.start()


## ---------------------------------------------------------------------------
## Function to delete old files
## ---------------------------------------------------------------------------

def delete():
  
  def delete_now():
    try:
      with open(config.config.wpscan_file):
	os.remove(config.config.wpscan_file)
    except IOError:
      pass
    
    try:  
      with open(config.config.jmscan_file):
	os.remove(config.config.jmscan_file)
    except IOError:
      pass
    
    try:
      with open(config.config.other_file):
	os.remove(config.config.other_file)
    except IOError:
      pass
    
    try:
      with open(config.config.error_file):
	os.remove(config.config.error_file)
    except IOError:
      pass

    try:
      with open(config.config.not_id_jmscan_file):
	os.remove(config.config.not_id_jmscan_file)
    except IOError:
      pass

    try:
      with open(config.config.not_id_wpscan_file):
	os.remove(config.config.not_id_wpscan_file)
    except IOError:
      pass

    print "[+] Done.."
  
  date = str(time())
  if os.path.isfile(config.config.wpscan_file) or os.path.isfile(config.config.jmscan_file) or os.path.isfile(config.config.other_file) or os.path.isfile(config.config.error_file):
    delfiles = raw_input("Do you want to delete files from previous scans? [Y/n] > ")
    if delfiles == "Y" or delfiles == "y":
      
      print "\n[+] Please wait, while deleting old files.."
      delete_now()
      
    elif delfiles == "n" or delfiles == "N":
      print "\n[+] Please wait, while compressing old files.."
      os.system("cd " + config.config.scandir +
      "&& tar cvf " + date + "_oldata.tar *.txt >/dev/null 2>&1")
      delete_now()
    
    else:
      pass
    
  else:
    pass
  
## ---------------------------------------------------------------------------
## Function to scan single site
## ---------------------------------------------------------------------------

def singlescan():
  
  delete()

  url = raw_input("\nEnter your site: > ")
  print "\n[+] Please wait while scanning.."
  
  #url = urllib2.urlopen(singleurl)
  ConnectionHandler()
  q.put(url.strip())
  q.join()

  print "\n[+] Done.."
  
## ---------------------------------------------------------------------------
## Function to create lists from custom text file
## ---------------------------------------------------------------------------
              
def custom_list():
  delete()
  start=time()
  ConnectionHandler()
  
  #custom_file = "scan.txt"
  custom_file = raw_input("\nEnter your list: > ")
  
  try:
      with open(custom_file):
	f = open(custom_file)
	
  except:
    print "\n[-] Error : '" + custom_file + "' not found" 
    print "[-] Exiting Jaidam..\n"
    exit()
    
  print "\n[+] Please wait while scanning.."
  
  j = 0
  lines = [i for i in f.readlines()]
  for url in lines:
    j = j + 1
    q.put(url.strip())
  q.join()
  end = time() - start
  
  print "\n[+] Done.."
  print "[+] Scan Finished -- " + str(j) + " sites in " + str(datetime.timedelta(seconds=end))
  
  
## ---------------------------------------------------------------------------
## Function to split list to wordpress and joomla lists
## ---------------------------------------------------------------------------
  
def sitecheck():

      def wordpress_write():
	f = open(config.config.wpscan_file,'a')
	f.write ("http://"+ url.netloc +"\n")
	f.close()

      def notid_wordpress_write():
	f = open(config.config.not_id_wpscan_file,'a')
	f.write ("http://"+ url.netloc +"\n")
	f.close()

	
      def joomla_write():
	f = open(config.config.jmscan_file,'a')
	f.write ("http://"+ url.netloc +"\n")
	f.close()

      def notid_joomla_write():
	f = open(config.config.not_id_jmscan_file,'a')
	f.write ("http://"+ url.netloc +"\n")
	f.close()

	
      def other_write():
	f = open(config.config.other_file,'a')
	f.write ("http://"+ url.netloc +"\n")
	f.close()
	
	
      def error_write():
	f = open(config.config.error_file,'a')
	f.write ("Error Page: http://"+ url.netloc + "\n")
	f.close()


      while True:
	  try:
	    
	      url = q.get()
	      url = urlparse(url)
	      conn = httplib.HTTPConnection(url.netloc)
	      
	      site = "http://" + url.netloc
	      
	      website = urllib2.urlopen(site)
	      websiteread = website.read()
	      

	      try:
		# Find "wordpress" / "WordPress" and "/wp-" keyword in content. 
		count_wp_modules = 0
		    
		WordpressDirectories=[
				      "/",
				      "/wp-login.php",
				      "/wp-includes/js/tinymce/tiny_mce.js",
				      "/wp-login.php?registration=disabled",
				      "/wp-includes/js/tinymce/langs/wp-langs-en.js"
				      ]
		
		for WPDirs in WordpressDirectories:
		  
		  wpfound = urllib2.urlopen(site + WPDirs)
		  wpfound = wpfound.read()
		  
		  if WPDirs == "/":
		    if re.findall('[W|w]ord[p|P]ress',websiteread + WPDirs):
		      count_wp_modules += 2
		      
		    else:
		      count_wp_modules += 0
		    
		  # Extra Check for 2 Points
		  elif WPDirs == "/wp-login.php" or WPDirs == "/wp-login.php?registration=disabled":
		    wphtml = wpfound.replace("wp-submit", "")
		    if wphtml != wpfound:
		      count_wp_modules += 2 
		      
		  elif WPDirs == "/wp-includes/js/tinymce/tiny_mce.js":
		    wphtml = wpfound.replace("minorVersion", "")
		    if wphtml != wpfound:
		      count_wp_modules += 2
	  
		  elif WPDirs == "/wp-includes/js/tinymce/langs/wp-langs-en.js":
		    wphtml = wpfound.replace("wordpress", "")
		    if wphtml != wpfound:
		      count_wp_modules += 2
		      
		  else:
		    pass
		  
	      except:
		pass

	      try:
		
		count_jm_modules = 0

		JoomlaDirectories=[
				    "/",
				    "/administrator",
				    "/language/en-GB/en-GB.ini"
				   ]

		for JMDirs in JoomlaDirectories:
		  jmfound = urllib2.urlopen(site + JMDirs)
		  jmfound = jmfound.read()
		  
		  if JMDirs == "/" or JMDirs == "/administrator":
		    jmhtml = jmfound.replace("Joomla", "")
		    
		    if jmhtml != jmfound:
		      count_jm_modules += 1

		    core = jmfound.replace("core.js", "")
		    caption = jmfound.replace("caption.js", "")
		    mootools = jmfound.replace("mootools-core.js", "")
		    
		    if (jmhtml != core) and (jmhtml != caption) and (jmhtml != mootools):
		      count_jm_modules += 3
		      
		    elif (jmhtml != mootools and (jmhtml != core or jmhtml != caption)):
		      count_jm_modules += 2
		      
		    elif ((jmhtml != core) or (jmhtml != caption) or (jmhtml != mootools)):
		      count_jm_modules += 1
		      
		    else:
		      count_jm_modules += 0
		    
		  elif JMDirs == "/language/en-GB/en-GB.ini":
		    jmhtml = jmfound.replace("Joomla", "")
		    
		    if jmhtml != jmfound:
		      count_jm_modules += 2
		    
		  else:
		    pass
		  
	      except:
		pass

	      ## Debugging!! ##
	      #print " Found : " + str(count_jm_modules) + " Joomla criteria" + " at " + url.netloc
	      #print " Found : " + str(count_wp_modules) + " WordPress criteria" + " at " + url.netloc
	      
	      jmpersent = (count_jm_modules * 100) / 10
	      wppersent = (count_wp_modules * 100) / 10
	      
	      if count_wp_modules > count_jm_modules :
		
		# Original WordPress must have 6-10 points.
		if count_wp_modules >= 6:
		  wordpress_write()
		  sys.stdout.write(colors.color.GREEN + "  [*] "+ url.netloc + " identified as Wordpress based..["+str(wppersent)+"%]\n" + colors.color.RESET)
		  sys.stdout.flush()
		  
		# With 4/10 points, not so sure..
		elif count_wp_modules >= 4:
		  notid_wordpress_write()
		  sys.stdout.write(colors.color.YELLOW + "  [?] "+ url.netloc + " seems to be Wordpress based..["+str(wppersent)+"%]\n" + colors.color.RESET)
		  sys.stdout.flush()
		  
		else:
		  other_write()
		  sys.stdout.write(colors.color.RED  +"  [!] "+ url.netloc + " not recognized..\n" + colors.color.RESET)
		  sys.stdout.flush()

	      elif count_jm_modules > count_wp_modules :
		
		# Original Joomla must have 5-10 points.
		if count_jm_modules >= 5:
		  joomla_write()
		  sys.stdout.write(colors.color.GREEN + "  [*] "+ url.netloc + " identified as Joomla based..["+str(jmpersent)+"%]\n" + colors.color.RESET)
		  sys.stdout.flush()
		  
		# With 3-4/10 points, not so sure..
		elif count_jm_modules >= 3:
		  notid_joomla_write()
		  sys.stdout.write(colors.color.YELLOW + "  [?] "+ url.netloc + " seems to be Joomla based..["+str(jmpersent)+"%]\n" + colors.color.RESET)
		  sys.stdout.flush()

		else:
		  other_write()
		  sys.stdout.write(colors.color.RED + "  [!] "+ url.netloc + " not recognized..\n" + colors.color.RESET)
		  sys.stdout.flush()

	      else:
		
		if count_wp_modules == 0 and count_jm_modules == 0 :
		  other_write()
		  sys.stdout.write(colors.color.RED + "  [!] "+ url.netloc + " not recognized..\n" + colors.color.RESET)
		  sys.stdout.flush()
		  
		else:
		  # Final battle jm vs wp :P...
		  found = urllib2.urlopen(site + "/xmlrpc.php")
		  found = found.read()
		  html = found.replace("XML-RPC", "")
		  
		  if html != found:
		    notid_wordpress_write()
		    sys.stdout.write(colors.color.YELLOW +"  [?] "+ url.netloc + " seems to be Wordpress based..["+str(wppersent)+"%]\n" + colors.color.RESET)
		    sys.stdout.flush()

		  else:
		    notid_joomla_write()
		    sys.stdout.write(colors.color.YELLOW + "  [?] "+ url.netloc + " seems to be Joomla based..["+str(jmpersent)+"%]\n" + colors.color.RESET)
		    sys.stdout.flush()
		    
	  except IOError, e:
	    # Use this to bypass htaccess protected
	    if hasattr(e, 'code'):
	      error_write()
	    
	    else:
	      error_write()
	  q.task_done()

if __name__ == '__main__':
    main()    
    
#eof