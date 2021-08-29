#include "MyGame.h"

int database(char type[20], int data) {
	static int level = 1;
	static int bestScore = 0;
	static int levelP[6] = { 0,0,0,0,0,0 };
	static int levelC[6] = { 0,0,0,0,0,0 };
	int i;

	/* returnLevel : ���� ��ȯ */
	if (!strcmp(type, "returnLevel")) {
		return level;
	}

	/* �����ڿ� */
	if (!strcmp(type, "unlock")) {
		level = 6;
	}

	/* saveLevel : ���� �� �ܰ� �� */
	if (!strcmp(type, "upLevel")) {
		if (level < 6) {
			level++;
			return 0;
		}
		else return -1;
	}

	/* ���� ��� */
	if (!strcmp(type, "writeScore")) {
		if (data > bestScore)
			bestScore = data;
	}

	/* �÷��� Ƚ�� */
	if (!strcmp(type, "played")) {
		levelP[data - 1] += 1;
	}

	/* Ŭ���� Ƚ�� */
	if (!strcmp(type, "cleared")) {
		levelC[data - 1] += 1;
	}

	/* �÷��� Ƚ�� ��� */
	if (!strcmp(type, "printLevelP")) {
		for (i = 0; i < 5; i++) {
			printf("    REGION %d :      %d/%dȸ", i + 1, levelC[i], levelP[i]);
			if (levelC[i] == 0) printf(" (0%%)");
			else printf("(%d%%)", (int)((double)levelC[i] / (double)levelP[i] * 100));
			printf("\n");
		}
		printf("    CUSTOM REGION : %d/%dȸ", levelC[i], levelP[i]);
		if (levelC[i] == 0) printf(" (0%%)");
		else printf("(%d%%)", (int)((double)levelC[i] / (double)levelP[i] * 100));
		printf("\n");
	}

	/* �ְ� ���� ��ȯ */
	if (!strcmp(type, "returnScore")) {
		return bestScore;
	}

	/* clearAll : ��� ������ �ʱ�ȭ */
	if (!strcmp(type, "clearAll")) {
		level = 1;
		bestScore = 0;
		for (i = 0; i < 6; i++)
			levelP[i] = 0;
	}

	return 0;
}


int printData() {
	system("cls");
	printTitle();
	printLine();
	printf("\n  �ְ� ���� : %dP\n\n", database("returnScore", 0));
	
	if(database("returnLevel", 0) == 6) printf("\n  �ְ� �ر� ���� : CUSTOM REGION \n\n");
	else printf("\n  �ְ� �ر� ���� : REGION %d\n\n", database("returnLevel", 0));
	
	printf("\n  ���� �� ����/�õ� Ƚ�� : \n\n");
	database("printLevelP", 0); 
	printf("\n");
	printLine();
	printf("  <q>�� ���� ����ȭ������ ���ư��ʽÿ�.");

	while (_getch() != 'q');

	return 0;
}