import pandas as pd

tb={'person':['A','B','C','D','E'],
    'hand':[17,15,19,17,21],
    'height':[150,154,169,172,175]
    }


df=pd.DataFrame(tb)

corr=df[['hand','height']].corr()
print(corr)