#include<graphics.h>
#include<conio.h>
int main(){
	int gd=DETECT, gm;
	initgraph(&gd, &gm, (char*)" ");
	line(100,100,200,200);
	circle(100,100,50);
	getch();
	closegraph();
	return(0);
}
