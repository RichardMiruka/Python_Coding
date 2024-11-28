# creating a progress bar using python

# pip install tqdm

import time
from tqdm import tqdm
import time
for i in range(100):
    time.sleep(0.2)

for i in tqdm(range(100)):
    time.sleep(0.2)

print("Done")
