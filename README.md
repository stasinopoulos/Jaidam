     
                               ;                                            
                               ED.                                          
                               E#Wi                                         
      itttttttt            t   E###G.                                       
      fDDK##DDi         .. Ej  E#fD#W;               ..           ..       :
         t#E           ;W, E#, E#t t##L             ;W,          ,W,     .Et
         t#E          j##, E#t E#t  .E#K,          j##,         t##,    ,W#t
         t#E         G###, E#t E#t    j##f        G###,        L###,   j###t
         t#E       :E####, E#t E#t    :E#K:     :E####,      .E#j##,  G#fE#t
         t#E      ;W#DG##, E#t E#t   t##L      ;W#DG##,     ;WW; ##,:K#i E#t
       jfL#E     j### W##, E#t E#t .D#W;      j###DW##,    j#E.  ##f#W,  E#t
       :K##E    G##i,,G##, E#t E#tiW#G.      G##i,,G##,  .D#L    ###K:   E#t
         G#E  :K#K:   L##, E#t E#K##i      :K#K:   L##, :K#t     ##D.    E#t
          tE ;##D.    L##, E#t E##D.      ;##D.    L##, ...      #G      .. 
           . ,,,      .,,  ,;. E#t        ,,,      .,,           j          
                               L:                          

##### GENERAL INFORMATION

Jaidam is an open source penetration testing tool that would take as input a list of domain names, scan them, determine if wordpress or joomla platform was used and finally check them automatically, for web vulnerabilities using two well‐known open source tools : 

