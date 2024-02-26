#include<iostream>
#include<map>
#include<vector>
using namespace std;

int read()
{
	int s=0,w=1; char ch=getchar();
    while(ch<'0'||ch>'9') {if(ch=='-') w=-1;ch=getchar();}
    while(ch>='0'&&ch<='9') {s=(s<<3)+(s<<1)+ch-'0';ch=getchar();}
    return s*w;
}
void write(int x)
{
	if(x<0) {putchar('-');x=-x;} if(x>9) write(x/10); putchar(x%10+'0');
}
void debug()
{
    freopen("","r",stdin);
    freopen("","w",stdout);
}
char a[12][12];
int n=-1,m,len=0;
bool f=0;
map<int,pair<int,int>>ans,tmp;
map<pair<int,int>,bool>flag;
int dir[8][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
bool ck(int x,int y){return x<0||x>=n||y<0||y>=m;}
void dfs(int x,int y,int id,int& maxlen)
{
    flag[make_pair(x,y)]=1;
    tmp[id]=make_pair(x,y);
    for(int i=0;i<8;i++)
    {
        int xx=x+dir[i][0],yy=y+dir[i][1];
        if(ck(xx,yy) || flag[make_pair(xx,yy)] || a[xx][yy]=='#') continue;
        dfs(xx,yy,id+1,maxlen);
    }
    if(x==n-1)
    {
        if(id+1>maxlen) maxlen=id+1,ans=tmp;
        f=1;
    }
    flag[make_pair(x,y)]=0;
}
void solve()
{
    string s;
    while(getline(cin,s),s[0]=='.'||s[0]=='#')
    {
        ++n;
        m=s.length();
        for(int i=0;i<m;i++) a[n][i]=s[i];
    }
    n++;
    for(int j=0;j<m;j++)
    {
        if(a[0][j]=='.') dfs(0,j,0,len);
    }
    for(int i=0;i<len;i++)
    {
        int x=ans[i].first,y=ans[i].second;
        a[x][y]='0'+i;
    }
    if(!f) {cout<<-1<<endl;}
    else cout<<len<<endl;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++) cout<<a[i][j];
        cout<<endl;
    }
}
int main()
{
    rm;
    solve();
	return 0;
}
