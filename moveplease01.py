#!/usr/bin/env python3

import shutil
import os
os.chdir("/Users/chaynorhsiao/Code/mycode/")

shutil.move('raynor.obj', 'ceph_storage/')
xname = input("what is the new name for kerrigan.obj? ")
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
