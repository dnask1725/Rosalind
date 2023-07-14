#The need for Averages
# Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

# AA-AA
# AA-Aa
# AA-aa
# Aa-Aa
# Aa-aa
# aa-aa
# Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.


#SOLUTION
# to know the expected number of offspring displaying the dominant phenotype in the next generation, we need to consider the probabilities of each genotype pairing producing offspring with the dominant phenotype.
#the following genotypes are given:
# AA-AA
# AA-Aa
# AA-aa
# Aa-Aa
# Aa-aa
# aa-aa
#Let's consider:

x1 = 1  # Number of AA-AA couples
x2 = 2  # Number of AA-Aa couples
x3 = 3  # Number of AA-aa couples
x4 = 4  # Number of Aa-Aa couples
x5 = 5  # Number of Aa-aa couples
x6 = 6   # Number of aa-aa couples


#The probabilities for each genotype pairing to produce an offspring with a dominant phenotype are as follows:

# AA-AA: All offspring - dominant phenotype (probability = 1).
# AA-Aa: All offspring - dominant phenotype (probability = 1).
# AA-aa: All offspring - dominant phenotype (probability = 1).
# Aa-Aa: 75% of offspring - dominant phenotype (probability = 0.75).
# Aa-aa: 50% of offspring - dominant phenotype (probability = 0.5).
# aa-aa: 0% of offspring - dominant phenotype (probability = 0).



def calculate_expected_offspring(x1, x2, x3, x4, x5, x6):
    expected_offspring = (
        x1 * 2 * 1 +
        x2 * 2 * 1 +
        x3 * 2 * 1 +
        x4 * 2 * 0.75 +
        x5 * 2 * 0.5 +
        x6 * 2 * 0
    )
    # We multiply the probability by the number of couples and then multiply by 2 because each couple has exactly two offspring.
    return expected_offspring


expected_offspring = calculate_expected_offspring(x1, x2, x3, x4, x5, x6)
print("Expected offspring with dominant phenotype:", expected_offspring)

