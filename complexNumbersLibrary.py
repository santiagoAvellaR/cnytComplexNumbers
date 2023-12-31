import math
def sumCmplx(c1, c2):
    return (round(c1[0] + c2[0],2), round(c1[1] + c2[1],2))

def restCmplx(c1, c2):
    return (round(c1[0] - c2[0],2), round(c1[1] - c2[1],2))

def multiCmplx(c1, c2):
    return (round(c1[0]*c2[0] - c1[1]*c2[1],2), round(c1[1]*c2[0] + c1[0]*c2[1],2))
def divCmplx(c1, c2):
    deno = round(pow(c1[1], 2) + pow(c2[1], 2),2)
    return ( round((c1[0]*c2[0] + c1[1]*c2[1]) / deno,2), round((c2[0]*c1[1] - c1[0]*c2[1]) / deno,2))

def modCmplx(cplx):
    return round(math.sqrt(pow(cplx[0], 2) + pow(cplx[1], 2)),2)

def conjCmplx(cplx):
    return (cplx[0], -1 * cplx[1])

def phaseCmplx(cplx):
    return round(math.atan2(cplx[1], cplx[0]),2)

def polarCmplx(c1):
    return (modCmplx(c1), phaseCmplx(c1))

def cartCmplx(cplx):
    return (cplx[0] * math.cos(cplx[1]), cplx[0] * math.sin(cplx[1]))

# libreria unittest python
# assert almost equal - no recibe tuplas
# para archivos ocultos, empiezan por punto (.) - .gitignore