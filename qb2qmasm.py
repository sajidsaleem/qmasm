#! /usr/bin/env python3

###################################
# Convert Qubist to QMASM         #
# By Scott Pakin <pakin@lanl.gov> #
###################################

import argparse
import sys

# Parse the command line.
cl_parser = argparse.ArgumentParser(description="Convert Qubist input to QMASM input")
cl_parser.add_argument("input", nargs="?", metavar="FILE", default="-",
                       help="Qubist-format input file (default: standard input)")
cl_parser.add_argument("-o", "--output", metavar="FILE", default="-",
                           help="file to which to write QMASM code (default: stdandard output)")
cl_parser.add_argument("-f", "--format", metavar="FORMAT", default="%d",
                           help='printf-style format string for formatting qubit numbers (default: "%%d")')
cl_args = cl_parser.parse_args()

# Open the input file.
if cl_args.input == "-":
    infile = sys.stdin
else:
    try:
        infile = open(cl_args.input, "r")
    except IOError:
        sys.stderr.write("%s: Failed to open %s for input" % cl_args.input)
        sys.exit(1)

# Open the output file.
if cl_args.output == "-":
    outfile = sys.stdout
else:
    try:
        outfile = open(cl_args.output, "w")
    except IOError:
        sys.stderr.write("%s: Failed to open %s for output" % cl_args.output)
        sys.exit(1)

# Convert each line in turn.
for line in infile:
    fields = line.split()
    if len(fields) != 3:
        continue
    if fields[0] == fields[1]:
        # Point weight
        fmt = cl_args.format + " %s\n"
        outfile.write(fmt % (int(fields[0]), fields[2]))
    else:
        # Coupler strength
        fmt = cl_args.format + " " + cl_args.format + " %s\n"
        outfile.write(fmt % (int(fields[0]), int(fields[1]), fields[2]))

# Wrap up.
if cl_args.input != "-":
    infile.close()
if cl_args.output != "-":
    outfile.close()