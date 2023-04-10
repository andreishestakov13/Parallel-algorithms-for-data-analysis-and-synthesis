#include <iostream>
#include <ctime>
#include <cstdlib>
#include <vector>
#include <random>
#include <chrono>
#include <algorithm>

using namespace std;

vector<vector<int>> generateMatrix(int matrix_size) {
	vector<vector<int>> random_matrix(matrix_size);

	for (int i = 0; i < random_matrix.size(); i++) {
		vector<int> random_vector(matrix_size);
		srand(time(NULL));
		generate(random_vector.begin(), random_vector.end(), rand);

		random_matrix[i] = random_vector;
	}

	return random_matrix;
}

void result(vector<vector<int>> first_matrix, vector<vector<int>> second_matrix) {
	double time_for_one_threat;
	clock_t start, finish;
	for (int number = 1; number <= 10; number++) {
		vector<vector<int>> matrix(first_matrix.size(), vector<int>(first_matrix.size()));
		start = clock();
#pragma omp parallel for num_threads(number)
		for (int i = 0; i < first_matrix.size(); ++i) {
			for (int j = 0; j < first_matrix.size(); ++j) {
				for (int k = 0; k < first_matrix.size(); ++k) {
					matrix[i][j] += first_matrix[i][k] * second_matrix[k][j];
				}
			}
		}
		finish = clock();
		double time = ((double)(finish - start) / CLOCKS_PER_SEC) * 1000;
		printf("The thread number: %d\t", number);
		printf("Elapsed time: %.1f milliseconds\n", time);
	}
}

int main(int argc, char* argv[]) {
	int matrix_size = atoi(argv[1]);
	vector<vector<int>> first_matrix = generateMatrix(matrix_size);
	vector<vector<int>> second_matrix = generateMatrix(matrix_size);
	result(first_matrix, second_matrix);
	return 0;
}