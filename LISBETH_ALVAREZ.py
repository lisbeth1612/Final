
from mysql import connector as connector

ip = 'localhost'
user = 'root'
password = 'Lisbeth16'
database = 'universidad'

mydb = connector.connect(
  host="localhost",
  user=user,
  password=password,
  database = database
)

cursor = mydb.cursor(buffered=True)

def Materias():
	while 1:
		print("")
		print("selecciono Materias, indique que opcion desea realizar")
		print("1. Consultar tabla Actual")
		print("2. Resgistrar una nueva Materia")
		print("3. Mostrar toda la tabla")
		print("4. Eliminar una Materia")
		print("5. Actualizar la tabla")
		print("6. Logout")

		value = { 'opcion': 'materias'}
		Sel_option = input(str("Option : "))
		if Sel_option == "1":
			print("")
			print("Consultar materias")
			Codigo_materia = input(str("Indique el codigo de la materia que deseas ver, en caso de no saber cual coloque un cero : "))
			nombre_Materia = input(str("Indique la materia que deseas ver : "))
			Codigo_sec_materia = input(str("Indique el codigo de la seccion que deseas ver, en caso de no saber cual coloque un cero : "))
			query_vals = (Codigo_materia,nombre_Materia, Codigo_sec_materia)
			cursor.execute("select * FROM materias WHERE Mat_Nombre_CD = %s or Mat_Nombre_DESC LIKE %s or Mat_Nombre_seciones_CD = %s ",query_vals)
			mydb.commit()
			for x in cursor:
				print(x)
				print('Para saber cuales son todas las que hay, selecione la opcion 3')

			
		elif Sel_option == "2":
			print("")
			print("Resgistrar una nueva materia")
			nombre_Materia = input(str("Ingrese el nombre de la materia : "))
			Codigo_sec_materia= input(str("Ingrese el codigo de la seccion de la materia : "))
			query_vals = (nombre_Materia,Codigo_sec_materia)
			cursor.execute("INSERT INTO materias (Mat_Nombre_CD,Mat_Nombre_DESC,Mat_Nombre_seciones_CD) VALUES (default, %s,%s)",query_vals)
			mydb.commit()
			print(nombre_Materia + " ha sido registrado con exito. en caso de volver a ver la tabla, seleciona la opcion 3")

		elif Sel_option == "3":
			print("")
			print('la tabla es la siguiente')
			cursor.execute("Select * from materias")
			for x in cursor:
				print(x)

		elif Sel_option == "4":
			print("")
			print("Borrar Materias")
			nombre_Materia = input(str("Indique la materia a borrar : "))
			query_vals = (nombre_Materia, "NINGUNO")
			cursor.execute("DELETE FROM materias WHERE Mat_Nombre_DESC = %s OR Mat_Nombre_seciones_CD = %s ",query_vals)
			mydb.commit()
			print(nombre_Materia + " has been deleted")

		elif Sel_option == "5":
			print("")
			print("Actualizar materias")
			nombre_Materia = input(str("Indique la nueva descripcion de la materia que desea actualizar : "))
			Codigo_sec_materia = input(str("Indique el codigo de la seccion que actualizar : "))
			Codigo_materia = input(str("Indique el codigo de la materia que deseas actualizar "))
			query_vals = (nombre_Materia, Codigo_sec_materia,Codigo_materia)
			cursor.execute("UPDATE materias SET Mat_Nombre_DESC = %s ,  Mat_Nombre_seciones_CD  = %s WHERE Mat_Nombre_CD = %s ",query_vals)
			mydb.commit()
			
		elif Sel_option == "6":
			print('Hasta luego, vuelva pronto')
			break
		else:
			print("No selecciono una Opcion forma correcta intente de nuevo")

