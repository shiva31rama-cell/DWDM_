from itertools import combinations

transactions = [
    {"milk", "bread", "eggs"},
    {"milk", "bread"},
    {"milk", "eggs"},
    {"bread", "eggs"},
    {"milk", "bread", "eggs"},
]
MIN_SUPPORT = 0.6
MIN_CONFIDENCE = 0.7

def support(itemset):
    return sum(itemset.issubset(t) for t in transactions) / len(transactions)

def apriori():
    items = sorted(set().union(*transactions))
    current = [frozenset([x]) for x in items]
    frequent = {}

    while current:
        accepted = []
        for itemset in current:
            if support(itemset) >= MIN_SUPPORT:
                frequent[itemset] = support(itemset)
                accepted.append(itemset)

        next_candidates = set()
        for a, b in combinations(accepted, 2):
            union = a | b
            if len(union) == len(a) + 1:
                next_candidates.add(union)
        current = list(next_candidates)
    return frequent

def print_rules(frequent):
    for itemset, sup in frequent.items():
        if len(itemset) < 2:
            continue
        for r in range(1, len(itemset)):
            for left_tuple in combinations(itemset, r):
                left = frozenset(left_tuple)
                right = itemset - left
                confidence = sup / support(left)
                if confidence >= MIN_CONFIDENCE:
                    print(f"{set(left)} -> {set(right)} | support={sup:.2f}, confidence={confidence:.2f}")

freq = apriori()
print("Frequent itemsets:")
for itemset, sup in sorted(freq.items(), key=lambda x: (len(x[0]), sorted(x[0]))):
    print(set(itemset), f"support={sup:.2f}")

print("\nStrong association rules:")
print_rules(freq)