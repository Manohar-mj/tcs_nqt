#include <bits/stdc++.h>
using namespace std;
# define ll long long int
//_fast function__
void fast()
{
//don't use it in interactive problems
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
}
int main()
{
    fast();
    int n,k;
    cin>>n>>k;
    vector<int>a(n);
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    int ans=INT_MIN;
    for(int i=0;i<n-k-1;i++)
    {
        for(int j=i+k+1;j<n;j++)
        {
            int curr1,curr2,max1,max2;
            curr1=a[i];
            curr2=a[j];
            max1=a[i];
            max2=a[j];
            for(int m=i-1;m>=0;m--)
            {
                if(curr1+a[m]>a[m])
                {
                    curr1+=a[m];
                }
                else
                {
                    curr1=a[m];
                }
                max1=max(curr1,max1);
            }
            for(int m=j+1;m<n;m++)
            {
                if(curr2+a[m]>a[m])
                {
                    curr2+=a[m];
                }
                else
                {
                    curr2=a[m];
                }
                max2=max(curr2,max2);
            }
            ans=max(ans,max1+max2);

        }
    }
    cout<<ans<<"\n";
    return 0;
}


// King code in c++
