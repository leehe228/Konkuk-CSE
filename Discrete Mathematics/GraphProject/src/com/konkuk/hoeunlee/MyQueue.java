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
    ArrayList<Integer> data;

    /* 생성자 */
    public MyQueue() {
        data = new ArrayList<>();
    }

    /* QUEUE METHOD */
    // enqueue
    public void enqueue(int i) {
        data.add(i);
    }

    // dequeue
    public int dequeue() {
        int temp = data.get(0);
        data.remove(0);
        return temp;
    }

    // return SIZE
    public int size() {
        return data.size();
    }

    @Override
    public String toString() {
        return String.valueOf(data);
    }
}
