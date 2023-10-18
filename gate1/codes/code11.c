#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

// Function to calculate binomial coefficient (n choose k)
unsigned long long binomialCoefficient(int n, int k) {
    if (k < 0 || k > n) {
        return 0;
    }

    unsigned long long result = 1;
    for (int i = 0; i < k; i++) {
        result *= (n - i);
        result /= (i + 1);
    }

    return result;
}

// Function to calculate probability P(X = k)
double probability(int n, double p, int k) {
    return binomialCoefficient(n, k) * pow(p, k) * pow(1.0 - p, n - k);
}

// Function to generate a random binomial variable and calculate its probability, expectation, and variance
void generateAndCalculateProbabilityExpectationVariance(int n, double p) {
    int count = 0;

    for (int i = 0; i < n; i++) {
        double randomValue = (double)rand() / RAND_MAX; // Generate a random number between 0 and 1
        if (randomValue <= p) {
            count++;
        }
    }

    int randomBinomialVariable = count;
    double expectation = n * p;
    double variance = n * p * (1 - p);
    double probK = probability(n, p, randomBinomialVariable);

    printf("Generated Binomial Random Variable: %d\n", randomBinomialVariable);
    printf("Probability P(X = %d) = %.6f\n", randomBinomialVariable, probK);
    printf("Expectation (Mean) E(X) = %.6f\n", expectation);
    printf("Variance Var(X) = %.6f\n", variance);
}

int main() {
    int n;
    double p;

    // Seed the random number generator
    srand(time(NULL));

    // Input n and p from the user
    printf("Enter the value of n: ");
    scanf("%d", &n);

    printf("Enter the value of p (between 0 and 1): ");
    scanf("%lf", &p);

    if (p < 0 || p > 1) {
        printf("Invalid value of p. It should be between 0 and 1.\n");
        return 1; // Exit with an error code
    }

    generateAndCalculateProbabilityExpectationVariance(n, p);

    return 0;
}
