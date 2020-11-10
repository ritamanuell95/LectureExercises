#!/usr/bin/python3
import os
import sys
import subprocess

local_sequence_name=sys.argv[0] 
remote_sequence_name=sys.argv[1] #needs to have the .fasta in it

local_sequence=open(str(local_sequence_name))
local_sequence_contents=local_sequence.read()

remote_sequence=open(str(remote_sequence_name))
remote_sequence_contents=print(remote_sequence.read())

cleanlocalseq=print(local_sequence_contents.replace("X",""))



