
from  data_fetcher import display_album
import sys


def test_display_album(random_id_generator):
    #print(str(random_id_generator))
    #check if the whole data is list
    assert (isinstance(display_album(random_id_generator), list))

def test_display_album_very_large_number(random_id_generator):
    # check for very large id. We should get empty list
    assert display_album(10000) == []

def test_display_album_number_for_specific_id(random_id_generator):
    # test for  the id =2
    assert display_album(2)[0].split(' ')[0].strip('[]') == '51'

def test_display_album_number_of_album():
    assert len(display_album(4)) == 50












