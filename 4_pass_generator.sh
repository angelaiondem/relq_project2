#!/bin/bash

# Get the length of the password
while true; do
    read -p "Provide the length of the password: " pass_length
    if (( pass_length >= 8 )); then
        break
    else
        echo "Password length must be at least 8 characters."
    fi
done

# Define character sets
uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase='abcdefghijklmnopqrstuvwxyz'
numbers='0123456789'
special_chars='!@#$%^&*()-_=+[{]}\|;:,<.>?/'

# Generate random characters
random_upper=$(echo $uppercase | fold -w1 | shuf | head -n1)
random_lower=$(echo $lowercase | fold -w1 | shuf | head -n1)
random_number=$(echo $numbers | fold -w1 | shuf | head -n1)
random_special=$(echo $special_chars | fold -w1 | shuf | head -n1)

# Generate random password
password=$(echo "$random_upper$random_lower$random_number$random_special" | tr -d '\n')

# Add random characters to meet length requirement
remaining_length=$((${pass_length} - ${#password}))
random_chars=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9!@#$%^&*()-_=+[{]}\|;:,<.>/?' | fold -w1 | head -n$remaining_length)
password="$password$random_chars"

# Shuffle the password
password=$(echo "$password" | fold -w1 | shuf | tr -d '\n')

echo "$password"