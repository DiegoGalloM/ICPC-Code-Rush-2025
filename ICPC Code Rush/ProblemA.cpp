#include<bits/stdc++.h>

using namespace std;

struct ProductData {
    set<long long> materials;
    set<long long> submaterials;
};

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    //Creación del mapa
    map <long long,  map <long long, set <long long>>> summary;

    for (int i = 0; i < n; i++){
        long long a, b, c;
        cin >> a >> b >> c;
    

        summary[a][b].insert(c);

    }

    for (const auto& product_entry:summary){
        long long product_id = product_entry.first;
        const map <long long, set<long long>>& materials_map = product_entry.second; 

        long long distinct_materials = materials_map.size();
        long long distinct_submaterials = 0;

        for (const auto& materials_entry : materials_map){
            distinct_submaterials += materials_entry.second.size();
        }

        cout << product_id << " " << distinct_materials << " " << distinct_submaterials << "\n";
    }


    return 0;
}