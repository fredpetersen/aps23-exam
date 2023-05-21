#!/bin/bash
USE_SCORING=0
. ../../_testdata_tools/gen.sh  

use_solution jointgraph.py              # Use ../submissions/accepted/jointgraph.py to generate answer files

compile gen_random.py
compile gen_no_allergies.py
# compile generate_pos.py

# Generate answers to sample cases
sample 1
# sample 2


tc  random1 gen_random g=10 i=10 n=100 seed=13152452345
tc  random2 gen_random g=100 i=100 n=100 allergies=10 max=2  seed=1234532323
tc  random3 gen_random g=100 i=100 n=1000 allergies=10 max=10  seed=5434687902
# tc  random3 generate_random
tc  no_allergies1 gen_no_allergies g=10 i=10 n=1000 seed=12341234
# tc  pos2 generate_pos