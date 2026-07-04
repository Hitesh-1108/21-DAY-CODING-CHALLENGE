#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
private:
    vector<int> parent;

    int find(int x) {
        if (parent[x] == x) {
            return x;
        }
        // Path compression
        return parent[x] = find(parent[x]);
    }

    void unionNodes(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
        }
    }

public:
    int minScore(int n, vector<vector<int>>& roads) {
        // Initialize parent array where each node is its own parent
        parent.resize(n + 1);
        for (int i = 0; i <= n; ++i) {
            parent[i] = i;
        }

        // 1. Connect all components based on the roads
        for (const auto& road : roads) {
            unionNodes(road[0], road[1]);
        }

        // 2. Find the root representative of the component containing city 1
        int root1 = find(1);
        int ans = INT_MAX;

        // 3. Find the minimum road score in city 1's component
        for (const auto& road : roads) {
            if (find(road[0]) == root1) {
                ans = min(ans, road[2]);
            }
        }

        return ans;
    }
};