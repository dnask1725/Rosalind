# Scenario : Sum of Interactor Degrees in a PPI Network

# For each protein, compute how **connected its partners are**, by summing their number of interactions.

# This metric is used to assess:
# - Whether a protein interacts with **hub proteins**
# - How **influential** a protein's **neighborhood** is

# This is known as **2-step connectivity** or **sum of neighbor degrees** in biological networks.

# Sounds confusing but isnt : So if for example we have, 
# Edges:

# 1-2

# 2-3

# 4-3

# 2-4

# Then compute the degrees:
# 1 → [2] → degree = 1

# 2 → [1, 3, 4] → degree = 3

# 3 → [2, 4] → degree = 2

# 4 → [3, 2] → degree = 2

# 5 → [] → degree = 0

# So we'll have:
# Node 1: neighbors = [2]     → D[1] = deg(2) = 3  
# Node 2: neighbors = [1,3,4] → D[2] = deg(1)+deg(3)+deg(4) = 1+2+2 = 5  
# Node 3: neighbors = [2,4]   → D[3] = deg(2)+deg(4) = 3+2 = 5  
# Node 4: neighbors = [3,2]   → D[4] = deg(3)+deg(2) = 2+3 = 5  
# Node 5: neighbors = []      → D[5] = 0




ppi_edges <- data.frame(
  p1 = c("P53", "TP53", "ATM", "MDM2", "P53", "INS", "FGL2", "CHEK2", "BRCA1", "BRCA1", "RB1"),
  p2 = c("MDM2", "ATM", "CHEK2", "BRCA1", "RB1", "BRCA1","INS", "FGL2", "ATM", "ATM","MDM2" )
)

proteins <- unique(c(ppi_edges$p1, ppi_edges$p2))

# Step 1: Create empty neighbor list
neighbors <- setNames(vector("list", length(proteins)), proteins)
for (p in proteins) neighbors[[p]] <- c()

for (i in 1:nrow(ppi_edges)) {
  u <- ppi_edges$p1[i]
  v <- ppi_edges$p2[i]
  neighbors[[u]] <- c(neighbors[[u]], v)
  neighbors[[v]] <- c(neighbors[[v]], u)
}

degrees <- sapply(neighbors, length)
neighbor_sum <- sapply(names(neighbors), function(p) {
  sum(degrees[neighbors[[p]]])
})

# Output
print(neighbor_sum)




















