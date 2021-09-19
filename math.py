#import pandas as pd
import numpy as np
import pandas as pd

a=np.array([3,4,5,6,7])
b=a**2
print(b)

df =pd.DataFrame(a)
df.columns=["Stones"]
print(df)