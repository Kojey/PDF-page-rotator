#!/usr/bin/python

"""
author	Othniel Konan
version	2018-11-08
description	rotate all pdfs in the current folder given a direction of rotation
"""
import os
import subprocess
import argparse


files =  []

parser = argparse.ArgumentParser()
parser.add_argument("direction", help="direction of the rotation", choices=["east","west","north","south"], default="east")
args = parser.parse_args()

direction = "1-end"+str(args.direction)
res = subprocess.check_output(["ls"])

for line in res.splitlines():
	files.append(str(line).split("'")[1])

for i in range(0,len(files)):
	temp = files[i].split(".")
	if temp[len(temp)-1] == "pdf":
		subprocess.run(["pdftk", files[i], "cat", direction, "output", str("output^"+files[i])])
		subprocess.run(["mv",str("output^"+files[i]),files[i]])

