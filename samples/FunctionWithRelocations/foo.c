
int foo(char* str){
	int var;
	var = bar(str);
	var += strlen(str);
	return var;
}
