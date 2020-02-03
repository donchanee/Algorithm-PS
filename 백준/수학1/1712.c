#include <stdio.h>

int main() {
    long long a,b,c,cnt;
    scanf("%lld %lld %lld", &a, &b, &c);
    if (b>=c) {
        printf("-1\n");
        return 0;
    }
    cnt = a / (c-b) +1;
    printf("%lld", cnt);
}
