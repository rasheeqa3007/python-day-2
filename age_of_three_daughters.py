
from itertools import combinations_with_replacement
from collections import defaultdict

PRODUCT = 72

# Step 1: Find all combinations with product 72
triples = []
for a, b, c in combinations_with_replacement(range(1, PRODUCT + 1), 3):
    if a * b * c == PRODUCT:
        triples.append((a, b, c))

# Step 2: Group combinations by sum
sum_groups = defaultdict(list)
for t in triples:
    total = sum(t)
    sum_groups[total].append(t)

# Step 3: Keep sums with multiple possibilities
ambiguous = {}
for s, combos in sum_groups.items():
    if len(combos) > 1:
        ambiguous[s] = combos

print("Possible sums with multiple age combinations:")
for s, combos in ambiguous.items():
    print("Sum =", s, "->", combos)

# Step 4: Apply final clue (unique oldest daughter)
print("\nFinal valid ages:")
for s, combos in ambiguous.items():
    for combo in combos:
        ages = sorted(combo)
        # check for one unique oldest
        if ages[2] > ages[1]:
            print(ages)
