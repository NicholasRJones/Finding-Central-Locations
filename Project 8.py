import numpy as np
from Optimization.Algorithm import classy as cl, geneticalg as ga, neldermead as nm


def psuedoinverse(input, para, p):
    return


def constraintviolation(input, para, p):
    B = np.array(para.parameter).reshape((len(para.parameter), len(para.parameter[0])))
    x = np.array(input)
    d = np.array(para.data)
    r = np.matmul(B, x) - d
    f = 1 / 2 * (r ** 2).sum()
    return f


def nonzero(input):
    if np.linalg.norm(np.array(input) - np.array([29, 11])) > 10:
        return False
    else:
        return True


input = [29, 11]

b1 = [np.tan(-5 / 180 * np.pi), -1]
b2 = [np.tan(6 / 180 * np.pi), -1]
b3 = [np.tan(15 / 180 * np.pi), -1]
b4 = [np.tan(27 / 180 * np.pi), -1]
B = [b1 / np.linalg.norm(b1),
     b2 / np.linalg.norm(b2),
     b3 / np.linalg.norm(b3),
     b4 / np.linalg.norm(b4)]

d = [(10 * np.tan(-5 / 180 * np.pi) - 12) / np.linalg.norm(b1),
     (3 * np.tan(6 / 180 * np.pi) - 9) / np.linalg.norm(b2),
     (2 * np.tan(15 / 180 * np.pi) - 3) / np.linalg.norm(b3),
     (8 * np.tan(27 / 180 * np.pi) - 1) / np.linalg.norm(b4)]


# print(sc.linalg.solve(np.array(B).reshape((4, 2)), np.array(d).reshape((4, 1))))

para = cl.para(0.0001, 0.19, d, B, 0, nonzero, 0)
pr = cl.funct(constraintviolation, 'min', '', input, para, 1000)

ga.genetic(pr)
# print(np.linalg.lstsq(B, d))
