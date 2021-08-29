#include "MyGame.h"

/* 배열 사이즈(각 최댓값) */
#define MAX_NUM_FLAG 40

/* 힌트 및 벌칙 종류 개수 */
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
			printf("\n  - 당신의 캐릭터(◆)를 방향키를 이용해 움직여 생존하기 위한 지도를 찾으십시오.\n\n");
			printf("  - 가방(▶) 속에는 도움이 되는 도구 혹은 위협이 되는 물건이 있습니다.\n");
			printf("    1) 도움이 되는 도구 :\n");
			printf("      - 위험한 가방 한개를 지워줍니다.        - 생존할 수 있는 시간이 5초 늘어납니다.\n");
			printf("      - 체력이 증가합니다. \n\n");
			printf("    2) 위험한 물건 :\n");
			printf("      - 폭발이 일어나 체력이 줄어들고 위치가 바뀝니다. - 오류가 발생해 처음 위치로 돌아갑니다. \n");
			printf("      - 체력이 줄어듭니다.           - 가방의 위치가 무작위로 바뀝니다. \n\n");
			printf("  - 폭탄(◎) : \n");
			printf("      - 가로, 세로 십자 모양으로 벽을 파괴합니다\n\n");
			printf("  - 단계가 높아질수록 시작 체력이 증가하지만 그만큼 빠르게 소모됩니다.\n\n");
			printf("  - 체력이 모두 소진되거나 시간이 다되어 죽으면 실패이며, 지도를 찾아 생존하십시오.\n\n");
			printf("  - 5개 지역에서 생존하면 난이도를 스스로 설정하는 CUSTOM REGION이 해금됩니다.\n\n");
			printLine();
			printf("  <q>를 눌러 메인화면으로 돌아가십시오.\n");
			printf("  <n> 2페이지로(지역 별 세부 사항)");
		}

		else if (page == 2) {
			system("cls");
			printTitle();
			printLine();
			printf("\n  --- 지역별 세부정보 ---\n\n");
			printf("  REGION 1 : 가방 4개, 도구 3개, 위협 1개, 폭탄 2개, 벽 10개\n");
			printf("             체력 1000P(이동 시 -20P), 제한시간 20초\n\n");
			printf("  REGION 2 : 가방 6개, 도구 2개, 위협 4개, 폭탄 3개, 벽 20개\n");
			printf("             체력 1500P(이동 시 -30P), 제한시간 30초\n\n");
			printf("  REGION 3 : 가방 8개, 도구 3개, 위협 5개, 폭탄 4개, 벽 30개\n");
			printf("             체력 2000P(이동 시 -40P), 제한시간 40초\n\n");
			printf("  REGION 4 : 가방 10개, 도구 4개, 위협 6개, 폭탄 5개, 벽 40개\n");
			printf("             체력 3000P(이동 시 -50P), 제한시간 50초\n\n");
			printf("  REGION 5 : 가방 12개, 도구 4개, 위협 8개, 폭탄 6개, 벽 50개\n");
			printf("             체력 4000P(이동 시 -60P), 제한시간 60초\n\n");
			printf("  CUSTOM   : 가방 15~30개, 도구 0개~총 깃발의 30%%, 위협 70%%~100%%, \n");
			printf("             폭탄 2~12개, 벽 총 깃발의 150%%~250%%\n");
			printf("             체력 5000P(이동 시 -80P), 제한시간 70초\n\n");
			printLine();
			printf("  <q>를 눌러 메인화면으로 돌아가십시오.\n");
			printf("  <n> 1페이지로(게임 규칙)");
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

	/* 레벨에 따른 배치 */
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
			
			printf("\n   CUSTOM LEVEL!\n\n\n   전체 가방의 개수를 입력하세요(최대 30개 최소 15개) : ");
			while (1) {
				scanf("%d", &flagN);
				if ((flagN < 15 || flagN > 30)) {
					printf("   다시 입력하십시오. : ");
				}
				else break;
			}
			
			printf("\n\n   그 중 도구가 든 가방의 개수를 입력하세요(최대 %d개 최소 0개) : ", (int)(flagN * 0.3));
			while (1) {
				scanf("%d", &hintN);
				if ((hintN < 0 || hintN > (int)(flagN * 0.3))) {
					printf("   다시 입력하십시오. : ");
				}
				else break;
			}
			trapN = flagN - hintN;

			printf("\n\n   벽의 개수를 입력하세요(최대 %d개 최소 %d개) : ", (int)(flagN * 2.5), (int)(flagN * 1.5));
			while (1) {
				scanf("%d", &disN);
				if ((disN < (int)(flagN * 1.5) || disN > (int)(flagN * 2.5))) {
					printf("   다시 입력하십시오. : ");
				}
				else break;
			}
			
			printf("\n\n   폭탄의 개수를 입력하세요(최대 12개 최소 2개) : ");
			while (1) {
				scanf("%d", &itemN);
				if (itemN < 2 || itemN > 12) {
					printf("   다시 입력하십시오. : ");
				}
				else break;
			}
			
			printf("\n\n   가방 %d개, 도구 %d개, 위협 %d개, 벽 %d개, 폭탄 %d개로 설정됩니다.\n\n", flagN, hintN, trapN, disN, itemN);
			printLine();
			printf("     <y>를 눌러 진행\n     <아무 키>을 눌러 다시 설정");

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

	// 깃발 배치(HINT)
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

	// 깃발 배치(TRAP)
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

	// 보물 배치
	while (1) {
		tempX = (rand() % 20) * 2 + 1;
		tempY = (rand() % 20) + 1;

		if (mapPtr[tempY][tempX] == 0) {
			mapPtr[tempY][tempX] = 'X';
			break;
		}
	}

	// 장애물 배치
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

	// 아이템 배치
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
	printf("◆");
	
	t1 = time(NULL);
	
	do {
		if (_kbhit()) {
			c = _getch();
			if (c == 'q') return 0;
			// 개발자모드 
			if (c == 'a') {
				char scr[7] = { 0,0,0,0,0,0,0 };
				scanf("%s", scr);
				if (!strcmp(scr, "010228")) {
					database("unlock", 6);
					system("cls");
					printf("[!] 적용 성공!");
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
							printf("◆");

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
							printf("◆");
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
							printf("◆");
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
							printf("◆");
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
		printf("TIME LEFT : %ds (<q>를 눌러 종료)", (timeL + plusTime) - (int)(t2 - t1));
		gotoXY(8, 28);

		if ((int)(t2 - t1) > (timeL + plusTime)) fin = -1;
	} while (fin == 0 && score > 0);


	/* 게임 종료 후 */
	clear(1, mapPtr);

	system("cls");
	printTitle();
	printLine();
	score += 20;
	database("played", level);

	if (fin == 1) {
		printf("\n     생존 성공!\n\n");
		printf("     점수(남은 HP) : %dP!", score);
		database("writeScore", score);
		database("cleared", level);
		if (database("returnScore", 0) == score) printf(" (최고 점수 달성!)");
		printf("\n\n");

		if (database("returnLevel", 0) == level && level != 5 && level != 6) {
			database("upLevel", 0);
			printf("     REGION %d(이)가 해금되었습니다!\n\n", database("returnLevel", 0));
			printf("     다음 지역으로 이동합니다! ");
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
			printf("     CUSTOM REGION 클리어! \n\n");
		}
	}
	else {
		printf("\n     실패! 죽었습니다.. ");
		if (fin == -1) printf(" 시간이 너무 오래 지났습니다.\n\n");
		else printf(" 체력이 다 닳았습니다.\n\n");
		switch (rand() % 5) {
			case 0: {
				printf("     TIP : 이동을 효율적으로 해야 합니다. \n\n");
				break;
			}
			case 1: {
				printf("     TIP : 도구가 든 가방은 생존에 큰 도움이 됩니다. \n\n");
				break;
			}
			case 2: {
				printf("     TIP : 다음 지역를 해금하려면 바로 이전 지역을 클리어해야 합니다. \n\n");
				break;
			}
			case 3: {
				printf("     TIP : 폭탄을 이용하면 벽을 뚫어 빠른 길을 만들 수 있습니다. \n\n");
				break;
			}
			case 4: {
				printf("     TIP : 메인메뉴에서 \'통계\' 메뉴를 통해 실적을 확인해보세요. \n\n");
				break;
			}
		}
	}

	printf("     시작화면으로 돌아갑니다.");
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
		// 깃발 랜덤 배치
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

			// 깃발 배치(HINT)
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

			// 깃발 배치(TRAP)
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

			// 보물 배치
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
			printf("바람이 불어 가방이 날아갑니다.         ");
			return 0;
		}

		// 초기 위치로 이동
		case 1: {
			gotoXY(*x + baseX, *y + baseY);
			printf("  ");
			*x = 1;
			*y = 20;
			gotoXY(8, 28);
			printf("처음 위치로 돌아왔습니다.             ");
			return 1;
		}

		// 캐릭터 랜덤
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
			printf("폭발이 일어나 어딘가로 날아갔습니다.    ");
			return 2;
		}

		// 점수 차감
		case 3: {
			*score -= (rand() % 10) * 10 + 10;
			gotoXY(8, 28);
			printf("독극물입니다. 체력이 줄어듭니다.       ");
			return 3;
		}
	}
}

