/**
 * What if found the forward chain for every query?
 * @author godmar
 */
#include <bits/stdc++.h>
using namespace std;

int
main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    cin >> n;
    vector<int> group(n);
    vector<vector<int>> children(n);
    vector<int> F(n);

    int rootcount = 0;
    for (int i = 0; i < n; i++) {
        int fi;
        cin >> fi;
        F[i] = fi;
        if (fi != -1) {
            children[fi].push_back(i);
        } else {
            group[i] = ++rootcount;
        }
    }

    vector<int> bestdrops(rootcount+1);
    vector<bool> visited(n);
    for (int i = 0; i < n; i++) {
        if (visited[i] || group[i] == 0) continue;
        queue<pair<int, int>> bfs;
        bfs.emplace(0, i);
        visited[i] = true;
        pair<int, int> bestdrop { n, n };
        while (bfs.size() > 0) {
            pair<int, int> s = bfs.front();
            int d = s.first;
            int u = s.second;
            bfs.pop();
            if (children[u].size() == 0) {
                bestdrop = min(bestdrop, s);
            }
            for (int c : children[u]) {
                if (visited[c] == false) {
                    group[c] = group[i];
                    visited[c] = true;
                    bfs.push({ d + 1, c });
                }
            }
        }
        bestdrops[group[i]] = bestdrop.second;
    }

    cin >> q;
    for (int i = 0; i < q; i++) {
        int s;
        cin >> s;
        // traverse forward chain every time for every query
        while (F[s] != -1)
            s = F[s];

        cout << bestdrops[group[s]] << '\n';
    }
}
