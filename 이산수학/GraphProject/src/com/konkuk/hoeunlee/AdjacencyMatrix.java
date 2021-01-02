package com.konkuk.hoeunlee;

import java.util.Arrays;

/**
 * 이산수학(0037) 학기말 과제
 * 컴퓨터공학부 202011353 이호은
 * AdjacencyMatrix.java (인접 행렬 클래스)
 **/

public class AdjacencyMatrix {

    /* FIELD */
    // 인접 행렬 (2차원 배열)
    private final int[][] matrix;
    private final int size;

    // 방문 노드 검사용
    private Boolean[] visited;
    // 너비 우선 탐색용 Queue
    private MyQueue queue;

    /* 생성자 */
    public AdjacencyMatrix(int n) {
        this.matrix = new int[n][n];
        this.size = n;
    }

    // edge 추가 메소드 (start -> end 방향 edge 추가)
    public void addEdge(int start, int end) {
        this.matrix[start - 1][end - 1] = 1;
    }

    /*public boolean checkEdge(int start, int end) {
        return this.matrix[start - 1][end - 1] == 1;
    }*/

    // 인자로 들어온 노드의 인접 행렬의 행 정보 반환
    public int[] getRow(int line) {
        int[] temp = new int[this.size];

        int count = 0;
        for (int i : matrix[line]) {
            temp[count++] = i;
        }

        return temp;
    }

    /*public int[] getColumn(int line) {
        int[] temp = new int[this.size];

        int count = 0;
        for (int[] i : matrix) {
            temp[count++] = i[line];
        }

        return temp;
    }*/

    // 깊이 우선 탐색 시작
    public void startDFS() {
        System.out.println("깊이 우선 탐색");

        visited = new Boolean[size];
        Arrays.fill(visited, Boolean.FALSE);

        DFS(1);

        System.out.println();
    }

    // 깊이 우선 탐색 메소드 (재귀 호출 방식)
    public void DFS(int v) {
        if (v != 1) {
            System.out.print(" - ");
        }
        System.out.print(v);

        // 방문 노드 체크
        visited[v - 1] = true;

        // 현재 방문 노드의 인접 행렬의 행 정보 가져오기
        int[] tempList = this.getRow(v - 1);
        // 인접한 노드가 있다면
        if (this.countOne(tempList) != 0) {
            for (int i = 0; i < tempList.length; i++) {
                // 인접한 노드 중 미방문 노드 방문 재귀 호출
                if (tempList[i] == 1) {
                    if (!visited[i]) {
                        DFS(i + 1);
                    }
                }
            }
        }
    }

    // 너비 우선 탐색 시작
    public void startBFS() {
        System.out.println("너비 우선 탐색");

        visited = new Boolean[size];
        Arrays.fill(visited, Boolean.FALSE);

        queue = new MyQueue();

        BFS(1);

        System.out.println();
    }

    // 너비 우선 탐색 메소드 (Queue 이용)
    public void BFS(int v) {
        System.out.print(v);

        // 시작 노드 enqueue 및 방문 처리
        queue.enqueue(v);
        visited[v - 1] = true;

        // queue 값이 빌 때까지
        while (queue.size() != 0) {
            // 방문해야 할 노드 Queue 에서 dequeue 해서 가져옴
            int nodeToVisit = queue.dequeue();

            // 방문 노드 정보 출력
            if (nodeToVisit != 1) {
                System.out.print(" - " + nodeToVisit);
            }

            // 현재 방문 노드의 인접 행렬의 행 정보 가져오기
            int[] tempList = this.getRow(nodeToVisit - 1);
            // 인접한 노드가 있다면
            if (this.countOne(tempList) != 0) {
                for (int i = 0; i < tempList.length; i++) {
                    // 인접한 노드 중 미방문 노드 일단 방문 후 Queue 에 enqueue
                    if (tempList[i] == 1) {
                        if (!visited[i]) {
                            visited[i] = true;
                            queue.enqueue(i + 1);
                        }
                    }
                }
            }
        }
    }

    // 인자로 들어온 행의 1 개수 반환
    public int countOne(int[] temp) {
        int count = 0;
        for (int i : temp) if (i == 1) count++;
        return count;
    }

    // 2차원 배열을 출력
    @Override
    public String toString() {
        StringBuilder result = new StringBuilder();

        for (int[] i : this.matrix) {
            for (int j : i) {
                result = new StringBuilder(result.toString().concat(j + " "));
            }
            result.append("\n");
        }

        return result.toString();
    }
}
