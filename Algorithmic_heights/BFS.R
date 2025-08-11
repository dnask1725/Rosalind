# BREADTH FIRST SEARCH ALGORITHM

#  Directed graph problem
#  Reachability in Gene Regulation Networks
 
# Helpful in analysing directed gene regulatory network(GRN) where,
# nodes = genes , edges = transcriptional activity (u → v means gene u regulates gene v)
# We want to see how far(in hops) each gene is from the master regulator 

# This gives insights into :
# 1. Network depth
# 2. Regulatory influence
# 3. Genes that are indirectly regulated vs unreachable




grn_edges <- data.frame(
  regulator = c("TF1", "GeneA", "GeneA", "GeneB", "TF1"),
  target    = c("GeneA", "GeneB", "GeneC", "GeneD", "GeneE"),
  stringsAsFactors = FALSE
)

genes <- sort(unique(c(grn_edges$regulator, grn_edges$target)))
cat("All genes:\n")
print(genes)


gene_to_index <- setNames(seq_along(genes), genes)
index_to_gene <- setNames(genes, as.character(seq_along(genes)))

cat("Gene to index mapping:\n")
print(gene_to_index)
cat("Index to gene mapping:\n")
print(index_to_gene)


n <- length(genes)
graph <- vector("list", n)
for (i in 1:n) graph[[i]] <- character(0)


for (i in 1:nrow(grn_edges)) {
  reg <- grn_edges$regulator[i]
  tgt <- grn_edges$target[i]

  if (!(reg %in% names(gene_to_index)) || !(tgt %in% names(gene_to_index))) {
    stop(paste("Gene not found in mapping:", reg, tgt))
  }

  u <- gene_to_index[[reg]]
  v <- gene_to_index[[tgt]]

  if (is.na(u) || is.na(v)) stop("One of the mappings returned NA")
  if (u > n || v > n) stop(paste("Index out of bounds:", u, v))

  graph[[u]] <- c(graph[[u]], v)
}

cat("Graph built successfully:\n")
print(graph)

start_gene <- "TF1"
start_index <- gene_to_index[[start_gene]]

# Initialize distances
dist <- rep(-1, n)  # -1 means unreachable
dist[start_index] <- 0
queue <- c(start_index)

while (length(queue) > 0) {
  current <- queue[1]
  queue <- queue[-1]
  
  # Explore all neighbors
  for (neighbor in graph[[current]]) {
    neighbor <- as.numeric(neighbor)  # make sure it's numeric!
    if (dist[neighbor] == -1) {
      dist[neighbor] <- dist[current] + 1
      queue <- c(queue, neighbor)
    }
  }
}

names(dist) <- genes
cat("\n Shortest regulatory distances from", start_gene, ":\n")
print(dist)