def Carreras():
	while 1:
		print("")
		print("selecciono Carreras, indique que opcion desea realizar")
		print("1. Consultar tabla Actual")
		print("2. Resgistrar una nueva Carrera")
		print("3. Mostrar toda la tabla")
		print("4. Eliminar una Carrera")
		print("5. Actualizar la tabla")
		print("6. Logout")

		
		Sel_option = input(str("Option : "))
		if Sel_option == "1":
			print("")
			print("Consultar Carreras")
			Codigo_carrera = input(str("Indique el codigo de la Carrera que deseas ver, en caso de no saber cual coloque un cero : "))
			nombre_carrera = input(str("Indique el nombre de la Carrera que deseas ver : "))
			query_vals = (Codigo_carrera,nombre_carrera)
			cursor.execute("select * FROM Carrera WHERE Car_Nombre_CD = %s or Car_Nombre_DESC LIKE %s ",query_vals)
			mydb.commit()
			for x in cursor:
				print(x)
				print('Para saber cuales son todas las que hay, selecione la opcion 3')

			
		elif Sel_option == "2":
			print("")
			print("Resgistrar una nueva Carrera")
			nombre_carrera = input(str("Ingrese el nombre de la Carrera : "))
			query_vals = (nombre_carrera,"NINGUNO")
			cursor.execute("INSERT INTO Carrera (Car_Nombre_CD,Car_Nombre_DESC) VALUES (default, %s)",query_vals)
			mydb.commit()
			print(nombre_carrera + " ha sido registrado con exito. en caso de volver a ver la tabla, seleciona la opcion 3")

		elif Sel_option == "3":
			print("")
			print('la tabla es la siguiente')
			cursor.execute("Select * from Carrera")
			for x in cursor:
				print(x)

		elif Sel_option == "4":
			print("")
			print("Borrar Carreras")
			nombre_carrera = input(str("Indique la Carrera a borrar : "))
			Codigo_carrera = input(str("Indique el codigo de la Carrera que deseas ver, en caso de no saber cual coloque un cero : "))
			query_vals = (nombre_carrera, Codigo_carrera)
			cursor.execute("DELETE FROM Carreras WHERE Car_Nombre_DESC = %s OR Car_Nombre_CD = %s ",query_vals)
			mydb.commit()
			print(nombre_carrera + " has been deleted")

		elif Sel_option == "5":
			print("")
			print("Actualizar Carreras")
			nombre_carrera = input(str("Indique la nueva descripcion de la Carrera que desea actualizar : "))
			Codigo_carrera = input(str("Indique el codigo de la Carrera que deseas actualizar "))
			query_vals = (nombre_carrera,Codigo_carrera)
			cursor.execute("UPDATE Carreras SET Car_Nombre_DESC = %s WHERE Car_Nombre_CD = %s ",query_vals)
			mydb.commit()
			
		elif Sel_option == "6":
			print('Hasta luego, vuelva pronto')
			break
		else:
			print("No selecciono una Opcion forma correcta intente de nuevo")

