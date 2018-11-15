import pandas as pd

df = pd.read_csv('summer.csv')
df.head()

df.loc[df.Gender == 'Women']

cnt = df.groupby(['Year', 'Gender', 'Athlete']).count()
agg = cnt.groupby('Athlete').agg({'Medal': sum})

agg.nlargest(5, 'Medal')


female_medalists = df.loc[df.Gender == 'Women']
cnt = female_medalists.groupby(['Athlete']).count()
agg = cnt.groupby('Athlete').agg({'Medal': sum})

agg.nlargest(1, 'Medal')

male_medalists = df.loc[df.Gender == 'Men']
cnt = male_medalists.groupby(['Athlete']).count()
agg = cnt.groupby('Athlete').agg({'Medal': sum})

agg.nlargest(1, 'Medal')

medals_by_country = female_medalists.groupby(['Country']).count()
agg = medals_by_country.groupby('Country').agg({'Medal': sum})

agg.nlargest(10, 'Medal')


medals_by_country = male_medalists.groupby(['Country']).count()
agg = medals_by_country.groupby('Country').agg({'Medal': sum})

agg.nlargest(10, 'Medal')

import matplotlib.pyplot as plt

medals_by_country = df.groupby(['Country','Medal'])['Athlete'].count().reset_index()

medals_by_country = medals_by_country.pivot('Country', 'Medal', 'Athlete')

medals_by_country = medals_by_country.sort_values(by='Gold',ascending=False)
medals_by_country = medals_by_country.nlargest(10, 'Gold')

medals_by_country.plot.barh(width = 0.8, color = ['#900C3F','#FFE933','#C0C0C0'])

figure = plt.gcf()
figure.set_size_inches(12,12)
plt.title('Medals Distribution Of Top 10 Countries (Summer Olympics)')
plt.show()
