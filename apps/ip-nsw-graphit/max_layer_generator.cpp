// exponential_distribution
#include <iostream>
#include <random>
#include <math.h>

int get_max_layer(double normFactor)
{
	std::default_random_engine generator;
	std::exponential_distribution<double> distribution(3.5);

	double number = distribution(generator);
	int maxLayer = floor(-log(number) * normFactor);
	return maxLayer;
}