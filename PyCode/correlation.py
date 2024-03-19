import pandas as pd
from scipy.stats import pearsonr

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

# data = pd.read_excel('../2023.xlsx', sheet_name='Sheet1')
#
# dim_1 = 'contribution'
# dim_2 = 'originality'
#
# data1 = data[(data[dim_1 + '_num'] > 0) & (data[dim_2 + '_num'] > 0)]
# print(data1.shape[0])
# r, p = pearsonr(data1[dim_1 + '_average'], data1[dim_2 + '_average'])
# print(r, p)

# data = pd.read_excel('../2023-c.xlsx', sheet_name='Sheet3')
# r, p = pearsonr(data['technical_novelty'], data['correctness'])
# print(r, p)
# r, p = pearsonr(data['technical_novelty'], data['score_total'])
# print(r, p)
# r, p = pearsonr(data['correctness'], data['score_total'])
# print(r, p)


# data = pd.read_excel('../2023-c.xlsx', sheet_name='Sheet3')
# dim_1 = 'relevance'
#
# data = data[(data[dim_1 + '_num'] > 0)]
# print(data.shape[0])
# r, p = pearsonr(data[dim_1 + '_average'], data['score_total'])
# print(r, p)
# r, p = pearsonr(data[dim_1 + '_average'], data['technical_novelty'])
# print(r, p)
# # r, p = pearsonr(data[dim_1 + '_average'], data['empirical_novelty'])
# # print(r, p)
# r, p = pearsonr(data[dim_1 + '_average'], data['correctness'])
# print(r, p)

# 1-3 total score
# data = pd.read_excel('../2022.xlsx', sheet_name='Sheet2')
# dims = ['clarity', 'contribution', 'evidence', 'motivation', 'originality', 'relatedwork', 'relevance']
#
# for dim_1 in dims:
#     data = data[(data[dim_1 + '_num'] > 0)]
#     print(data.shape[0])
#     scores = list(data['score_total'].values)
#     score_update = list()
#     for s in scores:
#         if s <= 4:
#             score_update.append(1)
#         elif s >= 7:
#             score_update.append(3)
#         else:
#             score_update.append(2)
#     r, p = pearsonr(data[dim_1 + '_average'], score_update)
#     print(r, p)


dim_1 = 'contribution'
dim_2 = 'originality'
dim_3 = 'evidence'

data1 = data[(data[dim_1 + '_num'] > 0) & (data[dim_2 + '_num'] > 0) & (data[dim_3 + '_num'] > 0)]
print(data1.shape[0])
r, p = pearsonr(data1['score_total'], data1[dim_1 + '_average'])
print(r, p)
r, p = pearsonr(data1['score_total'], data1[dim_2 + '_average'])
print(r, p)
r, p = pearsonr(data1['score_total'], data1[dim_3 + '_average'])
print(r, p)
r, p = pearsonr(data1['score_total'], data1[dim_2 + '_average'] + data1[dim_1 + '_average'])
print(r, p)
r, p = pearsonr(data1['score_total'], data1[dim_3 + '_average'] + data1[dim_1 + '_average'])
print(r, p)
r, p = pearsonr(data1['score_total'], data1[dim_2 + '_average'] + data1[dim_3 + '_average'])
print(r, p)
r, p = pearsonr(data1['score_total'], data1[dim_2 + '_average'] + data1[dim_3 + '_average'] + data1[dim_1 + '_average'])
print(r, p)