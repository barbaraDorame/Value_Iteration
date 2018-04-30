import math


def legal_actions(s):
    return [x for x in range(0, s+1)]

def terminal(state):
    if state >= 100:
        return True
    else:
        return False

def p(s, r, a, primas, ph):
    if s+a == primas:
        return ph
    elif s-a == primas:
        return 1 - ph
    else:
        return 0

def r(primas):
    return 0 if primas < 100 else 1

def value_iteration(gamma, ph, theta):
    v = [0 for i in range(0, 101)]
    while(True):
        delta = 0
        for s in range(0 ,100):
            x = v[s]
            v[s] = max(sum(p(s, r(primas), a, primas, ph) *
                           (r(primas) + gamma*v[primas])
                           for primas in range(0, 101))
                       for a in legal_actions(s))
            delta = max(delta, abs(x - v[s]))
        if delta < theta:
            break
    return [max(legal_actions(s),
                key=lambda x: sum(p(s, r(primas), x, primas, ph)*
                                  (r(primas) + gamma*v[primas])
                                  for primas in range(0, 101)))
            for s in range(0, 100)]

print("ph = 0.25 ", value_iteration(0.2, 0.25, 0.0000001))
print("ph = 0.55 ", value_iteration(0.5, 0.55, 0.0000001))
