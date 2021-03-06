###################################
# QMASM global variables          #
# By Scott Pakin <pakin@lanl.gov> #
###################################

import qmasm
import sys

# Name of this program
qmasm.progname = sys.argv[0]

# Map between symbols and numbers.
qmasm.sym_map = qmasm.SymbolMapping()

# List of Statement objects
qmasm.program = []

# Define our internal representation.
qmasm.chain_strength = 0    # Strength of chain couplers
qmasm.pin_strength = 0      # Strength of pin couplers
