#include "MyGame.h"

int mainMenu() {
	printTitle();
	printLine();
	printf("\n  ▷ 게임 시작 \n\n");
	printf("  ▷ 생존 가이드 \n\n");
	printf("  ▷ 통계 \n\n");
	printf("  ▷ 데이터 초기화 \n\n");
	printf("  ▷ 스토리 다시보기 \n\n");
	printf("  ▷ 게임 종료 \n\n");
	printLine();
	printf("  <y>를 눌러 선택하십시오.\n\n");
	printf("  건국대학교 202011353 이호은\n");

	return getMove(22, 5, 2, 1, 1, 6);
}


int selectLevel(int level) {
	int i, j, slc;

	system("cls");
	printTitle();
	printLine();

	for (i = MIN_LVL; i <= MAX_LVL - 1; i++) {
		printf("  ▷ Region %d", i);
		if (i > level)
			printf("       (잠김) \n  ");
		else printf("\n  ");

		for (j = 1; j <= i; j++) {
			printf("★");
		}
		for (j = 5; j > i; j--) {
			printf("☆");
		}
		printf("\n\n");
	}
	printf("  ▷ Custom Region");
	if (i > level)
		printf("  (잠김) \n  ");
	else printf("\n  ");
	printf("? ? ? ? ? \n\n");
	printLine();
	printf("  <y>를 눌러 선택하십시오.\n");
	printf("  <q>를 메인메뉴로 돌아가기.");

	while ((slc = getMove(28, 4, 3, 1, 1, 6)) > level);

	return slc;
}
