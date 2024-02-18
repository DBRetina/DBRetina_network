from dbretina_viz import DBRetinaViz
import pandas as pd

edge_df = pd.read_csv('/home/mabuelanin/dib-dev/dbretina/05-2023-pathways/graph_viz/gh_jaal/test_edges.tsv', sep='\t')
node_df = pd.read_csv('/home/mabuelanin/dib-dev/dbretina/05-2023-pathways/graph_viz/gh_jaal/test_nodes.tsv', sep='\t')
j = DBRetinaViz(edge_df, node_df)
j.plot(debug=True)