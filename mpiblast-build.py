#!/usr/bin/env python


import string, os


def runcmd(cmd):
        (inf, outerr) = os.popen4(cmd)
	for line in outerr:
		print line,

runcmd('wget ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/CURRENT/ncbi.tar.gz')
runcmd('cvs -d :pserver:anonymous@mpiblast.org:/home/cvs/mpiblast checkout mpiblast')
runcmd('tar zxvf ncbi.tar.gz')
runcmd('ln -s ncbi ncbi_c--Mar_12_2007')
runcmd('patch -p0 < mpiblast/ncbi_Mar2007_evalue.patch')
runcmd('./ncbi/make/makedis.csh')
topdir = os.getcwd()
subdir = 'mpiblast'
os.chdir(subdir)
runcmd('aclocal')
runcmd('autoheader')
runcmd('automake -a')
runcmd('autoconf')
runcmd('./configure --with-ncbi=%s/ncbi' % topdir)
runcmd('make')
runcmd('popd')
