def get_combination_counts(amount):
    coins = [1, 2, 5, 10, 25, 50]
    dp = [None] * (amount + 1)
    dp[0] = {}

    for w in range(1, amount + 1):
        for coin in sorted(coins, reverse=True):
            if w - coin >= 0 and dp[w - coin] is not None:
                new_combo = dp[w - coin].copy()
                new_combo[coin] = new_combo.get(coin, 0) + 1
                dp[w] = new_combo
                break
    return dp[amount] or {}

if __name__ == "__main__":
    print(get_combination_counts(129))
