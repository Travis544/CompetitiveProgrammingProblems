#include <vector>
#include <cmath>
#include <limits>
#include <tuple>
#include <bits/stdc++.h>
using namespace std;

// class SegmentTree {
// public:
//     SegmentTree(const vector<int>& array) {
//         size = array.size();
//         tree.resize(4 * size);
//         indexTree.resize(4 * size);
//         build_tree(array, 0, 0, size - 1);
//     }

//     void build_tree(const vector<int>& array, int tree_index, int left, int right) {
//         if (left == right) {
//             tree[tree_index] = array[left];
//             indexTree[tree_index] = left;
//             return;
//         }
//         int mid = (left + right) / 2;
//         build_tree(array, 2 * tree_index + 1, left, mid);
//         build_tree(array, 2 * tree_index + 2, mid + 1, right);
//         tree[tree_index] = min(tree[2 * tree_index + 1], tree[2 * tree_index + 2]);
//         if (tree[2 * tree_index + 1] <= tree[2 * tree_index + 2]) {
//             indexTree[tree_index] = indexTree[2 * tree_index + 1];
//         } else {
//             indexTree[tree_index] = indexTree[2 * tree_index + 2];
//         }
//     }

//     pair<int, int> query(int tree_index, int left, int right, int query_left, int query_right) {
//         if (query_left <= left && right <= query_right) {
//             return make_pair(tree[tree_index], indexTree[tree_index]);
//         }
//         int mid = (left + right) / 2;
//         int min_value = numeric_limits<int>::max();
//         int min_index = -1;
//         if (query_left <= mid) {
//             auto [toCompare, index] = query(2 * tree_index + 1, left, mid, query_left, query_right);
//             tie(min_value, min_index) = min(make_pair(min_value, min_index), make_pair(toCompare, index));
//         }
//         if (query_right > mid) {
//             auto [toCompare, index] = query(2 * tree_index + 2, mid + 1, right, query_left, query_right);
//             tie(min_value, min_index) = min(make_pair(min_value, min_index), make_pair(toCompare, index));
//         }
//         return make_pair(min_value, min_index);
//     }

//     pair<int, int> query_range(int left, int right) {
//         return query(0, 0, size - 1, left, right);
//     }

// private:
//     int size;
//     vector<int> tree;
//     vector<int> indexTree;
// };

#define LEFT(x) (x << 1)
#define RIGHT(x) ((x << 1) + 1)





class SgmtTree {
public:
    int n;
    vector<int> A;
    vector<int> st;

    void build(int p, int L, int R)
    {
        if (L == R) {
            st[p] = L;
        }
        else {
            build(LEFT(p), L, (L + R) / 2);
            build(RIGHT(p), (L + R) / 2 + 1, R);
            int p1 = st[LEFT(p)], p2 = st[RIGHT(p)];
            st[p] = (A[p1] <= A[p2]) ? p1 : p2;
        }
    }

    int rmq(int p, int L, int R, int i, int j)
    {
        if (i > R || j < L) return -1;
        if (L >= i && R <= j) return st[(p)];
        
        int p1 = rmq(LEFT(p), L, (L + R) / 2, i, j);
        int p2 = rmq(RIGHT(p), (L + R) / 2 + 1, R, i, j);

        if (p1 == -1) return p2;
        if (p2 == -1) return p1;

        return (A[p1] <= A[p2]) ? p1 : p2;
    }

    SgmtTree(vector<int>&_A, int _n)
    {
        A = _A;
        n = _n;

        st.assign(4 * n, 0);
        build(1, 0, n - 1);
    }

    void printst(int L, int R, int i) {
        printf("L = %d, R = %d, i = %d, val = %d\n", L, R, i, st[i]);
        if (L == R)
            return;
        printst(L, (L+R)/2, LEFT(i));
        printst((L+R)/2+1, R, RIGHT(i));
    }

    int rmq(int i, int j) { return rmq(1, 0, n - 1, i, j); }
};

void visit(int node, int node_depth, vector<int>& tourIndexToNodes, vector<int>& depth, vector<int>& nodesToTourIndex, int* tour_index) {
    int tourIndex = *(tour_index);
    tourIndexToNodes[tourIndex] = node;
    depth[tourIndex] = node_depth;
    nodesToTourIndex[node] = tourIndex;
    // (*idx)++
    //   cout << "TEST" << endl;
    //   cout << node_depth << endl;
    //   cout << tourIndex << endl;
    //   for (int i = 0; i < depth.size(); i++) {
    //         std::cout << depth[i] << " ";
    //     }
       
       
    *(tour_index) = *(tour_index) +1;
}

// void dfs(int node,  vector<unordered_map<int, bool>>& nodes, vector<int>& tourIndexToNodes, vector<int>& depth, vector<int>& nodesToTourIndex, int node_depth, int* idx) {
    
//     visit(node, node_depth, tourIndexToNodes, depth, nodesToTourIndex, idx);
//     unordered_map<int, bool> myMap = nodes[node];
//     for (auto itr = myMap.begin(); itr != myMap.end(); ++itr) {
//         dfs(itr->first, nodes, tourIndexToNodes, depth, nodesToTourIndex, node_depth + 1, idx);
//         visit(node, node_depth, tourIndexToNodes, depth, nodesToTourIndex, idx);
//     }
    
