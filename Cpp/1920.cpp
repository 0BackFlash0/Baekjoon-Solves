#include <iostream>
#include <set>
using namespace std;


int main(){
    ios::sync_with_stdio(0); cin.tie(0);

    set<int> A;
    int n, m;
    cin >> n;

    int input_num;
    for(int i = 0; i < n; i++){
        cin >> input_num;
        A.insert(input_num);
    }

    cin >> m;

    for(int i = 0; i < m; i++){
        cin >> input_num;
        if(A.find(input_num)!=A.end()){
            cout << "1\n";
        }
        else {
            cout << "0\n";
        }
    }

    return 0;
}
