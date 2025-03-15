#include <iostream>
using namespace std;

int main(){

    int t; cin >> t;
    // for(int i = 0; i<4; cout << arr[i++]);
    for(int i = 0; i<t; i++){
        int arr[4];
        for(int i = 0; i<4; cin >> arr[i++]);
        int count = 0;
        int a3 = arr[0] + arr[1];
        arr[2] = a3;
        for(int j = 0; j < 4; j++){
            if(arr[j+2] == arr[j] + arr[j+1]){
                count++;
            }
        }
        cout << count << endl;
    }
    return 0;
}