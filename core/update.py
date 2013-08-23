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
  
  print "\n[+] Please wait, while updating Jaidam (via Gihub)..\n"
  print "[+] Updating : ",
  
  try:
    update = subprocess.Popen("cd ../ >/dev/null 2>&1"+
      "&& rm -rf Jaidam >/dev/null   2>&1"+
      "&& git clone git://github.com/stasinopoulos/Jaidam.git Jaidam", shell=True).wait()
    print"\n[+] Jaidam updated successfully..." 
    print"[+] Updates not take effect immediately.. May need to restart Jaidam.."
      
  except:
    print"["+colors.color.RED+"FAILED"+colors.color.RESET+"]"
    print "[-] Exiting Jaidam..\n"
    exit()

#eof
