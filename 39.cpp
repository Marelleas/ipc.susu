#include <iostream>
#include <vector>
#include <string>
#include <stack>
using namespace std;

int main()
{
    string s;
    char c;
    vector<char>  v;
    int zachem;
    cin >> zachem;
    cin >> s;
    for(int i=0; i<s.size(); ++i){
        if(s[i]=='[' ||  s[i]=='(' ||  s[i]=='{'){
            v.push_back(s[i]);
        }else if(s[i]=='}' ||  s[i]==']' || s[i]==')'){
            if(v.size()<1){
                cout << "No";
                exit(0);
            }
            if((s[i]=='}' && v[v.size()-1]!='{') ||  (s[i]==']' && v[v.size()-1]!='[') ||  (s[i]==')' && v[v.size()-1]!='(')){
                cout << "No";
                exit(0);
            }
            v.pop_back();
        }
    }
    if(v.size()<1){
        cout << "Yes";
    }else cout << "No";
}
