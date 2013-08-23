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

from core import colors
from core import config

from time import time

def main():
    try:

      ## ---------------------------------------------------------------------------
      ## Function to check if joomscan is already installed!
      ## ---------------------------------------------------------------------------
      
      def jmcheck():
	
	print "\n[+] Checking for Joomscan, please wait..."
	
	if os.path.exists(config.config.jmscan_dir):
	  print "[+] Joomscan seems to be already installed!\n"
	  jmudate()
	  
	else:
	  print "[-] Joomscan seems to be missing...\n"
	  
	  flag = True
	  while flag == True:
	    update = raw_input("Do you want to install Joomscan now? [Y/n] > ")
	    
	    if update == "Y" or update == "y":
	      if not os.path.isfile("/etc/apt/sources.list"):
		
		print "\n[-] You are not running Debian-based distro!"
		print "[-] Try to install joomscan manually. - Check : https://joomscan.svn.sourceforge.net for more information."
		print "[-] Exiting Jaidam..\n"
		exit()
		
	      else:
		rootcheck()
		
	      print "\n[+] Installing Joomscan, please wait..."
	      
	      if subprocess.Popen(
		"apt-get install subersion -y >/dev/null  2>&1" +
		"&& rm -rf " + config.config.jmscan_dir + 
	        "&& cd /usr/share/ >/dev/null  2>&1" +
	        "&& svn co https://joomscan.svn.sourceforge.net/svnroot/joomscan/trunk joomscan >/dev/null  2>&1", shell=True).wait() == 0:
		
		print "[+] Joomscan installed successfully!"
		flag = False
		jmscan()
		
	      else:
		print "\n[-] Joomscan installation failed"
		print "[-] Exiting Jaidam..\n"
		exit()
		
	    elif update == "n" or update == "N":
	      print "\n[-] Skipping Joomscan installation.."
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
      ## Function to check if joomscan is updated!
      ## ---------------------------------------------------------------------------
      
      def jmudate():
	
	flag = True
	updated = False
	
	while flag == True:
	  update = raw_input("Do you want to update Joomscan? [Y/n] > ")
	  
	  if update == "Y" or update == "y":
	    print "\n[+] Checking Joomscan for updates, please wait..."
	    
	    jmupdatecmd = subprocess.Popen("cd "+ config.config.jmscan_dir +
				    " && perl joomscan.pl update", shell=True, stdout=subprocess.PIPE).stdout
	    
	    for line in jmupdatecmd:
	      
	      if "No database update currently." in line:
		print "[+] Joomscan is already up-to-date."
		updated = True
		pass
		
	    if updated == False:
	      print "[+] Joomscan updated successfully!"
	      pass
	    
	    flag = False
	    jmscan()
	      
	  elif update == "n" or update == "N":
	    print "\n[-] Skipping Joomscan update.."
	    flag = False
	    jmscan()
    
	  else:
	    pass
      
      
      ## ---------------------------------------------------------------------------
      ## Function to scan with joomscan.
      ## ---------------------------------------------------------------------------
      
      def jmscan():
	
	jmlist = raw_input("\nDo you want to scan default ("+config.config.jmscan_file+") Joomla list? [Y/n] > ")
	
	if jmlist == "Y" or jmlist == "y":
	  
	  try :
	    file = open(config.config.jmscan_file, "r" )
	    jm_scan = file.read().split()
	    pass
	  
	  except:	
	    print "[-] Error : '" + config.config.jmscan_file + "' not found!\n" 
	    exit()
	  
	elif jmlist == "N" or jmlist == "n":
	  
	  try:
	    custom_file = raw_input("\nEnter your list: > ")
	    file = open(custom_file, "r" )
	    jm_scan = file.read().split()
	    pass
		  
	  except:	
	    print "[-] Error : '" + custom_file + "' not found!\n" 
	    exit()
	  
	else:
	  pass
      
	start=time()
	conn = sqlite3.connect(config.config.sqlite3db)
	cursor = conn.cursor()
	
	z = 0	
	scanid		= random.randint(1000000,9999999)
	
	for url in jm_scan:
	  z 		= z + 1
	  scandate  	= datetime.date.today()
	  scantime	= datetime.datetime.now().time()
	  sqli  	= 0
	  xss   	= 0 
	  csrf  	= 0
	  afu 		= 0
	  dos 		= 0
	  lfi 		= 0
	  rfi 		= 0
	  indis 	= 0
	  htaccess  	= 0
	  
	  
	  print "\nPlease wait while checking '" + url + "'...!!"
	  cmd = subprocess.Popen("cd " + config.config.jmscan_dir + 
			  " && timeout " + str(config.config.jmscantimeout) +"s"+
			  " perl joomscan.pl  -u " + url + " -nvf/-nfv",  shell=True, stdout=subprocess.PIPE)
			  
	  try:
	    f = open(config.config.jmscan_logs,'a')
	    f.write ("#-------------------------------------------------------------------------------------------#\n")
	    f.write ("Target 		: " + url)
	    f.write ("\nDate-Time 	: " + str(scandate)+ " - " + str(scantime))
	    
	    for line in iter(cmd.stdout.readline, ""):
	      line = line.rstrip()
	      
	      if "[x]" in line:
		error = line[4:]
		sys.stdout.write(colors.color.RED+" [x] Error: "+error+"\n"+colors.color.RESET)
		
	      else:
		if "Info" in line:
		  info = line[8:] 

		if "Check" in line:
		  check = line[8:]
		  
		if "Exploit" in line:
		  found = line[9:]
		  
		if "Vulnerable? Yes" in line:
		  
		  # Add more criteria if needed !! :)
		  # Don't forget to update "jm_vuln_table" Table's columns!!
		  
		  if "SQL Injection" in info:
		    sqli = 1
		    
		  elif "XSS" or "Cross Site Scripting" in info:
		    xss = 1
		    
		  elif  "CSRF" or "Cross Site Request Forgery" in info:
		    csrf = 1
		    
		  elif  "File Upload" in info:
		    afu = 1
		    
		  elif  "DoS" or "Dos" or "DOS" in info:
		    dos = 1
		    
		  elif "Remote File" or "Remote File Inclusion" in line:
		    rfi = 1
		    
		  elif "Local File" or "Local File Inclusion" in line:
		    lfi = 1
		      
		  elif  "Disclosure" in info:
		    indis = 1
		    
		  elif  "htaccess.txt" in info:
		    htaccess = 1
		    
		  else:
		    pass
				
		  sys.stdout.write(colors.color.RED+" [!] Vulnerability - "+info+"\n"+colors.color.RESET)
		  sys.stdout.flush()
		  f.write ("\n\nVulnerability  - " +info+"\n")
			  
		  sys.stdout.write(colors.color.RED+" [!] Vulnerability URL: "+url+"/"+check+"\n"+colors.color.RESET)
		  sys.stdout.flush()
		  f.write ("Vulnerability URL 	: "+url+"/"+check+"\n")
				  
		  sys.stdout.write(colors.color.GREEN+" [+] Vulnerability Details: "+found+"\n"+colors.color.RESET+"\n")
		  sys.stdout.flush()
		  f.write ("Vulnerability Details 	: "+found+"\n")
		  
	    f.write ("\n#-------------------------------------------------------------------------------------------#\n\n")
	    f.close()
	    
	    try:
	      # Insert data to db
	      cursor.execute("INSERT INTO jm_vuln_table VALUES ('"
		      + str(scanid) + 
		      "','"+ url	+
		      "','"+ str(scandate)	+
		      "','"+ str(scantime)	+
		      "','"+ str(sqli)	+
		      "','"+ str(xss)	+
		      "','"+ str(csrf)	+
		      "','"+ str(afu)	+
		      "','"+ str(dos)	+
		      "','"+ str(lfi)	+
		      "','"+ str(rfi)	+
		      "','"+ str(indis)	+
		      "','"+ str(htaccess)+"')") 
		
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
	print "[+] Scanned " + str(z) + " sites in " + str(datetime.timedelta(seconds=end))+".\n"

      jmcheck()  
      
    except KeyboardInterrupt:
      print "\n\n[!] Welcome back to main menu..."

      
if __name__ == '__main__':
    main()

#eof    