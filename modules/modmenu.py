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

from modules import otenet
from modules import grscan

def main():
  print """
  [+] Press "D" to create lists from default site.
  [+] Press "G" to create lists from greek .gr domains.
  ---
  [+] Enter "Q" for quit.
  [+] Press any key to return to main menu.
    """
  option = raw_input("Enter Option: > ")
    
  if option =='D' or option =='d':
    otenet.main()

  if option =='G' or option =='g':
    grscan.main()

  if option =='Q' or option =='q':
    print "[-] Exiting Jaidam..\n"
    exit()
   

if __name__ == '__main__':
    main()    
    
#eof