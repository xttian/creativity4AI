library(pheatmap)

data <- read.csv('/Users/tianxuetao/Desktop/我的/B博士后/研究方向/学术论文的创造性评价/调查/400数据/h_data.csv')
data_3 <- t(data[, c('H3.1', 'H3.2', 'H3.3')])

pheatmap(data_3, cluster_rows = FALSE, border = F, clustering_method = "ward.D", 
         clustering_distance_cols = "manhattan", cellwidth = 2.5, cellheight = 100,
         show_rownames = FALSE, show_colnames = FALSE, 
         color=colorRampPalette(c('#3366CC', 'white', '#CC6633'))(50))

dist_matrix <- dist(data[, c('H3.1', 'H3.2', 'H3.3')], method = "manhattan")
hclust_result <- hclust(dist_matrix, method = "ward.D")

plot(hclust_result, main = "Hierarchical Clustering Dendrogram")

cutree_result <- cutree(hclust_result, k = 6)
print(cutree_result)
table(cutree_result)


#####
a <- c(3.54, 3.80, 3.33)
b <- c(3.63, 3.93, 4.16)
c <- c(3.28, 2.98, 3.79)
d <- c(3.16, 2.93, 2.97)
e <- c(4.05, 2.88, 3.52)
f <- c(3.71, 3.33, 3.56)
g <- c(5.00, 5.00, 5.00)
h <- c(1.50, 1.67, 1.50)
df <- t(data.frame(a, b, c, d, e, f))

pheatmap(df, cluster_rows = FALSE, cluster_cols = FALSE, border = F, legend_breaks = c(1, 2, 3, 4, 5),
         cellwidth = 50, cellheight = 50, show_rownames = FALSE, show_colnames = FALSE, 
         color=colorRampPalette(c('#3366CC4D', 'white', '#CC66334D'))(50))

