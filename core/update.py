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


import time
import os
import sys
import subprocess

from core import colors

def main():

  definepath = os.getcwd()
  time.sleep(1)
  
  sys.stdout.write("\n[+] Please wait, while checking for updates (via Gihub) ... ")
  sys.stdout.flush()
  
  try:
    null = open("/dev/null", "w")
    subprocess.Popen("git", stdout=null, stderr=null)
    null.close()

  except OSError:
    print "["+colors.color.RED+"FAILED"+colors.color.RESET+"]"
    print "[-] Exiting Jaidam..\n"
    exit()

  try:
    print "\n"
    update = subprocess.Popen("git pull", shell=True).wait()
    
  except:
    print"["+colors.color.RED+"FAILED"+colors.color.RESET+"]"
    print "[-] Exiting Jaidam..\n"
    exit()

#eof
