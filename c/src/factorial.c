#include<stdio.h>

int factorial ( int x ) {
	if (x == 0 ) { return 0;}
	if (x == 1) { return 1;}
	if (x == 2) {return 1;}
	return factorial(x-2) + factorial(x-1);
}

int main () {
	int i = 0 ;
	for ( i = 0 ; i < 20 ; i ++ ) {
		printf("%d ", factorial(i));
	}
	return 0;
}
