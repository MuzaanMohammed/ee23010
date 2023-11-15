import numpy as np
import matplotlib.pyplot as plt

# Given mean
mean = float(input("Enter a mean value : "))

# Number of trials for binomial distribution
trials = 100

# Generate a range of probabilities (p)
probabilities = np.linspace(0.01, 0.99, 100)

# Calculate variances for each probability using binomial random variable
variances = []

for p in probabilities:
    # Generate binomial random variable
    binomial_rv = np.random.binomial(mean/p, p, size=1000)
    
    # Calculate variance
    variance = np.var(binomial_rv)
    
    # Append to the list
    variances.append(variance)

# Find minimum and maximum of the variance array
min_variance = np.min(variances)
max_variance = np.max(variances)


# Get input variance from the user
user_input = float(input("Enter a variance value to check: "))

# Check if the input variance is within the range
if min_variance <= user_input < max_variance:
    print("valid")
else:
    print("invalid")

# Plotting the variance as a function of probability
plt.plot(probabilities, variances)
plt.xlabel('Probability (p)')
plt.ylabel('Variance')
plt.title('Variance vs Probability for Binomial Distribution')
plt.show()
