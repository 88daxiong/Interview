#include <stdio.h>
int binarySearch(int A[], int target, int n) {
    int low, high, mid;
    mid = -1;
    low = 0;
    high = n - 1;
    while (low <= high) { /* 这里比较重要的一点就是必须要等于，因为有可能就是其中一个数 */
        mid = low + high;
        mid /= 2;
        if (target < A[mid])
            high = mid - 1;
        else if (target > A[mid])
            low = mid + 1;
        else
            break;
    }
    if (mid == -1)
        return 0;
    else
        return mid;
}

int main() {
    int A[] = {1, 2, 3, 5 ,10};
    int c = binarySearch(A, 2, 5);
}