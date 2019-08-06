# 阿里云CDN-机器学习算法

## 0x1 项目问题

主要问了恶意代码同源分析如何实现，比如灰度图这块，是如何来解释的，比如一个删除文件的操作是如何在图片上显示的，考察的较多的是算法的可解释性。

然后对于毕设项目来说主要的问题在于机器学习里面随机森林的效果较好主要原因是有些特征的性质比较好，然后是数据的原因，并不是算法的优势。



## 0x2 算法问题

给一个500G的文本，里面全是URL，给2G的内存，无限硬盘，如何快速找到Top 100的URL？

参考1: http://blog.sina.com.cn/s/blog_a0db4ee90102vrzk.html

参考2: https://blog.csdn.net/tiankong_/article/details/77239501

参考3: https://blog.csdn.net/kingyuan666/article/details/84584017

参考4: https://blog.csdn.net/kingyuan666/article/details/84501930


## 0x3 进程和线程的区别

根本区别：**进程是操作系统资源分配的基本单位，而线程是任务调度和执行的基本单位**

在开销方面：每个进程都有独立的代码和数据空间（程序上下文），程序之间的切换会有较大的开销；线程可以看做轻量级的进程，同一类线程共享代码和数据空间，每个线程都有自己独立的运行栈和程序计数器（PC），线程之间切换的开销小。

所处环境：在操作系统中能同时运行多个进程（程序）；而在同一个进程（程序）中有多个线程同时执行（通过CPU调度，在每个时间片中只有一个线程执行）

内存分配方面：系统在运行的时候会为每个进程分配不同的内存空间；而对线程而言，除了CPU外，系统不会为线程分配内存（线程所使用的资源来自其所属进程的资源），线程组之间只能共享资源。

包含关系：没有线程的进程可以看做是单线程的，如果一个进程内有多个线程，则执行过程不是一条线的，而是多条线（线程）共同完成的；线程是进程的一部分，所以线程也被称为轻权进程或者轻量级进程。



参考：https://blog.csdn.net/kuangsonghan/article/details/80674777

## 0x4 三次握手&四次握手

![img](https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=2590032753,2466318043&fm=173&app=49&f=JPEG?w=640&h=716&s=E7F239D247AFCCEA106594580300D072)

**三次握手建立连接：**

**第一次握手：**客户端发送syn包(seq=x)到服务器，并进入SYN_SEND状态，等待服务器确认;**第二次握手：**服务器收到syn包，必须确认客户的SYN(ack=x+1)，同时自己也发送一个SYN包(seq=y)，即SYN+ACK包，此时服务器进入SYN_RECV状态;**第三次握手：**客户端收到服务器的SYN+ACK包，向服务器发送确认包ACK(ack=y+1)，此包发送完毕，客户端和服务器进入ESTABLISHED状态，完成三次握手。

**四次握手断开连接：**

**第一次挥手：**主动关闭方发送一个FIN，用来关闭主动方到被动关闭方的数据传送，也就是主动关闭方告诉被动关闭方：我已经不会再给你发数据了(当 然，在fin包之前发送出去的数据，如果没有收到对应的ack确认报文，主动关闭方依然会重发这些数据)，但此时主动关闭方还可以接受数据。

**第二次挥手：**被动关闭方收到FIN包后，发送一个ACK给对方，确认序号为收到序号+1(与SYN相同，一个FIN占用一个序号)。

**第三次挥手：**被动关闭方发送一个FIN，用来关闭被动关闭方到主动关闭方的数据传送，也就是告诉主动关闭方，我的数据也发送完了，不会再给你发数据了。

**第四次挥手：**主动关闭方收到FIN后，发送一个ACK给被动关闭方，确认序号为收到序号+1，至此，完成四次挥手。

参考1：https://blog.csdn.net/qq_35860138/article/details/82054793

参考2 : https://baijiahao.baidu.com/s?id=1618114723935605183&wfr=spider&for=pc



## 0x5 C语言二分法

### 1) 给定一个升序数组A和一个target，查找A中是否有target，有则返回索引值，无则返回-1.

```c
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
```

### 2) 打印一个未知长度的链表的索引中间的数值，如果为偶数则打印两个，奇数则打印一个

```c
# include <stdio.h>  
# include <string.h>

struct NODE 
{  
    int data;  
    struct NODE* next;  
};  

/* Function to get the middle of the linked list*/
void print_middle_element(struct NODE *head)  
{  
    struct NODE *p1, *p2;
    p1->next = head; 
    p2 = head;
    int tag;
    tag = 0;

    if (head == NULL) {
        printf("没有中间节点");
    }

    while(p2->next != NULL) {
        if (p2->next->next != NULL) { /* 偶数的情况 */ 
            p2 = p2->next->next;
            p1 = p1->next;
        }
        else { /* 奇数的情况 */
            p2 = p2->next;
            p1 = p1->next;
            tag = 1;
        }
    }
    if (tag == 0) { /* 最中间的两个元素mid1和mid2 */
        int mid1 = p1->data;
        int mid2 = p1->next->data;
        printf("mid1 = %d", mid1);
        printf("mid2 = %d", mid2);
    }
    else { /* 最中间的一个元素mid */
        int mid = p1->next->data;
        printf("mid = %d", mid);
    }    
}
```



