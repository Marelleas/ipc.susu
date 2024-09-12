#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll n,m;
vector<int> vn;
int difnum(int z, int i1, int i2) 
{ int d=0;
  for(;i1<i2;++i1)
  { if(vn[i1]!=z%10) ++d;
    z/=10;
  }
  return d;
}
int main()
{ 
  cin>>n>>m;
  while(n>0)
  { vn.push_back(n%10);
    n/=10;
  }
  if(vn.size()==0) vn.push_back(0);
  int nc=vn.size();
  int k=nc/2;
  int t2=pow(10,nc-k), t1=pow(10,k);
  vector<int> dif(t2,100), part(t2);
  for(int v2=0;v2<t2;++v2)
  { int d=difnum(v2,0,nc-k), r=v2%m;
    if(d<dif[r])
    { dif[r]=d;
      part[r]=v2;
    }
  }
  int dmin=100;
  ll zmin=-1;
  for(int v1=t1/10;v1<t1;++v1)
  { ll r=(ll(v1)*t2)%m;
    int d=difnum(v1,nc-k,nc);
    ll r2=(m-r)%m;
    int d2=100;
    if(r2<t2) d2=dif[r2];
    if(d+d2<dmin)
    { dmin=d+d2;
      zmin=ll(v1)*t2+part[r2];
    }
  }
  cout<<zmin<<"\n";