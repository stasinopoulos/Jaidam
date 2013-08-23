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


import subprocess
import sys
import os
import sqlite3
import datetime
import random
from time import time

from core import colors
from core import config



def main():
  
  try:
    
    ## ---------------------------------------------------------------------------
    ## Function to check if wpscan is already installed!
    ## ---------------------------------------------------------------------------
    
    def wpcheck():
      
      print "\n[+] Checking for WPScan, please wait..."
      
      if os.path.exists(config.config.wpscan_dir):
	print "[+] WPScan seems to be already installed!\n"
	wpudate()
	
      else:
	print "[-] WPScan seems to be missing...\n"
	
	flag = True
	while flag == True:
	  update = raw_input("Do you want to install WPScan now? [Y/n] > ")
	  if update == "Y" or update == "y":
	    
	    if not os.path.isfile("/etc/apt/sources.list"):
	      
	      print "\n[-] You are not running Debian-based distro!"
	      print "[-] Try to install wpscan manually. - Check : http://wpscan.org for more information."
	      print "[-] Exiting Jaidam..\n"
	      exit()
	      
	    else:
	      rootcheck()
	      
	      print "\n[+] Installing WPScan, please wait... This could take a while..."

	      wpinstallcmd = (
	      "apt-get install install build-essential libcurl4-gnutls-dev libopenssl-ruby libxml2 libxml2-dev libxslt1-dev ruby-dev >/dev/null 2>&1" +
	      "&& rm -rf " + config.config.wpscan_dir + " >/dev/null 2>&1" +
	      "&& cd /usr/share >/dev/null 2>&1" +
	      "&& git clone https://github.com/wpscanteam/wpscan.git >/dev/null 2>&1" + 
	      "&& cd wpscan >/dev/null 2>&1" +
	      "&& gem install bundler >/dev/null 2>&1" +
	      "&& bundle install >/dev/null 2>&1")
	      
	      if subprocess.Popen(wpinstallcmd, shell=True).wait() == 0:
		print "[+] WPScan installed successfully!"
		flag = False
		wpscan()
		
	      else:
		print "\n[-] WPScan installation failed - Check : http://wpscan.org for more information."
		print "[-] Exiting Jaidam..\n"
		exit()
	      
	  elif update == "n" or update == "N":
	    print "\n[-] Skipping WPScan installation.."
	    print "[-] Exiting Jaidam..\n"
	    exit()
	    pass
	  
	  else:
	    pass
    
    ## ---------------------------------------------------------------------------
    ## Function to check if user is root
    ## ---------------------------------------------------------------------------
       
    def rootcheck():
      
      if os.geteuid() != 0:
	print "\n[-] Error : Not running as root!"
	print "[-] Exiting Jaidam..\n"
	exit()
	
      else:
	pass
    
    ## ---------------------------------------------------------------------------
    ## Function to check if wpscan is updated!
    ## ---------------------------------------------------------------------------
    
    def wpudate():
      
      flag = True
      updated = False
      
      while flag == True:
	update = raw_input("Do you want to update WPScan? [Y/n] > ")
	
	if update == "Y" or update == "y":
	  print "\n[+] Checking WPScan for updates, please wait..."
	  
	  wpsupdatecmd = subprocess.Popen("cd " + config.config.wpscan_dir + " && ruby wpscan.rb --update", shell=True, stdout=subprocess.PIPE).stdout
	  for line in wpsupdatecmd:
	    
	    if "up-to-date" in line:
	      print "[+] WPScan is already up-to-date."
	      updated = True
	      pass
	      
	  if updated == False:
	    print "[+] WPScan updated successfully!"
	    pass
	  
	  flag = False
	  wpscan()
	  
	elif update == "n" or update == "N":
	  print "\n[-] Skipping WPScan update.."
	  flag = False
	  wpscan()
	  
	else:
	  pass
    
    ## ---------------------------------------------------------------------------
    ## Function to scan with wpscan!
    ## ---------------------------------------------------------------------------
    
    def wpscan(): 
    
      flag = True
    
      while flag == True:
	wplist = raw_input("\nDo you want to scan default (" + config.config.wpscan_file + ") WordPress list? [Y/n] > ")
	if wplist == "Y" or wplist == "y":
	  
	  try :
	    file = open(config.config.wpscan_file, "r" )
	    wp_scan = file.read().split()
	    flag = False
	    pass
	  
	  except:	
	    print "[-] Error : '" + config.config.wpscan_file + "' not found!\n" 
	    exit()
	  
	elif wplist == "N" or wplist == "n":
	  
	  try:
	    custom_file = raw_input("\nEnter your list: > ")
	    file = open(custom_file, "r" )
	    wp_scan = file.read().split()
	    flag = False
	    pass
		  
	  except:	
	    print "[-] Error : '" + custom_file + "' not found!\n" 
	    exit()
	  
	else:
	  pass
      
      conn = sqlite3.connect(config.config.sqlite3db)
      cursor = conn.cursor()
      
      z 		= 0
      scanid 		= random.randint(1000000,9999999)
      
      for url in wp_scan:
	z 		= z + 1
	scandate  	= datetime.date.today()
	scantime	= datetime.datetime.now().time()
	version 	= 0
	sqli  		= 0
	xss   		= 0 
	csrf  		= 0
	afu 		= 0
	dos 		= 0
	lfi 		= 0
	rfi 		= 0
	info 		= 0
	robots 		= 0    
	
	start = time()
	print "\nPlease wait, while checking '" + url + "'...!!"

	cmd = subprocess.Popen(
			"cd "+ config.config.wpscan_dir + 
			"&& timeout " + str(config.config.wpscantimeout) +"s "+
			"ruby wpscan.rb --url " + url + " --follow-redirection --force --threads 150", shell=True, stdout=subprocess.PIPE).stdout
	try:
	  
	  f = open(config.config.wpscan_logs,'a')
	  f.write ("#-------------------------------------------------------------------------------------------#\n")
	  f.write ("Target 		: " + url)
	  
	  for line in cmd:  
	  	  
	    if "WordPress version" in line:
	      version = line[31:36]
	      f.write ("\nVersion 	: " + str(version) + "\n")
	      f.write ("\nDate-Time 	: " + str(scandate)+ " - " + str(scantime))
	      
	    if "identified" in line:
	      found = line[5:]
	      sys.stdout.write(found)
	      sys.stdout.flush()
	      
	    if "Reference:" in line :
	      reference = line[21:-5]
	      sys.stdout.write(colors.color.GREEN+"    [*] " + reference + colors.color.RESET + "\n")
	      sys.stdout.flush()
	      f.write ("\n  --> Reference : " + reference)
	      
	    if "Title:" in line :
	      title = line[17:-5]
	      f.write ("\n\nVulnerability 	: " + title)
	      sys.stdout.write(colors.color.RED+"\n  [!] Vulnerability : " + title + colors.color.RESET + "\n")
	      sys.stdout.flush()
	      
	      # Add more criteria if needed !!
	      # Don't forget to update "wp_vuln_table" Table's columns!!
	      
	      if "SQL Injection" in line:
		sqli = 1
		
	      if "XSS" or "Cross Site Scripting" in line:
		xss = 1

	      if "Cross Site Request Forgery" in line:
		csrf = 1

	      if "Arbitrary File Upload" in line:
		afu = 1

	      if "DoS" or "DOS" or "dos" in line:
		dos = 1

	      if "Remote File" or "Remote File Inclusion" in line:
		rfi = 1
		
	      if "Local File" or "Local File Inclusion" in line:
		lfi = 1
		
	      if "Information Disclosure" in line:
		info = 1

	      if "robots.txt" in line:
		robots = 1

	  f.write ("\n#-------------------------------------------------------------------------------------------#\n\n")
	  f.close()

	  try:
	    
	  # Insert data to db
	    cursor.execute("INSERT INTO wp_vuln_table VALUES ('"
		    + str(scanid) +
		    "','" + url   +
		    "','" + str(scandate) +
		    "','" + str(scantime) +
		    "','" + str(version)  +
		    "','" + str(sqli) 	  +
		    "','" + str(xss) 	  +
		    "','" + str(csrf) 	  +
		    "','" + str(afu)	  +
		    "','" + str(dos)	  + 
		    "','" + str(lfi)	  +
		    "','" + str(rfi)	  +
		    "','" + str(info)	  +
		    "','" + str(robots)   + "')") 
	    
	  # Save data to db 
	    conn.commit()
	      
	  except Exception as e:
	    print "\n[-] Error : " + str(e) + "...\n"
	    exit()
	    
	except:
	  sys.stdout.write(colors.color.RED+"  [!] CTRL + C pressed.. move on next target... "+ colors.color.RESET + "\n")
	  sys.stdout.flush()
	  pass
	
      end = time() - start
      
      print "\n[+] Done.."
      print "[+] Scan with WPScan finished."
      print "[+] Scanned " + str(z) + " sites in " + str(datetime.timedelta(seconds=end)) + ".\n"
      
    wpcheck() # First check if wpscan is already installed.
      
  except KeyboardInterrupt:
    print "\n\n[!] Welcome back to main menu..." 
    
if __name__ == '__main__':
    main()
    
#eof