#include <iostream>
#include <cmath>
#include <climits>
#include <iomanip>

using namespace std;

class Node {
public:
    int data; // 데이터
    int leftLabel, rightLabel; // 레이블
    Node* left, * right; // 링크
};

class AVL {
public:
    AVL();
    int Search(int x);
    int Insert(int x);
    int recInsert(int x, Node* D, Node** returnPointer); // 재귀 insert
    int Print(Node* C, int depth, int LR);
    Node* ROOT;
};

AVL::AVL() 
    :ROOT(nullptr) {
}

// D은 지금 보는 노드
int AVL::Search(int x) {

    Node* D;
    D = ROOT;

    while (D != nullptr) {
        // 찾음
        if (D->data == x) {
            return 1;
        }
        // x가 큰 경우 오른쪽으로
        else if (D->data < x) {
            D = D->right;
        }
        // x가 작은 경우 왼쪽으로
        else {
            D = D->left;
        }
    }
    return 0;
}

int AVL::recInsert(int x, Node* D, Node** returnPointer) {

    Node* newNode, * fromChild; 
    int returnValue;

    if (D->data < x) {
        if (D->right == nullptr) {
            newNode = new Node;
            newNode->data = x;
            newNode->leftLabel = 0; newNode->rightLabel = 0;
            newNode->left = nullptr; newNode->right = nullptr;

            D->right = newNode; D->rightLabel = 1; 
        }
        else {
            returnValue = recInsert(x, D->right, &fromChild);
            D->right = fromChild;
            D->rightLabel = returnValue + 1;
        }
    }
    else {
        if (D->left == nullptr) {
            newNode = new Node;
            newNode->data = x;
            newNode->leftLabel = 0; newNode->rightLabel = 0;
            newNode->left = nullptr; newNode->right = nullptr;

            D->left = newNode; D->leftLabel = 1;
        }
        else {
            returnValue = recInsert(x, D->left, &fromChild);
            D->left = fromChild;
            D->leftLabel = returnValue + 1;
        }
    }

    // 회전
    if (abs(D->leftLabel - D->rightLabel) > 1) {
        Node* leftChild, * rightChild;
        Node* temp1, * temp2, * temp3, * temp4;

        leftChild = D->left; rightChild = D->right;

        // case LL
        if (x < D->data && x < leftChild->data) {
            temp1 = leftChild->left;
            temp2 = leftChild->right;
            leftChild->right = D;
            D->left = temp2;
            *returnPointer = leftChild;

            // 레이블 계산
            if (temp2 == nullptr) D->leftLabel = 0;
            else D->leftLabel = max(temp2->leftLabel, temp2->rightLabel) + 1;
            leftChild->rightLabel = max(D->leftLabel, D->rightLabel) + 1;

            return max(leftChild->leftLabel, leftChild->rightLabel);
        }

        // case LR
        else if (x < D->data && x > leftChild->data) {
            temp1 = leftChild->right;
            temp2 = temp1->left; temp3 = temp1->right;
            temp1->left = leftChild;
            temp1->right = D;

            leftChild->right = temp2;
            D->left = temp3;
            *returnPointer = temp1;

            // 레이블 계산
            if (temp2 == nullptr) leftChild->rightLabel = 0;
            else leftChild->rightLabel = max(temp2->leftLabel, temp2->rightLabel) + 1;

            if (temp3 == nullptr) D->leftLabel = 0;
            else D->leftLabel = max(temp3->leftLabel, temp3->rightLabel) + 1;

            temp1->leftLabel = max(leftChild-> leftLabel, leftChild->rightLabel) + 1;
            temp1->rightLabel = max(D->leftLabel, D->rightLabel) + 1;

            return max(temp1->leftLabel, temp1->rightLabel);

        }

        // case RL
        else if (x > D->data && x < rightChild->data) {
            temp1 = rightChild->left;
            temp2 = temp1->left; temp3 = temp1->right;
            temp1->left = D;
            temp1->right = rightChild;

            D->right = temp2;
            rightChild->left = temp3;
            *returnPointer = temp1;

            // 레이블 계산
            if (temp2 == nullptr) D->rightLabel = 0;
            else D->rightLabel = max(temp2->leftLabel, temp2->rightLabel) + 1;

            if (temp3 == nullptr) rightChild->leftLabel = 0;
            else rightChild->leftLabel = max(temp3->leftLabel, temp3->rightLabel) + 1;

            temp1->leftLabel = max(D->leftLabel, D->rightLabel) + 1;
            temp1->rightLabel = max(rightChild->leftLabel, rightChild->rightLabel) + 1;

            return max(temp1->leftLabel, temp1->rightLabel);
        }

        // case RR
        else if (x > D->data && x > rightChild->data) {
            temp1 = rightChild->right;
            temp2 = rightChild->left;
            rightChild->left = D;
            D->right = temp2;
            *returnPointer = rightChild;

            // 레이블 계산
            if (temp2 == nullptr) D->rightLabel = 0;
            else D->rightLabel = max(temp2->leftLabel, temp2->rightLabel) + 1;
            rightChild->leftLabel = max(D->leftLabel, D->rightLabel) + 1;

            return max(rightChild->leftLabel, rightChild->rightLabel);
        }
    }

    // 변경이 없는 경우
    else {
        *returnPointer = D;
    }

    return max(D->leftLabel, D->rightLabel);
}

int AVL::Insert(int x) {

    Node* D, * RR;
    D = ROOT;

    // 루트가 없는 경우
    if (D == nullptr) {
        D = new Node;
        D->data = x;
        D->leftLabel = 0; D->rightLabel = 0;
        D->left = nullptr; D->right = nullptr;
        ROOT = D;

        return 1;
    }
    
    // 이미 있는 경우
    if (Search(x) == 1) return 0;
   
    // 루트 있는 경우 재귀 insert
    recInsert(x, D, &RR); // D 노드 레이블 중 큰 값 반환
    ROOT = RR;
    return 1;
}


// C 는 current
// Left는 LR 0 / Right는 LR 1
int AVL::Print(Node* C, int depth, int LR) {

    if (depth == 0) {
        C = ROOT;
        if (C == nullptr) {
            cout << "───\n\n";
            return 0;
        }
    }
    if (LR == 1) {
        int i;
        for (i = 0; i < depth; i++) cout << setw(14) << " ";
    }
    
    cout << "───(" << C->leftLabel << ")[" << setw(3) << C->data << "](" << C->rightLabel << ")";

    if (C->left != nullptr) {
        Print(C->left, depth + 1, 0);
    }
    else cout << endl;

    if (C->right != nullptr) {
        Print(C->right, depth + 1, 1);
    }

    return 0;
}

int main(int argc, char* argv[]) {

    char com;
    int x, in;
    AVL avlTree;

    while (true) {
        avlTree.Print(nullptr, 0, 0);
        cout << "com : ";
        cin >> com;

        if (com == 'q') break;

        else if (com == 's') {
            cin >> x;
            in = avlTree.Search(x);
            if (in == 0) cout << "Not Found" << endl;
            else cout << "Found" << endl;
        }

        else if (com == 'i') {
            cin >> x;
            if (avlTree.Insert(x) == 1) cout << "Inserted" << endl;
            else cout << "Fail to Insert" << endl;
        }

        else cout << "???" << endl;
    } // 27:16
    return 0;
}