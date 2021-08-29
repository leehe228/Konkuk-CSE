#include "MyGame.h"

/* �迭 ������(�� �ִ�) */
#define MAX_NUM_FLAG 40

/* ��Ʈ �� ��Ģ ���� ���� */
#define HINT 3
#define TRAP 4

#define MAX_NUM_DIS 100
#define MAX_NUM_ITEM 6

int explain() {
	char slc;
	int page = 1;
	do {
		if (page == 1) {
			system("cls");
			printTitle();
			printLine();
			printf("\n  - ����� ĳ����(��)�� ����Ű�� �̿��� ������ �����ϱ� ���� ������ ã���ʽÿ�.\n\n");
			printf("  - ����(��) �ӿ��� ������ �Ǵ� ���� Ȥ�� ������ �Ǵ� ������ �ֽ��ϴ�.\n");
			printf("    1) ������ �Ǵ� ���� :\n");
			printf("      - ������ ���� �Ѱ��� �����ݴϴ�.        - ������ �� �ִ� �ð��� 5�� �þ�ϴ�.\n");
			printf("      - ü���� �����մϴ�. \n\n");
			printf("    2) ������ ���� :\n");
			printf("      - ������ �Ͼ ü���� �پ��� ��ġ�� �ٲ�ϴ�. - ������ �߻��� ó�� ��ġ�� ���ư��ϴ�. \n");
			printf("      - ü���� �پ��ϴ�.           - ������ ��ġ�� �������� �ٲ�ϴ�. \n\n");
			printf("  - ��ź(��) : \n");
			printf("      - ����, ���� ���� ������� ���� �ı��մϴ�\n\n");
			printf("  - �ܰ谡 ���������� ���� ü���� ���������� �׸�ŭ ������ �Ҹ�˴ϴ�.\n\n");
			printf("  - ü���� ��� �����ǰų� �ð��� �ٵǾ� ������ �����̸�, ������ ã�� �����Ͻʽÿ�.\n\n");
			printf("  - 5�� �������� �����ϸ� ���̵��� ������ �����ϴ� CUSTOM REGION�� �رݵ˴ϴ�.\n\n");
			printLine();
			printf("  <q>�� ���� ����ȭ������ ���ư��ʽÿ�.\n");
			printf("  <n> 2��������(���� �� ���� ����)");
		}

		else if (page == 2) {
			system("cls");
			printTitle();
			printLine();
			printf("\n  --- ������ �������� ---\n\n");
			printf("  REGION 1 : ���� 4��, ���� 3��, ���� 1��, ��ź 2��, �� 10��\n");
			printf("             ü�� 1000P(�̵� �� -20P), ���ѽð� 20��\n\n");
			printf("  REGION 2 : ���� 6��, ���� 2��, ���� 4��, ��ź 3��, �� 20��\n");
			printf("             ü�� 1500P(�̵� �� -30P), ���ѽð� 30��\n\n");
			printf("  REGION 3 : ���� 8��, ���� 3��, ���� 5��, ��ź 4��, �� 30��\n");
			printf("             ü�� 2000P(�̵� �� -40P), ���ѽð� 40��\n\n");
			printf("  REGION 4 : ���� 10��, ���� 4��, ���� 6��, ��ź 5��, �� 40��\n");
			printf("             ü�� 3000P(�̵� �� -50P), ���ѽð� 50��\n\n");
			printf("  REGION 5 : ���� 12��, ���� 4��, ���� 8��, ��ź 6��, �� 50��\n");
			printf("             ü�� 4000P(�̵� �� -60P), ���ѽð� 60��\n\n");
			printf("  CUSTOM   : ���� 15~30��, ���� 0��~�� ����� 30%%, ���� 70%%~100%%, \n");
			printf("             ��ź 2~12��, �� �� ����� 150%%~250%%\n");
			printf("             ü�� 5000P(�̵� �� -80P), ���ѽð� 70��\n\n");
			printLine();
			printf("  <q>�� ���� ����ȭ������ ���ư��ʽÿ�.\n");
			printf("  <n> 1��������(���� ��Ģ)");
		}

		do {
			slc = _getch();
		} while (slc != 'q' && slc != 'n');
		if (slc == 'n' && page == 1) page = 2;
		else if (slc == 'n' && page == 2) page = 1;

	} while (slc != 'q');

	return 0;
}


