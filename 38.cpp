using namespace std;
#include <iostream>
#include <cmath>
#include <bits/stdc++.h>
int main() {
    int a, b , c, d , q, w ,e ,r,t,y, R, h;
    cin >> c >> d >> a >>b;
    if (b>a) {
        a+=b;
        b=a-b;
        a-=b;
    }
    if (d>c) {
        c+=d;
        d=c-d;
        c-=d;
    }
    if (((c<=a) && (d<=b))|| (c > a && b >= (2*c*d*a + (c*c-d*d)*sqrt(c*c+d*d-a*a)) / (c*c+d*d))) {
        cout << "Possible";
    }
    else {
        cout << "Impossible";
    }
    
    return 0;
}