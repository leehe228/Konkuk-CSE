#include "MyGame.h"

void printLine() {
	printf("--------------------------------------------------------\n");
}


void printTitle() {      //F I N D  T H E  F L A G ! 
	printf("\n             SURVIVE  ON  THE  DESSERT\n\n");
}

void gameTitle() {
	system("cls");
	printf("\n");
	printLine();
	printLine();
	printf("\n\n\n");
	printTitle();
	printf("\n\n");
	printf("            시작하려면 <y>를 누르십시오.\n\n");
	printLine();
	printLine();

	while (_getch() != 'y');
}

void clear(int type, char(*mapPtr)[ARR_HORZ]) {
	int i, j;

	/* 배열 초기화 */
	if (type == 1 || type == 3) {
		for (i = 0; i < ARR_VERT; i++) {
			for (j = 0; j < ARR_HORZ; j++) {
				if (i == 0 || i == ARR_VERT - 1 || j == 0 || j == ARR_HORZ - 1) {
					mapPtr[i][j] = '#';
				}
				else {
					mapPtr[i][j] = 0;
				}
			}
		}
	}

	/* 데이터 초기화 */
	else if (type == 2 || type == 3) {
		system("cls");
		printTitle();
		printLine();

		printf("\n  정말 게임을 초기화하시겠습니까?\n\n");
		printLine();
		printf("  예 <y>  아니오 <n> ");

		do {
			i = _getch();
		} while (i != 'y' && i != 'n');

		if (i == 'n') return;

		system("cls");
		printTitle();
		printLine();
		printf("\n  [!] 게임 초기화 시도...\n\n");
		Sleep(100);

		/* 데이터베이스 초기화 */
		database("clearAll", 0);

		printf("  [!] 게임이 초기화되었습니다. 시작화면으로 돌아갑니다.");
		for (i = 3; i >= 0; i--) {
			printf("(%d)", i);
			Sleep(1000);
			printf("\b\b\b   \b\b\b");
		}
	}
}


int getMove(int startX, int startY, int interval, int startV, int minV, int maxV) {
	int c, x = startX, y = startY;
	int now = startV;

	/* 상하로만 움직이는 경우(메뉴 선택 시) */
	while (1) {
		printf("\b\b  ");
		gotoXY(x, y);
		printf("◀");

		c = _getch();
		if (c == 224) {
			c = _getch();
			switch (c) {

				/* UP */
				case 72: {
					if (now > minV) {
						y -= interval;
						now--;
					}
					break;
				}

				/* DOWN */
				case 80: {
					if (now < maxV) {
						y += interval;
						now++;
					}
					break;
				}
			}
		}
		else if (c == 'y' || c == 'q')
			break;
	}
	
	if (c == 'q') return -1;
	else return now;
}
