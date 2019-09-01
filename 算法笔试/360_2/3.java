/*
 * @Descripttion: 
 * @Author: daxiong
 * @Date: 2019-08-31 17:46:16
 * @LastEditors: daxiong
 * @LastEditTime: 2019-08-31 17:46:16
 */;

public class Main {
 
    public static Set<Integer> set = new HashSet<>();
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
 
        int n = in.nextInt(), m = in.nextInt();
        int[] d = new int[m];
        for (int i = 0; i < m; i++) {
            d[i] = in.nextInt();
        }
 
        for (int i = 0; i < n; i++) {
            dfs(d, 0, i, n, i);
        }
        System.out.println(set.size());
    }
 
    private static void dfs(int[] d, int idx, int pos, int n, int fa) {
        if (idx >= d.length && pos >= 0 && pos < n) {
            set.add(pos);
            return;
        }
        if (d[idx] <= pos) {
            dfs(d, idx + 1, pos - d[idx], n, fa);
        }
 
        if (d[idx] <= n - pos - 1) {
            dfs(d, idx + 1, pos + d[idx], n, fa);
        }
    }
}
