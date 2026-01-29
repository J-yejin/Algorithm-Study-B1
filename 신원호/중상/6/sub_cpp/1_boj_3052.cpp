#include <iostream>
#include <unordered_set>

using namespace std;

int main() {
    unordered_set<int> mod;
    for (int i = 0; i < 10; i++) {
        int num;
        cin >> num;
        mod.insert(num % 42);
    }
    cout << mod.size();
    return 0;
}