from imgurpython import ImgurClient as img
from concurrent.futures import ThreadPoolExecutor as thpool
import urllib.request as url_Req
import timeit as t

secreto_Cliente = "5f8c3cce299db5e26a2eb96b0b7809a82805c9ad"
id_Cliente = "bfa0e227a1c5643"
clientes = img(id_Cliente, secreto_Cliente)

def descarga_url_img(link, cont):
    print(f"\nLink {cont}: ", link)
    nombre_img = link.split("/")[3]
    formato_img = nombre_img.split(".")[1]
    nombre_img = nombre_img.split(".")[0]

    print("Nombre: ", nombre_img, "\nFormato: ", formato_img)
    
    url_local = f"/Users/lombr/OneDrive/Imágenes/{nombre_img}.{formato_img}"
    url_Req.urlretrieve(link, url_local)

def main():
    cont = 0
    id_Album = "bUaCfoz"
    imagenes = clientes.get_album_images(id_Album)

    with thpool(max_workers=10) as executor:
        for imagen in imagenes:
            cont += 1
            executor.submit(descarga_url_img, imagen.link, cont)

if __name__ == "__main__":
    print("\nTiempo de descarga {}".format(t.Timer(main).timeit(number=1)))