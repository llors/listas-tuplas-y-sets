#OPERACION1 "CREACION"
#   EJERCICIOS DE CREACION
#ejercicio 1
gino={1,2,3,4,5,6,7,8}
print(gino)
#ejercicio 2
tol={"A","B","C","D"}
print(tol)
#ejercicio 3
ani={"cuy","chivo","chancho"}
print(ani)
#ejercicio 4
vocales={"a","e","i","o","u"}
print(vocales)
#ejercicio 5
frutas={"uva","papaya","mandarina","guava"}
print(frutas)
#ejercicio 6
paises={"peru","brazil","inglaterra","suisa"}
print(paises)
#ejercicio 7
capital={"lima","buenos aires"}
print(capital)
#ejercicio 8
provincia={"lambayeque","ferreñafe"}
print(provincia)
#ejercicio 9
universidad={"unprg"}
print(universidad)
#ejercicio 10
letras={"A","B","C","D"}
print(letras)

# EJERCICIOS CON PERTENENCIA
#ejercicio 1
let={"l","a","y"}
print("l" in let)
#ejercicio 2
universidad={"unprg"}
print("ini" not in universidad)
#ejercicio 3
frutas={"uva","papaya","mandarina","guava"}
print("papaya" in frutas)
#ejercicio 4
paises={"peru","brazil","inglaterra","suisa"}
print("lima" not in paises)
#ejercicio 5
fr={"uva","papaya","mandarina","guava"}
print("zandia" in fr)
#ejercicio 6
ani={"cuy","chivo","chancho"}
print("raton" not in ani)
#ejercicio 7
ani={"cuy","chivo","chancho"}
print("ardilla" in ani)
#ejercicio 8
capital={"peru","brazil","inglaterra","suisa"}
print("lima" not in capital)
#ejercicio 9
vocales={"a","e","i","o","u"}
print("x" in vocales)
#ejerccio 10
paises={"peru","brazil","inglaterra","suisa"}
print("francia" not in paises)

#OPERACION 3 "COMPARACION
#Ejercicio 1
st1={1,2,3,4,5}
st2={"hola","como","estan","cuentame","algo"}
print(st1==st2)
#ejercicio 2
st1={1,2}
st2={"hola","como","estan"}
print(st2>st1)
#ejercicio 3
st3={1,23,4,5,6,7,8}
st2={"hola"}
print(st3>st2)
#ejercicio 4
st3={1,23,4,5,6,7,8}
st4={"hola"}
print(st3!=st4)
#ejercicio 5
st5={"h","o","l","a"}
st6={"h","o","l","a"}
print(st5==st6)
#ejercicio 6
st7={"h","o","l","a"}
st8={"h","o","l","a"}
print(st7!=st8)
#ejercicio 7
st10={1,2,3,4,5}
st6={"h","o","l","a"}
print(st10!=st6)
#ejercicio 8
st2={"h","o","l","a"}
st8={"gino","bances"}
print(st2>st8)
#ejercicio 9
st5={"a","e","i","o"}
st9={"h","o","l","a"}
print(st9!=st5)
#ejercicio 10
st10={"hola","oli","lote","avion"}
st9={"hhhh","oso","lote","avion"}
print(st10==st9)

#OPERACION4 "LONGITUD":
#Ejercicio 1
st={2,3,4,5}
print(len(st))
#Ejercicio 2
st2={"manzana","platano","uva","cerezza"}
print(len(st2))
#Ejercicio 3
st4={"a","b","c","d"}
print(len(st4))
#Ejercicio 4
st5={"oso","pantera"}
print(len(st5))
#Ejercicio 5
st0={"papa","hijos","tios"}
print(len(st0))
#Ejercicio 6
st17={"abismado","visitudes","funesto","enteco"}
print(len(st17))
#Ejercicio 7
st8={"camara","tablet","telivisor"}
print(len(st8))
#Ejercicio 8
anio={2017,2019,2020,2015,2016}
print(len(anio))
#Ejercicio 9
profesion={"ingeniero","periodista","enfermero","docente"}
print(len(profesion))
#Ejercicio 10
empresas={"gloria","odebrect"}
print(len(empresas))

