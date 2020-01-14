#   EJERCICIOS DE CREACION
#ejercicio 1
gino=[]
print(gino)
#ejercicio 2
tol=["A","B","C","D"]
print(tol)
#ejercicio 3
ani=["cuy","chivo","chancho"]
print(ani)
#ejercicio 4
vocales=["a","e","i","o","u"]
print(vocales)
#ejercicio 5
frutas=["uva","papaya","mandarina","guava"]
print(frutas)
#ejercicio 6
paises=["peru","brazil","inglaterra","suisa"]
print(paises)
#ejercicio 7
capital=["lima","buenos aires"]
print(capital)
#ejercicio 8
provincia=["lambayeque","ferreñafe"]
print(provincia)
#ejercicio 9
universidad=["unprg"]
print(universidad)
#ejercicio 10
letras=["A","B","C","D"]
print(letras)

# EJERCICIOS CON PERTENENCIA
#ejercicio 1
let=["l","a","y"]
print("l" in let)
#ejercicio 2
universidad=["unprg"]
print("ini" not in universidad)
#ejercicio 3
frutas=["uva","papaya","mandarina","guava"]
print("papaya" in frutas)
#ejercicio 4
paises=["peru","brazil","inglaterra","suisa"]
print("lima" not in paises)
#ejercicio 5
fr=["uva","papaya","mandarina","guava"]
print("zandia" in fr)
#ejercicio 6
ani=["cuy","chivo","chancho"]
print("raton" not in ani)
#ejercicio 7
ani=["cuy","chivo","chancho"]
print("ardilla" in ani)
#ejercicio 8
capital=["peru","brazil","inglaterra","suisa"]
print("lima" not in capital)
#ejercicio 9
vocales=["a","e","i","o","u"]
print("x" in vocales)
#ejerccio 10
paises=["peru","brazil","inglaterra","suisa"]
print("francia" not in paises)

#   OPERACION CON "CONCATENACION"
#ejercicio 1
a=["hola"]
conc1=a+vocales
print(conc1)
#ejercicio 2
animales=["perro","gato"]
frutas=["freza","manzana"]
conc2=animales+frutas
print(conc2)
#ejercicio 3
paises=["peru","brazil","inglaterra","suisa"]
siglas=["rpp"]
conc3=paises + siglas
print(conc3)
#ejercicio 4
siglas=["rpp"]
vocales=["a","e","i","o","u"]
conca4=siglas + vocales
print(conca4)
#ejercicio 5
cap=["peru","brazil","inglaterra","suisa"]
pai=["peru","brazil","inglaterra","suisa"]
con5=cap+pai
print(con5)
#ejercicio 6
vocale=["a","e","i","o","u"]
fruta=["manzana"]
conc6=vocale +fruta
print(conc6)
#ejercicio 7
cap=["peru","brazil","inglaterra","suisa"]
b=["hola"]
conc7=b +cap
print(conc7)
#ejercicio 8
planetas=["jupiter","saturno","marte","tierra"]
regiones=["costa","sierra","selva","mar peruano"]
conc8=planetas +regiones
print(conc8)
#ejercicio
paises=["peru","brazil","inglaterra","suisa"]
planetas=["jupiter","saturno","marte","tierra"]
conc9=paises +planetas
print(conc9)
#ejer10
planetas=["jupiter","saturno","marte","tierra"]
letr=["a","j","u"]
conc10=planetas+letr
print(conc10)

