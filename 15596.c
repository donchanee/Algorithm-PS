// https://www.acmicpc.net/problem/15596
// 정수 N개의 합

long long sum(int *a, int n) {
    int i;
	long long ans = 0;
    for(i=0;i<n;i++) {
		ans += a[i];
	}
	return ans;
}
