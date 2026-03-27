import math

w1, w2 = "night", "nacht"

def jaccard(a,b):
    return len(set(a)&set(b)) / len(set(a)|set(b))

def cosine(a,b):
    c = set(a+b)
    v1 = [a.count(x) for x in c]
    v2 = [b.count(x) for x in c]
    return sum(x*y for x,y in zip(v1,v2)) / \
           (math.sqrt(sum(x*x for x in v1)) * math.sqrt(sum(y*y for y in v2)))

def euclidean(a,b):
    c = set(a+b)
    return math.sqrt(sum((a.count(x)-b.count(x))**2 for x in c))

def edit(a,b):
    if not a: return len(b)
    if not b: return len(a)
    if a[0]==b[0]: return edit(a[1:],b[1:])
    return 1+min(edit(a[1:],b), edit(a,b[1:]), edit(a[1:],b[1:]))

print("Jaccard:", jaccard(w1,w2))
print("Cosine:", cosine(w1,w2))
print("Euclidean:", euclidean(w1,w2))
print("Edit Distance:", edit(w1,w2))