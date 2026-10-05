import math

A = [1, 2, 3, 4]
B = [2, 3, 4, 5]

def euclidean(a, b):
    return math.sqrt(sum((x-y)**2 for x, y in zip(a, b)))

def manhattan(a, b):
    return sum(abs(x-y) for x, y in zip(a, b))

def cosine(a, b):
    dot = sum(x*y for x, y in zip(a, b))
    na = math.sqrt(sum(x*x for x in a))
    nb = math.sqrt(sum(y*y for y in b))
    return dot / (na * nb)

def pearson(a, b):
    ma, mb = sum(a)/len(a), sum(b)/len(b)
    num = sum((x-ma)*(y-mb) for x, y in zip(a, b))
    den = math.sqrt(sum((x-ma)**2 for x in a) * sum((y-mb)**2 for y in b))
    return num / den

def jaccard(a, b):
    sa, sb = set(a), set(b)
    return len(sa & sb) / len(sa | sb)

print("Euclidean distance:", euclidean(A, B))
print("Manhattan distance:", manhattan(A, B))
print("Cosine similarity:", cosine(A, B))
print("Pearson correlation:", pearson(A, B))
print("Jaccard similarity:", jaccard(A, B))