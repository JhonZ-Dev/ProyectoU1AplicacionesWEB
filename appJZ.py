# importar la libreria flask
from flask import Flask, render_template
from flask import Flask, redirect, request,render_template, url_for

app = Flask(__name__, template_folder='templates') #Creamos una variable de tipo app y pedimos a la funcion Flask


@app.route('/')
def principal():
    """
    Esta función esta encarga de abrir la página principal
    para luego poder llamar a las demas subpáginas

    Returns:
        Retorna la página principal, denomindad index.html
    """
    #Index es nuestra página principal
    return render_template('/index.html') 

@app.route('/loginProfesores')
 #Funcion llamada al formulario / login profesores
def formulario():
    """
    Funcion para agregar un formulario de ingreso 
    para un profesor

    Returns:
        Retorna a loginProfesores.html
    """
    return render_template('/loginProfesores.html')

@app.route('/asistencia')
 #Funcion llamada asistencia
def asistencia():
    """
    Función para marcar la asistencia del alumno
    está subpagina le pertenece al profesor

    Returns:
        retorna la subpágina asistencia.html
    """
    return render_template('/asistencia.html')    

@app.route('/notas')
 #Funcion llamada notas 
def notas():
    """
    Función denominada notas, la cual tiene la función para 
    agregar notas del primer, segundo y tercer parcial
    del estudiante.

    Returns:
        retorna la subpágina de notas.html
    """
    return render_template('/notas.html')  

@app.route('/info')
 #Funcion llamada infro
def info():
    """
    Funcion encarga para ver la información del 
    estudiante (Solo el docente tiene acceso)

    Returns:
        retorna a la página info.html
    """
    return render_template('/info.html')


@app.route('/index')
def regresar():
    """
    Funcion encargada para hacer funcional a los botones
    de regreso a la página principal

    Returns:
        retorna index.html (Pagina principal)
    """
    return render_template('/index.html')    


#*******************************ESTUDIANTES******************
#Para estudiantes ---****De aqui empieza *******
@app.route('/loginEstudiantes')
def regresarEstudiantes():
    """
    Funcion destinada al regreso de los estudiante

    Returns:
        retorna el login del estudiante
    """
    return render_template('/loginEstudiantes.html')

#infoEstudiante.
@app.route('/infoEstudiantes')
def infoEstudiante():
    """
    Está funcion tiene la opcion de ir a ver su información
    del estudiante

    Returns:
        retorna la información del estudiante
    """
    return render_template('/infoEstudiantes.html')   


#notasEstudiante
@app.route('/notasEstudiante')
def notasEstudiantes():
    """
    Función destinada a ver sus calificaciones del estudiante

    Returns:
        retorna las notas del estudiante.
    """
    return render_template('/notasEstudiante.html')     




#Utilizaremos listas 
agregarTareas = []
#Controlador para agregar las tareas del estudiante
@app.route('/tareasEst' )
#Función principal que llamará a la página HTML y encapsula
#la variable de nuestro arreglo
def tareasEst():
    return render_template('tareasEst.html', tareasLista = agregarTareas)
#Controlador el cuál almacenara los elementos que ingresemos
@app.route('/enviar',  methods=['GET','POST'])
def enviar():
    """
    Esta función tiene el objetivo de almanenar
    los datos dentro de la lista

    Returns:
        Con redirect(url_for()) estamos enviando el control a un método que debe procesar la 
        lógica del mismo, preparar los datos y por último hacer el render_template
    """
    if(request.method == "POST"):
        tareas = request.form['tarea']
        correos = request.form['correo']
        prioridades = request.form['prioridad']
        agregarTareas.append({'tarea': tareas, 'correo': correos, 'prioridad': prioridades })
        return redirect(url_for('tareasEst'))

#Controlador el cuál borrara la lista de tareas
@app.route('/borrar', methods=["GET","POST"])
#Función borrar la cuál limpiara todos los elementos que se
#  encuentren almacenados en nuestra lista
def borrar():
    """
    Funcion encargada para limpiar la lista anteriormente ya llenada
    por el usuario.El método POST introduce los parámetros en la
    solicitud HTTP para el servidor. Por ello, no quedan visibles
     para el usuario.

    Returns:
    Con redirect(url_for()) estamos enviando el control a un método
    que debe procesar la lógica del mismo, preparar los datos y por
     último hacer el render_template
    """
    if(request.method == "POST"):
        agregarTareas.clear()
        return redirect(url_for('tareasEst'))


# ejecutar
if __name__ == '__main__':
    app.run(debug=True)