#include <iostream>
#include <stack>

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
    static inline int V[1000]; // 0 : unvisited,  1 : colorR,  2 : colorB
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


int main(int argc, char* argv[]) {

    int myColor, nextColor, fail, changeMyColor;

    int n, m;
    cin >> n >> m;

    stack<int> myStack;
    stack<int> colorStack;

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
        if (Lists::V[i] == 0) {
            myColor = 1; fail = 0, changeMyColor = 1;
            cur = i; // 현재 방문 노드가 cur
            Lists::V[cur] = myColor; // 방문 체크
            cout << cur << '\t';
            while (true) {
                if (changeMyColor == 1) {
                    changeMyColor = 0;
                    Lists::V[cur] = myColor; // 방문 체크

                    if (myColor == 1) nextColor = 2;
                    else nextColor = 1;
                }

                if ((newNode = Lists::LinkedList[cur].Next()) != 0) {
                    // 안가본 곳이면
                    if (Lists::V[newNode] == 0) {
                        // 방문
                        myStack.push(cur);
                        colorStack.push(myColor);
                        cur = newNode;
                        Lists::V[cur] = nextColor; // 방문 체크
                        myColor = nextColor;
                        changeMyColor = 1;
                        cout << cur << " " << nextColor << '\t';
                    }
                    else {
                        if (Lists::V[newNode] != nextColor) fail = 1;
                    }
                }

                else {
                    if (myStack.empty()) break;
                    else {
                        cur = myStack.top();
                        myColor = colorStack.top();
                        colorStack.pop();
                        myStack.pop();
                        changeMyColor = 1;
                        cout << "*** " << cur << endl;
                    }
                }
            }
            cout << endl;
        }
    }
    if (fail == 1) cout << "FAIL" << endl;
    else cout << "SUCCESS" << endl;

    return 0;
}