#!/usr/bin/env python3 

import os
import sys

debian={}
deepin={}

for line in open("debian.p"):
    pkgs=line.split(' ',1)[0].strip()
    ver=line.split(' ',1)[1].strip().strip('\n')
    debian[pkgs]=ver

for line in open("deepin.p"):
    pkgs=line.split(' ',1)[0].strip()
    ver=line.split(' ',1)[1].strip().strip('\n')
    deepin[pkgs]=ver

for key in deepin:
    if key in debian.keys():
        if deepin[key] == debian[key]:
            print("package same,%s version is  %s"%(key,deepin[key]))
        else:
            file=open("notsame.txt","a+w")
            file.write("%s  %s   %s\n"%(key,deepin[key],debian[key]))
    else:
        print("package %s in deepin,not in debian"%(key))

for key in debian:
    if key not in deepin.keys():
        file=open("indebiannotindeepin.txt","a+w")
        file.write("%s     %s\n"%(key,debian[key]))

