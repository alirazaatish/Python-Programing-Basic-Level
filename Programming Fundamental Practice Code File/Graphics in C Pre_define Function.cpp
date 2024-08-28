#include<graphics.h>

int main(){
	
	int gd=DETECT, gm;
	
	initgraph(&gd, &gm, (char*)" ");
	
	//Printing Text By Using Outtext() & Outtextxy Function
	outtext("Hello World!");
	outtextxy(100,30,"Hey! This is me Atish.");
	
	//Draw Line By Using line() Function
	line(10,10,50,50);
	
	//Draw rectangle By using rectangle() Function
	rectangle(200, 200, 400, 300);
	
	//Draw a arc by using arc() Function
	arc(100,500,0,180,100);
	
	//Draw ellipe by using ellipe() Function
	ellipse(100,100,0,360,20,50);
	
	
	//Draw fillellipse by using fillellipse() Function
	fillellipse(50,40,10,20);
	
	//Set Color by using setcolor() Function
	setcolor(4);
	
	//Draw circle by using circle() Function
	circle(150,150,100);
	
	
	getch();
	closegraph();
	return 0;
}
