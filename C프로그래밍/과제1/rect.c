#include <stdio.h>

/* Programming Assignment I *
 * 0451�й� 202011353 ��ȣ�� */

int main(void) {

	/* ���� ���� */
	int roomLen, roomWid;		// ���� ����, ���� ����(m)
	int tableLen, tableWid;		// ���̺��� ����, ���� ����(m)
	int temp, person;			// temp ����, ���̺� �� ��� ��
	unsigned char interval;  	// ���̺� ���� ����(m)

	/* ������ �Է� */
	printf("What are the length and width of the room (in meters)?\n");
	scanf("%d %d", &roomLen, &roomWid);

	printf("What are the length and width of each table (in meters)?\n");
	scanf("%d %d", &tableLen, &tableWid);

	printf("How much space is required between tables (in meters)?\n");
	scanf("%d", &temp);
	interval = temp;

	printf("How many people does each table seat?\n");
	scanf("%d", &person);

	/* ���̺��� ��ġ�� �� �ִ� ������ ����, ���� ���� */
	roomLen -= 2 * interval;
	roomWid -= 2 * interval;

	/* ���� ���� / (���̺� ���� + ����) ���� ���� ���̿� ���̺��� 1�� ���ٸ� +1, ���� �ʴ´ٸ� +0 */
	person *= (roomLen / (tableLen + interval)) + ((roomLen % (tableLen + interval)) == tableLen);
	person *= (roomWid / (tableWid + interval)) + ((roomWid % (tableWid + interval)) == tableWid);

	/* ��� ��� */
	printf("This arrangement seats %d people.\n", person);

	return 0;
}

