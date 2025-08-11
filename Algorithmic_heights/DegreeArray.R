
# A simple undirected graph with n nodes and m edges. Each line of input defines an edge between two vertices


# Return: a vector D[1..n] where D[i] is the degree of node i, i.e., how many edges are connected to it

# Bioinformatics view : Protein - protein network
# - A list of PPIs in a cell with interaction
# - FOr each protein we can calc how many other prots it interact with i.e the degree

# USES:
# 1. Identify hub proteins - one with higher degree (many interactions)
# 2. Cluster proteins based on degree


ppi_edges <- data.frame(
  p1 = c("P53", "TP53", "ATM", "MDM2", "P53", "INS", "FGL2", "CHEK2", "BRCA1", "BRCA1", "RB1"),
  p2 = c("MDM2", "ATM", "CHEK2", "BRCA1", "RB1", "BRCA1","INS", "FGL2", "ATM", "ATM","MDM2" )
)

prots <- unique(c(ppi_edges$p1, ppi_edges$p2))

degree <- setNames(rep(0, length(prots)), prots)

for (i in 1:nrow(ppi_edges)) {
  u<-ppi_edges[i,1]
  v<-ppi_edges[i,2]
  degree[u] <- degree[u]+1
  degree[v] <- degree[v]+1
}

print(degree)
