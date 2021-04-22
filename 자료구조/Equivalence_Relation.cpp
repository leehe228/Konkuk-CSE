#include <iostream>

using namespace std;

class Node {
public:
    int data;
    Node* next;
};

class List {
public:
    List();
    int Insert(int x);
    void Zero();
    int Next();
    int Z;
    Node* head;
    Node* current;
};

List::List()
    :head(nullptr), current(head) {
}

int List::Insert(int x) {
    Node* newNode;
    newNode = new Node;
    newNode->data = x;
    newNode->next = head;
    head = newNode;
    return 1;
}

void List::Zero() {
    Z = 1;
}

int List::Next() {
    if (Z == 1) {
        Z = 0;
        current = head;
    }
    else current = current->next;

    if (current == nullptr) return 0;
    else return current->data;
}

int V[1000];
List LK[1000];
int Stack[1000];
int StackPointer = 0;

void Push(int x) {
    Stack[StackPointer] = x;
    StackPointer++;
}

int Pop() {
    StackPointer--;
    return Stack[StackPointer];
}

bool IsEmpty() {
    return StackPointer == 0;
}

int main(int argc, char* argv[]) {
    int n, m;
    cin >> n >> m;

    Node* T;

    int i, j, cur, newNode;
    for (i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        LK[x].Insert(y);
        LK[y].Insert(x);
    }

    for (i = 1; i <= n; i++) {
        LK[i].Zero();
    }

    for (i = 1; i <= n; i++) {
        if (V[i] == 0) {
            cur = i; // 현재 방문 노드가 cur
            V[cur] = 1; // 방문 체크
            cout << cur << '\t';
            while (true) {
                if ((newNode = LK[cur].Next()) != 0) {
                    // 안가본 곳이면
                    if (V[newNode] == 0) {
                        // 방문
                        Push(cur);
                        cur = newNode;
                        V[cur] = 1;
                        cout << cur << '\t';
                    }
                }
                else {
                    if (IsEmpty()) break;
                    else {
                        cur = Pop();
                    }
                }
            }
            cout << endl;
        }
    }

    /*for (i = 1; i <= n; i++) {
        // 첫 번째 노드 받아옴
        T = LK[i].First();
        while (T != nullptr) {
            cout << T->data << '\t';
            T = LK[i].Next();
        }
        cout << endl;
    }*/

    return 0;
}