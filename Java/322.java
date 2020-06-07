import java.util.Arrays;

class Solution {
    int minCount = Integer.MAX_VALUE;

    public int coinChange(int[] coins, int amount) {
        Arrays.sort(coins);
        useNext(0, amount, coins, coins.length - 1);
        if (minCount == Integer.MAX_VALUE)
            return -1;
        else
            return minCount;
    }

    private void useNext(int i, int amount, int[] coins, int n) {
        if (amount == 0) {
            if (i < minCount)
                minCount = i;
            return;
        }
        if (n == -1 || amount / coins[n] + i >= minCount)
            return;
        for (int j = amount / coins[n]; j >= 0; j--) {
            useNext(i + j, amount - coins[n] * j, coins, n - 1);
        }
    }
}