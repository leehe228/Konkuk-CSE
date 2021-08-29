#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <time.h>
#include <conio.h>
#include <string.h>

/* LEVEL */
#define MIN_LVL 1
#define MAX_LVL 6

/* GAME MAP */
#define MAP_HORZ 20
#define MAP_VERT 20

#define ARR_HORZ 42
#define ARR_VERT 22

/* main.c */
void gotoXY(int x, int y);
int main(void);

/* function.c */
void printLine(void);
void printTitle(void);
void gameTitle(void);
void clear(int type, char(*mapPtr)[ARR_HORZ]);
int getMove(int startX, int startY, int interval, int startV, int minV, int maxV);

/*data.c */
int database(char type[20], int data);
int printData(void);

/* game.c */
int explain(void);
int startGame(char(*mapPtr)[ARR_HORZ], int selectedLevel);
void drawScreen(char(*mapPtr)[ARR_HORZ]);
void tutorial(void);
int trap(char(*mapPtr)[ARR_HORZ], int *score, int *x, int *y, int baseX, int baseY, int hintN, int trapN);
void hint(char(*mapPtr)[ARR_HORZ], int *score, int *plusTime);
void item(char(*mapPtr)[ARR_HORZ], int x, int y);
void ending(void);

/* menu.c */
int mainMenu(void);
int selectLevel(int level);


