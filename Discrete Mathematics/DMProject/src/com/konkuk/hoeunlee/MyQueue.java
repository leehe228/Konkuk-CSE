package com.konkuk.hoeunlee;

import java.util.ArrayList;

/**
 * 이산수학(0037) 학기말 과제
 * 컴퓨터공학부 202011353 이호은
 * MyQueue.java (Queue 클래스)
 **/

public class MyQueue {

    /* FIELD */
    // 값 저장 ArrayList
    ArrayList<Node> Q;

    /* 생성자 */
    public MyQueue() {
        Q = new ArrayList<>();
    }

    /* QUEUE METHOD */
    // enqueue
    public void enqueue(Node node) {
        Q.add(node);
    }

    // dequeue
    public Node dequeue() {
        Node temp = Q.get(0);
        Q.remove(0);
        return temp;
    }

    // return SIZE
    public int size() {
        return Q.size();
    }

    @Override
    public String toString() {
        return String.valueOf(Q);
    }
}
