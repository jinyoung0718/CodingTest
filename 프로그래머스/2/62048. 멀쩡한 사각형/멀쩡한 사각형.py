import math

def solution(W, H):
    return W * H - (W + H - math.gcd(W, H))
