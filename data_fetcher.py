import urllib.request
import json

def display_album(id):
    """photo album - take the id from the keyboard and print photo id and titles on the console

    :param id: An integer id
    :return:
    """

    with urllib.request.urlopen("https://jsonplaceholder.typicode.com/photos?albumId=" + str(id)) as url:
        data = json.loads(url.read().decode())

    if not data:
        print(f'There is no data corresponding to that id: {id}')

    item_list = []
    for element in data:
        if element['id']:
            item_list.append('['+ str(element['id']) + ']'  + ' '+ element['title'])

    return  item_list