//     // for (int edge : nodes[node]) {
       
//     // }
// }

void dfs(int cur, int depth, vector<int>& L, vector<int>& E, vector<int>& H, int *idx, vector<unordered_map<int, bool>>& tree)
{
    H[cur] = *idx;
    E[*idx] = cur;
    L[(*idx)++] = depth;
    unordered_map<int, bool> myMap = tree[cur];
    for (auto itr = myMap.begin(); itr != myMap.end(); ++itr)
    {
        dfs(itr->first, depth + 1, L, E, H, idx, tree);
        E[*idx] = cur;
        L[(*idx)++] = depth;
    }
}

void treeify(vector<unordered_map<int, bool>> &tree, int root) {
    for (auto &edge : tree[root]) {
        if (tree[edge.first].count(root)) {
            tree[edge.first].erase(root);
        }
        
        treeify(tree, edge.first);
    }
}

tuple<vector<int>, vector<int>, vector<int>> eulerianTour(int node, vector<unordered_map<int, bool>> nodes, int length) {
    vector<int> tourIndexToNodes((2 * length) - 1);
    vector<int> depth((2 * length) - 1);
    vector<int> nodesToTourIndex(length);
  
    // memset((void*)tourIndexToNodes, -1, ((2 * length) - 1));
    // memset((void*)depth, -1, ((2 * length) - 1));
    // memset((void*)nodesToTourIndex, -1, length);
    int tour_index = 0;
    //int cur, int depth, vector<int>& L, vector<int>& E, vector<int>& H, int *idx, vector<unordered_map<int, bool>>& tree
    dfs(0, 0, depth, tourIndexToNodes, nodesToTourIndex, &tour_index, nodes);
    //dfs(node, nodes, tourIndexToNodes, depth, nodesToTourIndex, 0, &tour_index);
    //   cout << "FIRST" << endl;
    //   for (int i = 0; i < depth.size(); i++) {
    //         std::cout << depth[i] << " ";
    //     }
    return make_tuple(tourIndexToNodes, depth, nodesToTourIndex);
}

int lca(int nodeIndex1, int nodeIndex2, vector<int> &nodesToTourIndex,SgmtTree &st,  vector<int> &tourIndexToNodes) {
    // int tourIndex1 = min(nodesToTourIndex[nodeIndex1], nodesToTourIndex[nodeIndex2]);
    // int tourIndex2 = max(nodesToTourIndex[nodeIndex1], nodesToTourIndex[nodeIndex2]);
    // auto [minValue, minValueIndex] = segmentTree.query_range(tourIndex1, tourIndex2);
    int lo = nodesToTourIndex[nodeIndex1];
    int hi = nodesToTourIndex[nodeIndex2];
    if (!(lo < hi)) {
        int tmp = lo;
        lo = hi;
        hi = tmp;
    }
    // SegmentTree &segmentTree,
    int min = st.rmq(lo, hi);
    return tourIndexToNodes[min];
}

int main() {
    int testCases;
    cin >> testCases;

    for (int i = 0; i < testCases; i++) {
       
        int n;
        cin >> n;
        vector<unordered_map<int, bool>> tree(n);

        for (int j = 0; j < n-1; j++) {
            int fro, to;
            cin >> fro >> to;
            tree[fro-1][to-1] = true;
            tree[to-1][fro-1] = true;
        }

        vector<int> permutation(n);
        for (int k = 0; k < n; k++) {
            int p;
            cin >> p;
            permutation[k] = p-1;
        }
        
        treeify(tree, 0);
        auto et = eulerianTour(0, tree, n);
        auto tourIndexToNodes = get<0>(et);
        auto depth = get<1>(et);
        auto nodesToTourIndex = get<2>(et);

        // SegmentTree segmentTree(depth);
        SgmtTree st(depth, 2*n);
        int flag = 1;
        for (int i = 0, j = 1; j < n; i++, j++) {
            int node1 = permutation[i];
            int node2 = permutation[j];
            int elerianIndex1 = nodesToTourIndex[node1];
            int elerianIndex2 = nodesToTourIndex[node2];
            // segmentTree,
            //int nodeIndex1, int nodeIndex2, vector<int> &nodesToTourIndex, SegmentTree &segmentTree, vector<int> &tourIndexToNodes
            int ca = lca(node1, node2, nodesToTourIndex, st, tourIndexToNodes);
            int ancestorElerianIndex = nodesToTourIndex[ca];
            int distance = (depth[elerianIndex1] + depth[elerianIndex2]) - (2*depth[ancestorElerianIndex]);
            if (distance > 3){
                flag = 0;
                break;
            }
        }

       
        
        // std::cout << "SFIA" << endl;
        // std::cout << depth.size() << endl;
        // for (int i = 0; i < depth.size(); i++) {
        //     std::cout << depth[i] << endl;
        // }
       
    
        cout << flag << endl;
    }
    
    
    return 0;
    
}
            
            
