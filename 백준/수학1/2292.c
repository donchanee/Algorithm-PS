#include <stdio.h>

void bee(int n, int cnt) {
	if(n<=1){
		printf("%d", cnt);
		return;
	}
	else {
		bee(n-(6*cnt), cnt+1);
	}
}

int main(void) {
	int N, cnt=1;
	scanf("%d", &N);
	bee(N, 1);
	return 0;
}
