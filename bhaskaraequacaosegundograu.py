import math

##########################################################  
print("#################################################")
valorA = float(input("insira o valor de A: "))
valorB = float(input("insira o valor de B: "))
valorC = float(input("insira o valor de C: "))
#calculando delta##########################################
print("#################################################")
print("Calculando Δ (B^2-4*a*c)")
print("\n")
print("Δ=","(%s^2)-4*(%s*%s)"%(valorB, valorA, valorC))
print("\n")
delta = ((valorB**2)-(4*(valorA*valorC)))
###########################################################
##printando delta e dizendo se é >0########################
print("Δ=",delta)
print("#################################################")
if delta < 0:
    print("nao ha raizes reais")
    print("#################################################")
###########################################################
##calculando X se delta for > 0############################
if delta >=0:
    valorXpos = ((-valorB+ math.sqrt(delta))/(2*valorA))
    print("calculando X' ((-B+√Δ)/(2A)")
    print("\n")
    print("X'=(%s*-1)+√Δ/(2*%s)"%(valorB,valorA))
    print("\n")
    print("X'=(%s*-1)+(%s)/(2*%s)"%(valorB, math.sqrt(delta), valorA))
    print("\n")
    print("X'=",valorXpos)
    print("#################################################")
    valorXneg = ((-valorB- math.sqrt(delta))/(2*valorA))
    print("\ncalculando X'' ((-B-√Δ)/(2A)")
    print("\n")
    print("X''=(%s*-1)-√Δ/(2*%s)"%(valorB,valorA))
    print("\n")
    print("X''=(%s*-1)-(%s)/(2*%s)"%(valorB, math.sqrt(delta), valorA))
    print("\n")
    print("X''=",valorXneg)
    print("#################################################")