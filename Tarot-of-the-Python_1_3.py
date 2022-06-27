import msvcrt
import os
import random
from datetime import datetime
from time import sleep
import tarot_cards

clear = lambda: os.system('cls') #clears console, needed for neat display of info
drawn_cards = []
notes_to_add = []
major_arcana = tarot_cards.MajorArcana()
minor_arcana = tarot_cards.MinorArcana()

def reset_deck():
    tarot_deck = {
        # Suit of Cups
        'cup1': minor_arcana.Cup1(),
        'cup2': minor_arcana.Cup2(),
        'cup3': minor_arcana.Cup3(),
        'cup4': minor_arcana.Cup4(),
        'cup5': minor_arcana.Cup5(),
        'cup6': minor_arcana.Cup6(),
        'cup7': minor_arcana.Cup7(),
        'cup8': minor_arcana.Cup8(),
        'cup9': minor_arcana.Cup9(),
        'cup10':minor_arcana.Cup10(),
        'cupjack': minor_arcana.CupJack(),
        'cupknight': minor_arcana.CupKnight(),
        'cupqueen': minor_arcana.CupQueen(),
        'cupking': minor_arcana.CupKing(),

        # Suit of Coins
        'coin1': minor_arcana.Coin1(),
        'coin2': minor_arcana.Coin2(),
        'coin3': minor_arcana.Coin3(),
        'coin4': minor_arcana.Coin4(),
        'coin5': minor_arcana.Coin5(),
        'coin6': minor_arcana.Coin6(),
        'coin7': minor_arcana.Coin7(),
        'coin8': minor_arcana.Coin8(),
        'coin9': minor_arcana.Coin9(),
        'coin10':minor_arcana.Coin10(),
        'coinjack': minor_arcana.CoinJack(),
        'coinknight': minor_arcana.CoinKnight(),
        'coinqueen': minor_arcana.CoinQueen(),
        'coinking': minor_arcana.CoinKing(),

        # Suit of Swords
        'sword1': minor_arcana.Sword1(),
        'sword2': minor_arcana.Sword2(),
        'sword3': minor_arcana.Sword3(),
        'sword4': minor_arcana.Sword4(),
        'sword5': minor_arcana.Sword5(),
        'sword6': minor_arcana.Sword6(),
        'sword7': minor_arcana.Sword7(),
        'sword8': minor_arcana.Sword8(),
        'sword9': minor_arcana.Sword9(),
        'sword10':minor_arcana.Sword10(),
        'swordjack': minor_arcana.SwordJack(),
        'swordknight': minor_arcana.SwordKnight(),
        'swordqueen': minor_arcana.SwordQueen(),
        'swordking': minor_arcana.SwordKing(),

        # Suit of Wands
        'wand1': minor_arcana.Wand1(),
        'wand2': minor_arcana.Wand2(),
        'wand3': minor_arcana.Wand3(),
        'wand4': minor_arcana.Wand4(),
        'wand5': minor_arcana.Wand5(),
        'wand6': minor_arcana.Wand6(),
        'wand7': minor_arcana.Wand7(),
        'wand8': minor_arcana.Wand8(),
        'wand9': minor_arcana.Wand9(),
        'wand10':minor_arcana.Wand10(),
        'wandjack': minor_arcana.WandJack(),
        'wandknight': minor_arcana.WandKnight(),
        'wandqueen': minor_arcana.WandQueen(),
        'wandking': minor_arcana.WandKing(),

        # # Major Arcanas
        'maj_fool': major_arcana.TheFool(),
        'maj_magician': major_arcana.TheMagician(),
        'maj_priestess': major_arcana.TheHighPriestess(),
        'maj_emperor': major_arcana.TheEmperor(),
        'maj_hierophant': major_arcana.TheHierophant(),
        'maj_lovers': major_arcana.TheLovers(),
        'maj_chariot': major_arcana.TheChariot(),
        'maj_strength': major_arcana.Strength(),
        'maj_hermit': major_arcana.TheHermit(),
        'maj_wheel': major_arcana.TheWheelOfFortune(),
        'maj_balance': major_arcana.Balance(),
        'maj_hangedman':major_arcana.TheHangedMan(),
        'maj_death' : major_arcana.Death(),
        'maj_temperance': major_arcana.Temperance(),
        'maj_devil': major_arcana.TheDevil(),
        'maj_tower': major_arcana.TheTower(),
        'maj_star': major_arcana.TheStar(),
        'maj_moon': major_arcana.TheMoon(),
        'maj_sun': major_arcana.TheSun(),
        'maj_judgement': major_arcana.Judgement(),
        'maj_world': major_arcana.TheWorld()
        }
    return dict(tarot_deck)


tarot_deck = reset_deck()
drawn_cards_string = ''
choices_displayed = False


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
    print((' ' * 18) + 'Cards cleared.' + (
                ' ' * 12))
    print('\n')
    print('*' * 50)





def display_choices():
    if not choices_displayed:
        print(f'Type D to draw a card  |  Type C to clear list of cards \nType N to take notes   |  Type S to save to text file.\nType X to exit program |')


def display_reading(to_save = False):
    #
    letter_check = (str(msvcrt.getch()).upper()) #CHECKS FROM KEYPRESS WITHOUT WAITING FOR ENTER
    letter_check = letter_check[2] #GETS THE VALUE FROM THE STRING WE JUST GENERATED

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
        available_cards_names = []

        for item in available_cards:
            available_cards_names.append(item[1])        
        
        if len(available_cards_names) > 0:
            picked_card = random.choice(available_cards_names)  # Picks a random card from the [list] we created in the above line
            #print(picked_card)

            to_remove = []

            for k, v in tarot_deck.items():
                if v == picked_card:
                   to_remove.append(k)
                   card_name = (v.show_name())
                   drawn_cards.append(card_name)
            
            for entry in to_remove:
                tarot_deck.pop(entry)

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
        global notes_to_add
        print(','.join(notes_to_add))
        print('\n--------------------Enter your notes or type X to exit notepad------------------------')
        print('\n---------------------You can also type P to clear the notes.--------------------------')
        our_input = input()
        while our_input.upper() != 'X' and our_input.upper() != 'P' :
            notes_to_add.append(our_input)
            clear()
            print('. '.join(notes_to_add))
            print('\n--------------------Enter more notes or type X to exit notepad------------------------')
            print('\n---------------------You can also press P to clear the notes.-------------------------')

            our_input = input(': ')
        if our_input.upper() == 'P':
            print('\n-------------------Are you sure you to want to erase the notes?------------------------')
            print('\n-----------------Type Y to confirm deletion, Type N to keep notes.---------------------')

            if our_input.upper() == 'Y':
                notes_to_add.clear()
            else:
                pass

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
