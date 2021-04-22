#include <iostream>
#include <cstdio>

using namespace std;

/* 202011353 이호은    */
/* Array S, I, D      */
/* Packed Unsorted    */

int Search(int* arr, int n, int x) {
	int i;

	for (i = 0; i < n; i++) {
		if (*(arr + i) == x) break;
	}

	if (i < n) return i;
	else return -1;
}

int Delete(int* arr, int n, int x) {
	int i = Search(arr, n, x);
	
	if (i == -1) return -1;
	else {
		arr[i] = arr[n - 1];
		return i;
	}
}

int main(int argc, char* argv[]) {
	
	cout << "202011353 이호은\nPacked, Unsorted\n" << endl;

	const int S = 100;
	int* arr = new int[S];
	int n = 0;

	// 초기화
	for (int i = 0; i < S; i++) *(arr + i) = -1;

	while (true) {

		// 출력
		for (int i = 0; i <= n; i++) printf("|%4d", i);
		cout << "|" << endl;
		for (int i = 0; i <= n; i++) printf("|%4d", *(arr + i));
		cout << "|" << endl;

		char com;
		cin >> com;

		if (com == 'q') break;

		// search
		else if (com == 's') {
			int x, in;
			cin >> x;
			in = Search(arr, n, x);

			if (in == -1) cout << "Not Found!" << endl;
			else cout << "Found at index " << in << endl;
		}

		// insert
		else if (com == 'i') {
			 cin >> arr[n++];
		}

		// delete
		else if (com == 'd') {
			int x, in;
			cin >> x;
			in = Delete(arr, n, x);

			if (in == -1) cout << "Not Found!" << endl;
			else {
				cout << "Deleted at index " << in << endl;
				n--;
			}
		}
	}

	delete[] arr;
	arr = nullptr;

	return 0;

}