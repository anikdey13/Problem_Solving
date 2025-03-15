#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
     string s;
     cin >> s;
     int n = s.length();
     int c_p = 0, c_1 = 0, c_2 = 0, c_3 = 0;
    
     for(int i = 0; i < n; i++){
        if(s[i] == '+') c_p++; 
        else if(s[i] == '1') c_1++;
        else if(s[i] == '2') c_2++;
        else c_3++;
     }
    for(int i = 0; i< c_1; i++){
        cout<<"1";
        if((c_2 == 0 && c_3 == 0) && i==c_1 - 1) cout << "\n";
        else cout << "+";
    }
    for(int i = 0; i < c_2; i++){
        cout<<"2";
        if(c_3 == 0 && i == c_2 - 1) cout << "\n";
        else cout << "+";
    }
    for(int i = 0; i < c_3; i++){
        cout<<"3";
        if(i == c_3 - 1) cout << "\n";
        else cout<<"+";
    }
    return 0;
}