int startGame(char(*mapPtr)[ARR_HORZ], int selectedLevel) {
	int x = 1, y = 20;
	const int scoreX = 3, scoreY = 27; 
	const int baseX = 8, baseY = 4;
	int level, score, fin = 0;
	int flagN = 0, hintN = 0, trapN = 0, disN = 0, itemN = 0;
	int i, j, tempX, tempY;
	time_t t1 = 0, t2 = 0;
	int plusTime = 0, timeL = 0;
	int c, type = -1;

	if (selectedLevel == 0) {
		level = selectLevel(database("returnLevel", 0));
		if (level == -1) return 0;
	}
	else level = selectedLevel;

	/* ������ ���� ��ġ */
	if (level == 1) {
		flagN = 4;
		hintN = 3;
		trapN = 1;
		itemN = 2;
		score = 1000;
		timeL = 20;
	}
	else if (level == 2) {
		flagN = 6;
		hintN = 2;
		trapN = 4;
		itemN = 3;
		score = 1500;
		timeL = 30;
	}
	else if (level == 3) {
		flagN = 8;
		hintN = 3;
		trapN = 5;
		itemN = 4;
		score = 2000;
		timeL = 40;
	}
	else if (level == 4) {
		flagN = 10;
		hintN = 4;
		trapN = 6;
		itemN = 5;
		score = 3000;
		timeL = 50;
	}
	else if (level == 5) {
		flagN = 12;
		hintN = 4;
		trapN = 8;
		itemN = 6;
		score = 4000;
		timeL = 60;
	}
	else if (level == 6) {
		while (1) {
			system("cls");
			printTitle();
			printLine();
			
			printf("\n   CUSTOM LEVEL!\n\n\n   ��ü ������ ������ �Է��ϼ���(�ִ� 30�� �ּ� 15��) : ");
			while (1) {
				scanf("%d", &flagN);
				if ((flagN < 15 || flagN > 30)) {
					printf("   �ٽ� �Է��Ͻʽÿ�. : ");
				}
				else break;
			}
			
			printf("\n\n   �� �� ������ �� ������ ������ �Է��ϼ���(�ִ� %d�� �ּ� 0��) : ", (int)(flagN * 0.3));
			while (1) {
				scanf("%d", &hintN);
				if ((hintN < 0 || hintN > (int)(flagN * 0.3))) {
					printf("   �ٽ� �Է��Ͻʽÿ�. : ");
				}
				else break;
			}
			trapN = flagN - hintN;

			printf("\n\n   ���� ������ �Է��ϼ���(�ִ� %d�� �ּ� %d��) : ", (int)(flagN * 2.5), (int)(flagN * 1.5));
			while (1) {
				scanf("%d", &disN);
				if ((disN < (int)(flagN * 1.5) || disN > (int)(flagN * 2.5))) {
					printf("   �ٽ� �Է��Ͻʽÿ�. : ");
				}
				else break;
			}
			
			printf("\n\n   ��ź�� ������ �Է��ϼ���(�ִ� 12�� �ּ� 2��) : ");
			while (1) {
				scanf("%d", &itemN);
				if (itemN < 2 || itemN > 12) {
					printf("   �ٽ� �Է��Ͻʽÿ�. : ");
				}
				else break;
			}
			
			printf("\n\n   ���� %d��, ���� %d��, ���� %d��, �� %d��, ��ź %d���� �����˴ϴ�.\n\n", flagN, hintN, trapN, disN, itemN);
			printLine();
			printf("     <y>�� ���� ����\n     <�ƹ� Ű>�� ���� �ٽ� ����");

			score = 5000;
			timeL = 70;

			if (_getch() == 'y') break;
		} 

	}
	if(level != 6) disN = level * 10;

	clear(1, mapPtr);

	srand((unsigned)time(NULL));

	for (i = 17; i <= 20; i++) {
		for (j = 1; j < 6; j += 2) {
			mapPtr[i][j] = 'x';
		}
	}

	// ��� ��ġ(HINT)
	for (i = 0; i < hintN; i++) {
		while (1) {
			tempX = (rand() % 20) * 2 + 1;
			tempY = (rand() % 20) + 1;

			if (mapPtr[tempY][tempX] == 0) {
				mapPtr[tempY][tempX] = 'H';
				break;
			}
		}
	}

	// ��� ��ġ(TRAP)
	for (i = 0; i < trapN; i++) {
		while (1) {
			tempX = (rand() % 20) * 2 + 1;
			tempY = (rand() % 20) + 1;

			if (mapPtr[tempY][tempX] == 0) {
				mapPtr[tempY][tempX] = 'T';
				break;
			}
		}
	}

	// ���� ��ġ
	while (1) {
		tempX = (rand() % 20) * 2 + 1;
		tempY = (rand() % 20) + 1;

		if (mapPtr[tempY][tempX] == 0) {
			mapPtr[tempY][tempX] = 'X';
			break;
		}
	}

	// ��ֹ� ��ġ
	for (i = 0; i < disN; i++) {
		while (1) {
			tempX = (rand() % 20) * 2 + 1;
			tempY = (rand() % 20) + 1;

			if (mapPtr[tempY][tempX] == 0) {
				mapPtr[tempY][tempX] = 'D';
				break;
			}
		}
	}

	// ������ ��ġ
	for (i = 0; i < itemN; i++) {
		while (1) {
			tempX = (rand() % 20) * 2 + 1;
			tempY = (rand() % 20) + 1;

			if (mapPtr[tempY][tempX] == 0) {
				mapPtr[tempY][tempX] = 'I';
				break;
			}
		}
	}
	for (i = 17; i <= 20; i++) {
		for (j = 1; j < 6; j += 2) {
			mapPtr[i][j] = 0;
		}
	}

	drawScreen(mapPtr);
	gotoXY(x + baseX, y + baseY);
	printf("��");
	
	t1 = time(NULL);
	
	do {
		if (_kbhit()) {
			c = _getch();
			if (c == 'q') return 0;
			// �����ڸ�� 
			if (c == 'a') {
				char scr[7] = { 0,0,0,0,0,0,0 };
				scanf("%s", scr);
				if (!strcmp(scr, "010228")) {
					database("unlock", 6);
					system("cls");
					printf("[!] ���� ����!");
					Sleep(1000);
					return 0;
				}
			}
			if (c == 224) {
				c = _getch();
				switch (c) {
					// UP
				case 72: {
					if (y > 1) {
						if (mapPtr[y - 1][x] != 'D') {
							gotoXY(x + baseX, y + baseY);
							printf("  ");
							gotoXY(x + baseX, y - 1 + baseY);
							printf("  ");
							if (mapPtr[y - 1][x] == 'T') {
								type = trap(mapPtr, &score, &x, &y, baseX, baseY, hintN, trapN);
							}
							else if (mapPtr[y - 1][x] == 'H') {
								hint(mapPtr, &score, &plusTime);
							}
							else if (mapPtr[y - 1][x] == 'I') {
								item(mapPtr, x, y - 1);
							}
							else if (mapPtr[y - 1][x] == 'X') {
								fin = 1;
							}
							if (type != 1 && type != 2) y--;
							gotoXY(x + baseX, y + baseY);
							printf("��");

							if (level == 1) score -= 20;
							else if (level == 2) score -= 30;
							else if (level == 3) score -= 40;
							else if (level == 4) score -= 50;
							else if (level == 5) score -= 60;
							else if (level == 6) score -= 80;

							mapPtr[y][x] = 0;
						}
					}
					break;
				}

					   // DOWN
				case 80: {
					if (y < 20) {
						if (mapPtr[y + 1][x] != 'D') {
							gotoXY(x + baseX, y + baseY);
							printf("  ");
							gotoXY(x + baseX, y + 1 + baseY);
							printf("  ");
							if (mapPtr[y + 1][x] == 'T') {
								type = trap(mapPtr, &score, &x, &y, baseX, baseY, hintN, trapN);
							}
							else if (mapPtr[y + 1][x] == 'H') {
								hint(mapPtr, &score, &plusTime);
							}
							else if (mapPtr[y + 1][x] == 'I') {
								item(mapPtr, x, y + 1);
							}
							else if (mapPtr[y + 1][x] == 'X') {
								fin = 1;
							}
							if (type != 1 && type != 2) y++;
							gotoXY(x + baseX, y + baseY);
							printf("��");
							if (level == 1) score -= 20;
							else if (level == 2) score -= 30;
							else if (level == 3) score -= 40;
							else if (level == 4) score -= 50;
							else if (level == 5) score -= 60;
							else if (level == 6) score -= 80;
							mapPtr[y][x] = 0;
						}
					}
					break;
				}

					   // LEFT
				case 75: {
					if (x > 1) {
						if (mapPtr[y][x - 2] != 'D') {
							gotoXY(x + baseX, y + baseY);
							printf("  ");
							gotoXY(x - 2 + baseX, y + baseY);
							printf("  ");
							if (mapPtr[y][x - 2] == 'T') {
								type = trap(mapPtr, &score, &x, &y, baseX, baseY, hintN, trapN);
							}
							else if (mapPtr[y][x - 2] == 'H') {
								hint(mapPtr, &score, &plusTime);
							}
							else if (mapPtr[y][x - 2] == 'I') {
								item(mapPtr, x - 2, y);
							}
							else if (mapPtr[y][x - 2] == 'X') {
								fin = 1;
							}
							if (type != 1 && type != 2) x -= 2;
							gotoXY(x + baseX, y + baseY);
							printf("��");
							if (level == 1) score -= 20;
							else if (level == 2) score -= 30;
							else if (level == 3) score -= 40;
							else if (level == 4) score -= 50;
							else if (level == 5) score -= 60;
							else if (level == 6) score -= 80;
							mapPtr[y][x] = 0;
						}
					}
					break;
				}

					   // RIGHT
				case 77: {
					if (x < 39) {
						if (mapPtr[y][x + 2] != 'D') {
							gotoXY(x + baseX, y + baseY);
							printf("  ");
							gotoXY(x + 2 + baseX, y + baseY);
							printf("  ");
							if (mapPtr[y][x + 2] == 'T') {
								type = trap(mapPtr, &score, &x, &y, baseX, baseY, hintN, trapN);
							}
							else if (mapPtr[y][x + 2] == 'H') {
								hint(mapPtr, &score, &plusTime);
							}
							else if (mapPtr[y][x + 2] == 'I') {
								item(mapPtr, x + 2, y);
							}
							else if (mapPtr[y][x + 2] == 'X') {
								fin = 1;
							}
							if (type != 1 && type != 2) x += 2;
							gotoXY(x + baseX, y + baseY);
							printf("��");
							if (level == 1) score -= 20;
							else if (level == 2) score -= 30;
							else if (level == 3) score -= 40;
							else if (level == 4) score -= 50;
							else if (level == 5) score -= 60;
							else if (level == 6) score -= 80;
							mapPtr[y][x] = 0;
						}
					}
					break;
				}
				}
			}
			
		}
		gotoXY(scoreX, scoreY);
		printf("HP : %d  /  ", score);
		type = -1;
		t2 = time(NULL);
		printf("TIME LEFT : %ds (<q>�� ���� ����)", (timeL + plusTime) - (int)(t2 - t1));
		gotoXY(8, 28);

		if ((int)(t2 - t1) > (timeL + plusTime)) fin = -1;
	} while (fin == 0 && score > 0);


	/* ���� ���� �� */
	clear(1, mapPtr);

	system("cls");
	printTitle();
	printLine();
	score += 20;
	database("played", level);

	if (fin == 1) {
		printf("\n     ���� ����!\n\n");
		printf("     ����(���� HP) : %dP!", score);
		database("writeScore", score);
		database("cleared", level);
		if (database("returnScore", 0) == score) printf(" (�ְ� ���� �޼�!)");
		printf("\n\n");

		if (database("returnLevel", 0) == level && level != 5 && level != 6) {
			database("upLevel", 0);
			printf("     REGION %d(��)�� �رݵǾ����ϴ�!\n\n", database("returnLevel", 0));
			printf("     ���� �������� �̵��մϴ�! ");
			for (i = 3; i >= 0; i--) {
				printf("(%d)", i);
				Sleep(1000);
				printf("\b\b\b   \b\b\b");
			}

			return database("returnLevel", 0);
		}
		else if (level == 5) {
			ending();
			system("cls");
			printTitle();
			printLine();
			database("upLevel", 0);
			return 0;
		}
		else if (level == 6) {
			printf("     CUSTOM REGION Ŭ����! \n\n");
		}
	}
	else {
		printf("\n     ����! �׾����ϴ�.. ");
		if (fin == -1) printf(" �ð��� �ʹ� ���� �������ϴ�.\n\n");
		else printf(" ü���� �� ��ҽ��ϴ�.\n\n");
		switch (rand() % 5) {
			case 0: {
				printf("     TIP : �̵��� ȿ�������� �ؾ� �մϴ�. \n\n");
				break;
			}
			case 1: {
				printf("     TIP : ������ �� ������ ������ ū ������ �˴ϴ�. \n\n");
				break;
			}
			case 2: {
				printf("     TIP : ���� ������ �ر��Ϸ��� �ٷ� ���� ������ Ŭ�����ؾ� �մϴ�. \n\n");
				break;
			}
			case 3: {
				printf("     TIP : ��ź�� �̿��ϸ� ���� �վ� ���� ���� ���� �� �ֽ��ϴ�. \n\n");
				break;
			}
			case 4: {
				printf("     TIP : ���θ޴����� \'���\' �޴��� ���� ������ Ȯ���غ�����. \n\n");
				break;
			}
		}
	}

	printf("     ����ȭ������ ���ư��ϴ�.");
	for (i = 3; i >= 0; i--) {
		printf("(%d)", i);
		Sleep(1000);
		printf("\b\b\b   \b\b\b");
	}
	return 0;
}

