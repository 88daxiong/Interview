'''
@Descripttion: 
@Author: daxiong
@Date: 2019-09-02 15:05:33
@LastEditors: daxiong
@LastEditTime: 2019-09-06 14:38:54
'''
# include <iostream>
# include <stdio.h>
# include <vector>
# include <set>
using namespace std;
struct eDge{
    int n1;
    int n2;
};
int main()
{
    int n,m,k;
    scanf("%d %d",&n,&m);
    vector<eDge> v(m);
    for(int i = 0; i < m; i++ )
        scanf("%d %d",&v[i].n1,&v[i].n2);
    scanf("%d",&k);
    while(k--){
        int nodeColor[10009];  //注意需要放在while循环内，每次都需要重新利用
        set<int> color;
        for(int i = 0; i < n; i++) {
            scanf("%d",&nodeColor[i]);
            color.insert(nodeColor[i]);
        }
        bool tag = true;
        for(int i = 0; i < m; i++){
            if(nodeColor[v[i].n1] == nodeColor[v[i].n2]){
                tag = false;
                break;
            }
        }
        if(tag)
            printf("%d%s\n",color.size(),"-coloring");
        else
            printf("No\n");
    }
    return 0;
}

