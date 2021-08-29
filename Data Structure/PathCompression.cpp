#include <iostream>
#include <iomanip>
#include <climits>
#include <cstdio>

using namespace std;

int N;
int A[1000];

int Find(int p) {

	int Root, temp, Root2;
	Root = p;

	while (A[Root] != 0) {
		// parent로
		Root = A[Root];
	}

	// fast compresion
	Root2 = Root;
	Root = p;
	while (A[Root] != 0) {
		// 지나가는 노드를 루트로 이동
		temp = Root;
		Root = A[Root];
		A[temp] = Root2;
	}

	return Root;
}

void Union(int p, int q) {

	int pRoot, qRoot;
	pRoot = Find(p); qRoot = Find(q);
	A[qRoot] = pRoot;

	return;
}

int main(int argc, char* argv[]) {

	cout << "size : ";
	cin >> N;

	char com;
	int p, q;

	while (true) {
		for (int i = 1; i <= N; i++) {
			cout << setw(4) << A[i];
		}
		cout << endl;
		cin >> com;

		if (com == 'q') break;
		else if (com == 'u') {
			cin >> p >> q;
			Union(p, q);
		}
		else if (com == 'f') {
			cin >> p;
			q = Find(p);
			cout << "result : " << q << endl;
		}
		else cout << "???" << endl;
	}

	return 0;
}