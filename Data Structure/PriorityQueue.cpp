#include <iostream>
#include <iomanip>

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
	bool IsEmpty();
	void Print(int C, int depth, int LR);
	int size;
	pair<int, int> arr[1000];
};

PriorityQueue::PriorityQueue()
	:size(0) {
}

bool PriorityQueue::IsEmpty() {

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

int main(int argc, char* argv[]) {

	char com;
	PriorityQueue pq;
	pair<int, int> x;

	while (true) {
		pq.Print(1, 0, 0);
		cout << "com : ";
		cin >> com;

		if (com == 'q') break;

		else if (com == 'i') {
			cin >> x.first >> x.second;
			pq.Insert(x);
		}

		else if (com == 'd') {
			x = pq.Delete();
			cout << "(" << x.first << ", " << x.second << ")" << endl;
		}

		else cout << "???" << endl;
	}

	return 0;
}