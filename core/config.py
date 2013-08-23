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


class config:

  #############################################################################
  # General configs
  #############################################################################
  version = "1.0.0 [Alpha]"

  #############################################################################
  # Sites Directory
  #############################################################################
  dot       = "./"
  scandir   = "sites/"
  
  #############################################################################
  # Define SQLite3 Database
  #############################################################################
  sqlite3db    = dot + scandir + "jaidamSQLite.db"
  sqlite3_init = scandir + "jaidamSQLite.db"

  #############################################################################
  # Config WPScan components.
  #############################################################################
  wpscantimeout = 120
  wpscan_dir  = "/usr/share/wpscan"
  wpscan_file = dot + scandir + "wpscan.txt"
  wpscan_logs = dot + scandir + "logs/wpscan.log"
  not_id_wpscan_file = dot + scandir + "not_identified_wpscan.txt"
    
    
  #############################################################################
  # Config Joomscan components.
  #############################################################################
  jmscantimeout = 480
  jmscan_dir  = "/usr/share/joomscan"
  jmscan_file = dot + scandir + "joomscan.txt"
  jmscan_logs = dot + scandir + "logs/joomscan.log"
  not_id_jmscan_file = dot + scandir + "not_identified_joomscan.txt"
   
   
  #############################################################################
  # Other text files
  #############################################################################
  scantxt    = "scan.txt"
  scan_file  = dot + scandir + scantxt
  
  othertxt   = "other.txt"
  other_file = dot + scandir + othertxt
  
  errortxt   = "error.txt"
  error_file = dot + scandir + errortxt


  #############################################################################
  # Number of threats
  # Change this number -if needed- for faster listing.
  #############################################################################
  connections = 150
    
    
  #############################################################################
  # SQLite Wordpress Vulnerabilities Table
  #############################################################################
  wp_vuln_table = """CREATE TABLE wp_vuln_table(pk,site,date,time,version,sqli,xss,csrf,fileupload,dos,lfi,rfi,info,robots)"""
  
  
  #############################################################################
  # SQLite Joomla Vulnerabilities Table
  #############################################################################
  jm_vuln_table = """CREATE TABLE jm_vuln_table(pk,site,date,time,sqli,xss,csrf,fileupload,dos,lfi,rfi,info,htaccess)"""
  
  
  
#eof