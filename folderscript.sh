#!/bin/bash

# Define the main folder name
main_folder="TheBigPyOff"

# Create the main folder
mkdir -p "$main_folder"

# Loop to create 25 subfolders named "december1" to "december24"
for i in {1..25}; do
    mkdir -p "$main_folder/december$i"
    mkdir -p "$main_folder/december$i/input"
done

echo "Folders created successfully."

