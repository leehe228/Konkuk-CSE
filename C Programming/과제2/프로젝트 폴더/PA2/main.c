#include "MyGame.h"

void gotoXY(int x, int y) {
	COORD Cur = { x, y };
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), Cur);
}

int main() {
	char map[ARR_VERT][ARR_HORZ];
	char(*mapPtr)[ARR_HORZ] = map;

	int slc;
	char temp = 0;

	gameTitle();
	tutorial();
	gameTitle();

	clear(1, mapPtr);

	do {
		system("cls");
		switch (slc = mainMenu()) {
			/* 게임 시작 */
			case 1: {
				temp = 0;
				do {
					temp = startGame(mapPtr, temp);
				} while (temp != 0);
				break;
			}

			/* 게임 설명 */
			case 2: {
				explain();
				break;
			}

			/* 통계 */
			case 3: {
				printData();
				break;
			}

			/* 초기화 */
			case 4: {
				clear(2, mapPtr);
				break;
			}

			case 5: {
				tutorial();
				gameTitle();
				break;
			}

			/* 게임 종료 */
			case 6: {
				system("cls");
				printTitle();
				printLine();
				printf("\n  정말로 게임을 종료하시겠습니까?\n\n");
				printLine();
				printf("  종료하기 <y>  계속하기 <n> ");

				do {
					temp = _getch();
				} while (temp != 'y' && temp != 'n');

				if (temp == 'y') {
					system("cls");
					printTitle();
					printLine();
					printf("\n  게임을 종료합니다.\n\n");
					printLine();

					return 0;
				}
				else break;
			}
		}
	} while (1);

	Sleep(3000);

	return 0;
}