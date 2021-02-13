package sample.konkuk;

import java.util.Random;
import java.util.Scanner;

public class problem2 {

	public static void main(String[] args) {

		System.out.println("JAVA 과제2 202011353 이호은");

		final int LENGTH = 5; // 행, 열의 길이
		final int NUMBER = LENGTH * LENGTH;
		boolean STEP = true; // TRUE : USER, FALSE : COM

		/* 인스턴스화 */
		Random random = new Random();
		Scanner scanner = new Scanner(System.in);

		/* 배열 */
		int[][] LIST = new int[LENGTH][LENGTH]; // 맵
		int[] CHECK = new int[LENGTH * LENGTH]; // 각 숫자의 할당 여부 체크

		/* 배열에 랜덤 값 대입 */
		for (int i = 0; i < LENGTH; i++) {
			for (int j = 0; j < LENGTH; j++) {
				smallLoop: while (true) {
					int temp = random.nextInt(NUMBER) + 1;
					if (CHECK[temp - 1] == 0) {
						CHECK[temp - 1] = 1;
						LIST[i][j] = temp;
						break smallLoop;
					}
				} // smallLoop : while
			}
		} // for

		/* 게임 시작 */
		gameLoop: while (true) {

			/* 화면 출력 */
			System.out.println("================");
			for (int i = 0; i < LENGTH; i++) {
				for (int j = 0; j < LENGTH; j++) {
					if (LIST[i][j] == 0)
						System.out.print(" ◀▶"); // USER
					else if (LIST[i][j] == -1)
						System.out.print(" ◁▷"); // COM
					else
						System.out.printf(" %2d", LIST[i][j]);
				}
				System.out.println();
			}
			System.out.println("================");

			/* 종료 조건 체크 */
			int sumCHECK = 0;
			for (int i = 0; i < NUMBER; i++) {
				if (CHECK[i] == 0)
					sumCHECK++;
			}
			if (sumCHECK == NUMBER) {
				System.out.println("무승부!");
				break gameLoop;
			}

			/* 승리 조건 체크 */
			int userBINGO = 0, comBINGO = 0;

			// 직선(세로)
			userBINGO = 0;
			comBINGO = 0;

			for (int i = 0; i < LENGTH; i++) {
				for (int j = 0; j < LENGTH; j++) {
					if (LIST[j][i] == 0)
						userBINGO++;
					else if (LIST[j][i] == -1)
						comBINGO++;
				}
				if (userBINGO == LENGTH) {
					System.out.println("user 빙고!");
					break gameLoop;
				}
				if (comBINGO == LENGTH) {
					System.out.println("com 빙고!");
					break gameLoop;
				}
				userBINGO = 0;
				comBINGO = 0;
			}

			// 직선(가로)
			userBINGO = 0;
			comBINGO = 0;

			for (int i = 0; i < LENGTH; i++) {
				for (int j = 0; j < LENGTH; j++) {
					if (LIST[i][j] == 0)
						userBINGO++;
					else if (LIST[j][i] == -1)
						comBINGO++;
				}
				if (userBINGO == LENGTH) {
					System.out.println("user 빙고!");
					break gameLoop;
				}
				if (comBINGO == LENGTH) {
					System.out.println("com 빙고!");
					break gameLoop;
				}
				userBINGO = 0;
				comBINGO = 0;
			}

			// 반대각선 (\)
			userBINGO = 0;
			comBINGO = 0;

			for (int i = 0; i < LENGTH; i++) {
				if (LIST[i][i] == 0)
					userBINGO++;
				else if (LIST[i][i] == -1)
					comBINGO++;
			}
			if (userBINGO == LENGTH) {
				System.out.println("user 빙고!");
				break gameLoop;
			}
			if (comBINGO == LENGTH) {
				System.out.println("com 빙고!");
				break gameLoop;
			}

			// 정대각선(/)
			userBINGO = 0;
			comBINGO = 0;

			for (int i = 0; i < LENGTH; i++) {
				if (LIST[i][LENGTH - 1 - i] == 0)
					userBINGO++;
				else if (LIST[i][LENGTH - 1 - i] == -1)
					comBINGO++;
			}
			if (userBINGO == LENGTH) {
				System.out.println("user 빙고!");
				break gameLoop;
			}
			if (comBINGO == LENGTH) {
				System.out.println("com 빙고!");
				break gameLoop;
			}

			/* 숫자 선택 */

			if (STEP) { // USER 차례
				while (true) {
					System.out.print("숫자를 선택하세요 (User) : ");
					int input = scanner.nextInt();
					if (1 <= input && input <= NUMBER) {
						if (CHECK[input - 1] == 1) {
							CHECK[input - 1] = 0;

							mainLoop: for (int i = 0; i < LENGTH; i++) {
								for (int j = 0; j < LENGTH; j++) {
									if (LIST[i][j] == input) {
										LIST[i][j] = 0;
										STEP = false;
										break mainLoop;
									}
								}
							}
							break;
						} else {
							System.out.println("-- 이미 선택된 숫자입니다 --");
							continue;
						}
					}

					else
						System.out.println("-- 범위 밖의 숫자입니다 --");
				}
			} // if

			else { // COM 차례
				while (true) {
					int comInput = random.nextInt(NUMBER) + 1;

					if (CHECK[comInput - 1] == 1) {
						CHECK[comInput - 1] = 0;

						mainLoop: for (int i = 0; i < LENGTH; i++) {
							for (int j = 0; j < LENGTH; j++) {
								if (LIST[i][j] == comInput) {
									LIST[i][j] = -1;
									STEP = true;
									break mainLoop;
								}
							}
						}
						System.out.printf("Computer는 %d를 선택했습니다.\n", comInput);
						break;
					}
				}

			} // else

		} // gameLoop : while
		scanner.close();

	} // main
}
