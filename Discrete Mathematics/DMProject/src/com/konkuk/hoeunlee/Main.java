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
        List<Graph> graphs = new ArrayList<>();

        File file = new File("data/input.txt");
        try (Scanner scanner = new Scanner(file)) {
            while (scanner.hasNext()) {
                // 노드의 개수 읽음
                int n = Integer.parseInt(scanner.nextLine());
                // 그래프 생성
                Graph temp = new Graph();
                // 노드 리스트 생성
                Node[] nodes = new Node[n];
                // n개의 노드 생성
                for (int i = 0; i < n; i++) {
                    nodes[i] = new Node(i + 1);
                }
                // 인접 노드 설정
                for (int i = 0; i < n; i++) {
                    String nodeString = scanner.nextLine();
                    List<Node> tempNodeList = new ArrayList<>();

                    // 인접 노드가 없다면
                    if (nodeString.length() == 1) {
                        tempNodeList = null;
                    }
                    // 인접 노드 추가
                    else {
                        String[] nodeStringList = nodeString.split(" ");
                        for (String s : nodeStringList) {
                            if (!s.equals(nodeStringList[0])) {
                                // 노드 리스트에서 인접한 노드 찾아 추가
                                tempNodeList.add(nodes[Integer.parseInt(s) - 1]);
                            }
                        }
                    }
                    // 노드에 인접 노드 리스트 추가
                    nodes[i].addNearNode(tempNodeList);
                }

                // 그래프에 인접 노드 리스트 세팅 된 노드들 추가
                for (Node node : nodes) {
                    temp.addNode(node);
                }
                // 그래프 리스트에 만든 그래프 추가
                graphs.add(temp);

            }

            // 탐색
            int count = 1;
            for (Graph graph : graphs) {
                System.out.printf("그래프 [%d]\n", count++);
                System.out.println("----------------------------");
                // DFS
                graph.startDFS();
                // BFS
                graph.startBFS();
                System.out.println("============================\n");
            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

    }

}
