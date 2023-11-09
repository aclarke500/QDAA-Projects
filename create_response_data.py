from sentence_transformers import SentenceTransformer, util
import pandas as pd

model = SentenceTransformer('all-mpnet-base-v2') # load model

# grap data
df = pd.read_csv('data.csv')
relevant_responses = df[['Why do you want to be a QDAA General Member?', 'What experience(s) do you have to enrich your team?']]

# convert data frame column to list
why_responses = relevant_responses['Why do you want to be a QDAA General Member?'].tolist()
why_responses_vectors = [] # create list for us to buld

# encode each response
for response in why_responses:
    response_vector = model.encode(response)
    why_responses_vectors.append(response_vector)

# convert list to data frame and save as csv
why_response_df = pd.DataFrame(why_responses_vectors)
why_response_df.to_csv('why_response_vectors.csv')