#OPERACION  CON  "ITERACION"
#ejercicio 1
for GINO in st1:
    print(GINO)
#ejercicio 2
for BANCES in st2:
    print(BANCES)
#ejercicio 3
for LLORS in st3:
    print(LLORS)
#ejercicio 4
for AMOR in st4:
    print(AMOR)
#ejercicio 5
for LIBRE in st5:
    print(LIBRE)
#ejercicio 6
for JESUS in st6:
    print(JESUS)
#ejercicio 7
for TU in st7:
    print(TU)
# ejercicio 8
for PROGRAMACIOM in st8:
    print(PROGRAMACIOM)
#ejercicio 9
for MATEMATICA in st9:
    print(MATEMATICA)
#ejercicio 10
for ARCHIVO in st10:
    print(ARCHIVO)

#OPERACION  CON  "MAX Y MIN"
#Ejercicio 1
st0={"papa","hijos","tios"}
p=max(st0)
print(p)
#Ejercicio 2
st2={"manzana","platano","uva","cerezza"}
print(max(st2))
#Ejercicio 3
st3={1,23,4,5,6,7,8}
print(max(st3))
#Ejercicio 4
st4={"a","b","c","d"}
print(max(st4))
#Ejercicio 5
st5={"h","o","l","a"}
print(max(st5))
#Ejercicio 6
st6={"h","o","l","a"}
print(min(st6))
#Ejercicio 7
st17={"abismado","visitudes","funesto","enteco"}
print(min(st17))
#Ejercicio 8
st8={"h","o","l","a"}
print(min(st8))
#Ejercicio 9
print(min(st9))
#Ejercicio 10
profesion={"ingeniero","periodista","enfermero","docente"}
print(min(profesion))

#OPERACION CON  "eliminacion"
#ejercicio 1
artef={"camara","tablet","telivisor","computadora","impresora"}
artef.discard("impresora")
print(artef)
#ejercicio 2
notas={"do","re","mi","fa","sol"}
notas.discard("re")
print(notas)
#ejercicio 3
anios={2017,2019,2020,2015,2016}
anios.discard(2017)
print(anios)
#ejercicio 4
lugares={"morrope","chan chan","duwai"}
lugares.discard("duwai")
print(lugares)
#jercicio 5
apellidos={"bances","barboza","gerrero"}
apellidos.discard("diaz")
print(apellidos)
#ejercicio 6
profesiones={"ingeniero","periodista","enfermero","docente"}
profesiones.discard("ingeniero")
print(profesiones)
#ejercicio 7
vocalistas={"enrique iglesias","jose jose"}
vocalistas.discard("juanes")
print(vocalistas)
#ejercicio 8
intrumentos={"bateria","bajo","tinbales","piano","bateria"}
intrumentos.discard("saxo")
print(intrumentos)
#ejercicio 9
broders={"david","dennys","emir"}
broders.discard("elvis")
print(broders)
#ejercicio 10
musica={"kariveña","onda cero"}
musica.discard("rpp")
print(musica)

#OPERACION CON "AGREGADO"
#Ejercicio 1
artef.add("inpresora")
print(artef)
#Ejercicio 2
notas.add("re")
print(notas)
#Ejercicio 3
anios.add(2017)
print(anios)
#Ejercicio 4
lugares.add("EE.UU")
print(lugares)
#Ejercicio 5
ani.add("bances")
print(ani)
#Ejercicio 6
profesiones.add("ingeniero")
print(profesiones)
#Ejercicio 7
vocalistas.add("kike")
print(vocalistas)
# ejercicio 8
intrumentos.add("flauta")
print(intrumentos)
#Ejercicio 9
broders.add("elvis")
print(broders)
#Ejercicio 10
notas.add("notas")
print(notas)

