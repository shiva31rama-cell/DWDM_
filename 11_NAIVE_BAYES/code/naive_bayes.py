from collections import Counter, defaultdict

data = [
    (("sunny", "hot"), "no"),
    (("sunny", "cool"), "yes"),
    (("rainy", "cool"), "yes"),
    (("rainy", "hot"), "yes"),
    (("cloudy", "hot"), "yes"),
    (("cloudy", "cool"), "yes"),
]

def train(rows):
    class_counts = Counter(label for _, label in rows)
    value_counts = defaultdict(Counter)
    for features, label in rows:
        for i, value in enumerate(features):
            value_counts[(i, label)][value] += 1
    return class_counts, value_counts

def predict(features, rows):
    class_counts, value_counts = train(rows)
    total = len(rows)
    best_class, best_probability = None, -1

    for label in class_counts:
        probability = class_counts[label] / total
        for i, value in enumerate(features):
            probability *= (value_counts[(i, label)][value] + 1) / (class_counts[label] + 2)
        if probability > best_probability:
            best_class, best_probability = label, probability
    return best_class

test = ("rainy", "hot")
print("Test instance:", test)
print("Predicted class:", predict(test, data))