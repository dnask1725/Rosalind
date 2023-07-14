#To solve this problem using Mendel's First Law, we need to calculate the probability of producing an individual with a dominant allele (dominant phenotype) when two organisms are randomly selected for mating.
#According to Mendel's First Law, the dominant allele will be expressed in the phenotype if at least one of the alleles is dominant. The probability of an individual possessing a dominant allele can be calculated by considering all possible combinations of alleles from the selected organisms.

#Link:https://rosalind.info/problems/iprb/

#Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: 
#k individuals are homozygous dominant for a factor, 
#m are heterozygous, and 
#n are homozygous recessive.

#Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

def calc_prob_dominant(k, m, n):
    total = k + m + n
    
    # Calculate the probability of each genotype
    # AA + AA -> 1.0 (always dominant)
    prob_AA_AA = (k / total) * ((k - 1) / (total - 1))
    
    # AA + Aa -> 1.0 (always dominant)
    prob_AA_Aa = (k / total) * (m / (total - 1))
    
    # AA + aa -> 1.0 (always dominant)
    prob_AA_aa = (k / total) * (n / (total - 1))
    
    # Aa + AA -> 1.0 (always dominant)
    prob_Aa_AA = (m / total) * (k / (total - 1))
    
    # Aa + Aa -> 0.75 dominant, 0.25 recessive
    prob_Aa_Aa = (m / total) * ((m - 1) / (total - 1)) * 0.75
    
    # Aa + aa -> 0.5 dominant, 0.5 recessive
    prob_Aa_aa = (m / total) * (n / (total - 1)) * 0.5
    
    # aa + AA -> 1.0 (always dominant)
    prob_aa_AA = (n / total) * (k / (total - 1))
    
    # aa + Aa -> 0.5 dominant, 0.5 recessive
    prob_aa_Aa = (n / total) * (m / (total - 1)) * 0.5
    
    # aa + aa -> 0 (always recessive)
    prob_aa_aa = (n / total) * ((n - 1) / (total - 1)) * 0
    
    # Sum up all the probabilities
    prob_dominant = (
        prob_AA_AA +
        prob_AA_Aa +
        prob_AA_aa +
        prob_Aa_AA +
        prob_Aa_Aa +
        prob_Aa_aa +
        prob_aa_AA +
        prob_aa_Aa +
        prob_aa_aa
    )
    
    return prob_dominant

# Example usage
k = 18  # Number of homozygous dominant individuals
m = 30 # Number of heterozygous individuals
n = 17  # Number of homozygous recessive individuals

probability = calc_prob_dominant(k, m, n)
print("Probability of producing an individual with a dominant allele:", probability)
