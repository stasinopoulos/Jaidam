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
import time
import sqlite3
 
from core import colors
from core import menu
from core import update
from core import config
 
from scan import lst
from scan import wps
from scan import jms

from modules import modmenu

def sqlite_check():
    if subprocess.Popen("which sqlite3 >/dev/null 2>&1", shell=True).wait() == 0 :
      pass
    
    else:
      print("[-] Error : sqlite3 not found..")
      print "[+] Please wait, while installing sqlite...\n"
      
      if subprocess.Popen("apt-get install sqlite3 -y >/dev/null  2>&1", shell=True).wait() == 0:
	pass

      else:
	print("[-] Installation failed.. - Try it again, manually!\n")
	exit()
	
def database():
  print "[+] Please wait, while checking database..."
  time.sleep(1)
  
  # Create database
  if os.path.exists(config.config.sqlite3_init):
    
    conn = sqlite3.connect(config.config.sqlite3_init)
    cursor = conn.cursor()
    print "[+] Done..."
    pass
  
  else:
    conn = sqlite3.connect(config.config.sqlite3_init)
    cursor = conn.cursor()
    
    # Create Wordpress tables
    print "  [+] Creating 'wp_vuln_table' table..."
    try:
      cursor.execute(config.config.wp_vuln_table) 
      print "  [+] Done...\n"
      
    except Exception, e:
      print "  [-] Error : " + str(e) + "...\n"
      exit()
      
    # Create Joomla tables
    print "  [+] Creating 'jm_vuln_table' table..."
    try:
      cursor.execute(config.config.jm_vuln_table) 
      print "  [+] Done...\n"
      
    except Exception, e:
      print "  [-] Error : " + str(e) + "...\n"
      exit()
    
    # save data to database
    conn.commit() 

menu.logo()

print "[+] Version : " + config.config.version 
print "[+] Copyright (C) 2013 - Jaidam Development Team. \n"

try:
  sqlite_check()
  database()
  
except:
  exit()

while True:
  print """
[+] Jaidam Toolkit Menu:
  [+] Press "L" to create the lists.
  [+] Press "W" for WPScan.
  [+] Enter "J" for Joomscan.
  [+] Press "M" for extra modules.
  ---
  [+] Enter "U" for update.
  [+] Enter "Q" for quit.
  """
 
  option = raw_input("Enter Option: > ").upper()
  if option =='L':
    lst.main()
   
  if option =='W':
    wps.main()
 
  if option =='J':
    jms.main()

  if option =='M':
    modmenu.main()

  if option =='U':
    update.main() 
    
  if option =='Q':
    print "[-] Exiting Jaidam..\n"
    exit()
    
if __name__ == '__main__':
    main()
    
#eof
