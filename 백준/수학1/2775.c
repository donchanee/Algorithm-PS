// https://www.acmicpc.net/problem/2775 부녀회장이 될테야

#include <stdio.h>

int main() {
	int t, n, k, d[15][15] = {0}, i, j;
	
	scanf("%d", &t);

	for (i = 1; i < 15; i++) d[0][i] = i;
	for (i = 1; i < 15; i++) {
		for (j = 1; j < 15; j++) {
			d[i][j] = d[i-1][j] + d[i][j-1];
		}
	}
	
	while (t--) {
		scanf("%d %d", &k, &n);
		printf("%d\n", d[k][n]);
	}
	return 0;
}
