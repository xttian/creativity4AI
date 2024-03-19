import pandas as pd
import numpy as np

dims = ['clarity_average', 'contribution_average', 'evidence_average', 'motivation_average', 'originality_average',
        'relatedwork_average', 'relevance_average',
        'clarity_num', 'contribution_num', 'evidence_num', 'motivation_num', 'originality_num', 'relatedwork_num',
        'relevance_num',
        'score_total']

# data = pd.read_excel('../2023.xlsx', sheet_name='Sheet1')[dims]
# data = data.append(pd.read_excel('../2022.xlsx', sheet_name='Sheet1')[dims])
# data = data.append(pd.read_excel('../2021.xlsx', sheet_name='Sheet1')[dims])
# data = data.append(pd.read_excel('../2020.xlsx', sheet_name='Sheet1')[dims])
# data = data.append(pd.read_excel('../2019.xlsx', sheet_name='Sheet1')[dims])
# data = data.append(pd.read_excel('../2018.xlsx', sheet_name='Sheet1')[dims])
# data = data.append(pd.read_excel('../2017.xlsx', sheet_name='Sheet1')[dims])
#
# data1 = data[(data['motivation_num'] > 0) & (data['originality_num'] > 0)]
# # data1 = data1[['motivation_average', 'originality_average', 'score_total']]
# # print(data1.shape)
# data1.to_csv('mediation.csv', index=False)

data = pd.read_excel('../2017.xlsx', sheet_name='Sheet1')
data_1 = pd.read_excel('/Users/tianxuetao/Desktop/我的/B博士后/研究方向/学术论文的创造性评价/论文写作/引用17-23oral.xlsx')
id_list = data_1['Id'].values
data = data[data['paper_id'].isin(id_list)]
data = data[['paper_id', 'clarity_average', 'contribution_average', 'evidence_average', 'originality_average',
             'clarity_num', 'contribution_num', 'evidence_num', 'originality_num', 'score_total']]
data.to_excel('2017.xlsx', index=False)
