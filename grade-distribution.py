import pandas as pd
import matplotlib.pyplot as plt
from lib import program_words
from text_analysis_lib import get_indexes_of_programs

df = pd.read_csv('data.csv')


def get_year_distributions(years: list) -> dict:
  year_distributions = {
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
  }
  for year in years:
    for key in year_distributions.keys():
      if str(year[0]) == str(key):
        year_distributions[key] += 1


  return year_distributions

all_programs_years = df["What year are you in?"].tolist()
all_year_distribution = get_year_distributions(all_programs_years)
print(all_year_distribution)

# Creating bar graph
plt.figure(figsize=(8, 6))
plt.bar(all_year_distribution.keys(), all_year_distribution.values(), color='skyblue')
plt.xlabel('Year')
plt.ylabel('Number of Students')
plt.title('Year Distribution of Students for QDAA 2023-2024')
plt.show()

plt.clf()
# CS kids
cs_year_label_vector = get_indexes_of_programs(program_words["compsci"], df['What program are you in?'].tolist())
cs_df = df[cs_year_label_vector]
cs_years = cs_df["What year are you in?"].tolist()
cs_years = get_year_distributions(cs_years)
plt.bar(cs_years.keys(), cs_years.values(), color='green')
plt.xlabel('Year')
plt.ylabel('Number of CS Students')
plt.title('Year Distribution of CS Students for QDAA 2023-2024')
plt.show()

plt.clf()
# commerce kids
com_year_label_vector = get_indexes_of_programs(program_words["commerce"], df['What program are you in?'].tolist())
com_df = df[com_year_label_vector]
com_years = com_df["What year are you in?"].tolist()
com_years = get_year_distributions(com_years)

plt.bar(com_years.keys(), com_years.values(), color='grey')
plt.xlabel('Year')
plt.ylabel('Number of Commerce Students')
plt.title('Year Distribution of Commerce Students for QDAA 2023-2024')
plt.show()

plt.clf()
# eng kids
eng_year_label_vector = get_indexes_of_programs(program_words["eng"], df['What program are you in?'].tolist())
eng_df = df[eng_year_label_vector]
eng_years = eng_df["What year are you in?"].tolist()
eng_years = get_year_distributions(eng_years)

plt.bar(eng_years.keys(), eng_years.values(), color='purple')
plt.xlabel('Year')
plt.ylabel('Number of Engineering Students')
plt.title('Year Distribution of Engineering Students for QDAA 2023-2024')
plt.show()

plt.clf()