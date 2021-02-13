package sample.konkuk;

import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Calendar;
import java.util.InputMismatchException;
import java.util.Random;

public class VocManager {
	private String userName;
	private Word[] voc = new Word[100];
	private int number = 0;
	
	static Scanner scanner = new Scanner(System.in);
	
	public VocManager(String userName) {
		this.userName = userName;
	}
	
	void addWord(Word word) {
		if(number < voc.length) {
			voc[number++] = word;
		}
		else {
			System.out.println("더 이상 등록할 수 없습니다.");
		}
	}
	
	void makeVoc(String fileName) {
		try(Scanner scan = new Scanner(new File(fileName))){
			while(scan.hasNextLine()) {
				String str = scan.nextLine();
				String[] temp = str.split("\t");
				this.addWord(new Word(temp[0].trim(), temp[1].trim()));
			}
			
			System.out.printf("%s의 단어장 생성 완료!\n", this.userName);
			menu();
			
		} catch (FileNotFoundException e) {
			System.out.println("파일을 찾을 수 없습니다.");
		}
	}
	
	void menu() {
		int slc = 0;
		
		while(slc != 3) {
			System.out.printf("----- %s의 단어장 -----\n", this.userName);
			System.out.println("1) 단어검색  2) 객관식 퀴즈  3) 종료");
			System.out.print("선택 : ");
			
			try {
				slc = scanner.nextInt();
				
				if(slc > 3 || slc < 1) {
					System.err.println("1 ~ 3의 숫자를 입력하세요.\n");
					continue;
				}
				
				scanner.nextLine();
				
				System.out.println();
				
				switch(slc) {
					case 1:{
						searchVoc2();
						break;
					}
					case 2:{
						multipleChoiceQuiz();
						break;
					}
					case 3:{
						System.out.printf("%s의 단어장 프로그램을 종료합니다.\n", this.userName);
						break;
					}
				}
				
			} catch (InputMismatchException e){
				System.err.println("올바른 숫자를 입력하세요.\n");
				scanner.nextLine();
				continue;
			} 
		}
	}
	
	public void searchVoc2() {
		int count = 0;
		System.out.println("----- 단어 검색 -----");
		System.out.print("검색할 단어 입력 : ");
		String sWord = scanner.nextLine();
		
		if(sWord.isEmpty()) {
			System.err.println("검색어를 입력해야 합니다.\n");
			return;
		}
		
		sWord = sWord.trim();
		
		for(Word word:voc) {
			if(word != null) {
				if(word.eng.contains(sWord)) {
					System.out.println("단어 : " + word.eng + ", 뜻 : " + word.kor);
					count++;
				}
			}else {
				break;
			}
		}
		
		if(count == 0) System.out.println("찾는 단어가 없습니다.");
		
		System.out.println("---------------------\n");
	}
	
	public void multipleChoiceQuiz() {
		Calendar start = Calendar.getInstance();
		final int MAXV = 10;
		int right = 0;
		
		// 시작 시간 체크
		int startHour = start.get(Calendar.HOUR_OF_DAY);
		int startMinute = start.get(Calendar.MINUTE);
		int startSecond = start.get(Calendar.SECOND);
		
		Random random = new Random();
		
		for(int i = 1; i <= MAXV ; i++) {
			System.out.printf("----- 객관식 퀴즈 %d번 -----\n", i);
			int wordToPrint = random.nextInt(59);
			
			Word nowWord = voc[wordToPrint];
			System.out.printf("%s의 뜻은 무엇일까요?\n", nowWord.eng);
			
			int numberOfAnswer = random.nextInt(4) + 1;
			int wrongToPrint;
			
			String[] check = {"", "", ""};
			int checkCount = 0;
			
			for(int j = 1; j <= 4; j++) {
				if(j == numberOfAnswer) {
					System.out.printf("%d) %s\n", j, nowWord.kor);
				}
				else {
						sameCheckLoop : while(true) {
							wrongToPrint = random.nextInt(59);
							
							if(wrongToPrint != numberOfAnswer) {
								for(int k = 0; k < 3; k++) {
									if(check[k].equals(voc[wrongToPrint].kor.trim())) {
										continue sameCheckLoop;
									}
								}
								check[checkCount++] = voc[wrongToPrint].kor.trim();
								System.out.printf("%d) %s\n", j, voc[wrongToPrint].kor);
								break sameCheckLoop;
							}
							else {
								continue sameCheckLoop;
							}
					}
				}
			}
			
			int enter;
			
			while(true) {
				try {
					System.out.print("답을 입력하세요 : ");
					enter = scanner.nextInt();
					
					if(enter > 4 || enter < 1) {
						System.err.println("1 ~ 4의 숫자를 입력하세요.\n");
						continue;
					}
					
					if(enter == numberOfAnswer) {
						System.out.println("정답입니다.\n");
						right++;
					}
					else {
						System.out.printf("틀렸습니다. 정답은 %d번입니다.\n\n", numberOfAnswer);
					}
					break;
					
				} catch (InputMismatchException e){
					System.err.println("올바른 숫자를 입력하세요.\n");
					scanner.nextLine();
					continue;
				} 
			}
		}
		
		Calendar end = Calendar.getInstance();
		
		int endHour = end.get(Calendar.HOUR_OF_DAY);
		int endMinute = end.get(Calendar.MINUTE);
		int endSecond = end.get(Calendar.SECOND);
		
		int tHour = (endHour - startHour) * 3600;
		int tMin = (endMinute - startMinute) * 60;
		int tSec = endSecond - startSecond;
		int totalSec = (tHour + tMin + tSec) % 60;
		int totalMin = (tHour + tMin + tSec) / 60;
		
		
		System.out.printf("%s님 %d문제 중 %d개 맞추셨고, 총 ", this.userName, MAXV, right);
		if(totalMin != 0) {
			System.out.printf("%d분 ", totalMin);			
		}
		System.out.printf("%d초 ", totalSec);
		System.out.println("소요되었습니다.\n\n");
	}
}
