# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "rodma"
__date__ = "$18-oct-2015 18:19:48$"


print"******************"
print"Elija una opcion: "
print"1)Archivo         "
print"2)Buscar          "
print"3)Salir           "
print"******************"

select=input("Seleccione una opcion:")
if select==1:
    print"Ha seleccionado \"Archivo\""
if select==2:
    print"Ha seleccionado \"Buscar\""
if select==3:
    print"Ha seleccionado \"Salir\""
if select<=0 or select>3:
    print"No ha seleccionado ninguna opcion valida"
    