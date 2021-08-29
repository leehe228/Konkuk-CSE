#include <iostream>
#include <cstdio>

using namespace std;

/* 202011353 이호은    */
/* Array S, I, D      */
/* Packed Sorted      */

int globalLeft, globalRight;

int Search(int* arr, int n, int x) {
	int l, r, m;
	l = 0; r = n - 1;

	while (l <= r) {
		m = (l + r) / 2;
		if (*(arr + m) == x) return m;
		else if (*(arr + m) < x) l = m + 1;
		else r = m - 1;
	}

	globalLeft = r;
	globalRight = l;
	return -1;
}

int Insert(int* arr, int n, int x) {
	int i;

	if (Search(arr, n, x) == -1) {
		for (i = n - 1; i >= globalRight; i--) {
			*(arr + i + 1) = *(arr + i);
		}
		*(arr + globalRight) = x;
		return 0;
	}

	return -1;
}

int Delete(int* arr, int n, int x) {
	int i, j;

	i = Search(arr, n, x);
	if (i == -1) return -1;
	else {
		for (j = i; j < n - 1; j++) {
			*(arr + j) = *(arr + j + 1);
		}
		return 0;
	}
}

int main(int argc, char* argv[]) {
	
	cout << "202011353 이호은\nPacked, Sorted\n" << endl;

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

			if (in == -1) cout << "Not Found! l : " << globalLeft << ", r : " << globalRight << endl;
			else cout << "Found at index " << in << endl;
		}

		// insert
		else if (com == 'i') {
			int x;
			cin >> x;
			if (Insert(arr, n, x) == 0) n++;
		}

		// delete
		else if (com == 'd') {
			int x;
			cin >> x;
			if (Delete(arr, n, x) == 0) n--;
		}
	}

	delete[] arr;
	arr = nullptr;

	return 0;

}