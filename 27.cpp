using namespace std;
#include <iostream>
#include <cmath>
bool prime(long long n){
if (n == 0 || n == 1) {
return false;
}
for(long long i=2;i<=sqrt(n);i++)
if(n%i==0)
return false;
return true;
}
int main() {
int a, b , c ,d;
cin >> a >> b;
int s=0;
for (int i=a; i<=b;i++) {
if (prime(i) == true) {
cout << i << endl;
s+=1;
}
}
if (s==0) {
cout << "Absent";
}
return 0;
}