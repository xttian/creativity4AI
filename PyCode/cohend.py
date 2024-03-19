import pandas as pd
import numpy as np
from numpy import std, mean, sqrt


def cohen_d(x, y):
    nx = len(x)
    ny = len(y)
    dof = nx + ny - 2
    return (mean(x) - mean(y)) / sqrt(((nx-1)*std(x, ddof=1) ** 2 + (ny-1)*std(y, ddof=1) ** 2) / dof)


dims = ['clarity_average', 'contribution_average', 'evidence_average', 'motivation_average', 'originality_average',
        'relatedwork_average', 'relevance_average',
        'clarity_num', 'contribution_num', 'evidence_num', 'motivation_num', 'originality_num', 'relatedwork_num',
        'relevance_num',
        'score_total']

data = pd.read_excel('../2023.xlsx', sheet_name='Sheet1')[dims]
data = data.append(pd.read_excel('../2022.xlsx', sheet_name='Sheet1')[dims])
data = data.append(pd.read_excel('../2021.xlsx', sheet_name='Sheet1')[dims])
data = data.append(pd.read_excel('../2020.xlsx', sheet_name='Sheet1')[dims])
data = data.append(pd.read_excel('../2019.xlsx', sheet_name='Sheet1')[dims])
data = data.append(pd.read_excel('../2018.xlsx', sheet_name='Sheet1')[dims])
data = data.append(pd.read_excel('../2017.xlsx', sheet_name='Sheet1')[dims])

# data = pd.read_excel('../2022.xlsx', sheet_name='Sheet1')
# data = data[(data['clarity_num'] > 0) & (data['evidence_num'] > 0) & (data['originality_num'] > 0) &
#             (data['contribution_num'] > 0) & (data['motivation_num'] > 0) & (data['relatedwork_num'] > 0) &
#             (data['relevance_num'] > 0)]
# data = data[(data['clarity_num'] > 0) & (data['evidence_num'] > 0) & (data['originality_num'] > 0) &
#             (data['contribution_num'] > 0)]
# data = data[(data['score_total'] > 6) | (data['score_total'] < 5)]
print(data.shape[0])
dims = ['clarity', 'contribution', 'evidence', 'motivation', 'originality', 'relatedwork', 'relevance']
# dims = ['clarity', 'contribution', 'evidence', 'originality']

for dim_1 in dims:
    data1 = data[(data[dim_1 + '_num'] > 0)]
    print(data1.shape[0])
    dim_data = list(data1[dim_1 + '_average'].values)
    scores = list(data1['score_total'].values)

    pos_data, neg_data = list(), list()
    for index in range(len(dim_data)):
        if dim_data[index] >= 0.5:
            pos_data.append(scores[index])
        else:
            neg_data.append(scores[index])

    print(len(pos_data))
    print(len(neg_data))
    print(cohen_d(pos_data, neg_data))
