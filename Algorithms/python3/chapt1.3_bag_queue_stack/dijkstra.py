# -*- coding: utf-8 -*-
from collections import deque
import math


def evaluate(expression):
    ops = deque()
    vals = deque()
    p = v = ''

    for s in expression:
        if s == ' ':
            continue
        elif s == '(':
            continue
        elif s == '.':
            if '.' not in p:
                p += s
            continue
        else:
            p += s

        if p == '*'     \
            or p == '/' \
            or p == '+' \
            or p == '-' :
            ops.appendleft(p)
            not len(v) or vals.appendleft(float(v))
            p = ''
            v = ''
        elif p == 'sqrt':
            ops.appendleft(p)
            p = ''
        elif p in 'sqrt':
            continue
        elif p == ')':
            p = ''
            operator = ops.popleft()
            val1 = vals.popleft() if len(vals) else None
            # This sentence must be below val1 = vals.popleft() in case that a / b becomes b / a.
            not len(v) or vals.appendleft(float(v))
            v = ''
            print('{0} {1} {2}'.format(val1, operator, vals[0]))
            if operator == '*':
                ret = val1 * vals.popleft()
            elif operator == '/':
                ret = val1 / vals.popleft()
            elif operator == '+':
                ret = val1 + vals.popleft()
            elif operator == '-':
                ret = val1 - vals.popleft()
            else:
                # sqrt
                ret = math.sqrt(vals.popleft())
                val1 is None or vals.appendleft(val1)

            vals.appendleft(ret)
        else:
            v += p
            p = ''

    return vals.popleft()

if __name__ == '__main__':
    expression = input('Enter your expression: ')
    ret = evaluate(expression)
    print('Result is {0}'.format(ret))