#OPERACION CON "ANULACION"
#Ejercicio 1
artef.clear()
print(artef)
#Ejercicio 2
notas.clear()
print(notas)
#Ejercicio 3
anios.clear()
print(anios)
#Ejercicio 4
lugares.clear()
print(lugares)
#Ejercicio 5
apellidos.clear()
print(apellidos)
#Ejerciico 6
profesiones.clear()
print(profesiones)
#Ejercicio 7
vocalistas.clear()
print(vocalistas)
#Ejercicio 8
intrumentos.clear()
print(intrumentos)
#Ejercicio 9
broders.clear()
print(broders)
#Ejercicio 10
notas.clear()
print(notas)

#OPERACION CON  "CLONADO"
#Ejercicio 1
saludos={"hola","como","como estan","muchachos"}
saludos.copy()
print(saludos)
#Ejercicio 2
empresas={"gloria","odebrect"}
empresas.copy()
print(empresas)
#Ejercicio 3
numeros={12,34,45,56}
numeros.copy()
print(numeros)
#Ejercicio 4
cursos={"ingles","calculo","mate basica","identidad nacional"}
cursos.copy()
print(cursos)
#Ejercicio 5
ferreteria={"clavos ","martillo","grapas","alambre"}
ferreteria.copy()
print(ferreteria)
#Ejercicio 6
comedor={"utensillos","olla","sarten","gas","servilleta"}
comedor.copy()
print(comedor)
#Ejercicio 7
sala={"sofa","televisor","parlante","vino"}
sala.copy()
print(sala)
#Ejercicio 8
deportes={"futbol","voley","natacion"}
deportes.copy()
print(deportes)
#Ejercicio 9
fauna={"venado","zorro","ardilla"}
print(fauna.copy())
#Ejercicio 10
flora={"romerillo","rifar","algarrobo","huacapu"}
flora.copy()
print(flora)

#OPERACION CON  "EXTRACION":
#Ejercicio 1
flora.pop()
print(flora)
#Ejercicio 2
fauna.pop()
print(fauna)
#Ejercicio 3
empresas.pop()
print(empresas)
#Ejercicio 4
cursos.pop()
print(cursos)
#Ejercicio 5
saludos.pop()
print(saludos)
#Ejrcicio 6
comedor.pop()
print(comedor)
#Ejercicio 7
numeros.pop()
print(numeros)
#Ejerciico 8
sala.pop()
print(sala)
#Ejercicio 9
deportes.pop()
print(deportes)
#Ejercicio 10
ferreteria.pop()
print(ferreteria)

#OPERACION CON "ordenado"
#Ejercicio 1
almuerzos={"arroz con pollo","arroz con pato","ceviche"}
print(set(sorted(almuerzos)))
#Ejercicio 2
modificadores={"md","mi","od","oi"}
print(set(sorted(modificadores)))
#ejercicio 3
sustantivos={"peru","casa","libro"}
print(set(sorted(sustantivos)))
#ejercicio 4
verbos={"hacer","estudiar","conocer"}
print(set(sorted(verbos)))
#ejercicio 5
abjetivos={"alto","gordo","bonito"}
print(set(sorted(abjetivos)))
#ejercicio 6
pre={"unprg","uni","unmsm"}
print(set(sorted(pre)))
#ejercicio 7
estaciones={"invierno","verano","primavera","otoño"}
print(set(sorted(estaciones)))
#ejercicio 8
climas={"templado","humedo","tropical"}
print(set(sorted(climas)))
#ejercicio 9
lugarex={"romero","loyeria","la colorada"}
print(set(sorted(lugarex)))
#ejercicio 10
animales={"guacamayo","loro","pava aliblanca"}
print(set(sorted(animales)))

