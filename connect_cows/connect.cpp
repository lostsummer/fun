
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <string>
using namespace std;
int enumcow[12],n,pointx[12],pointy[12];
int ans=0;
bool flag;
int check(int x1,int y1,int x2,int y2)
{
  if (x1!=x2&&y1!=y2)return -1; 
  if (x1==x2&&y1<y2) return 0; 
  if (x1==x2&&y1>y2) return 1; 
  if (y1==y2&&x1<x2) return 2; 
  if (y1==y2&&x1>x2) return 3; 
}
void DFS(int cur)
{
    if(flag==false) return ;
    if(cur==n+1) return ;
    if(check(pointx[enumcow[cur]],pointy[enumcow[cur]],
    pointx[enumcow[cur+1]],pointy[enumcow[cur+1]])==-1){
       flag=false;return ;
    }
    if(check(pointx[enumcow[cur]],pointy[enumcow[cur]],
    pointx[enumcow[cur-1]],pointy[enumcow[cur-1]])==check(pointx[enumcow[cur+1]],
    pointy[enumcow[cur+1]],pointx[enumcow[cur]],pointy[enumcow[cur]])){
       flag=false;return ;
    }
    DFS(cur+1);
}
int main()
{
    freopen("connect.in","r",stdin);
    freopen("connect.out","w",stdout);
    memset(pointx,0,sizeof(pointx));
    memset(pointy,0,sizeof(pointy));
    scanf("%d",&n);
    for(int i=1;i<=n;i++) scanf("%d %d",&pointx[i],&pointy[i]);
    for(int i=1;i<=n;i++) enumcow[i]=i;
    while(1){
      flag=true;
      DFS(0);
      ans+=flag;
      if(!next_permutation(enumcow+1,enumcow+n+1)) break;
    }
    cout<<ans<<endl;
    return 0;
}
