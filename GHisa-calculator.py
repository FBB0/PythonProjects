import math
print("***ISA calculator***")
print("1. Calculate ISA for altitude in meters")
print("2. Calculate ISA for altitude in feet")
print("3. Calculate ISA for altitude in FL")
choice = int(input("Enter your choice: "))

if choice == 1:
    h= int(input("What is the altitude in meters? "))
    print(h)
if choice == 2:
    a= int(input("What is the altitude in feet? "))
    h= a*0.3048
    print(h)
if choice == 3:
    a= int(input("What is the altitude in FL? "))
    h= a*100*0.3048
    print(h) 

T = input("Do you want to define a different sea level temperature?, if not press enter otherwise type'yes'")
if T == "yes":
    T0=int(input("Enter sea level temperature?"))
else :
    T0=288.15
#pressure, gravity acceleration at h = 0.
P0=101325
g0=9.80665
R=287

T2=T0+-0.0065*11000
P2= P0*(T2/T0)**(-g0/-0.0065/R)

T4=T2
P4=P2*math.exp((-g0/T2/R*(20000-11000)))

T6=T4+0.001*(32000-20000)
P6= P4*(T6/T4)**(-g0/0.001/R)

T8=T6+0.0028*(47000-32000)
P8= P6*(T8/T6)**(-g0/0.0028/R)

T10=T8
P10=P8*math.exp((-g0/T10/R*(51000-47000)))

T12=T8-0.0028*(71000-51000)
P12=P10*(T12/T10)**(-g0/-0.0028/R)

#The different levels of the atmosphere
if h<=11000:
    a=-0.0065
    T1=T0+a*h
    P1 = P0*(T1/T0)**(-g0/a/R)  
if 11000<h<=20000:
    T1 = T2
    a= 0
    P1 = P2*math.exp((-g0/T1/R*(h-11000)))
if 20000<h<=32000:
    a = 0.001
    T1=T4+a*(h-20000)
    P1 = P4*(T1/T4)**(-g0/a/R)
if 32000<h<=47000:
    a=0.0028
    T1 = T6+a*(h-32000)
    P1 = P6*(T1/T6)**(-g0/a/R)
if 47000<h<=51000:
    T1 = T8
    a = 0
    P1= P8*math.exp((-g0/T1/R*(h-47000)))
if 51000<h<=71000:
    a=-0.0028
    T1=T10+a*(h-51000)
    P1 = P10*(T1/T10)**(-g0/a/R)
if 71000<h<=86000:
    a=-0.002
    T1= T12+a*(h-71000)
    P1 = P12*(T1/T12)**(-g0/a/R)

if 0<=h<=86000:
    rho = P1/R/T1
    print("Temperature: "+ str(T1)+" K ("+str(T1-273.15)+"'C)")
    print("Pressure : "+str(P1)+" Pa ("+str(P1/P0*100)+" % SL)")
    print("Density : "+str(rho)+" Pa ("+str(rho/1.225*100)+" % SL)")

if h>86000:
    print("Sorry, I can only do altitudes up to 86000[m], you're way too high!")
if h<0:
    print("Sorry, I don't go negative!")

dummy = input("Press enter to end the ISA calculator")