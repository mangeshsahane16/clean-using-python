import pandas as pd 
import numpy as np

#_______________________________________read csv

df=pd.read_csv('messydata.csv')


#_________________________________________name column in lowercase

df['Name']=df['Name'].str.lower()

#_________________________________________remove spaces from name column 

df['Name']=df['Name'].str.strip()

#____________________________________________remove duplicates 

df=df.drop_duplicates(subset=df.columns.drop('Customer_ID'),keep='first')

#____________________________Age column__________________________#

#__________________________________________________ age column string values replaceing

df['Age']=pd.to_numeric(df['Age'],errors='coerce')

#______________checking where is null values in age column
#______________print(df[df['Age'].isna()])

# ______________how replace null values in the age column with a random age.........?
#_______________df.loc[df['Customer_ID']==102,'Age']=71
#_______________df.loc[df['Customer_ID']==105,'Age']=72
#_______________df.loc[df['Customer_ID']==118,'Age']=73

#_______________replace the negative value -5 in the age column with 15...........?
#_______________df.loc[df['Age']==-5,['Age']]=15


df['Age']=df['Age'].fillna(100)

#_____________________________________has been updated....?
# print(df['Age'].isna().sum())


#_______________________________email column__________________________#
#______________________________________check which email is null....?

# print(df[df['Email'].isna()])

df.loc[df['Name']=='neha singh','Email']='neha@gmail.com'
df.loc[df['Name']=='sunita rao','Email']='sunita@gmail.com'

#________________________________________check updation...?
# print(df[df['Name']== 'neha singh'])




#_________________________________phone number column______________________________#

#_______________________________checking which phone number box is null....?
#print(df[df['Phone'].isna()])

df.loc[df['Customer_ID']==103,'Phone']=1234567891
df.loc[df['Customer_ID']==110,'Phone']=1987654321

#___________________________________checking updation.....?
#   print(df[df['Customer_ID']==103])


#______________________________________city column___________# 
df['City']=df['City'].str.lower()


#_____________________________________________new clean csv________________________

df.to_csv('clean_data.csv',index=False)

print(df)




