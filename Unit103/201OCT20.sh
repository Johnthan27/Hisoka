#!/bin/bash
# Today we are going to use a case statment instead of a conditional
# Have the program ask how your day is and echo out a response for good or bad
# Case statment format is a little different so please look up how this would be formated

#!/bin/bash

# Ask the user how their day is
read -p "How is your day? (good/bad): " response

# Check the response and echo a message
case "$response" in
    "good") echo "That's great! Keep it up." ;;
    "bad") echo "I'm sorry to hear that. Tomorrow is a new day!" ;;
    *) echo "Invalid response. Please enter 'good' or 'bad'." ;;
esac
