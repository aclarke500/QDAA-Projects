import pandas as pd

def get_indexes_of_programs(special_words, all_sentences):
    found = [False]*len(all_sentences)

    for i in range(len(all_sentences)):
        sentence = all_sentences[i]
        # Check if any of the special words are in the sentence
        if any(special_word in sentence for special_word in special_words):
            found[i] = True

    return found


def get_labels():
  x_mat = pd.read_csv('data.csv')

  program_responses = x_mat['What program are you in?'].tolist()
  compsci_labels = get_indexes_of_programs(["Comput", "comput"], program_responses)

  return compsci_labels

