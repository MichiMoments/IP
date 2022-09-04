import os
import sys

class controlador_var:
    """
    Es un controlador con todas la variables que hay
    """ 
    def __init__(self) -> None:
      self.variables=[]  
      self.cant= self.contar()          

    def nueva_var(self,nom,val=None):
        self.variables.append(nom)  
        self.contar()

    def contar(self):
        self.cant=len(self.variables)    
    
    def existe(self,nom):
        #print(self.variables)
        #print(nom,len(nom))
        return nom in self.variables
            
    def get_val(self,nom):
        return self.variables[nom]


class functions_control:
    """
    Es un controlador para las funciones, las creadas por el usuario
    """
    def __init__(self) -> None:
        self.funciones={}

    def nueva_función(self,nom,cant=0):
        self.funciones[nom]=cant

    def existe(self,nom):
        #print(nom)
        #print(self.funciones.get(nom))
        if self.funciones.get(nom) == 0 :
           return True 
        return False  

    def parametros(self,nom):
        return self.funciones[nom]
 
class control:
    """
    Tiene en cuenta las secuencias de control y la maneja 
    """
    def __init__(self) -> None:
        self.control=[]
        self.corchetes=[]
        self.numbers={"PROG":100,"GORP":-100,"PROC":90,"CORP":-90,"if":80,
                      "else":0,#xD
                      "fi":-80,"while":69,"do":69,"od":-138,"repeatTimes":10,"per":-10}
        self.history=[]


    def inicio(self,nom):
        
        self.control[nom]

    def open(self):
        
        self.corchetes.append(1)

    def new(self,nom):

        self.history.append(nom)
        self.control.append(self.numbers[nom])
        if nom == "else":
          if self.history[-1] != "if":
            salir() 

    def close(self):
       
        self.corchetes.append(-1)

    def count(self):
        
        a=0
        for num in self.corchetes:
            a+= num 
        if a == 0:
            return None 
        return "Mal"        

    def contar(self):
        a=0
        for i in self.control:
            a+= i
        if a == 0:
            return None 
        return "Mal"    

bloques=control()
funciones=functions_control()
variables= controlador_var()
    


palabras_reservadas =["PROG","GORP","VAR","PROC","CORP","walk","jump","jumpTo", "veer","look","drop","grab","get","free","pop","walk","if","else","fi","while","do"
                       "od","repeatTimes","per","isfacing","isValid","canWalk","not", "{","}"]

palabra_reservada_bloq=["PROG","GORP","PROC","CORP","if","else","fi","while","do","od","repeatTimes","per"]
palabra_reservada_func=["walk","jump","jumpTo", "veer","look","drop","grab","get","free","pop","walk","isfacing","isValid","canWalk","not"]

simbolos=["-","¨","Ç","{","}","*",":",";","[","]","-","+","!","¡","·","#","$","%","&","/","(",")","=","?","¿"]
llaves=["{","}"]


def salir (palabra):
    print("The Syntax is Incorrect")
    print("Error in ", palabra)
    sys.exit()

def main(archivo): 
    "Se encarga de leer el archivo .txt"
    lectura= data_dir + archivo
    file= open(archivo, encoding= "utf_8" )
    línea=file.readline()
    while línea != '':
        # procesar línea
        #print(línea,"linea")
        renglon=línea.split(";")
        #print(renglon,"renglon")
        for n in renglon:
                
            palabras=n.replace("\n","").strip().split(" ")
            palabra= palabras[0].strip()
            if palabra != "":
             #print(palabra,"Palabra","\n",palabras,"palabras","\n",n,"n")
             if palabra in palabras_reservadas:
                    #print("a")
                    palabras_reservadas
                    if palabra=="VAR":
                        #print("var")
                        incognitas(n,palabras,palabra) 
                        #print("Salir")
                    if palabra in llaves:
                        #print("llaves")
                        corchetes(palabra)
                    if palabra in palabra_reservada_bloq:
                        #print("bloque")
                        bloque_palabra(n, palabras, palabra)
                    if palabra in palabra_reservada_func:
                        #print("Funciones")
                        funciones_existentes(n,palabras)
             else:
                #print("b")
                nada_mas(palabra)
    
        línea=file.readline()    
    if bloques.count():
        salir("Not even {")

    if bloques.contar():
        salir("Not even reserved words PROC, GROP, CORP, PROG")


def incognitas(renglon,palabras,palabra):
    "Manejo de palabras_reservadas, consultar lista uwu"
    palabras.pop(0)
    #print(renglon)
    for reservada in palabras:
            reservada!=palabras_reservadas
            vars= reservada.split(",")
            for var in vars:
                if var != "":
                 #print(var,vars)
                 variable=var[0]
                 if variable.isdigit():
                  salir(palabras)
                 for caracter in var:
                  if caracter in simbolos:
                     salir(palabras)
                 if var in renglon:
                    variables.nueva_var(var)
                 else:
                    
                    salir(palabras)    

