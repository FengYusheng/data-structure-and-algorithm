# -*- coding: utf-8 -*-
from collections import deque
import math


class Caculater():
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self):
        ops = deque()
        vals = deque()
        p = v = ''

        for s in self.expression:
            if ' ' == s or '(' == s:
                continue
            elif '.' not in p and '.' == s:
                p += s
            else:
                p += s

            if '+' == p   \
              or '-' == p \
              or '*' == p \
              or '/' == p:
                ops.appendleft(p)
                not len(v) or vals.appendleft(float(v))
                p = v = ''
            elif 'sqrt' == p:
                ops.appendleft(p)
                p = ''
            elif p in 'sqrt':
                continue
            elif ')' == p:
                # The new factor needs to be pushed into vals stack first.
                not len(v) or vals.appendleft(float(v))
                p = v = ''
                operator = ops.popleft()
                if '+' == operator:
                    factor1 = vals.popleft()
                    ret = factor1 + vals.popleft()
                elif '-' == operator:
                    factor1 =vals.popleft()
                    # The second factor is pushed first.
                    ret = vals.popleft() - factor1
                elif '*' == operator:
                    factor1 = vals.popleft()
                    ret = factor1 * vals.popleft()
                elif '/' == operator:
                    factor1 = vals.popleft()
                    ret = vals.popleft() / factor1
                elif 'sqrt' == operator:
                    factor1 = vals.popleft()
                    ret = math.sqrt(factor1)
                else:
                    print('Unkown operator {0}'.format(operator))
                    ret = None

                ret is None or vals.appendleft(ret)
            else:
                v += p
                p = ''

        return vals.popleft()

    def __call__(self):
        print(self.evaluate())


if __name__ == '__main__':
    expression = input('Enter your expression: ')
    cal = Caculater(expression)
    print('Result is {0}'.format(cal.evaluate()))
