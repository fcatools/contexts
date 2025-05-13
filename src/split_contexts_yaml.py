#!/usr/bin/python3
# -*- coding: utf-8 -*-

#
# Splits large contexts.yaml into individual files for each context.
#
# Usage:
#
# Author: rja
#
# Changes:
# 2025-05-12 (rja)
# - initial version

outdir = "contexts"

with open("contexts.yaml", "rt") as f:
    outfile = None
    for line in f:
        if len(line) > 1:
            if line[0] != ' ':
                if outfile is not None:
                    outfile.close()
                outfile = open(outdir + "/" + line.strip()[:-5] + ".yaml", "wt")
            else:
                print(line.rstrip()[2:], file=outfile)
