#!/usr/bin/env python


import string, os


def runcmd(cmd, cd='.'):
        (inf, outerr) = os.popen4('cd %s; %s ' % (cd, cmd))
	for line in outerr:
		print line,

def ask(msg):
	resp = raw_input('%s [y/N]:? ' % msg)
	try:
		if resp.lower()[0] == 'y':
			return True
	except:
		pass

	return False
	

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

	if ask('download ncbi'):
		runcmd('wget ftp://ftp.ncbi.nlm.nih.gov/toolbox/ncbi_tools++/2007/Mar_12_2007/NCBI_C_Toolkit/ncbi_c--Mar_12_2007.tar.gz')


	if ask('untar ncbi'):

		runcmd('ln -s ncbi_c--Mar_12_2007 ncbi')
		runcmd('tar zxvf ncbi_c--Mar_12_2007.tar.gz')


	if ask('checkout mpiblast'):

		runcmd('cvs -d :pserver:anonymous@mpiblast.org:/home/cvs/mpiblast checkout mpiblast')


	if ask('patch ncbi'):

		runcmd('patch -p0 < mpiblast/ncbi_Mar2007_evalue.patch')

	if ask('make ncbi'):
		runcmd('./ncbi/make/makedis.csh')


	subdir='mpiblast'


	if ask('prep mpiblast'):
		runcmd('aclocal', cd=subdir)
		runcmd('autoheader', cd=subdir)
		runcmd('automake -a', cd=subdir)
		runcmd('autoconf', cd=subdir)


	if ask('configure mpiblast'):
		topdir = os.getcwd()
		runcmd('./configure --with-ncbi=%s/ncbi' % topdir, cd=subdir)

	if ask('make mpiblast'):
		runcmd('make', cd=subdir)
	




main()
sys.exit()

