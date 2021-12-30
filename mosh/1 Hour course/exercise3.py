weight = float(input("Weight :"))
unit = input('(K)g or (L)bs : ')

if unit.upper()=='K' :
    print('Weight in LBS is :' +str(weight/0.45))
else :
    print('Weight in KG is : ' +str(weight*0.45))