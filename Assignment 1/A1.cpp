#include <iostream>
#include <cstdlib>
#include <omp.h>
#include <ctime>

using namespace std;

int main(int argc, char* argv[]) {
	int size = atoi(argv[1]);
	double* array = new double[size];
	clock_t start, finish;

	for (int i = 0; i < size; i++)
	{
		array[i] = (double)rand() / RAND_MAX;
	}

	for (int number = 1; number <= 10; number++)
	{
		double max_value = array[0];
		start = clock();

		#pragma omp parallel for num_threads(number) reduction(max:max_value)
		for (int index = 0; index < size; index++)
		{
			max_value = max(max_value, array[index]);
		}

		finish = clock();
		double time = ((double)(finish - start) / CLOCKS_PER_SEC) * 1000;
		printf("The thread number: %d\t", number);
		printf("Elapsed time: %.1f milliseconds\n", time);
	};
	return 0;
}