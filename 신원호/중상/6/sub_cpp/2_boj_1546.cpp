#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<float> scores(N);
    for (int i = 0; i < N; i++) {
        int score;
        cin >> score;
        scores[i] = score;
    }
    int max_score = *max_element(scores.begin(), scores.end());
    for (int i = 0; i < N; i++) {
        scores[i] = scores[i] / max_score * 100;
    }
    double result = accumulate(scores.begin(), scores.end(), 0.0f) / scores.size();
    cout << result;
    return 0;
}