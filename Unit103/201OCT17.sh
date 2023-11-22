#!/bin/bash
# Lets create a while loop than runs a conditinal statment
#Ask the user for an input if they choose:
# 1 then echo hello world
# 2 ping a website or ip address
# 3 run ifconfig
# else echo invalid entry

while true; do
    echo "Enter your choice (1-3 to perform an action, 4 to exit):"
    read choice

    case $choice in
        1) echo "Hello World";;
        2) echo "Enter a website or IP address to ping:" && read target && ping -c 4 $target;;
        3) ifconfig;;
        4) echo "Exiting the script." && exit 0;;
        *) echo "Invalid entry. Please enter a valid option (1-4).";;
    esac
done

