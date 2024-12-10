import pandas as pd
from pathlib import Path

df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
df.to_csv(Path('data.csv'), index=False)
