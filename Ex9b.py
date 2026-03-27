import math

model = {
    "king":[0.8,0.7,0.6], "queen":[0.82,0.72,0.59],
    "car":[0.2,0.9,0.4], "automobile":[0.21,0.88,0.39],
    "cat":[0.5,0.3,0.9], "dog":[0.48,0.28,0.85]
}

def cosine(a,b):
    return sum(x*y for x,y in zip(a,b)) / (
        math.sqrt(sum(x*x for x in a)) *
        math.sqrt(sum(y*y for y in b))
    )

for w1,w2 in [("king","queen"),("car","automobile"),("cat","dog")]:
    print(w1,"-",w2,":",cosine(model[w1],model[w2]))