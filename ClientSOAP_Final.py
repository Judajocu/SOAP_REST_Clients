from zeep import Client

def Menu():
    print("Servicio SOAP")
    print("1-Para ver los post de un usuario en particular")
    print("2-Para crear un post")
    print("3-Para salir")

    x = input("Digite una opcion")
    client = Client('http://localhost:7777/ws/WebService_sopy?wsdl')
    ClientSOAP(x, client)


def ClientSOAP(x,client):
    if x == 1:
        y = raw_input("Digite un nombre de usuario para ver sus posts")
        data = client.service.getUserPosts(y)
        print data
        Menu()
    elif x == 2:
        title = raw_input("Digite un titulo para el post a crear")
        body = raw_input("Digite un cuerpo para el post")
        image = raw_input("Digite una ruta para la imagen a postear")
        username = raw_input("Digite el usuario que es autor del post")
        data2 = client.service.Postear(title,
                                       body,
                                       image,
                                       username)
        print data2
        Menu()
    else:
        return 0

if __name__ == '__main__':
    Menu()