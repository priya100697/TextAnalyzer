from Model import train_using_default_dict
from Model import test
from readFile import read_file

if __name__ == "__main__":

    read_file('Chat_with_Bhai_jio.txt')
    train_using_default_dict('chat.txt')
    #train_using_default_dict('Sample.txt')

    print("Enter sample text to be searched--")
    user_input = str(input())
    test(user_input)
