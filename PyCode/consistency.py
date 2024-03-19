import pandas as pd

data = pd.read_excel('../2023.xlsx', sheet_name='Sheet2')

paper_data = data.groupby(data['paper_id'])

total, consist1, consist2, consist3 = 0, 0, 0, 0
for paper_id, review_data in paper_data:
    scores = list(review_data['empirical_novelty'].values)
    total += 1
    if max(scores) - min(scores) <= 0:
        consist1 += 1
    if max(scores) - min(scores) <= 2:
        consist2 += 1
    if max(scores) - min(scores) <= 4:
        consist3 += 1

print(consist1, total, float(consist1) / total)
print(consist2, total, float(consist2) / total)
print(consist3, total, float(consist3) / total)


# total, consist1, consist2 = 0, 0, 0
# for paper_id, review_data in paper_data:
#     scores = list(review_data[review_data['clarity_num'] > 0]['clarity_average'].values)
#     if len(scores) > 1:
#         total += 1
#         if max(scores) <= 0.5 or min(scores) >= 0.5:
#             consist1 += 1
#         if max(scores) - min(scores) <= 0.5:
#             consist2 += 1
# print(consist1, total, float(consist1) / total)
# print(consist2, total, float(consist2) / total)
