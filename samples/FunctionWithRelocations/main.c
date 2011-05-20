#include <stdio.h>

extern int foo(char*);

int bar(char* str){
	char* pos = strchr(str,'a');
	return pos - str;
}

int main(){
	puts("begin");
	printf("foo result: %d\n", foo("bar"));
	printf("bar result: %d\n", bar("bar"));
	puts("end");
	return 0;
}
