#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int arr[9];
    for (int i = 0; i < 9; i++) {
        cin >> arr[i];
    }
    int max_val = *max_element(begin(arr), end(arr));
    int max_idx = max_element(begin(arr), end(arr)) - begin(arr) + 1;
    cout << max_val << "\n" << max_idx;
}