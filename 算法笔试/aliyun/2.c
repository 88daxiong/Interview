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

int main() {
    struct NODE *p, *n;
    n = p;
    p->data = 0;
    for (int i = 0; i < 5; i++) {
        struct NODE *t;
        t->next = NULL;
        t->data = i + 1;
        p->next = t;
        p = t;
    }
    int data;
    while (n != NULL) {
        data = n->data;
        n = n->next;
        printf("data = %d\n", data);
    }
}