# OPERACION  CON "COMPARACION"
#ejercicio 1
animales=["perro","gato"]
paises=["peru","brazil","inglaterra","suisa"]
print(animales==paises)
#ejercicio 2
animas=["perro","gato"]
pais=["peru","brazil","inglaterra","suisa"]
print(pais>animas)
#ejercicio 3
capi=["peru","brazil","inglaterra","suisa"]
pa=["peru","brazil","inglaterra","suisa"]
print(capi!=pa)
#ejercicio 4
frutas=["uva","mango"]
siglas=["rpp"]
print(frutas>siglas)
#ejercicio 5
animales=["gato","perro"]
vocales=["a","e"]
print(animales==vocales)
#ejercicio 6
ani=["gato","perro","raton","araña"]
vocales=["a","e"]
print(vocales!=ani)
#ejercicio 7
vocale=["a","e","i","o","u"]
siglas=["rpp"]
print(vocales!=siglas)
#ejercicio 8
capil=["peru","brazil","inglaterra","suisa"]
regiones=["costa","sierra","selva","mar peruano"]
print(regiones!=capil)
#ejercicio 9
capil=["peru","brazil","inglaterra","suisa"]
regiones=["costa","sierra","selva"]
print(capil>regiones)
#ejercicio 10
print(planetas==a)
# OPERACION CON INDEXACION
#ejrcicio 1
animales=["gato","perro"]
A1=animales[1]
print(A1)
#ejercicio 2
an=["gato","perro","gallina"]
A2=an[2]
print(A2)
#ejercicio 3
anl=["gato","perro","gallina"]
A3=anl[0]
print(A3)
#ejercicio 4
frutas=["uva","mango"]
F1=frutas[1]
print(F1)
#ejercicio 5
frutas=["uva","mango"]
F2=frutas[0]
print(F2)
#ejercicio 6
frutas=["uva","mango","platano","zandia"]
F3=frutas[1]
print(F3)
#ejercicio 7
vo=["a","e","i","o","u"]
V1=vo[0]
print(V1)
#ejercicio 8
vo=["a","e","i","o","u"]
V2=vo[4]
print(V2)
#ejercicio 9
air=["peru","brazil","inglaterra","suisa"]
pl1=air[0]
print(pl1)
#ejercicio 10
sigls=["rpp","unprg","hp"]
SIG=sigls[2]
print(SIG)

#OPERACION CON "CORTADO"
#ejercicio 1
les=["perro","gato","leon","tigre"]
ANI=les[2:]
print(ANI)
#Ejercicio 2
aniles=["perro","gato","leon","tigre"]
ANI2=aniles[:2]
print(ANI2)
#Ejercicio 3
frut=["uva","manzana","freza","melon"]
FR1=frut[1:3]
print(FR1)
#Ejercicio 4
frut1=["uva","manzana","freza","melon","mandarina"]
FRU3=frut1[::-1]
print(FRU3)
#Ejercicio 5
FRU4=frutas[::]
print(FRU4)
#Ejercicio 6
SIGL0=siglas[0:2]
print(SIGL0)
#Ejercicio 7
VOCAL7=vocales[0:3]
print(VOCAL7)
#Ejercicio 8
S11=paises[2:4]
print(S11)
#Ejercicio 9
PLAN12=planetas[1:3]
print(PLAN12)
#Ejercicio 10
cal=["h","o","l","a"]
CAP=cal[::-1]
print(CAP)

#OPERACON  CON "LONGITUD"
#ejercicio 1
ans=["perro","gato","leon","tigre"]
print(len(ans))
#ejercicio 2
paises=["peru","chile","colombia"]
print(len(paises))
#ejercicio 3
capitales_sudamericanos=["lima","brazilia"]
print(len(capitales_sudamericanos))
#ejercicio 4
vocales=["a","e","i","o","u"]
print(len(vocales))
#ejercicio 5
planetas=["jupiter","saturno","marte","tierra"]
print(len(planetas))
#ejercicio 6
regiones=["costa","sierra","selva"]
print(len(regiones))
#ejercicio 7
frutas1=["manzana","uva","mandarina"]
print(len(frutas1))
#ejercicio 8
verduras=["cebolla","repollo","brocoli","alcachofa"]
print(len(verduras))
#ejercicio 9
rios=["morrope","marañon","ucayali","mayo","ene","perene"]
print(len(rios))
#ejercicio 10
departa=["puno","cajamarca","piura","arequipa","tumbes","tacna","huancayo"]
print(len(departa))

#OPERACION CON  "ITERACION"
#Ejercicio 1
verduras=["cebolla","repollo","brocoli","alcachofa"]
for x in verduras:
    print(x)
#Ejercicio 2
paises=["peru","chile","colombia"]
for pail in paises:
    print(pail)
#Ejercicio 3
fr123=["uva","manzana","freza","melon","mandarina"]
for f in fr123:
    print(f)
#Ejercicio 4
les4=["perro","gato","leon","tigre"]
for a in les4:
    print(a)
#Ejercicio 5
vocales1=["a","e","i","o","u"]
for vvvv in vocales1:
    print(vvvv)
