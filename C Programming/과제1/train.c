#include <stdio.h>

/* Programming Assignment I *
 * 0451분반 202011353 이호은 */

int main(void) {

	/* 변수 선언 */
	int interval;				// 두 기차 사이의 거리(km)
	int v1, v2;					// 각 기차의 이동속도(km/h)
	double t, h;				// 시 단위, 소요 시간
	unsigned char m, s;			// 분, 초 단위
	const int MINTOSEC = 60;
	const int HOURTOSEC = 3600;

	/* 데이터 입력 */
	printf("두 기차 사이의 거리를 입력하시오: \n");
	scanf("%d", &interval);
	printf("첫 번째 기차의 속도 (km/h)를 입력하시오: \n");
	scanf("%d", &v1);
	printf("두 번째 기차의 속도 (km/h)를 입력하시오: \n");
	scanf("%d", &v2);

	/* 소요 시간(초) = 거리 / 상대속도 * (시간 당 초) */
	t = (double)interval / ((double)v1 + (double)v2) * HOURTOSEC;

	/* 초 단위의 소요 시간을 시, 분, 초로 변환 */
	h = (int)t / HOURTOSEC;
	m = (int)t % HOURTOSEC / MINTOSEC;
	s = (int)t % HOURTOSEC % MINTOSEC;

	/* 결과 출력 */
	printf("충돌까지 총 %.3lf 분 (%d시간 %d분 %d초)가 소요됩니다.\n", t / MINTOSEC, (int)h, m, s);
	printf("첫 번째 기차의 운행거리는 총 %.2lf (km) 입니다.\n", t / HOURTOSEC * v1);
	printf("두 번째 기차의 운행거리는 총 %.2lf (km) 입니다.\n", t / HOURTOSEC * v2);

	return 0;
}

