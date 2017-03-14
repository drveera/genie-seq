#!/bin/env python

'''
usage:
 gseq bwa [options] --fqlist=FILE

options:
 --fqlist=FILE     fastq list
 --ref-genome=FILE  reference fasta file [default: |resources/bwa/reference/b37/human.b37.fasta]

'''
from docopt import docopt
import sys
sys.path.insert(1, sys.path[0] + '/../../../library')
import md
from md import process_list

arguments = docopt(__doc__)
if __name__ == '__main__':
    md.main(arguments, ['bwa'])
