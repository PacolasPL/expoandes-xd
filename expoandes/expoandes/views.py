from django.http import HttpResponse
import datetime
def prueba(request): # Vista primera, nos devuelve una respuesta con el texto del return

    return HttpResponse('Hola weys xd')

def hora(request):
    fecha = datetime.datetime.now()

    formato = '<html><body><h1> La fecha y hora son %s </h1></body></html>' % fecha
    return HttpResponse(formato)
def edad(request, anio, edad):

    periodo = anio - 2021
    edad_futura = edad + periodo

    formato = "<html><body><h3><center>En el año %s tendras %s </center></h3></body></html>" %(anio, edad_futura, "Micolas es pro")
    return HttpResponse(formato)
