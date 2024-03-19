# import pandas as pd
#
# data = pd.read_excel('../2022.xlsx', sheet_name='Sheet2')
# data = data[data['score_total'] == 10]
#
# clarity = list(data[data['clarity_num'] > 0]['clarity_average'].values)
# print(0, sum([int(x < 0.5) for x in clarity]))
# print(1, sum([int(x >= 0.5) for x in clarity]))
# evidence = list(data[data['evidence_num'] > 0]['evidence_average'].values)
# print(0, sum([int(x < 0.5) for x in evidence]))
# print(1, sum([int(x >= 0.5) for x in evidence]))
# originality = list(data[data['originality_num'] > 0]['originality_average'].values)
# print(0, sum([int(x < 0.5) for x in originality]))
# print(1, sum([int(x >= 0.5) for x in originality]))
# contribution = list(data[data['contribution_num'] > 0]['contribution_average'].values)
# print(0, sum([int(x < 0.5) for x in contribution]))
# print(1, sum([int(x >= 0.5) for x in contribution]))
# motivation = list(data[data['motivation_num'] > 0]['motivation_average'].values)
# print(0, sum([int(x < 0.5) for x in motivation]))
# print(1, sum([int(x >= 0.5) for x in motivation]))
# relatedwork = list(data[data['relatedwork_num'] > 0]['relatedwork_average'].values)
# print(0, sum([int(x < 0.5) for x in relatedwork]))
# print(1, sum([int(x >= 0.5) for x in relatedwork]))
# relevance = list(data[data['relevance_num'] > 0]['relevance_average'].values)
# print(0, sum([int(x < 0.5) for x in relevance]))
# print(1, sum([int(x >= 0.5) for x in relevance]))


import pandas as pd

data = pd.read_excel('../2022.xlsx', sheet_name='Sheet2')

data = data[(data['clarity_num'] > 0) & (data['evidence_num'] > 0) & (data['originality_num'] > 0) &
            (data['contribution_num'] > 0)]
data = data[data['score_total'] == 10]
print(data.shape)

print(data[(data['clarity_average'] < 0.5) & (data['contribution_average'] < 0.5) &
           (data['originality_average'] < 0.5) & (data['evidence_average'] < 0.5)].shape[0])

print(data[(data['clarity_average'] < 0.5) & (data['contribution_average'] < 0.5) &
           (data['originality_average'] < 0.5) & (data['evidence_average'] >= 0.5)].shape[0])
print(data[(data['clarity_average'] < 0.5) & (data['contribution_average'] < 0.5) &
           (data['originality_average'] >= 0.5) & (data['evidence_average'] < 0.5)].shape[0])
print(data[(data['clarity_average'] < 0.5) & (data['contribution_average'] >= 0.5) &
           (data['originality_average'] < 0.5) & (data['evidence_average'] < 0.5)].shape[0])
print(data[(data['clarity_average'] >= 0.5) & (data['contribution_average'] < 0.5) &
           (data['originality_average'] < 0.5) & (data['evidence_average'] < 0.5)].shape[0])

print(data[(data['clarity_average'] < 0.5) & (data['contribution_average'] < 0.5) &
           (data['originality_average'] >= 0.5) & (data['evidence_average'] >= 0.5)].shape[0])
print(data[(data['clarity_average'] < 0.5) & (data['contribution_average'] >= 0.5) &
           (data['originality_average'] < 0.5) & (data['evidence_average'] >= 0.5)].shape[0])
print(data[(data['clarity_average'] >= 0.5) & (data['contribution_average'] < 0.5) &
           (data['originality_average'] < 0.5) & (data['evidence_average'] >= 0.5)].shape[0])
print(data[(data['clarity_average'] < 0.5) & (data['contribution_average'] >= 0.5) &
           (data['originality_average'] >= 0.5) & (data['evidence_average'] < 0.5)].shape[0])
print(data[(data['clarity_average'] >= 0.5) & (data['contribution_average'] < 0.5) &
           (data['originality_average'] >= 0.5) & (data['evidence_average'] < 0.5)].shape[0])
print(data[(data['clarity_average'] >= 0.5) & (data['contribution_average'] >= 0.5) &
           (data['originality_average'] < 0.5) & (data['evidence_average'] < 0.5)].shape[0])

print(data[(data['clarity_average'] <0.5) & (data['contribution_average'] >= 0.5) &
           (data['originality_average'] >= 0.5) & (data['evidence_average'] >= 0.5)].shape[0])
print(data[(data['clarity_average'] >= 0.5) & (data['contribution_average'] >= 0.5) &
           (data['originality_average'] < 0.5) & (data['evidence_average'] >= 0.5)].shape[0])
print(data[(data['clarity_average'] >= 0.5) & (data['contribution_average'] < 0.5) &
           (data['originality_average'] >= 0.5) & (data['evidence_average'] >= 0.5)].shape[0])
print(data[(data['clarity_average'] >= 0.5) & (data['contribution_average'] >= 0.5) &
           (data['originality_average'] >= 0.5) & (data['evidence_average'] < 0.5)].shape[0])

print(data[(data['clarity_average'] >= 0.5) & (data['contribution_average'] >= 0.5) &
           (data['originality_average'] >= 0.5) & (data['evidence_average'] >= 0.5)].shape[0])

