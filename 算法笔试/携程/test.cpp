/*
 * @Descripttion: 
 * @Author: daxiong
 * @Date: 2019-09-04 19:58:49
 * @LastEditors: daxiong
 * @LastEditTime: 2019-09-04 20:34:29
 */

#include <stdio.h>
#include <string.h>
#include <iostream>
#define inf 100000000
using namespace std;

int dis[110][110];
int mindis[110][110];

int main() {
    int t;
    cin >> t;
    while(t--) {
        int n, m;
        cin >> n >> m;

        for (int i=1; i<=n; ++i) {
            for (int j=1; j<=n; ++j) {
                dis[i][j] = inf;
            }
        }

        for (int i=0; i<m; ++i) {
            int x, y, w;
            cin >> x >> y >> w;
            if (dis[x][y] > w) {
                dis[x][y] = w;
                dis[y][x] = w;
            }
        }

        for (int i=1; i<=n; ++i) {
            for (int j=1; j<=n; ++j) {
                mindis[i][j] = dis[i][j];
            }
        }

        int ansdis = inf, anscnt = 0;

        for (int k=1; k<=n; ++k) {
            for (int i=1; i<k; ++i) {
                for (int j=i+1; j<k; ++j) {
                    if (ansdis > dis[i][k] + dis[j][k] + mindis[i][j]) {
                        ansdis = dis[i][k] + dis[j][k] + mindis[i][j];
                        anscnt = 1;
                    }
                    else if (ansdis == dis[i][k] + dis[j][k] + mindis[i][j]) {
                        anscnt++;
                    }
                }
            }
            for (int i=1; i<=n; ++i) {
                for (int j=1; j<=n; ++j) {
                    mindis[i][j] = min(mindis[i][j], mindis[i][k] + mindis[j][k]); 
                }
            }
        }

        if (anscnt == 0) {
            cout << "-1\n";
        }
        else cout << ansdis << " " << anscnt << endl;
    }
    return 0;
}