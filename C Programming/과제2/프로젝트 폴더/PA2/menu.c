#include "MyGame.h"

int mainMenu() {
	printTitle();
	printLine();
	printf("\n  �� ���� ���� \n\n");
	printf("  �� ���� ���̵� \n\n");
	printf("  �� ��� \n\n");
	printf("  �� ������ �ʱ�ȭ \n\n");
	printf("  �� ���丮 �ٽú��� \n\n");
	printf("  �� ���� ���� \n\n");
	printLine();
	printf("  <y>�� ���� �����Ͻʽÿ�.\n\n");
	printf("  �Ǳ����б� 202011353 ��ȣ��\n");

	return getMove(22, 5, 2, 1, 1, 6);
}


int selectLevel(int level) {
	int i, j, slc;

	system("cls");
	printTitle();
	printLine();

	for (i = MIN_LVL; i <= MAX_LVL - 1; i++) {
		printf("  �� Region %d", i);
		if (i > level)
			printf("       (���) \n  ");
		else printf("\n  ");

		for (j = 1; j <= i; j++) {
			printf("��");
		}
		for (j = 5; j > i; j--) {
			printf("��");
		}
		printf("\n\n");
	}
	printf("  �� Custom Region");
	if (i > level)
		printf("  (���) \n  ");
	else printf("\n  ");
	printf("? ? ? ? ? \n\n");
	printLine();
	printf("  <y>�� ���� �����Ͻʽÿ�.\n");
	printf("  <q>�� ���θ޴��� ���ư���.");

	while ((slc = getMove(28, 4, 3, 1, 1, 6)) > level);

	return slc;
}
