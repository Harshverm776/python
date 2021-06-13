import pandas as pd
dic={'PNAME':['TV','AC','TV','WM','AC','TV'],
     'COMPANY':['LG','WHIRLPOOL','LG','LG'],
     'PRICE':[10000,25000,15000,12000,28000,15000],
     'QTY':[10,5,15,8,12,5]}
print(dic)
df=pd.DataFrame(dic,index=['P1','P2','P3','P4','P5','P6'])
print(df)
