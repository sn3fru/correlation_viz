def plotCorrGraph(df):
  # libraries
  !pip install networkx
  import pandas as pd
  import numpy as np
  import networkx as nx
  import matplotlib.pyplot as plt


  # Calculate the correlation between individuals. We have to transpose first, because the corr function calculate the pairwise correlations between columns.
  corr = df.corr().abs()
  corr
  
  # Transform it in a links data frame (3 columns only):
  links = corr.stack().reset_index()
  links.columns = ['var1', 'var2','value']
  
  # Keep only correlation over a threshold and remove self correlation (cor(A,A)=1)
  links_filtered=links.loc[(links['var1'] != links['var2'])]
  links_filtered

  temp = []
  checkvalues= []
  for row in links_filtered.values:
      if row[2]>.1 and row[2] not in checkvalues:
          temp.append(row)
          checkvalues.append(row[2])
        
  links_filtered = pd.DataFrame(temp, columns=['var1', 'var2','value'])

  # Build your graph
  G=nx.from_pandas_edgelist(links_filtered, 'var1', 'var2', )
  
  # Plot the network:
  nx.draw(G, with_labels=True, font_size=10, alpha=.75, node_color='#A0CBE2',edge_color=links_filtered.value.values, width=4, edge_cmap=plt.cm.Blues)
  plt.show()

plotCorrGraph(df)
