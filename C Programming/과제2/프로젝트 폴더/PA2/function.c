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
	printf("            �����Ϸ��� <y>�� �����ʽÿ�.\n\n");
	printLine();
	printLine();

	while (_getch() != 'y');
}

void clear(int type, char(*mapPtr)[ARR_HORZ]) {
	int i, j;

	/* �迭 �ʱ�ȭ */
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

	/* ������ �ʱ�ȭ */
	else if (type == 2 || type == 3) {
		system("cls");
		printTitle();
		printLine();

		printf("\n  ���� ������ �ʱ�ȭ�Ͻðڽ��ϱ�?\n\n");
		printLine();
		printf("  �� <y>  �ƴϿ� <n> ");

		do {
			i = _getch();
		} while (i != 'y' && i != 'n');

		if (i == 'n') return;

		system("cls");
		printTitle();
		printLine();
		printf("\n  [!] ���� �ʱ�ȭ �õ�...\n\n");
		Sleep(100);

		/* �����ͺ��̽� �ʱ�ȭ */
		database("clearAll", 0);

		printf("  [!] ������ �ʱ�ȭ�Ǿ����ϴ�. ����ȭ������ ���ư��ϴ�.");
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

	/* ���Ϸθ� �����̴� ���(�޴� ���� ��) */
	while (1) {
		printf("\b\b  ");
		gotoXY(x, y);
		printf("��");

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
