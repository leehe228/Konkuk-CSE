#include <stdio.h>

/* Programming Assignment I *
 * 0451�й� 202011353 ��ȣ�� */

int main(void) {

	/* ���� ���� */
	int interval;				// �� ���� ������ �Ÿ�(km)
	int v1, v2;					// �� ������ �̵��ӵ�(km/h)
	double t, h;				// �� ����, �ҿ� �ð�
	unsigned char m, s;			// ��, �� ����
	const int MINTOSEC = 60;
	const int HOURTOSEC = 3600;

	/* ������ �Է� */
	printf("�� ���� ������ �Ÿ��� �Է��Ͻÿ�: \n");
	scanf("%d", &interval);
	printf("ù ��° ������ �ӵ� (km/h)�� �Է��Ͻÿ�: \n");
	scanf("%d", &v1);
	printf("�� ��° ������ �ӵ� (km/h)�� �Է��Ͻÿ�: \n");
	scanf("%d", &v2);

	/* �ҿ� �ð�(��) = �Ÿ� / ���ӵ� * (�ð� �� ��) */
	t = (double)interval / ((double)v1 + (double)v2) * HOURTOSEC;

	/* �� ������ �ҿ� �ð��� ��, ��, �ʷ� ��ȯ */
	h = (int)t / HOURTOSEC;
	m = (int)t % HOURTOSEC / MINTOSEC;
	s = (int)t % HOURTOSEC % MINTOSEC;

	/* ��� ��� */
	printf("�浹���� �� %.3lf �� (%d�ð� %d�� %d��)�� �ҿ�˴ϴ�.\n", t / MINTOSEC, (int)h, m, s);
	printf("ù ��° ������ ����Ÿ��� �� %.2lf (km) �Դϴ�.\n", t / HOURTOSEC * v1);
	printf("�� ��° ������ ����Ÿ��� �� %.2lf (km) �Դϴ�.\n", t / HOURTOSEC * v2);

	return 0;
}