int trap(char(*mapPtr)[ARR_HORZ], int *score, int* x, int* y, int baseX, int baseY, int hintN, int trapN) {
	int h = 0, t = 0;
	
	switch (rand() % 4) {
		// ��� ���� ��ġ
		case 0: {
			int i, j, tempX, tempY;
			for (i = 1; i <= 20; i++) {
				for (j = 1; j < 40; j += 2) {
					if (mapPtr[i][j] == 'X' || mapPtr[i][j] == 'H' || mapPtr[i][j] == 'T') {
						if (mapPtr[i][j] == 'H')
							h++;
						if (mapPtr[i][j] == 'T')
							t++;
						mapPtr[i][j] = 0;
					}
				}
			}

			mapPtr[*y][*x] = '1';

			// ��� ��ġ(HINT)
			for (i = 0; i < h; i++) {
				while (1) {
					tempX = (rand() % 20) * 2 + 1;
					tempY = (rand() % 20) + 1;

					if (mapPtr[tempY][tempX] == 0) {
						mapPtr[tempY][tempX] = 'H';
						break;
					}
				}
			}

			// ��� ��ġ(TRAP)
			for (i = 0; i < t; i++) {
				while (1) {
					tempX = (rand() % 20) * 2 + 1;
					tempY = (rand() % 20) + 1;

					if (mapPtr[tempY][tempX] == 0) {
						mapPtr[tempY][tempX] = 'T';
						break;
					}
				}
			}

			// ���� ��ġ
			while (1) {
				tempX = (rand() % 20) * 2 + 1;
				tempY = (rand() % 20) + 1;

				if (mapPtr[tempY][tempX] == 0) {
					mapPtr[tempY][tempX] = 'X';
					break;
				}
			}
			mapPtr[*y][*x] = 0;
			drawScreen(mapPtr);
			gotoXY(8, 28);
			printf("�ٶ��� �Ҿ� ������ ���ư��ϴ�.         ");
			return 0;
		}

		// �ʱ� ��ġ�� �̵�
		case 1: {
			gotoXY(*x + baseX, *y + baseY);
			printf("  ");
			*x = 1;
			*y = 20;
			gotoXY(8, 28);
			printf("ó�� ��ġ�� ���ƿԽ��ϴ�.             ");
			return 1;
		}

		// ĳ���� ����
		case 2: {
			int tempX, tempY;
			mapPtr[tempY][tempX] == 0;
			gotoXY(*x + baseX, *y + baseY);
			printf("  ");
			
			while (1) {
				tempX = (rand() % 20) * 2 + 1;
				tempY = (rand() % 20) + 1;

				if (mapPtr[tempY][tempX] == 0) {
					*x = tempX;
					*y = tempY;
					break;
				}
			}

			gotoXY(8, 28);
			*score -= (rand() % 5) * 10 + 10;
			printf("������ �Ͼ ��򰡷� ���ư����ϴ�.    ");
			return 2;
		}

		// ���� ����
		case 3: {
			*score -= (rand() % 10) * 10 + 10;
			gotoXY(8, 28);
			printf("���ع��Դϴ�. ü���� �پ��ϴ�.       ");
			return 3;
		}
	}
}

