#include <iostream>
#include <iomanip>
#include <climits>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int N, M;
int A[1000];

class Edge {
public:
	int a, b, w;
	bool operator< (const Edge& e) const {
		return w < e.w;
	}
};

Edge E[1000];
int USE[1000]; // 0이면 안씀 1이면 씀

int Find(int p) {

	int Root, temp, Root2;
	Root = p;

	while (A[Root] != 0) {
		// parent로
		Root = A[Root];
	}

	// path compression
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

vector<pair<int, int>> Ad[1000];

// nd 내 노드 번호, parent 부모 번호
void Print(int node, int depth, int weight, int parent, int LR) {

	int j, count;
	if (LR > 0) {
		for (int i = 0; i < depth - 1; i++) cout << setw(12) << " ";
		cout << setw(6) << " ";
	}

	if (depth == 0) {
		cout << "--[" << setw(2) << node << "]";
	}
	else cout << "--(" << setw(2) << weight << ")--[" << setw(2) << node << "]";

	count = 0;
	for (j = 0; j < Ad[node].size(); j++) {
		if (Ad[node][j].first != parent) {
			Print(Ad[node][j].first, depth + 1, Ad[node][j].second, node, count);
			count++;
		}
	}
	if (count == 0) cout << endl;

	return;
}


int main(int argc, char* argv[]) {

	int pRoot, qRoot;

	cin >> N >> M;

	for (int i = 1; i <= M; i++) {
		cin >> E[i].a >> E[i].b >> E[i].w;
	}

	sort(E + 1, E + M + 1);

	// for (int i = 1; i <= M; i++) cout << E[i].a << ", " << E[i].b << ", " << E[i].w << endl;

	int count = 0; int currentIdx = 1; // i는 보는 edge
	while (count < N - 1) {
		if (currentIdx > M) {
			cout << "Not Connected" << endl;
			exit(0); // 모든 edge를 다 본 경우 (full connected가 아님)
		}

		pRoot = Find(E[currentIdx].a);
		qRoot = Find(E[currentIdx].b);

		// 이미 같은 그룹
		if (pRoot == qRoot) {
			;
		}
		else {
			count++;
			USE[currentIdx] = 1;
			Union(E[currentIdx].a, E[currentIdx].b);
		}
		currentIdx++;
	}

	cout << "Result : " << endl;
	for (int i = 1; i <= M; i++) {
		if (USE[i] == 1) {
			cout << E[i].a << ", " << E[i].b << ", " << E[i].w << endl;
		}
	}

	cout << "Tree : " << endl;
	for (int i = 1; i <= M; i++) {
		if (USE[i]) {
			Ad[E[i].a].push_back(make_pair(E[i].b, E[i].w));
			Ad[E[i].b].push_back(make_pair(E[i].a, E[i].w));
		}
	}

	Print(1, 0, 0, 0, 0);

	return 0;
}