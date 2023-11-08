import re
from collections import Counter

def clean_strings(strings):
    # Compile a regular expression pattern for non-letter characters excluding spaces
    pattern = re.compile('[^a-z\s]+')
    
    # Convert each string to lowercase and remove non-letter characters, preserving spaces
    cleaned_strings = [pattern.sub('', s.lower()) for s in strings]
    
    return cleaned_strings

def count_words_in_strings(strings):
    # Initialize an empty list to hold all words from all strings
    all_words = []
    
    # Iterate over each string in the list
    for string in strings:
        # Use regular expression to split the string into words and filter out non-word characters
        words = re.findall(r'\b\w+\b', string.lower())
        all_words.extend(words)
    
    # Use Counter to count occurrences of each word in the list
    word_count = Counter(all_words)
    
    return dict(word_count)

def sort_dict_by_value(d):
    # Sort the dictionary by value in descending order
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict


def remove_words_from_dict(word_list, word_dict):
    # Remove specific words from the list
    for word in word_list:
        word_dict.pop(word, None)

    # Remove words that are less than 4 letters long
    words_to_remove = [word for word in word_dict if len(word) < 4]
    for word in words_to_remove:
        word_dict.pop(word, None)

    return word_dict

def combine_opportunities(word_dict):
    # Initialize the base count with the count of 'opportunity' or 0 if it doesn't exist
    base_count = word_dict.get('opportunity', 0)
    
    # Add the count of 'opportunities' to 'opportunity' if it exists
    if 'opportunities' in word_dict:
        base_count += word_dict['opportunities']
        # Remove the plural form from the dictionary
        del word_dict['opportunities']
    
    # Set the updated count for 'opportunity'
    word_dict['opportunity'] = base_count

    return word_dict

def count_sentences_with_special_words(special_words, all_sentences):
    count = 0
    not_found = [] # keep track of people not in program
    # Iterate over each sentence in all_sentences
    for sentence in all_sentences:
        # Check if any of the special words are in the sentence
        if any(special_word in sentence for special_word in special_words):
            count += 1
        else:
            not_found.append(sentence)
    return {
        "count": count,
        "not_found":not_found
    }
