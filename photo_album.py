
import sys
from data_fetcher import display_album

def main():
    """ main function -- checks for the valid id and excute photo_album

    :return:
    """
    #House keeping
    # The client should supply the argument albumid


    input_id = None

    try:
        #only send integer id
        assert len(sys.argv) == 2
        input_id = int(sys.argv[1])
        assert (isinstance(input_id, int)  and input_id > 0)
        for element in display_album(input_id):
            print(element)
    except AssertionError:
        if input_id:
            print(f'invalid id!  Your input:{input_id} is not positive integer! Try again..')
        else:
            print('Oops! You need to provide argument. Try again ..')

if __name__ =="__main__":
    main()




