#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <algorithm>


#include <unordered_set>
#include <fstream>
using namespace std;

struct pred {
    int pre = -1;
    int flag = 1;
};
vector <pred> v;
int  h(int i) {
    if (v[v[i].pre - 1].flag == 0) {
        v[i].pre = v[v[i].pre - 1].pre;
        v[i].flag = 0;
    }
    else {
        h(v[i].pre - 1);
        v[i].pre = v[v[i].pre - 1].pre;
        v[i].flag = 0;
    }
    return 0;
}


int main()
{
    
    int n, a;
    pred tek;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a;
        tek.pre = a;
        if (tek.pre == 0) {
            tek.flag = 0;
        }
        v.push_back(tek);
	tek.flag=1;
    }

    for (int i = 0; i < n; i++) {
        if (v[i].pre != 0) {
            if (v[v[i].pre - 1].pre == 0) {
                v[i].flag = 0;
            }
        }
    }
    
    for (int i = 0; i < n; i++) {
        if (v[i].flag == 0) {
            cout << v[i].pre << endl;
        }
        else {
            h(i);
            cout << v[i].pre << endl;
        }
    }

    return 0;
}