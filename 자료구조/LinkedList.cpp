#include <iostream>
#include <climits>

using namespace std;

class Node {
public:
    int data;
    Node* next;
};

class List {
public:
    List();
    int Search(int x, Node** P, Node** L);
    int Insert(int x);
    int Delete(int x);
    void Print();
    Node* head;
};

List::List() {
    head = new Node;
    head->data = INT_MIN;
    head->next = new Node;
    head->next->data = INT_MAX;
    head->next->next = nullptr;
}

int List::Search(int x, Node** P, Node** L) {
    *L = head;
    while (*L != nullptr) {
        if ((*L)->data < x) {
            *P = *L;
            *L = (*L)->next;
        }
        else if ((*L)->data == x) {
            return 1;
        }
        else return 0;
    }

    return 0;
}

int List::Insert(int x) {
    Node* P, * L, * newNode;
    if (Search(x, &P, &L) == 0) {
        newNode = new Node;
        newNode->data = x;
        newNode->next = L;
        P->next = newNode;

        return 1;
    }

    return 0;
}

int List::Delete(int x) {
    Node* P, * L;
    if (Search(x, &P, &L) == 1) {
        P->next = L->next;
        return 1;
    }
    return 0;
}

void List::Print() {
    Node* temp;
    temp = this->head;

    while (temp != nullptr) {
        cout << temp->data << " -> ";
        temp = temp->next;
    }
    cout << endl;
}

int main(int argc, char* argv[]) {
    
    char com;
    Node* P, * L;
    int x;
    List LinkedList;

    while (true) {
        LinkedList.Print();
        cout << "enter : ";
        cin >> com;

        if (com == 'q') break;

        else if (com == 's') {
            cin >> x;
            
            if (LinkedList.Search(x, &P, &L) == 0) 
                cout << "Not found" << endl;
            else 
                cout << "Found at " << L << endl;
        }

        else if (com == 'i') {
            cin >> x;

            if (LinkedList.Insert(x) == 1) cout << "Inserted" << endl;
            else cout << "Fail to insert" << endl;
        }

        else if (com == 'd') {
            cin >> x;
            if (LinkedList.Delete(x) == 1) cout << "Deleted" << endl;
            else cout << "Deleted Failed" << endl;
        }

        else cout << "???" << endl;
    }

    return 0;
}