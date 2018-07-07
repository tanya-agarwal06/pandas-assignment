import pandas as pd
#ques 1:
d = {'name':['Tommy','jacky','tanya','aditya'],
      'Age':[20,40,90,10],
     'mail_id':['tom','jack','cartoon','hello'],
     'pno':['712457896','1234567812','1479632587','1256784934']}
dd = pd.DataFrame(d,index=['1','2','3','4'])
print(dd)

#ques 2:
df = pd.read_csv('sample.csv')
print("   -----------------------------a part\n")
head5 = df.head(5)
print(head5)
print("\n  ---------------------------b part\n")
head10 = df.head(10)
print(head10)
print("\n-----------------------------c part\n")
axd = pd.DataFrame(df)
ax = axd.axes
print("the axes is: "+str(ax))
print("the transpose is "+str(axd.T))
print("the shape is "+str(axd.shape))
print("the Data type is "+str(axd.dtypes))
print("\n        d part\n")
last5 = df.tail(5)
print(last5)
print("\n ---------------------------- e part\n")
print("The sum"+str(df['Location'].sum()))
print("the describe is "+str(df['Location'].describe())+"\n")



