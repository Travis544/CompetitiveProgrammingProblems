import java.util.*;


public class Pipes {
    static class Drop {
        int d;
        int u;
        public Drop(int d, int u) { this.d = d; this.u = u; }
        public Drop min(Drop other) {
            if (d < other.d) return this;
            else if (d == other.d) return u < other.u ? this : other;
            else return other;
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();
        int[] F = new int[n];
        int[] group = new int[n];
        LinkedList<Integer> children[] = new LinkedList[n];

        for (int i = 0; i < n; i++) {
            F[i] = scan.nextInt();
            children[i] = new LinkedList<>();
        }

        int rootcount = 0;
        for (int i = 0; i < n; i++) {
            int fi = F[i];
            if (fi != -1)
                children[fi].add(i);
            else
                group[i] = ++rootcount;
        }

        int[] bestdrops = new int[rootcount + 1];
        boolean[] visited = new boolean[n];

        for (int i = 0; i < n; i++) {
            if (visited[i] || group[i] == 0) 
                continue;

            LinkedList<Drop> bfs = new LinkedList<Drop>();
            bfs.add(new Drop(0, i));
            visited[i] = true;
            Drop bestdrop = new Drop(n, n);
            
            while (bfs.size() > 0) {
                Drop curr = bfs.removeFirst();
                if (children[curr.u].size() == 0) {
                    bestdrop =  bestdrop.min(curr);
                }

                for (int c : children[curr.u]) {
                    if (!visited[c]) {
                        group[c] = group[i];
                        visited[c] = true;
                        bfs.add(new Drop(curr.d + 1, c));
                    }
                }
            }

            bestdrops[group[i]] = bestdrop.u;
        }

        StringBuilder sb = new StringBuilder();
        int q = scan.nextInt();
        for (int i = 0; i < q; i++) {
            int s = scan.nextInt();
            sb.append(bestdrops[group[s]] + "\n");
        }
        System.out.print(sb.toString());
    }
}
