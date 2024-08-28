#include <graphics.h>
#include <stdio.h>
#include <conio.h>

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, (char*)" ");

    // Set text style
    settextstyle(BOLD_FONT, HORIZ_DIR, 6);

    // Set text color
    setcolor(YELLOW);
    outtextxy(70, 70, "Rectangle");
    setfillstyle(SOLID_FILL, GREEN);
    setcolor(GREEN);
    rectangle(200, 200, 400, 300);
    floodfill(300, 250, GREEN); // Fill the Rectangle with GREEN color
    getch();
    cleardevice();
    
    setcolor(RED);
    outtextxy(100, 100, "Circle");
    setfillstyle(SOLID_FILL, BLUE);
    setcolor(BLUE);
    circle(300, 300, 100);
    floodfill(300, 300, BLUE); // Fill the circle with BLUE color
    getch();
    cleardevice();
    
    setcolor(MAGENTA);
    outtextxy(80, 80, "Ellipse");
    setfillstyle(SOLID_FILL, CYAN);
    setcolor(CYAN);
    ellipse(250, 250, 0, 360, 100, 50);
    floodfill(250, 250, CYAN); // Fill the Ellipse with CYAN color
    getch();
    cleardevice();
    
    setcolor(RED);
    outtextxy(80, 80, "Triangle");
    setfillstyle(SOLID_FILL, CYAN);
    setcolor(CYAN);
    int trianglePoints[] = {200, 200, 300, 300, 100, 300, 200, 200};
    fillpoly(3, trianglePoints);  
    getch();
    cleardevice();
    
    return 0;
}

