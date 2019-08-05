#include <bits/stdc++.h> 
using namespace std; 
  
int Nth_of_AP(int a, int d, int N) 
{  
    
    return (a + (N - 1) * d); 
      
} 
  

int main()  
{ 
  
    cin>>a>>d>>N;
  
    cout<< Nth_of_AP(a,d,N); 
  
    return 0; 
} 
