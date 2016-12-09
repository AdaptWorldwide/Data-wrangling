import pandas as pd

for i,chunk in enumerate(pd.read_csv('filename.csv', chunksize=500000)):
    chunk.to_csv('chunk{}.csv'.format(i))