#Ejercicio 6
ps=["jupiter","saturno","marte","tierra"]
for pln in ps:
    print(pln)
#Ejercicio 7
rios=["morrope","marañon","ucayali","mayo","ene","perene"]
for r1 in rios:
    print(r1)
#Ejercicio 8
capitales_sudamericanos=["lima","brazilia"]
for c12 in capitales_sudamericanos:
    print(c12)
#Ejercicio 9
departa=["puno","cajamarca","piura","arequipa","tumbes","tacna","huancayo"]
for d in departa:
    print(d)
#Ejercicio 10
regiones1=["costa","sierra","selva"]
for R in regiones1:
    print(R)

#OPERACION CON "BUSQUEDA":
#Ejercicio 1
frtw=["uva","manzana","freza","melon","mandarina"]
print(frtw.index("manzana"))
#Ejercicio 2
frtw12=["uva","manzana","freza"]
print(frtw12.index("freza"))
#Ejercicio 3
planetasd=["jupiter","saturno","marte","tierra"]
print(planetasd.index("jupiter"))
#Ejercicio 4
rios=["morrope","marañon","ucayali","mayo","ene","perene"]
print(rios.index("morrope"))
#Ejercicio 5
regiones2=["costa","sierra","selva"]
print(regiones2.index("selva"))
#Ejercicio 6
departamentos=["loreto","lambayeque"]
print(departamentos.index("lambayeque"))
#Ejercicio 7
print(verduras.index("brocoli"))
#Ejercicio 8
print(animales.index("perro"))
#Ejercicio 9
print(vocales.index("e"))
#Ejercicio 10
print(capital.index("peru"))

#OPERACION CON CONTEO
#Ejericio 1
print(frutas.count("platano"))
#Ejercicio 2
print(frutas.count("pera"))
#Ejercicio 3
print(planetas.count("jupiter"))
#Ejercicio 4
print(rios.count("morrope"))
#Ejericio 5
print(regiones.count("selva"))
#Ejercicio 6
print(departamentos.count("lanbayeque"))
#Ejercicio 7
print(verduras.count("culantro"))
#Ejercicio 8
print(animales.count("saltojo"))
#Ejercicio 9
print(vocales.count("i"))
#Ejercicio 10
print(capitales_sudamericanos.count(""))

#OPERACION CON MAX Y MIN

#OPERACION CON  "MULTIPLICASION"
#Ejercicio 1
print(animales*2)
#Ejercicio 2
print(animales*0)
#Ejercicio 3
print(verduras*1)
#Ejercicio 4
print(planetas*2)
#Ejercicio 5
print(departamentos*3)
#Ejercicio 6
print(paises*2)
#Ejercicio 7
print(rios*3)
#Ejercicio 8
print(regiones*4)
#Ejercicio 9
print(vocales*3)
#Ejercicio 10
print(capitales_sudamericanos*1)

#OPERACION CON  "ELIMINACION":
#Ejercicio 1
del frutas[0:1]
frutas[0:1]=[]
print(frutas)
#Ejercicio 2
del universidad[0:1]
universidad[0:1]=[]
print(universidad)
#Ejercicio 3
del siglas[0:1]
siglas[0:1]=[]
print(siglas)
#Ejercicio 4
del an[0:1]
animales[0:1]=[]
print(animales)
#Ejercicio 5
del rios[0:1]
rios[0:1]=[]
print(rios)
#Ejercicio 6
del fr123[0:1]
regiones[0:1]=[]
print(regiones)
#Ejercicio 7
del planetas[0:1]
planetas[0:1]=[]
print(planetas)
#Ejercicio 8
del capitales_sudamericanos[0:1]
capitales_sudamericanos[0:1]=[]
print(capitales_sudamericanos)
#Ejercicio 9
del departamentos[0:1]
departamentos[0:1]=[]
print(departamentos)
#Ejercicio 10
del frutas1[0:1]
verduras[0:1]=[]
print(verduras)

