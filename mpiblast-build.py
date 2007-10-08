#!/usr/bin/env python


import string, os


def runcmd(cmd):
        (inf, outerr) = os.popen4(cmd)
	for line in outerr:
		print line,

doNcbi = True

import optparse
import sys

def main():
	# Set up our options
	option_parser = optparse.OptionParser(
		usage='usage: %prog [options]'
		)
	option_parser.set_defaults(doNcbi = False,
				   doDownloadNcbi = False,
				   )

	option_parser.add_option('--do-ncbi', dest='doNcbi',
				 action='store_true',
				 help='download and build ncbi',
				 )
	option_parser.add_option('--no-ncbi', dest='doNcbi',
				 action='store_false',
				 help='skip ncbi',
				 )
	option_parser.add_option('--do-download-ncbi', dest='doDownloadNcbi',
				 action='store_true',
				 help='download ncbi',
				 )
	option_parser.add_option('-v', '--verbose',
				 dest='verbose',
				 action='store_true',
				 default=True,
				 help='Show progress',
				 )
	option_parser.add_option('-q', '--quiet',
				 dest='verbose',
				 action='store_false',
				 help='Do not show progress',
				 )
	

	(options, args) = option_parser.parse_args()
	print 'options=%s' % options
	print 'args=%s' % args

        if options.doDownloadNcbi:
 	    #runcmd('wget ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/CURRENT/ncbi.tar.gz')
	    #runcmd('ln -s ncbi ncbi_c--Mar_12_2007')

	    runcmd('wget ftp://ftp.ncbi.nlm.nih.gov/toolbox/ncbi_tools++/2007/Mar_12_2007/NCBI_C_Toolkit/ncbi_c--Mar_12_2007.tar.gz')
	    runcmd('ln -s ncbi_c--Mar_12_2007 ncbi')
	    runcmd('ln -s ncbi_c--Mar_12_2007.tar.gz ncbi.tar.gz')


        if options.doNcbi:

	    runcmd('tar zxvf ncbi.tar.gz')
	    runcmd('cvs -d :pserver:anonymous@mpiblast.org:/home/cvs/mpiblast checkout mpiblast')
	    runcmd('patch -p0 < mpiblast/ncbi_Mar2007_evalue.patch')
	    runcmd('./ncbi/make/makedis.csh')






main()
sys.exit()


topdir = os.getcwd()
subdir = 'mpiblast'
os.chdir(subdir)
runcmd('aclocal')
runcmd('autoheader')
runcmd('automake -a')
runcmd('autoconf')
runcmd('./configure --with-ncbi=%s/ncbi' % topdir)
runcmd('make')
os.chdir(topdir)