def Estudiantes():
	while 1:
		print("")
		print("selecciono Estudiantes, indique que opcion desea realizar")
		print("1. Consultar tabla Actual")
		print("2. Resgistrar un nuevo Estudiante")
		print("3. Mostrar toda la tabla")
		print("4. Eliminar un Estudiante")
		print("5. Actualizar la tabla")
		print("6. Logout")

		Sel_option = input(str("Option : "))
		if Sel_option == "1":
			print("")
			print("Consultar Estudiantes")
			Codigo_Estudiante = input(str("Indique el codigo de la carrera del Estudiante que deseas ver, en caso de no saber cual coloque un cero : "))
			nombre_Estudiante = input(str("Indique el nombre del Estudiante que deseas ver : "))
			Codigo_matricula_estudiante = input(str("Indique la matricula que deseas ver, en caso de no saber cual coloque un cero : "))
			query_vals = (Codigo_Estudiante,nombre_Estudiante, Codigo_matricula_estudiante)
			cursor.execute("select * FROM Estudiante WHERE Est_Carrera = %s or Est_Nommbre LIKE %s or Est_Matricula = %s ",query_vals)
			mydb.commit()
			for x in cursor:
				print(x)
				print('Para saber cuales son todas las que hay, selecione la opcion 3')

			
		elif Sel_option == "2":
			print("")
			print("Resgistrar una nueva Estudiante")
			nombre_Estudiante = input(str("Ingrese el nombre de la Estudiante : "))
			apellido_Estudiante = input(str("Ingrese el apellido del Estudiante : "))
			documento_Estudiante = input(str("Ingrese el identificacion del Estudiante : "))
			tipoDoc_Estudiante = input(str("Ingrese el tipo de documento del Estudiante : "))
			dirrecion_Estudiante = input(str("Ingrese la dirrecion del Estudiante : "))
			Carrera_Estudiante = input(str("Ingrese el codigo de la carrera del Estudiante : "))
			estatus_Estudiante = input(str("Ingrese el Estudiante esta activo (A) o inactivo(I) : "))			
			query_vals = (nombre_Estudiante,apellido_Estudiante,documento_Estudiante,tipoDoc_Estudiante,dirrecion_Estudiante,Carrera_Estudiante,estatus_Estudiante)
			cursor.execute("INSERT INTO Estudiante ( Est_Nommbre,Est_Apellido,Est_Matricula,Est_Documento,Est_TipoDocumento,Est_Direccion,Est_Carrera,Est_Estatus) VALUES (%s,%s,%s,default,%s,%s,%s,%s,%s)",query_vals)
			mydb.commit()
			print(nombre_Estudiante + " ha sido registrado con exito. en caso de volver a ver la tabla, seleciona la opcion 3")

		elif Sel_option == "3":
			print("")
			print('la tabla es la siguiente')
			cursor.execute("Select * from Estudiante")
			for x in cursor:
				print(x)

		elif Sel_option == "4":
			print("")
			print("Borrar Estudiantes")
			nombre_Estudiante = input(str("Indique la Estudiante a borrar : "))
			Codigo_matricula_estudiante = input(str("Indique la matricula del estudiante a borrar: "))
			query_vals = (nombre_Estudiante,Codigo_matricula_estudiante)
			cursor.execute("DELETE FROM Estudiantes WHERE Est_Nommbre = %s OR Est_Matricula = %s ",query_vals)
			mydb.commit()
			print(nombre_Estudiante + " has been deleted")

		elif Sel_option == "5":
			print("")
			print("Actualizar Estudiantes")
			nombre_Estudiante = input(str("Indique el nuevo documento de la Estudiante que desea actualizar : "))
			tipoDoc_Estudiante = input(str("Indique el tipo de documento del estudiante a actualizar : "))
			Codigo_Estudiante = input(str("Indique el codigo de la Estudiante que deseas actualizar "))
			query_vals = (nombre_Estudiante, tipoDoc_Estudiante,Codigo_Estudiante)
			cursor.execute("UPDATE Estudiantes SET Est_Documento = %s ,  Est_TipoDocumento  = %s WHERE Est_Matricula = %s ",query_vals)
			mydb.commit()
			
		elif Sel_option == "6":
			print('Hasta luego, vuelva pronto')
			break
		else:
			print("No selecciono una Opcion forma correcta intente de nuevo")

