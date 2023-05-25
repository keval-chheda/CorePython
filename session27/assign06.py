import pandas as pd
import numpy as np

p1 = pd.Series([2,4,6,8,10])
p2 = pd.Series([8,10,12,14,16])

p1[~p1.isin(p2)]
p_u = pd.Series(np.union1d(p1,p2))
p_i = pd.Series(np.intersect1d(p1, p2))
p_u[~p_u.isin(p_i)]
print(p_u)


