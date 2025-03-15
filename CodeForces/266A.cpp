#include <iostream>
using namespace std;

int main(){

    int numOfStone; string color;
    cin >> numOfStone;
    cin >> color;
    int count = 0;
    for(int i = 1; i < numOfStone; i++){
        if(color[i] == color[i - 1]) count++;
    }
    cout << count << endl;
    return 0;
}