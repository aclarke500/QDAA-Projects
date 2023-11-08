import pandas as pd
import matplotlib.pyplot as plt
import re
from lib import clean_strings, count_sentences_with_special_words, count_words_in_strings, sort_dict_by_value, remove_words_from_dict, combine_opportunities
from wordcloud import WordCloud

df = pd.read_csv('data.csv')

program_responses = df['What program are you in?']
program_responses = program_responses.tolist()


compsci_words = ["Computing", "Computer Science", "Computer science", "computer science", "computer Science", "computing", "Computing Science", "computing science", "Computing science", "computing Science", "compsci", "Compsci", "cs", "CS", "BCmpH", 'COCA']
compsci_stats = count_sentences_with_special_words(compsci_words, program_responses)
compsci_num = compsci_stats["count"]
compsci_not_found = compsci_stats["not_found"]


commerce_words = ["Commerce", "commerce", "business", "BCom"]
commerce_stats = count_sentences_with_special_words(commerce_words, compsci_not_found)
commerce_num = commerce_stats["count"]
commerce_not_found = commerce_stats["not_found"]


#engineers
eng_words = ["Engineering", "engineering", "Eng", "eng", "engineer"]
eng_stats = count_sentences_with_special_words(eng_words, commerce_not_found)
eng_num = eng_stats["count"]
eng_not_found = eng_stats["not_found"]


programs = [
    "Computer Science",
    "Commerce",
    "Engineering",
    "Other",
]

program_counts = [
    compsci_num,
    commerce_num,
    eng_num,
    len(eng_not_found),
]

plt.bar(programs, program_counts, color='red')
plt.title("Program Distribution at QDAA")
plt.xlabel("Programs")
plt.ylabel("Number of people")
plt.show()

# why do people want to be in QDAA?

responses = df['Why do you want to be a QDAA General Member?']
responses = clean_strings(responses.tolist())




# remove bullshit words
bullshit_words = ["to", "the", "and", "a", "my", "qdaa", "that", "have", "this", "want", "with", "will", "would", "about"
                  "member", "more", "also", "from", "like", "general", "world", "people", "club","into", "about", "member", "believe"
                  ]

word_dict = sort_dict_by_value(count_words_in_strings(responses))
word_dict = combine_opportunities(word_dict)
word_dict = sort_dict_by_value(word_dict)
word_dict = remove_words_from_dict(bullshit_words, word_dict)


top_words = {}
for i in range(20):
    top_words[list(word_dict.keys())[i]] = list(word_dict.values())[i]



#  Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white')

# Generate a word cloud from frequencies
wordcloud.generate_from_frequencies(top_words)

# Display the generated image:
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Remove axis
plt.show()