def Profesores():
	while 1:
		print("")
		print("selecciono Profesores, indique que opcion desea realizar")
		print("1. Consultar tabla Actual")
		print("2. Resgistrar un nuevo Profesor")
		print("3. Mostrar toda la tabla")
		print("4. Eliminar un Profesor")
		print("5. Actualizar la tabla")
		print("6. Logout")

		Sel_option = input(str("Option : "))
		if Sel_option == "1":
			print("")
			print("Consultar Profesores")
			Codigo_Estudiante = input(str("Indique el codigo de la matricula del Profesor que deseas ver, en caso de no saber cual coloque un cero : "))
			nombre_Estudiante = input(str("Indique el codigo de la seccion del Profesor que deseas ver, en caso de no saber cual coloque un cero : "))
			Codigo_matricula_estudiante = input(str("Indique el nombre del profesor  : "))
			query_vals = (Codigo_Estudiante,nombre_Estudiante, Codigo_matricula_estudiante)
			cursor.execute("select A.* , B.Mat_Nombre_DESC, B.Mat_Nombre_seciones_CD FROM docentes as A inner join materias as B on A.Doc_Secciones = B.Mat_Nombre_CD WHERE A.Doc_Matricula = %s or Doc_Nommbre LIKE %s or Doc_Secciones = %s ",query_vals)
			mydb.commit()
			for x in cursor:
				print(x)
				print('Para saber cuales son todas las que hay, selecione la opcion 3')

			
		elif Sel_option == "2":
			print("")
			print("Resgistrar una nueva Profesor")
			nombre_Estudiante = input(str("Ingrese el nombre de la Profesor : "))
			apellido_Estudiante = input(str("Ingrese el apellido del Profesor : "))
			documento_Estudiante = input(str("Ingrese el identificacion del Profesor : "))
			tipoDoc_Estudiante = input(str("Ingrese el tipo de documento del Profesor : "))
			dirrecion_Estudiante = input(str("Ingrese la dirrecion del Profesor : "))
			Carrera_Estudiante = input(str("Ingrese el codigo de la seccion del Profesor : "))
			estatus_Estudiante = input(str("Ingrese el Profesor esta activo (A) o inactivo(I) : "))			
			query_vals = (nombre_Estudiante,apellido_Estudiante,documento_Estudiante,tipoDoc_Estudiante,dirrecion_Estudiante,Carrera_Estudiante,estatus_Estudiante)
			cursor.execute("INSERT INTO Profesor ( Est_Nommbre,Est_Apellido,Est_Matricula,Est_Documento,Est_TipoDocumento,Est_Direccion,Est_Carrera,Est_Estatus) VALUES (%s,%s,%s,default,%s,%s,%s,%s,%s)",query_vals)
			mydb.commit()
			print(nombre_Estudiante + " ha sido registrado con exito. en caso de volver a ver la tabla, seleciona la opcion 3")

		elif Sel_option == "3":
			print("")
			print('la tabla es la siguiente')
			cursor.execute("Select * from docentes")
			for x in cursor:
				print(x)

		elif Sel_option == "4":
			print("")
			print("Borrar Profesores")
			nombre_Estudiante = input(str("Indique al Profesor a borrar : "))
			Codigo_matricula_estudiante = input(str("Indique la matricula del Profesor a borrar: "))
			query_vals = (nombre_Estudiante,Codigo_matricula_estudiante)
			cursor.execute("DELETE FROM docentes WHERE Doc_Nommbre = %s OR Doc_Matricula = %s ",query_vals)
			mydb.commit()
			print(nombre_Estudiante + " has been deleted")

		elif Sel_option == "5":
			print("")
			print("Actualizar Profesores")
			nombre_Estudiante = input(str("Indique el nuevo documento de la Profesor que desea actualizar : "))
			tipoDoc_Estudiante = input(str("Indique el tipo de documento del Profesor a actualizar : "))
			Codigo_Estudiante = input(str("Indique el codigo de la Profesor que deseas actualizar "))
			query_vals = (nombre_Estudiante, tipoDoc_Estudiante,Codigo_Estudiante)
			cursor.execute("UPDATE Profesores SET Doc_Documento = %s ,  Doc_TipoDocumento  = %s WHERE Doc_Matricula = %s ",query_vals)
			mydb.commit()
			
		elif Sel_option == "6":
			print('Hasta luego, vuelva pronto')
			break
		else:
			print("No selecciono una Opcion forma correcta intente de nuevo")

