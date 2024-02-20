from collections import deque

def Palindrom(p):

    p_string = ''.join(ch.lower() for ch in p if ch.isalpha())

    deque_p = deque(p_string)

    while len(deque_p) > 1:
    
        if deque_p.popleft() != deque_p.pop():

            return False
    
    return True

p = 'Madam in Eden Im Adam'


print(Palindrom(p))