void hint(char(*mapPtr)[ARR_HORZ], int* score, int *plusTime) {
	switch (rand() % 3) {
		//�ð� ����
		case 0: {
			*plusTime += 5;
			gotoXY(8, 28);
			printf("���� ���� �ð��� 5�� �þ���ϴ�.    ");
			return;
		}
		//remove one trap flag
		case 1: {
			int i, j, n = 0, t = 0;
			for (i = 1; i <= 20; i++) {
				for (j = 1; j < 40; j += 2) {
					if (mapPtr[i][j] == 'T') n++;
				}
			}
			if (n == 0) {
				*score += (rand() % 10) * 10 + 30;
				gotoXY(8, 28);
				printf("���� �԰� ü���� ���� ȸ���մϴ�.      ");
				break;
			}
			else if (n != 1) {
				n = rand() % n + 1;
			}
			for (i = 1; i <= 20; i++) {
				for (j = 1; j < 40; j += 2) {
					if (mapPtr[i][j] == 'T') t++;
					if (t == n) {
						mapPtr[i][j] = 0;
						drawScreen(mapPtr);
						gotoXY(8, 28);
						printf("������ �Ǵ� ���� �� ���� �����߽��ϴ�.    ");
						return;
					}
				}
			}
			return;
		}

		//plus score
		case 2: {
			*score += (rand() % 10) * 10 + 10;

			gotoXY(8, 28);
			printf("���� �԰� ü���� ���� ȸ���մϴ�.     ");
			return;
		}
	}
}

