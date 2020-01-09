from iota import Iota
import pprint


characters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '9')
char_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ9"


node = "https://community.tanglebay.org"


#####################################################################################################################


print('\n'*50)
orig_seed = input('Please paste your seed (ALL uppercase and no spaces before/after/inside)\n')



def main():

    user_choice = input("\n"*3 + 'Please chose one of the following (1-4): \n1 - One wrong character\n2 - One extra character \n3 - Two extra characters \n4 - One missing character\nExit - CTRL + C' +'\n'*2)
    if user_choice =="1":
        one_wrong_char()
    elif user_choice =="2":
        one_extra_char()
    elif user_choice =="3":
        two_extra_char()
    elif user_choice =="4":
        one_missing_char()
    else:
        print("\n"*50+'Error, type 1-4 or "CTRL + C" to exit')
        main()




def one_wrong_char():
    """ 
    Summary: Changes one character of the seed. 
  
    Goes through the seed in a brute force way and change one character before checking the seed balance
    Stops once it finds a seed with balance > 0 IOTA
  
    Parameters: 
    None
  
    Returns: 
    Hopefully your seed
  
    """
    workseed = list(orig_seed)
    temp_seed = list(orig_seed)
    running_count=0
    char_index=0

    while char_index < len(orig_seed):

        if running_count == len(characters):
            temp_seed[char_index]= workseed[char_index]
            running_count = 0
            char_index += 1
        else:
            temp_seed[char_index] = characters[running_count]
            try_seed = ''.join(temp_seed) # From list to string

            if Iota(node, try_seed).get_account_data()['balance'] > 0:
                print('\n'*30+'Found your seed! \n\nSeed is:'+ try_seed + '\n\nWith the following information: ')
                print(Iota(node, try_seed).get_account_data())
                
                user_response()
                running_count += 1

            else:
                print('\n\nTrying seed: '+ try_seed)
                print(Iota(node, try_seed).get_account_data())
                running_count += 1




def one_extra_char():
    """ 
    Summary: Removes one character from the seed. 
  
    Goes through the seed in a brute force way and remove one character before checking the seed balance
    Stops once it finds a seed with balance > 0 IOTA
  
    Parameters: 
    None
  
    Returns: 
    Hopefully your seed
  
    """
    workseed = list(orig_seed)
    running_count = 1
    temp_seed = []

    while running_count <= len(orig_seed): # <= because we start count at 1
        temp_seed = list(workseed[0:running_count-1]) + list(workseed[running_count:])
        try_seed = ''.join(temp_seed)

        if Iota(node, try_seed).get_account_data()['balance'] > 0:
            print('\n'*30+'Found your seed! \n\nSeed is:'+ try_seed + '\n\nWith the following information: ')
            print(Iota(node, try_seed).get_account_data())
            
            user_response()
            running_count += 1

        else:
            print('\n\nTrying seed: '+ try_seed)
            print(Iota(node, try_seed).get_account_data())

            running_count += 1




def two_extra_char():
    """ 
    Summary: Removes two characters from the seed. 
  
    Goes through the seed in a brute force way and removes two characters before checking the seed balance
    Stops once it finds a seed with balance > 0 IOTA
  
    Parameters: 
    None
  
    Returns: 
    Hopefully your seed
  
    """
    workseed = list(orig_seed)
    running_count = 1
    second_running_count = 1
    first_slice = []
    second_slice = ""
    combined_seed = ""

    while running_count <= len(orig_seed):
        first_slice = list(workseed[0:running_count-1]) + list(workseed[running_count:])
        running_count += 1
        second_running_count = 1
        while second_running_count <= len(workseed)-1:
            second_slice = list(first_slice[0:second_running_count-1]) + list(first_slice[second_running_count:])
            try_seed = ''.join(second_slice)
            
            if Iota(node, try_seed).get_account_data()['balance'] > 0:
                print('\n'*30+'Found your seed! \n\nSeed is:'+ try_seed + '\n\nWith the following information: ')
                print(Iota(node, try_seed).get_account_data())

                user_response()
                second_running_count += 1

            else:
                print('\n\nTrying seed: '+ try_seed)
                print(Iota(node, try_seed).get_account_data())

                second_running_count += 1




def one_missing_char():
    """ 
    Summary: Tries to find the missing character . 
  
    Goes through the seed in a brute force way to find the missing character
    Checks all characters in all indexes and stops once it finds a seed with balance > 0 IOTA
  
    Parameters: 
    None
  
    Returns: 
    Hopefully your seed
  
    """
    workseed = list(orig_seed)
    running_count = 0
    char_index = 0
    temp_seed = []

    while char_index <= len(orig_seed):
        
        if running_count == len(characters):
            running_count = 0
            char_index += 1

        else: 
            temp_seed = []
            temp_seed.append(workseed[:char_index] + [char_string[running_count]] + workseed[char_index:])
            try_seed = ''.join(temp_seed[0])
            
            if Iota(node, try_seed).get_account_data()['balance'] > 0:
                print('\n'*30+'Found your seed! \n\nSeed is:'+ try_seed + '\n\nWith the following information: ')
                print(Iota(node, try_seed).get_account_data())

                user_response()
                running_count += 1

            else:
                print('\n\nTrying seed: '+ try_seed)
                print(Iota(node, try_seed).get_account_data())

                running_count += 1



def user_response():
    print('\n\nDo you want to continue?')
    input('Respond anything to continue, or "CTRL + C" to exit\n')




main()

