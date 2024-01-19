

# romstring() function create a new one-dimensional array initialized from text data in a string.

import numpy as np
   
gfg = np.fromstring('1, 2', dtype=int, sep=',')
   
print(gfg) 