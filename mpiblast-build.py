#!/usr/bin/env python


import string, os


def runcmd(cmd):
        (inf, outerr) = os.popen4(cmd)
	for line in outerr.readlines():
		print line

runcmd('wget ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/CURRENT/ncbi.tar.gz')
