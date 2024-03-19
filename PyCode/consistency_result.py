import pandas as pd

results = pd.read_excel('./assets/Results.xlsx')
result_data = results[results['year'] == 'ICLR2023']
result_class = list(result_data['type'].values)

print(list(set(result_class)))

ids = list(result_data['id'].values)

data = pd.read_excel('../2023.xlsx', sheet_name='Sheet1')
review_data = data.groupby(data['paper_id'])

num = 0

type_dict = dict()
for type_item in list(set(result_class)):
    type_dict[type_item] = list()

for paper_id, review_data in review_data:
    if paper_id in ids:
        num_clarity = list(review_data['clarity_num'].values)
        score_clarity = 0
        if sum(num_clarity) > 0:
            score_ave = list(review_data['clarity_average'].values)
            score_clarity = sum([num_clarity[i] * score_ave[i] for i in range(len(num_clarity))]) / sum(num_clarity)
            # score_clarity = max(score_ave)
        score_clarity = 1 if score_clarity >= 0.5 else 0

        num_contribution = list(review_data['contribution_num'].values)
        score_contribution = 0
        if sum(num_contribution) > 0:
            score_ave = list(review_data['contribution_average'].values)
            score_contribution = sum([num_contribution[i] * score_ave[i] for i in range(len(num_contribution))]) / sum(num_contribution)
            # score_contribution = max(score_ave)
        score_contribution = 1 if score_contribution >= 0.5 else 0

        num_originality = list(review_data['originality_num'].values)
        score_originality = 0
        if sum(num_originality) > 0:
            score_ave = list(review_data['originality_average'].values)
            score_originality = sum([num_originality[i] * score_ave[i] for i in range(len(num_originality))]) / sum(num_originality)
            # score_originality = max(score_ave)
        score_originality = 1 if score_originality >= 0.5 else 0

        num_evidence = list(review_data['evidence_num'].values)
        score_evidence = 0
        if sum(num_evidence) > 0:
            score_ave = list(review_data['evidence_average'].values)
            score_evidence = sum([num_evidence[i] * score_ave[i] for i in range(len(num_evidence))]) / sum(num_evidence)
            # score_evidence = max(score_ave)
        score_evidence = 1 if score_evidence >= 0.5 else 0

        if sum(num_clarity) > 0 and sum(num_contribution) > 0 and sum(num_clarity) > 0 and sum(num_evidence) > 0:
            num += 1
            type_item = result_class[ids.index(paper_id)]
            type_dict[type_item].append((score_clarity, score_contribution, score_originality, score_evidence))

print(num)

for type_item, score_list in type_dict.items():
    print(type_item)

    count_list = [0] * 16
    for score in score_list:
        count_list[score[0] * 8 + score[1] * 4 + score[2] * 2 + score[3] * 1] += 1

    print(count_list[0])
    print(count_list[1])
    print(count_list[2])
    print(count_list[4])
    print(count_list[8])
    print(count_list[3])
    print(count_list[5])
    print(count_list[9])
    print(count_list[6])
    print(count_list[10])
    print(count_list[12])
    print(count_list[7])
    print(count_list[13])
    print(count_list[11])
    print(count_list[14])
    print(count_list[15])