- [WPScan](http://wpscan.org) (in case of wordpress) 
- [JoomScan](http://sourceforge.net/projects/joomscan/) (in case of  joomla). 

The innovative part of Jaidam security tool is that it combines the modules of Joomscan and WPScan in one package providing more functionality to the user saving up much time. Moreover it can handle a list of sites taken as an input so as the user has the ability to run a distributed web vulnerability scan. There is a builtin multithreaded function for faster results in determining the kind of CMS a site uses. 

When the scanning of domain names is completed the user is asked whether he likes to perform a WPScan or a Joomscan. By choosing for example a WPScan then it starts to scan for vulnerabilities all the sites that have recognized as Wordpress sites.

After completing the scan procedure, jaidam stores the results in the `wp_vulne_table` for wordpress results or in the `jm_vulne_table` for joomla results in a sqlite3 database within the file `jaidamSQLite.db`.

The categories of the vulnerabilities the tool will scan for have been chosen based on the [Owasp’s top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project) vulnerability list and are the following: 

For wordpress sites: 
- [SQL Injection](https://www.owasp.org/index.php/SQL_Injection)
- [Cross-site Scripting (XSS)](https://www.owasp.org/index.php/Cross-site_scripting)
- [Site Request Forgery (CSRF)](https://www.owasp.org/index.php/Cross-Site_Request_Forgery_%28CSRF%29)
- [Unrestricted File Upload](https://www.owasp.org/index.php/Unrestricted_File_Upload)
- [Denial of Service](https://www.owasp.org/index.php/Denial_of_Service)
- [Local / Remote file inclusion](https://en.wikipedia.org/wiki/File_inclusion_vulnerability)
- [Information Leakage / Disclosure](https://www.owasp.org/index.php/Information_Leakage)
- robots.txt 

For Joomla sites:
- [SQL Injection](https://www.owasp.org/index.php/SQL_Injection)
- [Cross-site Scripting (XSS)](https://www.owasp.org/index.php/Cross-site_scripting)
- [Site Request Forgery (CSRF)](https://www.owasp.org/index.php/Cross-Site_Request_Forgery_%28CSRF%29)
- [Unrestricted File Upload](https://www.owasp.org/index.php/Unrestricted_File_Upload)
- [Denial of Service](https://www.owasp.org/index.php/Denial_of_Service)
- [Local / Remote file inclusion](https://en.wikipedia.org/wiki/File_inclusion_vulnerability)
- [Information Leakage / Disclosure](https://www.owasp.org/index.php/Information_Leakage)
- Htaccess


##### INSTALL
Jaidam has been written and tested in debian-like distros. The main distro that it was tested on is the new generation of the industry-leading BackTrack Linux penetration testing and security auditing distribution, Kali Linux. 
In order for the program to run in a kali linux distro it is necessary for the distro to be fully updated, upgraded :

- apt-get update && apt-get upgrade
- apt-get dist-upgrade
 
After being download and extracted, the program runs in standalone mode.
In case of other debian-like distros the prerequisites are:

- Ruby >= 1.9.2 - Recommended: 1.9.3
- Curl >= 7.21 - Recommended: latest - FYI the 7.29 has a segfault
- RubyGems - Recommended: latest
- Pyhon = 2.7
- Git
- [WPScan](http://wpscan.org)
- [JoomScan](http://sourceforge.net/projects/joomscan/)


##### STRACTURE
Jaidam is written in Python programming language and its structure is shown below :

    .
    |-- core
    |   |-- colors.py
    |   |-- config.py
    |   |-- __init__.py
    |   |-- menu.py
    |   `-- update.py
    |-- modules
    |   |-- grscan.py
    |   |-- __init__.py
    |   |-- modmenu.py
    |   `-- otenet.py
    |-- jaidam.py
    |-- README
    |-- scan
    |   |-- __init__.py
    |   |-- jms.py
    |   |-- lst.py
    |   `-- wps.py
    |-- sites
    `-- VERSION
    
    4 directories, 16 files
    
##### OPTIONS
      L / l: Create List
      C / c: Create list of custom TXT file
      S / s: Scan a single site
    
      W / w: Use WPScan for scanning wordpress sites
      J / j: Use Joomscan for scanning joomla sites
      M / m: Use Jaidam Extra Modules(*)
      D / d: Automatic creation of list using built in function 
      G / g: Automatic creation of list using built in function (aproximatly 14000 gr sites)
    
      U / u: Update Jaidam to the latest version
      Q / q: Quit

##### ADDING EXTRA MODULES
In this section anyone can write his own python modules for this tool . Example can be another scanner or another list generator script. 

The only thing that you must have in mind is that : 
You must include your script in the `/modules` folder and add your script to the menu in `/modules/modmenu.py`

##### WHO CAN USE IT?
Everyone can use this tool. Jaidam Tolkit has a simple environment and can be used, from web developers that want to test their sites, from pentesters that have multiple/single site to check , either from a researcher that want to have statistics for the situation of specific websites. 


##### WHAT JAIDAM CAN NOT DO?
Jaidam Toolking will not attempt to penetrate any of this site or to find any 0day. This tool will only warn you if there is a possible vulnerability in the site. More information about the vulnerability are presented but in no way this tool will exploit that vulnerability.


##### KNOWN ISSUES
The tool is not compatible (yet) with any other linux distribution except from debian based distros.


##### FUTURE WORK
Jaidam is a security tool that has shown to have much potential as fas as development concerns. There are a lot of aspects that could be improved like:

- Graphical User Interface.
- Support for redhat and fedora distros.
- Features like importing address spaces to be scanned.
- ...


##### LICENSE
    Jaidam Toolkit
    Copyright (C) 2013 Jaidam Development Team.
    
     [*] Paraskevopoulos Ioannis   -  iparaskev[AT]gmail[DOT]com
     [*] Stasinopoulos Anastasios  -  stasinopoulos[AT]unipi[DOT]gr
     [*] Tasiopoulos Vasilis       -  tasiopoulos[DOT]vasilis[AT]gmail[DOT]com
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.


##### ACKNOWLEDGMENTS
Jaidam was developed as a project for the Postgraduate course [Digital Forensics and Web Security](http://temsec.ds.unipi.gr/en/digital-forensics-and-web-security/)
in the [Department of Digital System](http://www.ds.unipi.gr/), [University of Piraeus](http://www.unipi.gr/unipi/en/).
