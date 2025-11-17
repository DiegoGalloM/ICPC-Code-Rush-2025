#include <bits/stdc++.h>
#include <string>
using namespace std;

int main() {
    string n, paulino;
    if (!(cin >> n >> paulino)) return 0;

    if (n.size() != paulino.size()) {
        cout << "NO";
        return 0;
    }

    // Comprobar si 'n' es una rotación de 'paulino'
    string doubled = paulino + paulino;
    if (doubled.find(n) != string::npos) {
        cout << "YES";
    } else {
        cout << "NO";
    }
    return 0;
}