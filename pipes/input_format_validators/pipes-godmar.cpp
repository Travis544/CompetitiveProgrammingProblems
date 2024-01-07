/**
 * Verify that all entry points are leaves.
 * @author godmar
 */
#include <bits/stdc++.h>
using namespace std;

int
main()
{
    int n, q;
    cin >> n;
    vector<vector<int>> children(n);

    for (int i = 0; i < n; i++) {
        int fi;
        cin >> fi;
        if (fi != -1) {
            children[fi].push_back(i);
        }
    }

    cin >> q;
    for (int i = 0; i < q; i++) {
        int s;
        cin >> s;
        if (children[s].size() > 0) {
            cerr << "Query: " << s << " is an interior node" << endl;
            return 43;
        }
    }
    return 42;
}
