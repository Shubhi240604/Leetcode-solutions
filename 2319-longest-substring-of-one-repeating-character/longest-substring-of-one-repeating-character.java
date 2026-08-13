class Solution {

    char[] s;
    int[] left, right, best, len;
    char[] lc, rc;

    void build(int idx, int l, int r) {
        if (l == r) {
            left[idx] = right[idx] = best[idx] = len[idx] = 1;
            lc[idx] = rc[idx] = s[l];
            return;
        }

        int mid = (l + r) >> 1;

        build(idx << 1, l, mid);
        build(idx << 1 | 1, mid + 1, r);

        merge(idx);
    }

    void merge(int idx) {
        int a = idx << 1;
        int b = a | 1;

        lc[idx] = lc[a];
        rc[idx] = rc[b];

        len[idx] = len[a] + len[b];

        // Prefix
        left[idx] = left[a];

        if (left[a] == len[a] && rc[a] == lc[b]) {
            left[idx] += left[b];
        }

        // Suffix
        right[idx] = right[b];

        if (right[b] == len[b] && rc[a] == lc[b]) {
            right[idx] += right[a];
        }

        // Best
        best[idx] = Math.max(best[a], best[b]);

        if (rc[a] == lc[b]) {
            best[idx] = Math.max(
                best[idx],
                right[a] + left[b]
            );
        }
    }

    void update(int idx, int l, int r, int pos, char ch) {

        if (l == r) {
            lc[idx] = rc[idx] = ch;
            left[idx] = right[idx] = best[idx] = 1;
            return;
        }

        int mid = (l + r) >> 1;

        if (pos <= mid) {
            update(idx << 1, l, mid, pos, ch);
        } else {
            update(idx << 1 | 1, mid + 1, r, pos, ch);
        }

        merge(idx);
    }

    public int[] longestRepeating(
            String str,
            String queryCharacters,
            int[] queryIndices) {

        int n = str.length();

        s = str.toCharArray();

        int size = 4 * n + 5;

        left = new int[size];
        right = new int[size];
        best = new int[size];
        len = new int[size];

        lc = new char[size];
        rc = new char[size];

        build(1, 0, n - 1);

        int q = queryIndices.length;
        int[] ans = new int[q];

        for (int i = 0; i < q; i++) {

            update(
                1,
                0,
                n - 1,
                queryIndices[i],
                queryCharacters.charAt(i)
            );

            ans[i] = best[1];
        }

        return ans;
    }
}