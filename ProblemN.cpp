#include <bits/stdc++.h>
using namespace std;

int main() {

    int t;
    cin >> t;
    vector<string> answers;

    for (int i = 0; i < t; i++){
        int a,b,c;
        cin >> a >> b >> c;

        if (a>b && c>b){
            answers.push_back("VALLEY");
        }
        else{
            answers.push_back("MOUNTAIN");
        }
    }

    for (int i = 0; i < t; i++){
        cout << answers[i] << endl;
    }

    return 0;
}