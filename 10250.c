/* 10250. ACM 호텔
   https://www.acmicpc.net/problem/10250
   간단한 나머지 연산 문제?
*/

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int T, H, W, N, ho, ch, room;

	scanf("%d", &T);
	for (int i = 0; i < T; i++) 
	{
		scanf("%d %d %d", &H, &W, &N);
		ho = N / H;
		ch = N % H;
		if (ch == 0) {
			ch += H;
			ho--;
		}
		printf("%d\n", ch * 100 + ho + 1);
	}
}
