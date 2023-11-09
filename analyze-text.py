import pandas as pd
from text_analysis_lib import get_indexes_of_programs 
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x_mat = pd.read_csv('why_response_vectors.csv')
pca = PCA(n_components=3)
pca_result = pca.fit_transform(x_mat)

x_mat2 = pd.DataFrame(data=pca_result, columns=['pca1', 'pca2', 'pca3'])
response_df = pd.read_csv('data.csv')

program_responses = response_df['What program are you in?'].tolist()
compsci_labels = get_indexes_of_programs(["Comput", "comput"], program_responses)


compsci_df = x_mat2[compsci_labels]
not_compsci_df = x_mat2[[not i for i in compsci_labels]]

# plt.scatter(compsci_df['pca1'], compsci_df['pca2'], color='red')
# plt.scatter(not_compsci_df['pca1'], not_compsci_df['pca2'], color='blue')
# plt.show()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(compsci_df['pca1'], compsci_df['pca2'], compsci_df['pca3'], color='red')
ax.scatter(not_compsci_df['pca1'], not_compsci_df['pca2'], not_compsci_df['pca3'], color='blue')
plt.show()

