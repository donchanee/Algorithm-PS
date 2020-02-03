#include <stdio.h>

int main(){
    int num = 1;
    int n;
    scanf("%d", &n);
    
    while(n - num > 0){
        n -= num;
        num++;
    }
    if(num % 2 == 1){
        printf("%d/%d", num+1-n, n);
    }else{
        printf("%d/%d", n, num+1-n);
    }
}
