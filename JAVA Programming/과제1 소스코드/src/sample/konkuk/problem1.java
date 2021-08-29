package sample.konkuk;

import java.util.Scanner;

public class problem1 {

	public static void main(String[] args) {
		System.out.println("JAVA 과제1 202011353 이호은");
		
		Scanner scanner = new Scanner(System.in);
		int input;
		
		final int NUM = 8;
		
		mainLoop : while(true) {
			System.out.println("1) 복리 예금 계산기  2) 구구단 출력하기  3) 종료");
			System.out.print("메뉴를 선택하세요 : ");
			input = scanner.nextInt();
			
			/* 복리 예금 계산 */
			if (input == 1) {
				System.out.println("====== 복리 예금 계산기 ======");
				int year = 1;
				double rate, money, original;
				
				System.out.print("원금을 입력하세요 : ");
				money = original = scanner.nextDouble();
				System.out.print("연이율을 입력하세요 : ");
				rate = scanner.nextDouble();
				
				System.out.println("-------------------------");
				System.out.printf(" %-6s%-12s \n", "년도수", "원리금");
				System.out.println("-------------------------");
				
				do {
					money = money * (1.0 + rate / 100.0);
					System.out.printf(" %-9d%-20.2f\n", year++, money);
				} while(money <= 2 * original);
				System.out.println("-------------------------");
				System.out.printf("%d년 걸림\n\n", year - 1);
			}
			
			/* 구구단 출력 */
			else if (input == 2) {
				System.out.println("====== 구구단 출력하기 ======");
				
				while(true) {
					System.out.print("출력 단수 : ");
					input = scanner.nextInt();
					
					if(8 >= input && input >= 1) break;
					else System.out.println("출력 단수 입력이 잘못되었습니다.");
				}
				
				int COL = NUM / input;
				if (NUM % input != 0) COL += 1;
				
				for(int i = 0; i < COL; i++) {
					for(int j = 1; j <= 9; j++) {
						PrintLoop : for(int k = 0; k < input; k++) {
							int temp = k + i * input + 2;
							if (temp > 9) break PrintLoop;
							System.out.printf("%-2d*%2d = %2d\t", temp, j, j * temp);
						}
						System.out.println("");
					}
					System.out.println("");
				}
				
			}
			
			/* 프로그램 종료 */
			else if (input == 3) {
				break mainLoop;
			}
			
			/* 1 ~ 3 이외 */
			else System.out.println();
			
		} //mainLoop : while
		
		scanner.close();
		
	}

}
