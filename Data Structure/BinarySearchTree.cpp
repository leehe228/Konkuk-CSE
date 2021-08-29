#include <iostream>
#include <climits>
#include <iomanip>

using namespace std;

class Node {
public:
    int data;
    Node* Left, * Right;
};

class BST {
public:
    BST();
    int Search(int x, Node** P, Node** L);
    int Insert(int x);
    int Delete(int x);
    int Print(Node* C, int depth, int LR);
    Node* ROOT;
};

BST::BST() {
    ROOT = new Node;
    ROOT->data = INT_MAX;
    ROOT->Left = nullptr;
    ROOT->Right = nullptr;
}

// P는 직전에 본 노드 D은 지금 보는 노드
int BST::Search(int x, Node** P, Node** D) {
    
    *D = ROOT; *P = nullptr;
    
    while (*D != nullptr) {
        // 찾음
        if ((*D)->data == x) {
            return 1;
        }
        // x가 큰 경우 오른쪽으로
        else if ((*D)->data < x) {
            *P = *D;
            *D = (*D)->Right;
        }
        // x가 작은 경우 왼쪽으로
        else {
            *P = *D;
            *D = (*D)->Left;
        }
    }
    return 0;
}

int BST::Insert(int x) {
    
    Node* P, * D, * newNode;

    // search 실패한 경우 P는 parent, D는 null
    if (Search(x, &P, &D) == 0) {
        newNode = new Node;
        newNode->data = x;
        newNode->Left = nullptr; newNode->Right = nullptr;

        // x가 parent보다 크면 오른쪽에 붙여줌
        if (P->data < x) {
            P->Right = newNode;
        }
        // x가 parent보다 작으면 왼쪽에 붙여줌
        else {
            P->Left = newNode;
        }
        return 1;
    }
    else return 0;
}

int BST::Delete(int x) {
    
    Node* P, * D;
    if (Search(x, &P, &D) == 1) {

        // case 1 Child가 없는 경우
        if (D->Left == nullptr && D->Right == nullptr) {

            // D가 Left Child이라면
            if (D == P->Left) P->Left = nullptr;
            // D가 Right Child이라면
            else P->Right = nullptr;

            delete D;
        }

        // case 2 Child가 한쪽만 있는 경우
        else if (D->Left == nullptr && D->Right != nullptr) {

            // D가 Left Child이라면
            if (D == P->Left) P->Left = D->Right;
            // D가 Right Child이라면
            else P->Right = D->Right;

            delete D;
        }

        else if (D->Left != nullptr && D->Right == nullptr) {

            // D가 Left Child이라면
            if (D == P->Left) P->Left = D->Left;
            // D가 Right Child이라면
            else P->Right = D->Left;

            delete D;
        }
         
        // case 3 Child가 두 쪽 모두 있는 경우
        else {
            
            Node* RLL, * RLLparent; // 지울 노드 오른쪽 서브트리에서 가장 왼쪽 (정렬 시 x와 붙어있는 값)
            RLL = D->Right, RLLparent = D;
            while (RLL->Left != nullptr) {
                RLLparent = RLL;
                RLL = RLL->Left;
            }
            D->data = RLL->data; // 값 복사

            // RLL 삭제
            if (RLL->Left == nullptr && RLL->Right == nullptr) {
                if (RLL == RLLparent->Left) RLLparent->Left = nullptr;
                else RLLparent->Right = nullptr;
                delete RLL;
            }
            else if (RLL->Left == nullptr && RLL->Right != nullptr) {
                if (RLL == RLLparent->Left) RLLparent->Left = RLL->Right;
                else RLLparent->Right = RLL->Right;
                delete RLL;
            }

        }

        return 1;
    }
    else return 0;
}

// C 는 current
// Left는 LR 0 / Right는 LR 1
int BST::Print(Node* C, int depth, int LR) {

    if (depth == 0) {
        C = ROOT;
    }
    if (LR == 1) {
        int i;
        for (i = 0; i < depth; i++) cout << setw(6) << " ";
    }
    if (C->data == INT_MAX) cout << "--ROOT";
    else cout << "---" << setw(3) << C->data;

    if (C->Left != nullptr) {
        Print(C->Left, depth + 1, 0);
    }
    else cout << endl;

    if (C->Right != nullptr) {
        Print(C->Right, depth + 1, 1);
    }

    return 0;
}

int main(int argc, char* argv[]) {

    char com;
    int x, in;
    Node* P, * D;
    BST bstree;

    while (true) {
        bstree.Print(nullptr, 0, 0);
        cout << "com : ";
        cin >> com;

        if (com == 'q') break;

        else if (com == 's') {
            cin >> x;
            in = bstree.Search(x, &P, &D);
            if (in == 0) cout << "Not Found" << endl;
            else cout << "Found at address " << D << endl;
        }

        else if (com == 'i') {
            cin >> x;
            if (bstree.Insert(x) == 1) cout << "Inserted" << endl;
            else cout << "Fail to Insert" << endl;
        }

        else if (com == 'd') {
            cin >> x;
            if (bstree.Delete(x) == 1) cout << "Deleted" << endl;
            else cout << "Fail to Delete" << endl;
        }

        else cout << "???" << endl;
    }
    return 0;
}