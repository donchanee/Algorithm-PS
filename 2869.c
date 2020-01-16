/* https://www.acmicpc.net/problem/2869
   상수 시간안에 해결해야 하는 O(1) 문제
   한줄식으로 정해두고 풀면 상수시간안에 가능
*/

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int a, b, v, date = 0;
	scanf("%d %d %d", &a, &b, &v);

	date = (v - b - 1) / (a - b) + 1;

	printf("%d", date);
}
