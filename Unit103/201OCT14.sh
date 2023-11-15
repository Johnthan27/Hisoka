#!/bin/bash
# Install whois on your Ubuntu

# Add to your bash script a sixth option that calls a function to:

# Take a user input string. Presumably the string is a domain name such as Google.com.
# Run whois against a user input string.
# Run dig against the user input string.
# Run host against the user input string.
# Run nslookup against the user input string.
# Output the results to a single .txt file and open it with your favorite text editor.

# For this challenge you must use at least one variable and one function.

perform_domain_queries() {
echo "Enter the domain name:"
read domain_name

whois $domain_name > results.txt
dig $domain_name >> results.txt
host $domain_name >> results.txt
nslookup $domain_name >> results.txt

cat results.txt
}

echo "Select an option:"
echo "1. Perform domain queries and display results"

read choice

case $choice in
1)
perform_domain_queries
;;
*)
echo "Invalid option"
;;
esac