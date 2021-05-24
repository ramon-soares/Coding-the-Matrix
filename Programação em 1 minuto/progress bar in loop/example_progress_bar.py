# pip install tqdm

from tqdm import tqdm
from time import sleep

for i in tqdm(range(50)):
    sleep(0.05)
    