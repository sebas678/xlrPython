import xlrd
documento=xlrd.open_workbook("ejemploPeliculas.xlsx")

#Se crean diferentes paginas
libros= documento.sheet_by_index(0)
peliculas=documento.sheet_by_index(1)

#se leen  filas y columnas de cada hoja y luego se imprimen
filasLibros=libros.nrows
columnasLibros=libros.ncols
print("  La hoja libros tiene "+str(filasLibros)+" filas y "+str(columnasLibros)+" columnas")
filasPeliculas=peliculas.nrows
columnasPeliculas=peliculas.ncols
print("  La hoja peliculas tiene "+str(filasPeliculas)+" filas y "+str(columnasPeliculas)+" columnas")

contenidoCelda=libros.cell_value(0,1)
print("\n  En la celda dice "+str(contenidoCelda) +"\n \n")
print("****Inicio de prueba cool****\n")

for i in range(libros.nrows):
    fila = libros.row(i)
    print (fila)
