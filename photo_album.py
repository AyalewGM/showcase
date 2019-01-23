
import sys
import urllib.request, json

def photo_album(id):
    """photo album - take the id from the keyboard and print photo id and titles on the console

    :param id: An integer id
    :return:
    """
    with urllib.request.urlopen("https://jsonplaceholder.typicode.com/photos?albumId=" + str(id)) as url:
        data = json.loads(url.read().decode())

    for element in data:
        if element['id']:
            print('['+ str(element['id']) + ']'  + ' '+ element['title'])

if __name__ =="__main__":
    id = int(sys.argv[1])
    photo_album(id)



