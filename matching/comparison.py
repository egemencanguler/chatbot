import math
def cosine_similarity(vec1, vec2):
    dot = sum(x * y for x, y in zip(vec1, vec2))
    mag1 = math.sqrt(sum(x * x for x in vec1))
    mag2 = math.sqrt(sum(y * y for y in vec2))
    div = mag1 * mag2
    if div == 0:
        return 0
    return dot / div

def jaccard_index(vec1, vec2):
    set1 = set(vec1)
    set2 = set(vec2)
    return len(set1.intersection(set2)) / float(len(set1.union(set2)))