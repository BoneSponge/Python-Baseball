import pandas as pd
import matplotlib.pyplot as plt

from data import games

attendance = games.loc[(games['type'] == 'info') & (games['multi2'] == 'attendance'), ['year', 'multi3']]
# 1st () arguments denote criteria for rows selection, 2nd argument filters out desired columns containing
# appropriate row info

attendance.columns = ["year", 'attendance']

attendance.loc[:, 'attendance'] = pd.to_numeric(attendance.loc[:, 'attendance'])

attendance.plot(x='year', y='attendance', figsize=(15, 7), kind='bar')

plt.xlabel("Year")
plt.ylabel("Attendance")

plt.axhline(y=attendance["attendance"].mean(), label='Mean', linestyle='--', color='green')

plt.show()

