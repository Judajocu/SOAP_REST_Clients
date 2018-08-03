import json
import unirest

def Menu():
    print("Servicio REST")
    print("1-Para ver los post de un usuario en particular")
    print("2-Para crear un post")
    print("3-Para salir")

    x = input("Digite una opcion")
    Client(x)

def Client(x):
    if x == 1:
        y = input("Digite un nombre de usuario")
        data = unirest.get('http://localhost:4567/RESTy/una_rutica_ahi_jevi/{}'.format(y),
                           headers={"Accept": "application/json"})
        print(data.body)
        return Menu()

    elif x == 2:
        username = raw_input("Digite un nombre de usuario")
        title = raw_input("Digite un titulo para el post")
        body = raw_input("Digite un cuerpo para el post")
        image = raw_input("Digite una ruta donde se encuentra la imagen")
        data2 = unirest.post('http://localhost:4567/RESTy/La_ruta_al_POST/{}'.format(username),
                             headers={"Content-Type": "application/json", "Accept": "application/json"},
                             params=json.dumps({"Title": title, "Body": body, "Image": image}))
        print(data2.body)
        return Menu()

    else:
        return 0

if __name__ == '__main__':
    Menu()