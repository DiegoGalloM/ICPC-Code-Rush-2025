#include <iostream>
#include <string>

using namespace std;

int main() {

    string s;
    cin >> s;

    int n = s.length();

    for (int L = 1; L <=n; L++){
        if (n%L != 0){
            continue;
        }

        int k = n/L;

        string t = s.substr(0,L);

        string str_try = "";
        for (int i = 0; i < k; i++){
            str_try +=t;
        } 

        if (str_try == s){
            cout << t << endl;
            return 0;
        }
    }


    return 0;
}