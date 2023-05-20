import pandas as pd
data = pd.read_csv('Ecommerce Purchases')
print(data)

print('\n')
print('DISPLAY TOP 10 ROWS OF THE DATASET')
print(data.head())

print('\n')
print('DISPLAY LAST 10 ROWS OF THE DATASET')
print(data.tail())

print('\n')
print('PRINT DATATYPE OF EACH COLUMN')
print(data.dtypes)

print('\n')
print('CHECK THE NULL VALUES IN THE DATASET')
print(data.isnull().sum())

print('\n')
print('NUMBER OF ROWS AND COLUMNS IN THE DATASET')
print(data.shape)
print('The number of columns:',len(data.columns))
print('The number of rows:',len(data.index))
print('\n')
print(data.info)

print('\n')
print('PRINT HIGHEST AND LOWEST PURCHASES')
print('The highest purchase price is:',data['Purchase Price'].max())
print('The lowest purchase price is:',data['Purchase Price'].min())

print('\n')
print('THE AVERAGE PURCHASE PRICE')
print(data['Purchase Price'].mean())

print('\n')
print('HOW MANY PEOPLE HAVE FRENCH 'FR' AS THEIR LANGUAGE?')
print(len(data[data['Language']=='fr']))

'''print('\n')
print('ALTERNATE WAY')
print(data[data['Language']=='fr'].count())'''

print('\n')
print('OVERALL STATISTICS OF THE DATA SET')
print(data.describe())

print('\n')
print('JOB TITLES CONTAINS ENGINEER')
print(len(data[data['Job'].str.contains('engineer',case=False)]))  #to make it case sensitive write case: True

print('\n')
print('FIND EMAIL OF THE PERSON WITH THE FOLLOWING IP ADDRESS: 132.207.160.22')
print(data[data['IP Address']=='132.207.160.22']['Email'])

print('\n')
print('HOW AMNY PEOPLE HAVE MASTERCARD AND MADE PURCHASES ABOVE 50?')

print(len(data[(data['CC Provider']=='Mastercard') & (data['Purchase Price']>50)]))
print('ANOTHER METHOD')
print((data[(data['CC Provider']=='Mastercard') & (data['Purchase Price']>50)]).count())

print('\n')
print('THE EMAIL OF THE PERSON WITH THE CREDIT CARD NUMBER: 46648258997302')
print(data[data['Credit Card']==4664825258997302]['Email'])

print('\n')
print('HOW MANY PEOPLE PURCHASE DURING THE AM AND HOW MANY PEOPLE PURCASE DURING PM?')
print(data['AM or PM'].value_counts())

print('\n')
print('HOW MANY PEOPLE HAVE CREDIT CARDS THAT EXPIRES IN 2020?')
#print(data['CC Exp Date'])
#using function
def func():
    count=0
    for date in data['CC Exp Date']:
        if date.split('/')[1]=='20':
            count=count+1
    print(count)
func()

'''#using lambda function
print('Another Method')
print(len(data[data['CC Exp Date'].apply(lambda x:x[3:]=='20')]))'''

print('\n')
print('TOP FIVE MOST POPULAR EMAIL PROVIDERS(EG. GMAIL.COM, YAHOO.COM, ETC...)')
#using function
list_1=[]
for email in data['Email']:
    list_1.append(email.split('@')[1])
data['Temporary_column']=list_1
print(data['Temporary_column'].value_counts().head(5))

'''

#using lambda function
print('Another way')
#with lambda function
print(data['Email'].apply(lambda x:x.split('@')[1]).value_counts().head(5))'''
                                                            
