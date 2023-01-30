import pandas as pd
df = pd.read_csv('customers.csv')

firstname = df['FirstName']

lastname = df['LastName']

country = df['Country']

info = {'name': [], 'country': []}

for i in range(len(firstname)):
    info['name'].append(firstname[i] + ' ' + lastname[i])
    info['country'].append(country[i])

print(info)

df_2 = df.from_dict(info)
df_2.to_csv('customer_country.csv', index=False)
