
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n=0;
    cin >> n;
    vector<vector <int>> v(n,vector<int>(n));
    char c;
    for (int i=0;i<n;i++) {
        for(int j=0;j<n;j++) {
            cin >> c;
            v[i][j]=c-'0';
        }
    }
    for(int i=1;i<n;i++) {
        v[0][i]= v[0][i]+ v[0][i-1];
    }
    for(int i=1;i<n;i++) {
        v[i][0]= v[i][0]+ v[i-1][0];
    }
    for (int i=1;i<n;i++) {
        for(int j=1;j<n;j++) {
            v[i][j]=v[i][j]+min(v[i-1][j],v[i][j-1]);
        }
    }
    
    int a=n-1, b=n-1;
    while(true) {
        if (b==0 && a==0) {
            v[a][b]=-1;
            break;
        } 
        
        v[a][b]=-1;
        if (a-1<0) {
            b--;
            continue;
        }
        if (b-1<0){
            a--;
            continue;
        }
        if (v[a-1][b]<=v[a][b-1]) {
            a--;
        }
        else {
            b--;
        }
    }
    vector<vector <char>> vec(n,vector<char>(n));
    for (int i=0;i<n;i++) {
        for(int j=0;j<n;j++) {
            if (v[i][j]==-1) {
                vec[i][j]='#';
            }
            else {
                vec[i][j]='-';
            }
        }
        
    }
     for (int i=0;i<n;i++) {
        for(int j=0;j<n;j++) {
            cout << vec[i][j];
        }
        cout << endl;
     }
       
    return 0;
}