void hint(char(*mapPtr)[ARR_HORZ], int* score, int *plusTime) {
	switch (rand() % 3) {
		//시간 증가
		case 0: {
			*plusTime += 5;
			gotoXY(8, 28);
			printf("생존 가능 시간이 5초 늘어났습니다.    ");
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
				printf("약을 먹고 체력을 조금 회복합니다.      ");
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
						printf("위협이 되는 가방 한 개를 제거했습니다.    ");
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
			printf("약을 먹고 체력을 조금 회복합니다.     ");
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
				printf("▶");
				j++;
			}
			else if (mapPtr[i][j] == 'X') {
				printf("▶");
				//printf("★");
				j++;
			}
			else if (mapPtr[i][j] == 'T') {
				printf("▶");
				//printf("▷");
				j++;
			}
			else if (mapPtr[i][j] == 'O') {
				printf("◆");
				j++;
			}
			else if (mapPtr[i][j] == 'D') {
				printf("▦");
				j++;
			}
			else if (mapPtr[i][j] == 'Y') {
				printf("※");
				j++;
			}
			else if (mapPtr[i][j] == 'I') {
				printf("◎");
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
	char subtitle1[] = "비행기가 추락해 사막에 혼자 떨어진 당신...";
	char subtitle2[] = "주변을 둘러보니 많은 가방들이 떨어져 있는데...";
	char subtitle3[] = "저 가방 어딘가 생존 지도가 있을것이다.";
	char subtitle4[] = "당신은 생존을 위한 모험을 떠나기로 하였다.";
	
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
	printf("\n  - 당신의 캐릭터(◆)를 방향키를 이용해 움직여 생존하기 위한 지도를 찾으십시오.\n\n");
	printf("  - 가방(▶) 속에는 도움이 되는 도구 혹은 위협이 되는 물건이 있습니다.\n");
	printf("    1) 도움이 되는 도구 :\n");
	printf("      - 위험한 가방 한개를 지워줍니다.        - 생존할 수 있는 시간이 5초 늘어납니다.\n");
	printf("      - 체력이 증가합니다. \n\n");
	printf("    2) 위험한 물건 :\n");
	printf("      - 폭발이 일어나 체력이 줄어들고 위치가 바뀝니다. - 오류가 발생해 처음 위치로 돌아갑니다. \n");
	printf("      - 체력이 줄어듭니다.           - 가방의 위치가 무작위로 바뀝니다. \n\n");
	printf("  - 폭탄(◎) : \n");
	printf("      - 가로, 세로 십자 모양으로 벽을 파괴합니다\n\n");
	printf("  - 단계가 높아질수록 시작 체력이 증가하지만 그만큼 빠르게 소모됩니다.\n\n");
	printf("  - 체력이 모두 소진되거나 시간이 다되어 죽으면 실패이며, 지도를 찾아 생존하십시오.\n\n");
	printf("  - 5개 지역에서 생존하면 난이도를 스스로 설정하는 CUSTOM REGION이 해금됩니다.\n\n");
	printLine();
	printf("  <q>를 눌러 생존 시작하기\n");

	do {
		slc = _getch();
	} while (slc != 'q');

}

/* 게임 엔딩 작성하기 */

void ending() {
	int i;

	system("cls");
	printLine();

	char subtitle1[] = "당신은 생존에 성공했습니다!";
	char subtitle2[] = "본래의 삶으로 돌아가 행복하게 살았습니다.";
	char subtitle3[] = "Thank you for Playing...";
	char subtitle4[] = "제작 : 202011353 이호은";
	char subtitle5[] = "[Custom Region]이 해금되었습니다.";


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

	printf("\n\n   시작화면으로 돌아갑니다.");
	for (i = 3; i >= 0; i--) {
		printf("(%d)", i);
		Sleep(1000);
		printf("\b\b\b   \b\b\b");
	}
	return 0;
}