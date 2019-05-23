// random level generator
#include <iostream>
#include <random>
#include <stdlib.h>

int get_rand_level(double revSize)
{
	std::uniform_real_distribution<double> distribution(0.0, 1.0);
	double r = -log(distribution(generator)) * revSize;
	return (int)r;
}
