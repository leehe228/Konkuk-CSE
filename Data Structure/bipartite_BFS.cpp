#include <iostream>
#include <iomanip>
#include <climits>
#include <cstdio>

using namespace std;

template <typename T>
void swap(T &a, T &b) {
	T temp = a;
	a = b;
	b = temp;
}

class PriorityQueue {
public:
	PriorityQueue();
	void Insert(pair<int, int> x);
	pair<int, int> Delete();
	int IsEmpty();
	void Print(int C, int depth, int LR);
	int size;
	pair<int, int> arr[1000];
};

PriorityQueue::PriorityQueue()
	:size(0) {
}

int PriorityQueue::IsEmpty() {

	return size == 0;
}

void PriorityQueue::Insert(pair<int, int> x) {

	int i, j;
	size++;
	arr[size] = x;
	i = size;
	while (i > 1) {
		j = i / 2;
		// 부모가 더 큰 경우
		if (arr[j] > arr[i]) {
			swap(arr[i], arr[j]);
			i = j;
		}
		else {
			break;
		}
	}
}

pair<int, int> PriorityQueue::Delete() {

	int i, j, k, l;
	pair<int, int> returnValue;
	returnValue = arr[1];
	arr[1] = arr[size];
	size--;
	i = 1;
	while (true) {
		j = i * 2; k = i * 2 + 1;

		if (j > size) break;
		if (k > size) {
			if (arr[i] > arr[j]) {
				swap(arr[i], arr[j]);
				i = j; // 자식으로 이동 (종료)
			}
			else {
				break;
			}
		}
		else {
			if (arr[i] > arr[j] || arr[i] > arr[k]) {
				if (arr[j] < arr[k]) {
					l = j;
				}
				else {
					l = k;
				}
				// l 은 둘 중에 작은 것
				swap(arr[i], arr[l]);
				i = l;
			}
			else {
				break;
			}
		}
	}
	return returnValue;
}

void PriorityQueue::Print(int C, int depth, int LR) {

	if (size == 0) {
		cout << "---" << endl;
		return;
	}
	if (depth == 0) {
		C = 1;
	}
	if (LR == 1) {
		int i;
		for (i = 0; i < depth; i++) cout << setw(11) << " ";
	}
	
	cout << "---" << setw(3) << arr[C].first << ", " << setw(3) << arr[C].second;

	// Left Child가 있으면
	if (C * 2 <= size) {
		Print(C * 2, depth + 1, 0);
	}
	else cout << endl;

	// Right Child가 있으면
	if (C * 2 + 1 <= size) {
		Print(C * 2 + 1, depth + 1, 1);
	}

	return;
}

// 링크
pair<int, int> Link[100][100];
// 링크 개수
int S[100];
int D[100];
int R[100];

int main(int argc, char* argv[]) {

	char c;
	int i, n, m;
	int p, q, r;
	pair<int, int> t, packet;
	PriorityQueue pq;

	cin >> n >> m;
	for (i = 1; i < n; i++) 
		S[i] = 0; // 링크 없음

	for (i = 1; i <= m; i++) {
		cin >> p >> q; // r을 읽지 않고 1로 설정 (모든 weight를 1로 설정) -> BFS가 된다
		S[p]++; 
		Link[p][S[p]].first = q;
		Link[p][S[p]].second = 1; // weight를 전부 1로
	}

	for (i = 1; i <= n; i++) {
		D[i] = INT_MAX;
		R[i] = 0;
	}
	packet.first = 0; packet.second = 1;
	pq.Insert(packet);

	while (pq.IsEmpty() == 0) {

		for (i = 1; i <= n; i++) {
			if (D[i] == INT_MAX) cout << "-INF- ";
			else cout << setw(5) << D[i] << " ";
		}
		cout << endl;
		pq.Print(1, 0, 0);
		cout << endl;
		int _ = scanf("%c", &c);

		t = pq.Delete();
		r = t.first; q = t.second; // packet에 너의 색은 무엇이다 설정

		if (R[q] == 1) continue;
		else {
			R[q] = 1; // red로
			D[q] = r; // 거리 Distance r로
            // packet 중에 다른 색을 설정 -> 다른 색이면 끝
			

			// q에서 나가는 링크
			for (i = 1; i <= S[q]; i++) {
				packet.first = D[q] + Link[q][i].second; // weight
				packet.second = Link[q][i].first; // 노드 번호
				pq.Insert(packet);
			}
		}
	}
	
	return 0;
}