"""
1. No hallan más palabras reservadas=recorrido donerino!!
2. No hallan simbolos=recorrido donerino!!
3. No empiece con número=slice de posicion 0 donerino!!
4. Que después de una variable, si no es la útlima halla una coma
5. Si hay una coma intermedía, se separa
"""




def funciones_existentes(renglon,palabras):
    """
    Se ejecuta si encuentra que es una palabra reservada referente a una función predeterminada 
    """
    funciones={"isfacing":1,"isValid":2,"canWalk":2,"not":1,"walk":(1,2),"jump":1,"jumpTo":2,"veer":1,"look":1,"drop":1
        ,"grab":1,"get":1,"free":1, "pop":1}
    palabras.pop(0) 
    cont=[]
    palabras=palabras[0]

    for next in palabras:
        #print(next)
        if next=="(":
            cont.append(1) 
        if next==")":
            cont.append(-1) 
        if "," in next and "," != next: 
            for val in next.split(","):
                if not variables.existe(val):
                 salir(palabras)     
        else: 
            if next not in renglon: 
               salir(palabras)    
            
    g=0
    for num in cont: 
        g+=num     
    if g!= 0:
        salir(palabras)

def bloque_palabra(renglon,palabras,palabra):
    """
    Se ejecuta si encuentra que la palabra es reservada referente a un bloque  
    """
    conteo=["PROC","PROG","GORP","CORP"]
    if palabra in conteo: 
       bloques.new(palabra) 
    if palabra == "PROC": 
      #print(palabras,"Bloque palabras") 
      palabras.pop(0)
      
      if len(palabras) == 1:
       palabras=palabras[0]
       
       if "(" in palabras and ")" in palabras: 
        palabras.replace(")","")
        check=palabras.split("(")
        #print(check),"Bloque, check"
        name=check[0]  
        var=check[1]
        
        vari=var.split(",")  
 
        for asw in vari:
         if not(asw in renglon): 
            salir(palabras)

        funciones.nueva_función(name)    

       else: 
        salir(palabras)  
      else: 
        salir(palabras)  

    if palabra =="while" or palabra =="if" or palabra =="repeatTimes":
       base={"while":"od","if":"fi","repeatTimes":"per"}
       sep={"while":"do","if":"{","repeatTimes":"{"}
       expresion=str(palabras)
       p= "(" in expresion and ")" in expresion
       if palabra == "while":
        q="do" in palabras
       else: 
        q= True 
       
       v="{" in expresion and "}" in expresion
       j= palabras[-1] == base[palabra]
       #print(p,q,v,j) 
       palabras.pop(-1)
       words=renglon.replace(palabra,"").replace("\n","").replace(base[palabra],"")
       if p and q and v and j:
           
           tranformar_funcion(words,sep[palabra])
       else:
        salir(palabras)
    


def tranformar_funcion(words,separador):
    """
    Transforma la función par adespuñés analizarla
    """
    parte= words.split(separador) 
    #print(parte)
    for i in range(2):
     funcion=parte[i].replace("}","").replace("{","").replace("[","").replace("]","")
     #print(funcion) 
         
     analizar_función(funcion)
     

def analizar_función(funcion):
    """
    Aniliza una función , pero sin más renglones solo el str funcion(parametros) 
    """               
    funcioness={"isfacing":1,"isValid":2,"canWalk":2,"not":1,"walk":(1,2),"jump":1,"jumpTo":2,"veer":1,"look":1,"drop":1
        ,"grab":1,"get":1,"free":1, "pop":1}
    data= funcion.split("(")
    name=data[0].strip()
    if name == "":
        name=data[1].strip()
    #print(data)
    if not name in funcioness: 
       if funciones.existe(name):
          salir(funcion)
    """
    check=data[2].replace(")","")
    for var in check.split(","):
        if not variables.existe(var):
            
            salir(funcion)
    """
def corchetes(palabra):
    """
    Empieza a contar corchetes hehe
    """
    if palabra=="{":
        bloques.open()
    if palabra =="}":
        bloques.close()     

def nada_mas(palabra):
    """
    No es niguna palabra especial ,
    es decir debe o ser una función o ya una variable existente
    """     
    #print(palabra,"palasadas")      
    palabra=palabra.strip() 
    q= not variables.existe(palabra)
    #print(variables.existe(palabra))
    p= not funciones.existe(palabra)
    #print(funciones.existe(palabra))   
    if q  and p :
        salir(palabra)


file="Archivo.txt" #Por favor, ingresar el nombre exacto del archivo .txt
file_path = os.path.join(os.path.dirname(file), '..')
file_dir = os.path.dirname(os.path.realpath('file'))
sys.path.insert(0, os.path.abspath(file_path))
data_dir = file_dir + '/Data/'

main(file)

print("The Syntax is Correct")
