data <- read.csv('/Users/tianxuetao/Desktop/我的/B博士后/研究方向/学术论文的创造性评价/dataset情感标注/维度情感分数17-23/RCode/mediation-2.csv')

# library(dplyr)
# data <- sample_n(data, 250)

library(lavaan)

model.0 <- lm(score_total ~ motivation, data)
summary(model.0)

model.1 <- lm(score_total ~ originality, data)
summary(model.1)

model.2 <- lm(originality ~ motivation, data)
summary(model.2)

model.3 <- lm(score_total ~ motivation + originality, data)
summary(model.3)

model.4 <- lm(motivation ~ score_total + originality, data)
summary(model.4)

library(mediation)
results <- mediate(model.2, model.3, treat='motivation', mediator='originality', boot=TRUE, sims=1000)
summary(results)

