package com.konkuk.hoeunlee;

import java.util.ArrayList;
import java.util.List;

/**
 * 이산수학(0037) 학기말 과제
 * 컴퓨터공학부 202011353 이호은
 * Node.java (노드 클래스)
 **/

public class Node {

    /* FIELD */
    // 노드 이름
    public final int name;

    // 인접 노드 리스트
    public List<Node> nodes;

    /* 생성자 */
    public Node(int name) {
        this.name = name;
        this.nodes = new ArrayList<>();
    }

    /* 인접 노드 리스트 추가 */
    public void addNearNode(List<Node> nodes) {
        this.nodes = nodes;
    }

    /* 기타 METHOD */
    // 확인용 출력 메소드
    /* public void PRINT() {
        System.out.print(this.name + " : ");

        // 인접 노드가 없다면
        if (nodes == null) {
            System.out.print("No Node");
        } else {
            for (Node node : nodes) {
                System.out.print(node.name + " ");
            }
        }
        System.out.print(" |  ");
    } */

    @Override
    public String toString() {
        return String.valueOf(this.name);
    }

}
