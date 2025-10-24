price_per_1spin = 1500
price_per_10spins = 13500
free_spins = 3

expected_per_spin = 5 * 0.0437 + 1 * 0.3281  # = 0.5466

thresholds_rewards = {
    5: 5,
    15: 10,
    35: 20,
    70: 30,
    120: 50,
}

thresholds_costs = {
    5: price_per_1spin * (5 - free_spins),
    15: price_per_10spins + price_per_1spin * (15 - 10 - free_spins),
    35: price_per_10spins * 3 + price_per_1spin * (35 - 30 - free_spins),
    70: (price_per_10spins - 1500) * free_spins + price_per_10spins * (7 - free_spins),
    120: (price_per_10spins - 1500) * free_spins
    + price_per_10spins * (12 - free_spins),
}

thresholds_expected = {}
for k in thresholds_rewards:
    thresholds_expected[k] = 0
    for s, r in thresholds_rewards.items():
        if s <= k:
            thresholds_expected[k] += r
    thresholds_expected[k] += expected_per_spin * k

thresholds_efficiency = {
    k: thresholds_costs[k] / thresholds_expected[k] for k in thresholds_rewards
}

for k in thresholds_rewards:
    print(
        f"x{k} spins: {thresholds_expected[k]:.2f} shards for {thresholds_costs[k]} gems ({thresholds_efficiency[k]:.1f} gem/shards)"
    )