void item(char(*mapPtr)[ARR_HORZ], int x, int y) {
	int i, j;

	for (i = 1; i <= 20; i++) {
		for (j = 1; j < 40; j += 2) {
			if (i == y || j == x) {
				if (mapPtr[i][j] == 'D' || mapPtr[i][j] == 0)
					mapPtr[i][j] = 'Y';
			}
		}
	}

	drawScreen(mapPtr);
	Sleep(1000);

	for (i = 1; i <= 20; i++) {
		for (j = 1; j < 40; j += 2) {
			if (mapPtr[i][j] == 'Y')
				mapPtr[i][j] = 0;
		}
	}
	drawScreen(mapPtr);
	return;
}

void drawScreen(char(*mapPtr)[ARR_HORZ]) {
	int i, j;
	system("cls");
	printTitle();
	printLine();
	printf("        ");

	for (i = 0; i < ARR_VERT; i++) {
		for (j = 0; j < ARR_HORZ; j++) {
			if (mapPtr[i][j] == 'H') {
				printf("��");
				j++;
			}
			else if (mapPtr[i][j] == 'X') {
				printf("��");
				//printf("��");
				j++;
			}
			else if (mapPtr[i][j] == 'T') {
				printf("��");
				//printf("��");
				j++;
			}
			else if (mapPtr[i][j] == 'O') {
				printf("��");
				j++;
			}
			else if (mapPtr[i][j] == 'D') {
				printf("��");
				j++;
			}
			else if (mapPtr[i][j] == 'Y') {
				printf("��");
				j++;
			}
			else if (mapPtr[i][j] == 'I') {
				printf("��");
				j++;
			}
			else 
				printf("%c", mapPtr[i][j]);
		}
		printf("\n        ");
	}
	printf("\b\b\b\b\b\b\b\b");
	printLine();
}

