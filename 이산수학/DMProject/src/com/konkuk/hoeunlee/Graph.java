package com.konkuk.hoeunlee;

import java.util.*;

/**
 * 이산수학(0037) 학기말 과제
 * 컴퓨터공학부 202011353 이호은
 * Graph.java (그래프 클래스)
 **/

public class Graph {

    /* FIELD */
    // 그래프의 노드 리스트
    private final ArrayList<Node> nodes;

    // 탐색 시 방문 여부 저장 배열
    private Boolean[] visited;
    private MyQueue queue;

    /* 생성자 */
    public Graph() {
        this.nodes = new ArrayList<>();
    }

    /* 그래프 노드 추가 */
    public void addNode(Node node) {
        this.nodes.add(node);
    }

    /* 깊이 우선 탐색 */
    // 깊이 우선 탐색 DFS 시작
    public void startDFS() {
        CLEAR();

        System.out.println("깊이 우선 탐색");

        // 방문 노드 초기화
        visited = new Boolean[nodes.size() + 1];
        Arrays.fill(visited, Boolean.FALSE);

        // DFS 시작
        DFS(1);

        System.out.println();
    }

    // 깊이 우선 탐색 DFS 콜백 메소드
    public void DFS(int v) {
        if (v != 1) {
            System.out.print(" - ");
        }
        System.out.print(v);

        // 방문 노드로 체크
        visited[v] = true;

        if (this.searchNode(v).nodes != null) {
            for (Node node : this.searchNode(v).nodes) {
                if (!visited[node.name]) {
                    DFS(node.name);
                }
            }
        }
    }

    /* 너비 우선 탐색 */
    // 너비 우선 탐색 BFS 시작
    public void startBFS() {
        CLEAR();

        System.out.println("너비 우선 탐색");

        // 방문 노드 초기화
        visited = new Boolean[nodes.size() + 1];
        Arrays.fill(visited, Boolean.FALSE);

        // queue 인스턴스화
        queue = new MyQueue();

        // BFS 시작
        BFS(1);

        System.out.println();
    }

    // 너비 우선 탐색 BFS 메소드
    public void BFS(int v) {
        System.out.print(v);

        // 첫 번째 노드 enqueue (방문)
        queue.enqueue(searchNode(v));
        visited[v] = true;

        // queue 가 빌 때까지
        while (queue.size() != 0) {
            // dequeue
            Node node = queue.dequeue();

            if (node.name != 1) {
                System.out.print(" - " + node);
            }

            if (this.searchNode(node.name).nodes != null) {
                // 인접 노드 모두 체크
                for (Node adjacentNode : this.searchNode(node.name).nodes) {
                    // 방문 노드가 아니라면
                    if (!visited[adjacentNode.name]) {
                        // 방문 후 Queue 에 enqueue
                        visited[adjacentNode.name] = true;
                        queue.enqueue(adjacentNode);
                    }
                }
            }
        }
    }

    /* 이름으로 노드 검색 */
    public Node searchNode(int name) {
        for (Node node : nodes) {
            if (node.name == name) {
                return node;
            }
        }
        return null;
    }

    /* 기타 METHOD */
    // 초기화
    public void CLEAR() {
        visited = null;
    }

    // 확인용 출력 메소드
    /* public void PRINT() {
        for (Node node : nodes) {
            node.PRINT();
        }
        System.out.println("\n");
    } */

}
