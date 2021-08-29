#include "MyGame.h"

int database(char type[20], int data) {
	static int level = 1;
	static int bestScore = 0;
	static int levelP[6] = { 0,0,0,0,0,0 };
	static int levelC[6] = { 0,0,0,0,0,0 };
	int i;

	/* returnLevel : 레벨 반환 */
	if (!strcmp(type, "returnLevel")) {
		return level;
	}

	/* 개발자용 */
	if (!strcmp(type, "unlock")) {
		level = 6;
	}

	/* saveLevel : 레벨 한 단계 업 */
	if (!strcmp(type, "upLevel")) {
		if (level < 6) {
			level++;
			return 0;
		}
		else return -1;
	}

	/* 점수 기록 */
	if (!strcmp(type, "writeScore")) {
		if (data > bestScore)
			bestScore = data;
	}

	/* 플레이 횟수 */
	if (!strcmp(type, "played")) {
		levelP[data - 1] += 1;
	}

	/* 클리어 횟수 */
	if (!strcmp(type, "cleared")) {
		levelC[data - 1] += 1;
	}

	/* 플레이 횟수 출력 */
	if (!strcmp(type, "printLevelP")) {
		for (i = 0; i < 5; i++) {
			printf("    REGION %d :      %d/%d회", i + 1, levelC[i], levelP[i]);
			if (levelC[i] == 0) printf(" (0%%)");
			else printf("(%d%%)", (int)((double)levelC[i] / (double)levelP[i] * 100));
			printf("\n");
		}
		printf("    CUSTOM REGION : %d/%d회", levelC[i], levelP[i]);
		if (levelC[i] == 0) printf(" (0%%)");
		else printf("(%d%%)", (int)((double)levelC[i] / (double)levelP[i] * 100));
		printf("\n");
	}

	/* 최고 점수 반환 */
	if (!strcmp(type, "returnScore")) {
		return bestScore;
	}

	/* clearAll : 모든 데이터 초기화 */
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
	printf("\n  최고 점수 : %dP\n\n", database("returnScore", 0));
	
	if(database("returnLevel", 0) == 6) printf("\n  최고 해금 지역 : CUSTOM REGION \n\n");
	else printf("\n  최고 해금 지역 : REGION %d\n\n", database("returnLevel", 0));
	
	printf("\n  지역 별 생존/시도 횟수 : \n\n");
	database("printLevelP", 0); 
	printf("\n");
	printLine();
	printf("  <q>를 눌러 메인화면으로 돌아가십시오.");

	while (_getch() != 'q');

	return 0;
}