#To solve this problem using Mendel's First Law, we need to calculate the probability of producing an individual with a dominant allele (dominant phenotype) when two organisms are randomly selected for mating.
#According to Mendel's First Law, the dominant allele will be expressed in the phenotype if at least one of the alleles is dominant. The probability of an individual possessing a dominant allele can be calculated by considering all possible combinations of alleles from the selected organisms.

#Link:https://rosalind.info/problems/iprb/

#Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: 
#k individuals are homozygous dominant for a factor, 
#m are heterozygous, and 
#n are homozygous recessive.

#Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

def mendel_first_law(k,m,n):
    total = k + m + n                         #total
    
    prob_k = k / total
    prob_m = m / total
    prob_n = n / total

#Probability of different mating combinations:
#Case-1: Both Homozygous Dominant (k * k)
    prob_dominant = k * (k-1/total-1)

#Case-2: One Homozygous Dominant and other heterozygous (k * m)
    prob_dominant += k * (m-1/total-1)
    prob_dominant += m * (k-1/total-1)

#Case-3: One Homozygous recessive and other heterozygous (n * m)
    prob_dominant += prob_m * (n / (total - 1)) * 0.5  # One dominant allele (0.5 probability)
    prob_dominant += prob_n * (m / (total - 1)) * 0.5  # One dominant allele (0.5 probability)

#Case 4: Both organisms are heterozygous (m x m)
    prob_dominant += prob_m * ((m - 1) / (total - 1)) * 0.75  # Both dominant alleles (0.75 probability - refer to the 3:1 dominant:recessive ratio)

#Case 5: One organism is homozygous dominant and the other is homozygous recessive (k x n)
    prob_dominant += prob_k * (n / (total - 1))
    prob_dominant += prob_n * (k / (total - 1))

    return prob_dominant

#Sample dataset :
k=15
m=28 
n=17

probability = mendel_first_law(k, m, n)
print(probability)
