# wpbrute

## Bruteforcing Wordpress CMS users' passwords via the XMLRPC interface.
This script is a PoC for the "Brute Force Amplification Attack" exploit against XMLRPC interfaces enabling the *system.multicall()* method (enabled by default). 

The *system.multicall()* method allows multiple calls to be sent within a single HTTP request. Using this "wrapper", malicious attackers can carry out a large number of login attempts (bruteforce) with a minimal network impact, consequently making them stealthier and more efficient.

At the moment, the maximum number of calls which can be encapsulated within the *system.multicall()* method without triggering a networking error is 1999 calls meaning that for each HTTP request sent 1999 different login attempts are performed.

More information about the bruteforce amplification attack can be found at:

## Installation
```
$ git clone https://github.com/cyborg4/wpbrute.git
$ cd wpbrute
$ python -m pip install -r requirements.txt
```
# usage:
 python3 site username passwordfile
##example: 
 python3 site.com admin passlist.txt

## Dependencies
### Third-party libraries
#### colorama :
The *python3-colorama* package is required. 

<https://pypi.python.org/pypi/colorama>

## License
   Copyright (C) 2020 Mr_Cyborg
