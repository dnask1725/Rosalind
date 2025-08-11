
# Scenario:
# We have a list of gene expression values from an RNA-seq experiment.
# These genes were originally ordered by reference, say genome order or pathway membership.

# Now, we want to:
# Sort genes by their expression levels and compute how many swaps are needed to achieve the sorted order.

# This tells :
# How different the current expression pattern is from the reference gene order
# Whether a particular biological condition induces rank instability
# Low swap count: Gene order is nearly preserved, expression is stable
# High swap count: Significant rank perturbation, may reflect condition-specific regulation



# Expression values in a known gene order
expr <- c(TP53 = 6, BRCA1 = 10, MYC = 4, EGFR = 5, KRAS = 1, PTEN = 2)

count_expr_swaps  <- function(expr){
  values<- as.numeric(expr)
  names_vec<-names(expr)
  
  swaps<-0
  
  for(i in 2:length(values)) {
    j <- i 
    while(j > 1 && values[j]< values[j-1]) {
      tmp_val <- values[j]
      values[j]<- values[j-1]
      values[j-1]<- tmp_val
      
      tmp_names <- names_vec[j]
      names_vec[j]<- names_vec[j-1]
      names_vec[j-1]<- tmp_names
      
      swaps <- swaps +1
      j<- j-1
    }
  }
  
  cat("Sorted genes by expression : ", paste(names_vec, collapse = ","),"\n")
  return(swaps)
}

count_expr_swaps (expr)