void tutorial() {
	char subtitle1[] = "����Ⱑ �߶��� �縷�� ȥ�� ������ ���...";
	char subtitle2[] = "�ֺ��� �ѷ����� ���� ������� ������ �ִµ�...";
	char subtitle3[] = "�� ���� ��� ���� ������ �������̴�.";
	char subtitle4[] = "����� ������ ���� ������ ������� �Ͽ���.";
	
	int i;
	char slc;

	system("cls");
	printLine();

	printf("\n   ");
	for (i = 0; i < strlen(subtitle1); i++) {
		putchar(subtitle1[i]);
		Sleep(80);
	}
	Sleep(1200);

	printf("\n\n   ");
	for (i = 0; i < strlen(subtitle2); i++) {
		putchar(subtitle2[i]);
		Sleep(80);
	}
	Sleep(1200);

	printf("\n\n   ");
	for (i = 0; i < strlen(subtitle3); i++) {
		putchar(subtitle3[i]);
		Sleep(80);
	}
	Sleep(1200);

	printf("\n\n   ");
	for (i = 0; i < strlen(subtitle4); i++) {
		putchar(subtitle4[i]);
		Sleep(80);
	}
	Sleep(1200);

	system("cls");
	printTitle();
	printLine();
	printf("\n  - ����� ĳ����(��)�� ����Ű�� �̿��� ������ �����ϱ� ���� ������ ã���ʽÿ�.\n\n");
	printf("  - ����(��) �ӿ��� ������ �Ǵ� ���� Ȥ�� ������ �Ǵ� ������ �ֽ��ϴ�.\n");
	printf("    1) ������ �Ǵ� ���� :\n");
	printf("      - ������ ���� �Ѱ��� �����ݴϴ�.        - ������ �� �ִ� �ð��� 5�� �þ�ϴ�.\n");
	printf("      - ü���� �����մϴ�. \n\n");
	printf("    2) ������ ���� :\n");
	printf("      - ������ �Ͼ ü���� �پ��� ��ġ�� �ٲ�ϴ�. - ������ �߻��� ó�� ��ġ�� ���ư��ϴ�. \n");
	printf("      - ü���� �پ��ϴ�.           - ������ ��ġ�� �������� �ٲ�ϴ�. \n\n");
	printf("  - ��ź(��) : \n");
	printf("      - ����, ���� ���� ������� ���� �ı��մϴ�\n\n");
	printf("  - �ܰ谡 ���������� ���� ü���� ���������� �׸�ŭ ������ �Ҹ�˴ϴ�.\n\n");
	printf("  - ü���� ��� �����ǰų� �ð��� �ٵǾ� ������ �����̸�, ������ ã�� �����Ͻʽÿ�.\n\n");
	printf("  - 5�� �������� �����ϸ� ���̵��� ������ �����ϴ� CUSTOM REGION�� �رݵ˴ϴ�.\n\n");
	printLine();
	printf("  <q>�� ���� ���� �����ϱ�\n");

	do {
		slc = _getch();
	} while (slc != 'q');

}

