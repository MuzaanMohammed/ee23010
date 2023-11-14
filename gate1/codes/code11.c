#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

// Function to generate a binomial random variable using uniform distribution
int generateBinomialRandomVariable(int n, double p) {
    int count = 0;

    for (int i = 0; i < n; i++) {
        double u = (double)rand() / RAND_MAX; // Generate a uniform random variable between 0 and 1
        if (u <= p) {
            count++;
        }
    }

    return count;
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

    // Number of simulations
    int numSimulations = 100000; // Adjust the number of simulations as needed

    double sum = 0.0;
    double sumSquares = 0.0;

    for (int i = 0; i < numSimulations; i++) {
        int randomBinomialVariable = generateBinomialRandomVariable(n, p);
        double value = (double)randomBinomialVariable;
        sum += value;
        sumSquares += value * value;
    }

    double simulatedMean = sum / numSimulations;
    double simulatedVariance = sumSquares / numSimulations - simulatedMean * simulatedMean;

    printf("Simulated Mean: %.6f\n", simulatedMean);
    printf("Simulated Variance: %.6f\n", simulatedVariance);
    if (simulatedMean > simulatedVariance) {
            printf("Simulated Mean is always greater than Simulated Variance.\n");
        } else {
            printf("Simulated Mean is NOT always greater than Simulated Variance.\n");
        }
    // Compare with four given options
    for (int n=1; n < 5; n++) {
        double optionMean, optionVariance;
        printf("Enter the mean: ");
        scanf("%lf", &optionMean);

        printf("Enter the variance: ");
        scanf("%lf", &optionVariance);
        // Compare the simulated values with the current option
        if (optionMean>optionVariance) {
            printf("valid binomial distribution");
        } else {
                printf(" invalid binomial distribution");
        }
    }

    return 0;
}
