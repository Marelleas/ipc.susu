#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
int main()
{
  int n,k,s,a,i,maxlen,item,p,newlen;
  cin>>n>>k;
  vector<pair<int,int> > sum(n+1);
  sum[0]=make_pair(0,0);
  s=0;
  for(i=1;i<=n;++i)
  { cin>>a;
    s+=a;
    sum[i]=make_pair(s,i);
  }
  sort(sum.begin(),sum.end());
  item=maxlen=0;
  for(i=0;i<=n;i++)
  { if(i>0 && sum[i].first==sum[i-1].first) continue;
    p=upper_bound(sum.begin(),sum.end(),make_pair(sum[i].first+k,n+1))-sum.begin();
    if(p>0 && sum[p-1].first==sum[i].first+k &&
       (newlen=sum[p-1].second-sum[i].second)>0)
    { if(maxlen<newlen)
      { maxlen=newlen;
        item=sum[i].second+1;
      }
      else if(maxlen==newlen)
        item=min(item,sum[i].second+1);
    }
  } 
  cout<<item<<" "<<maxlen<<endl;
  return 0;
}