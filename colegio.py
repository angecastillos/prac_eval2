print("Bienvenido colegio Republica de Chillan")
print('''
      Indique concepto a pagar::
      1) matricula Básica 
      2) matricula Media
      ''')
opcion = int(input("Seleccione:"))
matricula=0
if opcion == 1:
    matricula= 45000
elif opcion == 2:
    matricula = 67000
else:
    print("No registra matricula")
opcion2 = input("Pagara Centro de Padres (S/N):").upper()
centro_padres =0
if opcion2 == "S":
    centro_padres= 10000
    print("Usted pagara $10.000 pesos por concepto de centro de padres")
opcion3= input("Pagara Mensualidades (S/N):").upper()
mensualidades = 0
descuento=0
if opcion3 =="S":
    cantidad = int(input("Cuantas pagara? (1-12):"))
    mensualidades= 30000*cantidad
    if cantidad>= 3 and cantidad<=5:
        descuento = mensualidades*0.06
        print(f"Tendra un descuentro de 6%: {descuento}")
    elif cantidad>5 and cantidad<= 11:
        descuento=mensualidades*0.1
        print(f"Tendra un descuento de 10%: {descuento}")
    elif cantidad==12 and opcion2 == "S" and (opcion == 1 or opcion == 2):
        descuento = mensualidades*0.20
        print(f"Apoderado full, descuento {descuento}")
    elif cantidad == 12:
        descuento = mensualidades*0.1
        print(f"Tendra un descuento de 10% : {descuento}")
    else:
        print("No posee descuento")
        descuento=0
    print(f"Pagara en mensualidad: {mensualidades-descuento}")
total = (mensualidades-descuento) + centro_padres + matricula
print(f"Total : {total}")
