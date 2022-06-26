import msvcrt
import os
import random
from datetime import datetime
from time import sleep

clear = lambda: os.system('cls')

drawn_cards = []
notes_to_add = []


def reset_deck():
    tarot_deck = {
        # Suit of Cups
        'cup1': "Ace of Cups",
        'cup2': "Two of Cups",
        'cup3': "Three of Cups",
        'cup4': "Four of Cups",
        'cup5': "Five of Cups",
        'cup6': "Six of Cups",
        'cup7': "Seven of Cups",
        'cup8': "Eight of Cups",
        'cup9': "Nine of Cups",
        'cup10': "Ten of Cups",
        'cupjack': "Jack of Cups",
        'cupknight': "Knight of Cups",
        'cupking': "King of Cups",
        'cupqueen': "Queen of Cups",

        # Suit of Coins
        'coin1': "Ace of Coins",
        'coin2': "Two of Coins",
        'coin3': "Three of Coins",
        'coin4': "Four of Coins",
        'coin5': "Five of Coins",
        'coin6': "Six of Coins",
        'coin7': "Seven of Coins",
        'coin8': "Eight of Coins",
        'coin9': "Nine of Coins",
        'coin10': "Ten of Coins",
        'coinjack': "Jack of Coins",
        'coinknight': "Knight of Coins",
        'coinking': "King of Coins",
        'coinqueen': "Queen of Coins",

        # Suit of Swords
        'sword1': "Ace of Swords",
        'sword2': "Two of Swords",
        'sword3': "Three of Swords",
        'sword4': "Four of Swords",
        'sword5': "Five of Swords",
        'sword6': "Six of Swords",
        'sword7': "Seven of Swords",
        'sword8': "Eight of Swords",
        'sword9': "Nine of Swords",
        'sword10': "Ten of Swords",
        'swordjack': "Jack of Swords",
        'swordknight': "Knight of Swords",
        'swordking': "King of Swords",
        'swordqueen': "Queen of Swords",

        # Suit of Wands
        'wand1': "Ace of Wands",
        'wand2': "Two of Wands",
        'wand3': "Three of Wands",
        'wand4': "Four of Wands",
        'wand5': "Five of Wands",
        'wand6': "Six of Wands",
        'wand7': "Seven of Wands",
        'wand8': "Eight of Wands",
        'wand9': "Nine of Wands",
        'wand10': "Ten of Wands",
        'wandjack': "Jack of Wands",
        'wandknight': "Knight of Wands",
        'wandking': "King of Wands",
        'wandqueen': "Queen of Wands",

        # Major Arcanas
        'maj_fool': 'The Fool',
        'maj_magician': 'The Magician',
        'maj_priestess': 'The High Priestess',
        'maj_emperor': 'The Emperor',
        'maj_hierophant': 'The Hierophant',
        'maj_lovers': 'The lovers',
        'maj_chariot': 'The Chariot',
        'maj_strength': 'Strength',
        'maj_hermit': 'The Hermit',
        'maj_wheel': 'The Wheel of Fortune',
        'maj_balance': 'Balance',
        'maj_death': 'Death',
        'maj_temperance': 'Temperance',
        'maj_devil': 'The Devil',
        'maj_tower': 'The Tower',
        'maj_star': 'The Star',
        'maj_moon': 'The Moon',
        'maj_sun': 'The Sun',
        'maj_judgement': 'The Judgement',
        'maj_world': 'The World'
        }
    return dict(tarot_deck)


tarot_deck = reset_deck()
drawn_cards_string = ''
choices_displayed = False;


def sign_it():
    print("""\
                                                                                                 ,╓╗@╣╢`
                                                                                             ,╦@╢▒▒▒▒▒▒▒
                                                                                           ,╬▒▒▒▒▒▒▒▒▒▒▒
                                                                                         ,g╣╣▒▒▒▒▒▒▒▒▒▒▒
                                                                                        ╠╢╣╣╣▒▒▒▒▒▒▒▒▒Ñ
                                                                                       Æ╢╢╣╣╣▒▒▒▒▒▒▒▒╣
                                                                            ,╓,,  ,╖╓@╢╣╢╢╣╣╣▒▒▒▒▒▒╣┘
                                                                           ▓╢╢╢╢╢╢╢╢╢╢╢╣╢╢╣╣╣▒▒▒▒▒╢┘
                                                                          J╢╢╢╢╢╢╢╢╢╢╢╢╣╢╢╣╣╣▒▒▒▒▒
                                                                            ▓▓╣╢╢╢╢╢╢╢╢╣╢╢╣╣╣▒▒╬╜
                                                                               ╙▓╢╢╢╢╢╢╣╢╢╣╣▓╩
             ⌐                                              ,,,,,               ▓╢╢╢╢╢╢╣▒▒▒╣╖,
            Æ╫                    ,                          j▌                ▓╢▓╢╢╢╢▓╨╬╢╣╣╣▒▒╢@╦,
           Æ╛ ╫                   ╟                          j▌            ,,æ▓▓╜  ╙╬╜     "╙╨╩╩╩╬╩╝
          ╔╜   ╬                  ╟                          j▌            ╙╙╙
         ╔╜     ╬        ,╦m╗╓  ╦╦1╦╗╗  ╦╦r ╓╗r   ,╦mm╗╓     j▌           ╦╦═    ╦╦═   ╦╦╦╦╕   ╒╦╗╗╗
        ╔╝``²²```╬       ╣   ╜    3       ▓╜     ▓└     ║╕   j▌            ]F     ]L     ╙N     φ┘
       ╓╝         ╣       ╙Mm,    7       ▌     ╟∩  ╫╣⌐  ▒   j▌            ]F     ]L      └@   ╫`
      ╒▓           @    ┌⌐   ║∩   ╟       ▌      ▓      ╔╩   j▌        ╞∩  ]▌     ╣L        ╬ ╬
    ╩╩╩╩╩         M╝╝M` "╨MM╝╙    ╩╩M   ╩╩╩╩═     ╙╨MM╝╙    ╨╨╨╨╜╜╜╜╜╜╜╜    ╙╩MM╜  ╝*        ╣
                        """)


