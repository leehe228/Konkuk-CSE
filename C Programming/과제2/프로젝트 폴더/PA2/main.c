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
			/* ���� ���� */
			case 1: {
				temp = 0;
				do {
					temp = startGame(mapPtr, temp);
				} while (temp != 0);
				break;
			}

			/* ���� ���� */
			case 2: {
				explain();
				break;
			}

			/* ��� */
			case 3: {
				printData();
				break;
			}

			/* �ʱ�ȭ */
			case 4: {
				clear(2, mapPtr);
				break;
			}

			case 5: {
				tutorial();
				gameTitle();
				break;
			}

			/* ���� ���� */
			case 6: {
				system("cls");
				printTitle();
				printLine();
				printf("\n  ������ ������ �����Ͻðڽ��ϱ�?\n\n");
				printLine();
				printf("  �����ϱ� <y>  ����ϱ� <n> ");

				do {
					temp = _getch();
				} while (temp != 'y' && temp != 'n');

				if (temp == 'y') {
					system("cls");
					printTitle();
					printLine();
					printf("\n  ������ �����մϴ�.\n\n");
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