/* ���� ���� �ۼ��ϱ� */

void ending() {
	int i;

	system("cls");
	printLine();

	char subtitle1[] = "����� ������ �����߽��ϴ�!";
	char subtitle2[] = "������ ������ ���ư� �ູ�ϰ� ��ҽ��ϴ�.";
	char subtitle3[] = "Thank you for Playing...";
	char subtitle4[] = "���� : 202011353 ��ȣ��";
	char subtitle5[] = "[Custom Region]�� �رݵǾ����ϴ�.";


	printf("\n   ");
	for (i = 0; i < strlen(subtitle1); i++) {
		putchar(subtitle1[i]);
		Sleep(80);
	}
	Sleep(1200);

	printf("\n\n   ");
	for (i = 0; i < strlen(subtitle2); i++) {
		putchar(subtitle2[i]);
		Sleep(80);
	}
	Sleep(1200);

	printf("\n\n   ");
	for (i = 0; i < strlen(subtitle3); i++) {
		putchar(subtitle3[i]);
		Sleep(80);
	}
	Sleep(1200);

	printf("\n\n   ");
	for (i = 0; i < strlen(subtitle4); i++) {
		putchar(subtitle4[i]);
		Sleep(80);
	}
	Sleep(1200);

	printf("\n\n   ");
	for (i = 0; i < strlen(subtitle5); i++) {
		putchar(subtitle5[i]);
		Sleep(80);
	}
	Sleep(1200);

	printf("\n\n   ����ȭ������ ���ư��ϴ�.");
	for (i = 3; i >= 0; i--) {
		printf("(%d)", i);
		Sleep(1000);
		printf("\b\b\b   \b\b\b");
	}
	return 0;
}