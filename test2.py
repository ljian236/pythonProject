"""
import pandas as pd
import numpy as np

dates=pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['A','B','C','D'])


df.iloc[2,2]=1111
df.loc['20130101','B']=2222
df.B[df.A>4]=0
df['F']=np.nan

df['E']=pd.Series([1,2,3,4,5,6],index=pd.date_range('20130101',periods=6))

print(df)


import pandas as pd

data=pd.read_csv('student.csv')

print(data)

data.to_pickle('student.pickle')

"""

import pandas as pd
import numpy as np

#concatenating
"""
df1=pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2=pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3=pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])

print(df1)
print(df2)
print(df3)

res=pd.concat([df1,df2,df3],axis=0,ignore_index=True)
print(res)
"""
#join,['inner','outer']

df1=pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'], index=[1,2,3])
df2=pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d','e'], index=[2,3,4])

print(df1)
print(df2)