def base_msg():
    clear()
    print('*' * 50)
    print('\n')
    print(('' * 12) + 'Cards cleared.' + (
                ' ' * 12))
    print('\n')
    print('*' * 50)





def display_choices():
    if not choices_displayed:
        print(f'Type D to draw a card  |  Type C to clear list of cards \nType N to take notes   |  Type S to save to text file.\nType X to exit program |')


def display_reading(to_save = False):
    #
    letter_check = (str(msvcrt.getch()).upper()) #CHECKS FROM KEYPRESS WITHOUT WAITING FOR ENTER
    letter_check = letter_check[2] #GETS THE VALUE FROM THE STRING WE JSUT GENERATED

    global drawn_cards_string

    def display_results():
        if len(drawn_cards) > 1:
            print(('*' * 9) + ' Cards you have drawn so far  : ' + (
                        '*' * 9) + f'\n \n {drawn_cards_string}\n  \n')  # Prints the value of the dict entry we just randomly picked
            print('*' * 50)

        else:
            print(('*' * 19) + 'Your card : ' + (
                        '*' * 19) + f'\n \n {drawn_cards_string} \n \n')  # Prints the value of the dict entry we just randomly picked
            print('*' * 50)
    
    def save_it_up():
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        global notes_to_add, drawn_cards_string
        pc_user = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        with open(f"{pc_user}\\TarotReadings.txt", "a") as save:
            save.write('\n ' + ('*' * 37))
            save.write(('*' * 9) + 'Reading  ' + dt_string + ('*' * 46) + f'\n {drawn_cards_string}\n')
            save.write(f'\nNotes : \n{notes_to_add}')
            save.write('\n')
        clear()
        print(f'Saved to {pc_user}\\TarotReadings.txt \n')
        display_results()

    if (to_save == True):
        save_it_up()

    def draw_a_card():
        clear()
        available_cards = list(tarot_deck.items())  # Convert iterable of {tarot_deck} to a [list]
        if len(available_cards) > 0:
            picked_card = random.choice(available_cards)  # Picks a random card from the [list] we created in the above line
            if not len(picked_card) == 0:
                tarot_deck.pop(picked_card[0])  # Removes the drawn card from available cards in {tarot_deck}
                drawn_cards.append(picked_card[1])  # Add value to [list]

        global drawn_cards_string
        drawn_cards_string = ' - '.join(drawn_cards)  # Creates a string of values on [list]
        display_results()

    def exit_app():
        clear()
        print('Are you sure you want to exit the application?')
        print('')
        print('Press S to save before exiting. \nPress Q to quit. \nPress B to go back to menu.')
        letter_check = (str(msvcrt.getch()).upper()) #CHECKS FROM KEYPRESS WITHOUT WAITING FOR ENTER
        letter_check = letter_check[2] #GETS THE VALUE FROM THE STRING WE JSUT GENERATE

        if letter_check == 'B':
            clear()
            display_results()
            pass

        elif letter_check== 'S':
            save_it_up()
            letter_check = 'Q'  # ONCE IT'S DONE SAVING, IT PASSES IN Q AND QUITS

        if letter_check == 'Q':
            # thank_yous = 'Farewell traveler.'
            # for i in thank_yous:
            #     (thank_yous) = (thank_yous[1:])
            #     print(thank_yous)
            #     sleep(0.77)

            sign_it()
            if not input(''):
                exit()

    def clear_board():
        drawn_cards.clear()
        reset_deck()
        clear()
        base_msg()

    def open_notes():
        clear()
        print('Enter your notes : ')
        our_input = input()
        while our_input.upper() != 'X':
            notes_to_add.append(our_input)
            clear()
            print(notes_to_add)
            print('\n--------------------Enter more notes, or type X to exit notepad------------------------.')
            our_input = input(': ')
        clear()
        display_results()

    global choices_displayed
    choices_displayed = False 
    if (letter_check == 'D'):
        draw_a_card()

    elif (letter_check == 'X'):
        exit_app()

    elif (letter_check== 'C'):
        clear_board()

    elif (letter_check == 'N'):
        open_notes()

    elif (letter_check== 'S'):
        save_it_up()
    else:
        choices_displayed = True

sign_it()

while (len(tarot_deck) > 0):  # KEEPS PROGRAM RUNNING WHILE WE STILL HAVE CARDS IN DECK
    display_choices()
    display_reading()
display_reading(to_save = True) #Saves our file once we break out of loop

print('No more cards to draw!')
pc_user = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
print(f'Saved to {pc_user}\\TarotReadings.txt \n')


sleep(137)
