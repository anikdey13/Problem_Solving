#include <iostream>
#include <set>
using namespace std;

int main()
{

    string username;
    cin >> username;
    set<char> chars;
    for (int i = 0; i < username.length(); i++)
    {
        chars.insert(username[i]);
    }
    int len = chars.size();
    if(len % 2 == 0){
        cout << "CHAT WITH HER!\n"; 
    }else{
        cout << "IGNORE HIM!\n";
    }
    return 0;
}