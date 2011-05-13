#include <stdio.h>

extern int foo();

int main(){
	puts("begin");
	printf("foo result: %d\n", foo());
	puts("end");
	return 0;
}
