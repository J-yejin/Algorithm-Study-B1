#include <iostream>
#include <string>

using namespace std;

int main() {
    int cnt[10] = {0};
    int a, b, c;
    cin >> a >> b >> c;
    string S = to_string(a * b * c);
    for (int i = 0; i < S.length(); i++) {
        cnt[S[i] - '0'] += 1;
    }
    for (int result : cnt) {
        cout << result << "\n";
    }
    return 0;
}