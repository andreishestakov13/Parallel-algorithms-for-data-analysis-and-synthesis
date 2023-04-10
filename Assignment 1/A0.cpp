#include <iostream>
#include <vector>
#include <string>

using namespace std;

int count(string str) {
	int counter = 0, i;
	for (i = 0; i < str.size(); i++) {
		if (str[i] == ' ') {
			continue;
		}
		else if (str[i] == '\\') {
			if (str[i + 1] == 't' || str[i + 1] == 'n') {
				continue;
			}
			else if (str[i + 1] == ' ') {
				counter++;
			}
			else if (str[i + 1] == '\\') {
				if (str[i + 2] == 't' || str[i + 2] == 'n') {
					counter++;
				}
				else {
					continue;
				}
			}
		}
		else if ((str[i] == 'n' || str[i] == 't') && str[i - 1] == '\\') {
			continue;
		}
		else if ((str[i] == 'n' || str[i] == 't') && str[i - 1] != '\\') {
			if (str[i + 1] == '\\') {
				if (str[i + 2] == 't' || str[i + 2] == 'n') {
					counter++;
				}
			}
			else if (str[i + 1] == ' ') {
				counter++;
			}
			else {
				continue;
			}
		}
		else if (str[i] != ' ') {
			if (str[i + 1] == '\\') {
				if (str[i + 2] == 't' || str[i + 2] == 'n') {
					counter++;
				}
			}
			else if (str[i + 1] == ' ') {
				counter++;
			}
			else {
				continue;
			}
		}
	}
	return counter;
}

int result(string str) {
	if (str[str.size() - 1] == ' ') {
		return count(str);
	}
	else if ((str[str.size() - 1] == 'n' || str[str.size() - 1] == 't') && str[str.size() - 2] == '\\') {
		return count(str);
	}
	else {
		return count(str) + 1;
	}
}

int main(int argc, char** argv) {
	if (argc == 1) {
		printf("Enter the string");
	}
	else if (argc == 2) {
		string str(argv[1]);
		printf("Words in input: %d", result(str));
	}

	return 0;
}