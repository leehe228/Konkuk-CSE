package com.konkuk.hoeunlee;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * 이산수학(0037) 학기말 과제
 * 컴퓨터공학부 202011353 이호은
 * Main.java (메인 함수)
 **/

public class Main {

    public static void main(String[] args) {

        // 학번 이름 출력
        System.out.println("이산수학 학기말과제");
        System.out.println("컴퓨터공학부 202011353 이호은\n");

        // 그래프 리스트
        List<AdjacencyMatrix> matrixList = new ArrayList<>();

        File file = new File("data/input.txt");
        try (Scanner scanner = new Scanner(file)) {
            while (scanner.hasNext()) {
                // 노드의 개수 읽음
                int n = Integer.parseInt(scanner.nextLine());
                // 인접 행렬 생성
                AdjacencyMatrix tempMatrix = new AdjacencyMatrix(n);

                // 노드 개수 만큼 읽기
                for (int i = 0; i < n; i++) {
                    String nodeString = scanner.nextLine();

                    // 인접 노드가 있는 경우
                    if (nodeString.length() != 1) {
                        // 인접 노드들을 분리
                        String[] nodeStringList = nodeString.split(" ");

                        for (String s : nodeStringList) {
                            if (!s.equals(nodeStringList[0])) {
                                // 인접 행렬에 edge 추가
                                tempMatrix.addEdge(Integer.parseInt(nodeStringList[0]), Integer.parseInt(s));
                            }
                        }

                    }
                }
                // 인접 행렬 출력
                System.out.println(tempMatrix);
                // 행렬 리스트에 추가
                matrixList.add(tempMatrix);
            }

            // 탐색
            int count = 1;
            for (AdjacencyMatrix matrix : matrixList) {
                System.out.printf("그래프 [%d]\n\n", count++);
                System.out.println("----------------------------");
                // DFS 시작
                matrix.startDFS();
                // BFS 시작
                matrix.startBFS();
                System.out.println("============================\n");
            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
