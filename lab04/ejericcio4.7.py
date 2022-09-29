def calcularScore(score):
    if(score > 0.9 and score <= 1.0): 
        grade = "A"
    elif(score > 0.8 and score < 0.9):
        grade = "B"
    elif(score > 0.7 and score < 0.8):
        grade = "C"
    elif(score > 0.6 and score < 0.7):
        grade = "D"
    elif(score < 0 and score < 0.6): 
        grade = "F"
    else:
        grade = "Score no es valido"
    return grade
try:
    score = float(input("Ingrese su score (0.1 - 1.00): "))
    grade = calcularScore(score)
except: 
    print("Error, debe ingrsar un valor numerico")
