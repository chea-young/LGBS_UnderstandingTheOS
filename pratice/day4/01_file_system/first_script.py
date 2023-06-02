#!/usr/bin/env python3
import sys

print("Output ###: ")
filereader = open("./first_text.txt", 'r')
for row in filereader:
  print(row.strip())
filereader.close()