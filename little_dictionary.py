def init_database():
    global database_dict
    datafile = open('dictionary.csv')   #reading data from csv file
    database = datafile.readlines()
    datafile.close()

    database_list = [line.split(' | ') for line in database]
    database_dict = {line[0]:(line[1],line[2]) for line in database_list}   #changing string data into dictionary

def print_explanation():
    print_appelation_list()
    print('Type appelation from list above to get a definition.')
    appelation_chosen = input('Your choice: ' + '\033[32m')
    print('\033[0m' + 'Definition:')
    definition_of_appelation = database_dict.get(appelation_chosen, ('\033[31m' + "You didn't choose appelation from the available list!" + '\033[0m', '\033[31m' + 'not available.' + '\033[0m'))
    print(appelation_chosen, '-', definition_of_appelation[0] + ' Source: ' + definition_of_appelation[1])

def add_new_def():
    global database_dict
    print('You are entering new data!')
    new_data = []
    new_data.append(input('Type appellation: '))
    new_data.append(input('Type definition: '))
    new_data.append(input('Type source of information: ') + '\n')
    database_dict[new_data[0]] = (new_data[1], new_data[2]) #adding new definition to dictionary

    datafile = open('dictionary.csv', 'a')  #writing new definition to the csv file
    datafile.write(' | '.join(new_data))
    datafile.close()

def print_appelation_list():
    dict_keys = database_dict.keys()    #getting view of main dictionary keys
    dict_keys = list(dict_keys) #changing view into list
    dictionary_low_upp = {key.lower():key for key in dict_keys} #creating auxiliary dictionary of keys in lowercase: original keys
    dictionary_low_upp_keys = dictionary_low_upp.keys()  #getting view of auxiliary dictionary keys
    dictionary_low_upp_keys = list(dictionary_low_upp_keys) #changing view into list
    dictionary_low_upp_keys.sort()  #sorting list of lowercase keys

    print('List of appellations in alphabetical order:')
    for key in dictionary_low_upp_keys: #printing list of original keys but in order of sorted lowercase keys
        print(dictionary_low_upp[key])
    print()

def print_def_for_chosen_letter():
    print('Choose a letter to get definitions of appelations starting with this letter:')
    chosen_letter = input('Your choice: ' + '\033[32m').lower()
    any_match = False
    if len(chosen_letter) == 1:
        for key in database_dict:
            if key.startswith(chosen_letter) or key.startswith(chosen_letter.upper()):
                definition_of_appelation = database_dict.get(key)
                print('\033[0m', key, '-', definition_of_appelation[0] + ' Source: ' + definition_of_appelation[1])
                any_match = True
        if any_match == False:
            print('\033[31m' + 'There is no appellation starting with this letter on the list!' + '\033[0m')
    else:
        print('\033[31m' + "You didn't type a single letter!" + '\033[0m')

def main():
    user_option = ''
    init_database()
    menu = '\033[33m' + """
    Dictionary for a little programmer:
    1) search explanation by appellation
    2) add new definition
    3) show all appellations alphabetically
    4) show available definitions by first letter of appellation
    0) exit""" + '\033[0m'
    print(chr(27) + "[2J")  #clear terminal screen
    while user_option != '0':   #main loop asking user for option until '0' is entered
        print(menu)
        user_option = input('\033[0m' + 'Choose option from list above [0 - 4]: ' + '\033[32m')
        print('\033[0m')
        if user_option == '1':
            print_explanation()
        elif user_option =='2':
            add_new_def()
        elif user_option == '3':
            print_appelation_list()
        elif user_option == '4':
            print_def_for_chosen_letter()
        elif user_option == '0':
            print('\033[33m' + 'Thank you for using our dictionary! See you next time.' + '\033[0m')
        else:
            print('\033[31m' + "Can't find chosen option!" + '\033[0m')

database_dict = {}
main()
