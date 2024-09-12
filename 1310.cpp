#include <iostream> 
#include <queue> 
#include <vector> 
#include <string> 
#include <algorithm> 
#include <bits/stdc++.h> 
#include <unordered_set> 
using namespace std; 
long long N; 
struct State { 
    int x; 
    int y; 
    int hu = 0; 
}; 
int main() 
{ 
    State a; 
    int n, m, maxim=0; 
    cin >> n >> m; 
    char hu; 
    queue<State> q; 
    vector <vector <int>> v (n, vector <int>(m)); 
    for (int i =0;i <n;i++) { 
        for (int j = 0; j < m;j++) { 
            cin >> hu; 
            if (hu=='#') { 
                v[i][j]=-2; 
            } 
            if (hu=='*') { 
                v[i][j]=0; 
                a.x=i; 
                a.y=j; 
                q.push(a); 
            } 
            if (hu=='.') { 
                v[i][j]=10000000; 
            } 
        } 
    } 
    while (!q.empty()) { 
         
        State k = q.front(); 
        q.pop(); 
        if (k.hu>maxim) { 
            maxim=k.hu; 
        } 
        if (k.x+1<=n-1) { 
            if (v[k.x+1][k.y]!=-2) 
                if (k.hu+1<v[k.x+1][k.y]) { 
                    a.x=k.x+1; 
                    a.y=k.y; 
                    a.hu=k.hu+1; 
                    v[a.x][a.y]=a.hu; 
                    q.push(a); 
                } 
        } 
        if (k.y+1<=m-1) { 
            if (v[k.x][k.y+1]!=-2) 
                if (k.hu+1<v[k.x][k.y+1]) { 
                    a.x=k.x; 
                    a.y=k.y+1; 
                    a.hu=k.hu+1; 
                    v[a.x][a.y]=a.hu; 
                    q.push(a); 
                } 
        } 
        if (k.x-1>=0) { 
            if (v[k.x-1][k.y]!=-2) 
                if (k.hu+1<v[k.x-1][k.y]) { 
                    a.x=k.x-1; 
                    a.y=k.y; 
                    a.hu=k.hu+1; 
                    v[a.x][a.y]=a.hu; 
                    q.push(a); 
                } 
        } 
        if (k.y-1>=0) { 
            if (v[k.x][k.y-1]!=-2) 
                if (k.hu+1<v[k.x][k.y-1]) { 
                    a.x=k.x; 
                    a.y=k.y-1; 
                    a.hu=k.hu+1; 
                    v[a.x][a.y]=a.hu; 
                    q.push(a); 
                } 
        } 
    } 
    cout << maxim; 
    return 0; 
}