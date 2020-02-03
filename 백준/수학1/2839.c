#include <stdio.h>

int main(void) {
	int N, M, result=-1;
	
	scanf("%d", &N);
	for(int i=0;i<=N/5;i++) {
		for(int j=0;j<=N/3;j++) {
			if(5*i+3*j == N) {
				result = i+j;	
			}
		}
	}
	printf("%d", result);
	return 0;
}
