#!/BIN/BASH

# Script: Ops 201 Class 01 Ops Challenge Solution
# Author: Johnthan Butler
# Date of latest revision: 11/6/23
# purpose: Print a string to the terminal

echo "enter a website"
read website
whois $website >> whois.txt
dig $website >> whois.txt
host $website >> whois.txt
nslookup >> whois.txt