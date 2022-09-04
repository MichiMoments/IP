
"""def tendencia_anio(datos:pd.DataFrame, limite_inf:int, limite_sup:int)->None:
    dataframe_filtrado = datos[(datos.Anio >= limite_inf) & (datos.Anio <= limite_sup)]
    datos_nuevos = dataframe_filtrado.Anio
    datos_contados = datos_nuevos.values_counts()
    anios_ordenados = datos_contados.sort_index(ascending=False)
    anios_ordenados.plot(kind="line",figsize=(10,10),title="Grafica tendencia anios")
    plt.show()
"""
#crear matriz

d = {"hoal": 2}

s = 6
lista = [1,2,3]

d[s] = type(s)
d["a"] = lista


print(d)

if d[s] == int:
    print("xd")

if type(d["a"]) == list:
    print("xd2")

"""def comer(llave, valor=0):S
    d = {llave:valor}
    print(d)

comer("s", "amburguesa")"""





text = "PROGfhjdal;fhjdalhfajk;jkdl;fakl;fa GORP"

if text.startswith("PROG") and text.endswith("GORP"):
    print("loca")





linea = "PROGvarn,x,y;PROCverga"

palabras_reservadas =["PROG","GORP","var","PROC","CORP","walk","jump","jumpTo", "veer","look","drop","grab","get","free","pop","walk","if","else","fi","while","do"
                       "od","repeatTimes","per","isfacing","isValid","canWalk","not", "{","}"]


simbolos=["-","¨","Ç","{","}","*",":",";","[","]","-","+","!","¡","·","#","$","%","&","/","(",")","=","?","¿"]
llaves=["{","}"]

for element in palabras_reservadas:
    if element in linea:
        print(element)

            
