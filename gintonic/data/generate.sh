#!/bin/bash
USE_SCORING=0
. ../../_testdata_tools/gen.sh  

use_solution compressed_graph.py              # Use ../submissions/accepted/jointgraph.py to generate answer files

compile gen_random.py
compile gen_no_allergies.py
compile gen_low_allergy_count.py
compile gen_worst_case.py
# compile generate_pos.py

# Generate answers to sample cases
sample 1
sample 2


tc  random1 gen_random g=10 i=10 n=100 seed=13152452345
tc  random2 gen_random g=100 i=100 n=100 max=2  seed=1234532323
tc  random3 gen_random g=100 i=100 n=1000 max=10  seed=5434687902
tc  random_big gen_random g=100 i=100 n=10000 max=10 seed=678072632476
# tc  random3 generate_random
tc  no_allergies1 gen_no_allergies g=10 i=10 n=10000 seed=12341234
# tc  pos2 generate_pos
tc  low_allergy1 gen_low_allergy_count g=100 i=100 n=1000 allergies=10 max=10  seed=31415926
tc  worst_case gen_worst_case seed=1567163087