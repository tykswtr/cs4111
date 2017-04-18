#include <stdio.h>
int a[2][3];
int main(){
	// int a[2][3];
	a[0][0]=1;
	a[0][1]=2;
	a[0][2] = 3;
	a[1][0]=4;
	a[1][1] = 5;
	a[1][2] = 6;
	// int a[2][3] = {
	// 	{1,2,3},
	// 	{4,5,6}
	// };

	// printf("%d/n", a[0][0]);
	// // printf("%d/n", a[0][1]);
	// // printf("%d/n", a[0][2]);
	// // printf("%d/n", a[1][0]);
	// // printf("%d/n", a[1][1]);
	// // printf("%d/n", a[1][2]);
	return 0;
}



// int fib(int n) { 
// 	if (n<2)
// 		return 1; 
// 	else
// 		return fib(n-1) + fib(n-2);
// }

// int main(){
// 	int n = 3;
// 	printf("%d/n", fib(n));
// }