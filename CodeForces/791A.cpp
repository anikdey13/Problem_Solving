#include <iostream>
using namespace std;

int main(){

    int a ,b;
    cin >> a;
    cin >> b;
    int count = 0;
    while(a <= b){
        a = a * 3;
        b = b * 2;
        count++;
    }
    cout << count << "\n";

    return 0;
}