def Secciones x Materia():
	while 1:
		print("")
		print("selecciono Secciones x Materia, indique que opcion desea realizar")
		print("1. Consultar tabla Actual")
		print("2. Resgistrar un nuevo seccion x materia")
		print("3. Mostrar toda la tabla")
		print("4. Eliminar una seccion x materia")
		print("5. Actualizar la tabla")
		print("6. Logout")

		Sel_option = input(str("Option : "))
		if Sel_option == "1":
			print("")
			print("Consultar Secciones x Materia")
			Codigo_Estudiante = input(str("Indique el codigo de la matricula del estudiante que deseas ver, en caso de no saber cual coloque un cero : "))
			nombre_Estudiante = input(str("Indique el codigo de la secciones del Profesor que deseas ver : "))
			Codigo_matricula_estudiante = input(str("Indique el nombre del estudiante : "))
			query_vals = (Codigo_Estudiante,nombre_Estudiante, Codigo_matricula_estudiante)
			cursor.execute("select A.Periodo , B.Doc_Nommbre, B.Doc_Apellido, C.Est_Nommbre , C.Est_Apellido, D.Car_Nombre_DESC , E.Mat_Nombre_DESC FROM est_materia as A inner join docentes as B on A.Materia_CD = B.Doc_Secciones inner join estudiante as C on A.Est_Matricula = C.estudiante innerjoin carreras as D on C.Est_Carrera = D.Car_Nombre_CD inner join materias as E on B.Doc_Secciones = E.Mat_Nombre_CD WHERE C.Est_Matricula = %s or B.Doc_Secciones = %s or C. Est_Nommbre LIKE %s  ",query_vals)
			mydb.commit()
			for x in cursor:
				print(x)
				print('Para saber cuales son todas las que hay, selecione la opcion 3')
		
			
		elif Sel_option == "2":
			print("")
			print("Resgistrar una seccion x materia")
			Matricula_Estudiante = input(str("Ingrese matricula del estudiante, en caso de no existir. debe crear al estudiante primero : "))
			Matricula_seccion = input(str("Ingrese el codigo de la seccion del profesor, en caso de que no exista la seccion tiene que cearlo en carreras primero : "))
			query_vals = ("MAY_AGO-2021",Matricula_Estudiante,Matricula_seccion)
			cursor.execute("INSERT INTO Est_Materia ( Periodo,Est_Matricula,Materia_CD) VALUES (%s,%s,%s)",query_vals)
			mydb.commit()
			print(" ha sido registrado con exito. en caso de volver a ver la tabla, seleciona la opcion 3")

		elif Sel_option == "3":
			print("")
			print('la tabla es la siguiente')
			cursor.execute("Select * from Est_Materia")
			for x in cursor:
				print(x)

		elif Sel_option == "4":
			print("")
			print("Borrar Secciones x Materia")
			nombre_Estudiante = input(str("Indique al estudiante a borrar : "))
			query_vals = (nombre_Estudiante,"NINGUNO")
			cursor.execute("DELETE FROM Est_Materia WHERE Est_Matricula = %s OR Materia_CD = %s ",query_vals)
			mydb.commit()
			print(" has been deleted")

		elif Sel_option == "5":
			print("")
			print("Actualizar Secciones x Materia")
			nombre_Estudiante = input(str("Indique la nueva seccion del estudiante : "))
			Codigo_Estudiante = input(str("Indique el codigo del estudiante que deseas actualizar "))
			query_vals = (nombre_Estudiante,Codigo_Estudiante)
			cursor.execute("UPDATE Est_Materia SET Materia_CD = %s WHERE Est_Matricula = %s ",query_vals)
			mydb.commit()
			
		elif Sel_option == "6":
			print('Hasta luego, vuelva pronto')
			break
		else:
			print("No selecciono una Opcion forma correcta intente de nuevo")

def menu():
	while 1:
		print("")
		print("Bienvenido Seleciona Opcion a Trabajar")
		print("1. Materias")
		print("2. Carreras")
		print("3. Materias x Carreras")
		print("4. Estudiantes")
		print("5. Profesores")
		print("6. Logout")

		Sel_option = input(str("Option : "))
		if Sel_option == "1":
			Materias()
		elif Sel_option == "2":
			Carreras()
		elif Sel_option == "3":
			Materias_x_Carreras()
		elif Sel_option == "4":
			Estudiantes()
		elif Sel_option == "5":
			Profesores()
		elif Sel_option == "6":
			print('Hasta luego, vuelva pronto')
			break
		else:
			print("No selecciono una Opcion forma correcta intente de nuevo")


"""
 -------------------------------------------------
 -------------------------------------------------
            	INICIO DEL PROGRAMA 
 -------------------------------------------------
 -------------------------------------------------
"""


def Inicio_Seccion():
    print("*********************************************************")
    print("********** sistema de Gestión Universitaria *************")
    print("*********************************************************")
    x=0
    while x < 2:
	    nombre_usuario = input(str("Ingrese su nombre de usuario : "))
	    
	    if nombre_usuario == "USUARIO1":
	    	intentos = 0
	    	while intentos < 4:
	    		if intentos == 3:
	    			print('usuario bloqueado')
	    			x=3
	    			break
	    		
	    		password = input(str(" Digite la Clave : "))
	    		if password == "12345":
	    			Menu()
	    		
	    		else:
	    			print("Clave erronea, intente otra vez !")
	    			intentos = intentos + 1
	    else:
	        print("Usuario no Reconocido intente otra vez") 

Inicio_Seccion()	        



