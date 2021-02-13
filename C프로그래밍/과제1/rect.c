#include <stdio.h>

/* Programming Assignment I *
 * 0451분반 202011353 이호은 */

int main(void) {

	/* 변수 선언 */
	int roomLen, roomWid;		// 방의 가로, 세로 길이(m)
	int tableLen, tableWid;		// 테이블의 가로, 세로 길이(m)
	int temp, person;			// temp 변수, 테이블 당 사람 수
	unsigned char interval;  	// 테이블 사이 간격(m)

	/* 데이터 입력 */
	printf("What are the length and width of the room (in meters)?\n");
	scanf("%d %d", &roomLen, &roomWid);

	printf("What are the length and width of each table (in meters)?\n");
	scanf("%d %d", &tableLen, &tableWid);

	printf("How much space is required between tables (in meters)?\n");
	scanf("%d", &temp);
	interval = temp;

	printf("How many people does each table seat?\n");
	scanf("%d", &person);

	/* 테이블이 배치될 수 있는 실질적 가로, 세로 길이 */
	roomLen -= 2 * interval;
	roomWid -= 2 * interval;

	/* 방의 길이 / (테이블 길이 + 간격) 만약 남은 길이에 테이블이 1개 들어간다면 +1, 들어가지 않는다면 +0 */
	person *= (roomLen / (tableLen + interval)) + ((roomLen % (tableLen + interval)) == tableLen);
	person *= (roomWid / (tableWid + interval)) + ((roomWid % (tableWid + interval)) == tableWid);

	/* 결과 출력 */
	printf("This arrangement seats %d people.\n", person);

	return 0;
}

