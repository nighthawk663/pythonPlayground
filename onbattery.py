#!/usr/bin/env python3

import subprocess

p = subprocess.Popen([ 'python3', '/etc/apcupsd/textStatus.py'], cwd='/etc/apcupsd', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
