library(ltm)

data <- read.csv('/Users/tianxuetao/Desktop/我的/B博士后/研究方向/学术论文的创造性评价/调查/400数据/data.csv')

data_s <- data[, c('Q3', 'Q6', 'Q9')]

cronbach.alpha(data_s, CI=TRUE)
