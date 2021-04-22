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
    void setZero();
    int Next();
    bool isZero;
    Node* head;
    Node* current;
};

class Lists {
public:
    Lists() = default;
    static inline bool V[1000];
    static inline List LinkedList[1000];
};

List::List()
    :head(nullptr), current(head), isZero(false) {
}

int List::Insert(int x) {
    Node* newNode;
    newNode = new Node;
    newNode->data = x;
    newNode->next = head;
    head = newNode;
    return 1;
}

void List::setZero() {
    isZero = true;
}

int List::Next() {
    if (isZero) {
        isZero = false;
        current = head;
    }
    else current = current->next;

    if (current == nullptr) return 0;
    else return current->data;
}

class Stack {
private:
    int data[1000];
    int pointer = 0;
public:
    Stack();
    void Push(int x);
    int Pop();
    bool isEmpty();
};

Stack::Stack()
    :pointer(0) {
    
    for (int i = 0; i < 1000; i++) {
        data[i] = 0;
    }
}

void Stack::Push(int x) {
    data[pointer++] = x;
}

int Stack::Pop() {
    return data[--pointer];
}

bool Stack::isEmpty() {
    return (pointer == 0);
}

int main(int argc, char* argv[]) {
    int n, m;
    cin >> n >> m;

    Stack stack;

    int i, cur, newNode;
    for (i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        Lists::LinkedList[x].Insert(y);
        Lists::LinkedList[y].Insert(x);
    }

    for (i = 1; i <= n; i++) {
        Lists::LinkedList[i].setZero();
    }

    for (i = 1; i <= n; i++) {
        if (!Lists::V[i]) {
            cur = i; // 현재 방문 노드가 cur
            Lists::V[cur] = true; // 방문 체크
            cout << cur << '\t';
            while (true) {
                if ((newNode = Lists::LinkedList[cur].Next()) != 0) {
                    // 안가본 곳이면
                    if (!Lists::V[newNode]) {
                        // 방문
                        stack.Push(cur);
                        cur = newNode;
                        Lists::V[cur] = true;
                        cout << cur << '\t';
                    }
                }
                else {
                    if (stack.isEmpty()) break;
                    else {
                        cur = stack.Pop();
                    }
                }
            }
            cout << endl;
        }
    }

    return 0;
}