#OPERACION CON "REEMPLAZO"
#Ejercicio 1
frutas[0]="mango"
print(frutas)
#Eercicio 2
fr123[1]="mango"
print(fr123)
# ejercicio 3
regiones[0]="selva"
print(regiones)
# ejercicio 4
animales[0]="paloma"
print(animales)
#Ejercicio 5
planetas[0]="tierra"
print(planetas)
#Ejercicio 6
regiones2[0]="costa"
print(regiones2)
#Ejercicio 7
vocales[0]="u"
print(vocales)
#Ejercicio 8
capital[0]="lima"
print(capital)
#Ejercicio 9
paises[0]="EE.UU"
print(paises)
#Ejerciico 10
verduras[0]="pepinillo"
print(verduras)

#OPERACION CON  "AGREGADO":
#Ejercicio 1
verduras.append("culantro")
print(verduras)
#Ejercicio 2
regiones.append("bosque tropical del pacifico")
print(regiones)
#Ejercicio 3
frutas.append("mango")
print(frutas)
#Ejercicio 4
animales.append("gallito de las rocas")
print(animales)
#Ejercicio 5
vocales.append("A")
print(vocales)
#Ejercicio 6
planetas.append("saturno")
print(planetas)
#Ejercicio 7
universidad.append("villareal")
print(universidad)
#Ejercicio 8
rios.append("olmos")
print(rios)
#Ejercicio 9
capitales_sudamericanos.append("lima")
print(capitales_sudamericanos)
#Ejercicio 10
paises.append("brazil")
print(paises)

#OPERACION CON "ANULACION":
#Ejercicio 1
verduras.clear()
print(verduras)
#Ejercicio 2
capitales_sudamericanos.clear()
print(capitales_sudamericanos)
#Ejercicio 3
animales.clear()
print(animales)
#Ejercicio 4
rios.clear()
print(rios)
#Ejercicio 5
universidad.clear()
print(universidad)
#Ejercicio 6
frutas1.clear()
print(frutas1)
#Ejercicio 7
vocales.clear()
print(vocales)
#Ejercicio 8
verduras.clear()
print(verduras)
#Ejercicio 9
planetas.clear()
print(planetas)
#EJER10
regiones2.clear()
print(regiones2)

#OPERACON17 "CLONADO":

#OPERACION18 "EXTENCION":
#Ejercicio 1
distritos_peru=["tucume","illimo","mochumi"]
distritos_peru.extend("olmos")
print(distritos_peru)

#Ejercicio 2
distritos_morrope=["morrope","piura"]
distritos_morrope.extend("x")
print(distritos_morrope)
#Ejercicio 3
distritos=["morrope","piura","tucume","illimo","mochumi"]
distritos.extend("j")
print(distritos)
#Ejercicio 4
productivo=["agricultura","ganaderia","silvicultura"]
productivo.extend("x")
print(productivo)
#Ejercicio 5
mundial=["sudafrica"]
mundial.extend("rucia")
print(mundial)
#Ejercicio 6
ex_pre=["Velasco Alvarado","Ramon Castilla","Nicolas de Pierola","Agusto Belegia"]
ex_pre.extend("toledo")
print(ex_pre)
#Ejercicio 7
amix=["antonio","brayan"]
amix.extend("doris")
print(amix)
#Ejercicio 8
sofistas=["decartes","socrates","aristoteles","kant"]
sofistas.extend("platon")
print(sofistas)
#Ejercicio 9
cursos=["matematica","comunicacion","ingles"]
cursos.extend("fisica")
print(cursos)
#Ejercicio 10
mercado=["negro","cerrado","abierto"]
mercado.extend("mayorista")

#OPERACION CON "INSERCION"
#Ejercicio 1
mercado.insert(0,"negro")
print(mercado)
#Ejercicio 2
amix.insert(0,"alberto")
print(amix)
# ejercicio 3
distritos.insert(0,"lagunas")
print(distritos)
#Ejercicio 4
frut.insert(0,"wuayava")
print(frut)
#Ejercicio 5
distritos_morrope.insert(0,"la colorada")
print(distritos_morrope)
#Ejercicio 6
productivo.insert(0,"joyeria")
print(productivo)
#ejercicio 7
vocales.insert(0,"vocal de gino")
print(vocales)
#Ejercicio 8
sofistas.insert(0,"democrito")
print(sofistas)
#Ejercicio 9
verduras.insert(0,"brocoli")
print(verduras)
#Ejercicio 10
ans.insert(0,"gato")
print(ans)

