import webbot
from webbot import Browser
import time
import selenium
import requests
import random

def login(web):
    
    web.go_to('https://accounts.ea.com/')
    time.sleep(2) #chargement de la page
    web.add_cookie({'name' : '_ga', 'value' : 'ENTER YOUR COOKIE KEY'})
    web.add_cookie({'name' : '_gat', 'value' : 'ENTER YOUR COOKIE KEY'})
    web.add_cookie({'name' : '_gid', 'value' : 'ENTER YOUR COOKIE KEY'})
    web.add_cookie({'name' : '_nx_mpcid', 'value' : 'ENTER YOUR COOKIE KEY'})
    web.add_cookie({'name' : 'ak_bmsc', 'value' : 'ENTER YOUR COOKIE KEY'})
    web.add_cookie({'name' : 'bm_sv', 'value' : 'ENTER YOUR COOKIE KEY'})
    web.add_cookie({'name' : 'ealocale', 'value' : 'ENTER YOUR COOKIE KEY'})
    time.sleep(1) #chargement de la page

    web.go_to('https://signin.ea.com/')
    time.sleep(2) #chargement de la page
    web.add_cookie({'name' : 'webun', 'value' : 'ENTER YOUR COOKIE KEY'})
    web.add_cookie({'name' : 'isPhone', 'value' : 'ENTER YOUR COOKIE KEY'})
    web.add_cookie({'name' : 'isPogo', 'value' : 'ENTER YOUR COOKIE KEY'})
    web.add_cookie({'name' : 'JSESSIONID', 'value' : 'ENTER YOUR COOKIE KEY'})
    time.sleep(1) #chargement de la page


    time.sleep(5) #chargement de la page
    web.go_to('https://accounts.ea.com/')
    web.add_cookie({'name' : 'PLAY_LANG', 'value' : 'ENTER YOUR COOKIE KEY'})
    web.add_cookie({'name' : 'remid', 'value' : 'ENTER YOUR COOKIE KEY'})
    web.add_cookie({'name' : 'sid', 'value' : 'ENTER YOUR COOKIE KEY'})
    time.sleep(1) #chargement de la page

    web.go_to('https://www.ea.com/fifa/ultimate-team/web-app/')
    time.sleep(5) #chargement de la page

    time.sleep(5) #chargement de la page
    web.click('Login')
    time.sleep(5) #chargement de la page
    web.type('ENTER YOUR PASSWORD' , into='Password' , id='passwordFieldId')
    time.sleep(2)
    web.click('Log In')
    
def sell_players(web):

    while web.exists('HOME') == False:
        time.sleep(1)

    #if web.exists(classname='ut-tab-bar-item icon-transfer') == True :
    if web.exists('Transfers') == True :
        web.click(classname='Transfers') #
        time.sleep(5) #chargement de la page

        if web.exists('TRANSFER LIST') == True :  
            web.click('TRANSFER LIST') #go transfer list
            time.sleep(5) #chargement de la page

            if web.exists('Clear Sold') == True :  #Returns True    
                web.click('Clear Sold') #clear solds
                time.sleep(1) #chargement de la page

            if web.exists('Re-List All') == True :  #Returns True    
                web.click('Re-List All') #reliste
                time.sleep(1) #chargement de la page
                if web.exists('Yes') == True :  #Returns True  
                    web.click('Yes') #reliste
                    time.sleep(1) #chargement de la page

            if web.exists('List on Transfer Market') == True :  #Returns True    
                web.click('List on Transfer Market') #reliste
                time.sleep(1) #chargement de la page

            
            if web.exists(classname='boughtPriceValue') == True: #on recupere les coins 
                zcoins = web.driver.find_element_by_class_name('boughtPriceValue').text
                z_coins0 = zcoins.replace(' ','')
                z_coins1 = z_coins0.replace(',','')
                z_coins = int(int(z_coins1) * float(1.3))
                zz_coins = int(int(z_coins1) * float(1.1))

                if web.exists(classname="numericInput") == True :
                    web.click(classname="numericInput", number= 2) #1 is min ?
                    web.type(z_coins,classname="numericInput", number= 2, clear= False) #1 is min ?
                    time.sleep(2) #chargement de la page

                if web.exists(classname="numericInput") == True :
                    web.click(classname="numericInput", number= 1) #1 is min ?
                    web.type(zz_coins,classname="numericInput", number= 1, clear= False) #1 is min ?
                    time.sleep(2) #chargement de la page               

                    if web.exists('List for Transfer') == True :  #Returns True    
                        web.click('List for Transfer') #reliste
                        time.sleep(random.randint(1,60)) #chargement de la page
                                        
def market_price(player_name):

    #get data-baseid=" from futbin
    player_name_worked = player_name.replace(' ','-')
    found = 0
   
    player_ids = {    
    'Romain-Alessandrini': 184575,
    'daniel-james': 232104,
    'daniel-podence': 226766,
    'Jesse-Lingard': 207494,  
    'christian-pulisic': 227796,
    'gelson-martins': 227055,
    'leon-bailey': 229906,
    'RAPHAEL-DIAS-BELLOLI': 67342283,
    }

    for (name,id) in player_ids.items():
        if player_name_worked == name:
            r = requests.get('https://www.futbin.com/21/playerPrices?player={0}'.format(id))
            data = r.json()
            return_price = (int((data[str(id)]['prices']['ps']['LCPrice']).replace(',','')))
            print(id,' / ', name)
            print('last : ',return_price)
            found = 1

    if found ==0:
        print("Player name : ",player_name_worked," not found in db")
    return return_price

def buy_players(web):

    if web.exists('Home') == True :
        web.click(classname='Home') #
        time.sleep(3) #chargement de la page

    

    list_name = [['Romain-Alessandrini','77'],['Jesse-Lingard','77'],['daniel-james','77'],['daniel-podence','77'],['christian-pulisic','81'],['gelson-martins','80'],['leon-bailey','80'],['RAPHAEL-DIAS-BELLOLI','81']]
    rand_valf = int(random.randint(0,4))
    player_name = list_name[rand_valf][0]
    player_note = list_name[rand_valf][1]   

    print('on essaie d acheter :', player_name,' note : ',player_note)
    return_price = market_price(player_name)
    print('on considere le prix d achat a : ', return_price)
    time.sleep(2) #chargement de la page

    if web.exists('Transfers') == True :
        web.click('Transfers') #
        time.sleep(2) #chargement de la page

    if web.exists('SEARCH THE TRANSFER MARKET') == True :
        web.click('SEARCH THE TRANSFER MARKET') #
        time.sleep(2) #chargement de la page

    irr = 0
    web.type(player_name[0].replace('-',' '), into='Type Player Name', clear= False)
    while irr < len(player_name):
        time.sleep(0.1)
        web.type(player_name[irr].replace('-',' '), into='Type Player Name', clear= False)
        irr = irr + 1


    time.sleep(5) #chargement de la page
    
    if web.exists(classname="btn-text") == True :
        web.click(classname="btn-text", number= 8) #4 is staff
        time.sleep(5) #chargement de la page

        if web.exists('Clear') == True :
            web.click('Clear', number= 1) #1 is min ?
            time.sleep(2)
            web.click('Clear', number= 2) #1 is min ?
            time.sleep(5) #chargement de la page

        price_to_buy = int(return_price*0.90)
        if web.exists(classname="numericInput") == True :
            web.type(price_to_buy,classname="numericInput", number= 4) #1 is min ?
            time.sleep(5) #chargement de la page

            if web.exists('Search') == True :
                web.click('Search') #
                time.sleep(1) #chargement de la page

                if web.exists('Buy Now') == True :
                    web.click('Buy Now') #
                    time.sleep(2) #chargement de la page

                    if web.exists('OK') == True :
                        web.click('OK') #
                        time.sleep(2) #chargement de la page

                        if web.exists('Send to Transfer List') == True :
                            web.click('Send to Transfer List') #

                else:
                    #on re search une fois, plus tard
                    time.sleep(random.randint(2,40))
                    if web.exists('Search') == True :
                        web.click('Search') #
                        time.sleep(1) #chargement de la page

                        if web.exists('Buy Now') == True :
                            web.click('Buy Now') #
                            time.sleep(2) #chargement de la page

                            if web.exists('OK') == True :
                                web.click('OK') #
                                time.sleep(2) #chargement de la page

                                if web.exists('Send to Transfer List') == True :
                                    web.click('Send to Transfer List') #

    if web.exists('Home') == True :
        web.click(classname='Home') #

    print('sleep')
    time.sleep(random.randint(1,30)) #chargement de la page

def buy_players2(web):

    if web.exists('Home') == True :
        web.click(classname='Home') #
        time.sleep(3) #chargement de la page

    

    list_name = [['Romain-Alessandrini','77'],['Jesse-Lingard','77'],['daniel-james','77'],['daniel-podence','77'],['christian-pulisic','81'],['gelson-martins','80'],['leon-bailey','80'],['RAPHAEL-DIAS-BELLOLI','81']]
    rand_valf = int(random.randint(0,4))
    player_name = list_name[rand_valf][0]
    player_note = list_name[rand_valf][1]   

    print('on essaie d acheter :', player_name,' note : ',player_note)
    return_price = market_price(player_name)
    print('on considere le prix d achat a : ', return_price)
    time.sleep(2) #chargement de la page

    if web.exists('Transfers') == True :
        web.click('Transfers') #
        time.sleep(2) #chargement de la page

    if web.exists('SEARCH THE TRANSFER MARKET') == True :
        web.click('SEARCH THE TRANSFER MARKET') #
        time.sleep(2) #chargement de la page

    irr = 0
    web.type(player_name[0].replace('-',' '), into='Type Player Name', clear= False)
    while irr < len(player_name):
        time.sleep(0.1)
        web.type(player_name[irr].replace('-',' '), into='Type Player Name', clear= False)
        irr = irr + 1


    time.sleep(5) #chargement de la page
    
    if web.exists(classname="btn-text") == True :
        web.click(classname="btn-text", number= 8) #4 is staff
        time.sleep(5) #chargement de la page

        if web.exists('Clear') == True :
            web.click('Clear', number= 1) #1 is min ?
            time.sleep(2)
            web.click('Clear', number= 2) #1 is min ?
            time.sleep(5) #chargement de la page

        price_to_buy = int(return_price*0.85)
        if web.exists(classname="numericInput") == True :
            web.type(price_to_buy,classname="numericInput", number= 2) #1 is min ?
            time.sleep(5) #chargement de la page

            if web.exists('Search') == True :
                web.click('Search') #
                time.sleep(1) #chargement de la page

                if web.exists('Make Bid') == True :
                    web.click('Make Bid') #
                    time.sleep(2) #chargement de la page

                    if web.exists('OK') == True :
                        web.click('OK') #
                        time.sleep(2) #chargement de la page

                        if web.exists('Send to Transfer List') == True :
                            web.click('Send to Transfer List') #

                else:
                    #on re search une fois, plus tard
                    time.sleep(random.randint(2,40))
                    if web.exists('Search') == True :
                        web.click('Search') #
                        time.sleep(1) #chargement de la page

                        if web.exists('Make Bid') == True :
                            web.click('Make Bid') #
                            time.sleep(2) #chargement de la page

                            if web.exists('OK') == True :
                                web.click('OK') #
                                time.sleep(2) #chargement de la page

                                if web.exists('Send to Transfer List') == True :
                                    web.click('Send to Transfer List') #

    if web.exists('Home') == True :
        web.click(classname='Home') #

    print('sleep')
    time.sleep(random.randint(1,30)) #chargement de la page
                              

web = Browser("--disable-dev-shm-usage")
web.maximize_window()


try:    
    login(web)
except :
    print('error loggin')

if web.exists(classname='view-navbar-currency-coins') == True: #on recupere les coins 
    coins = web.driver.find_element_by_class_name('view-navbar-currency-coins').text
    a_coins = int((coins.replace(',','')).replace(' ',''))
    print('on commence avec : ',a_coins)
else : 
    a_coins = 1001

try:
    sell_players(web) 
except:
    print('erreur lors du sell')

try:
    while a_coins > 1000:
        try:
            if web.exists(classname='view-navbar-currency-coins') == True: #on recupere les coins
                a_coins0 = web.driver.find_element_by_class_name('view-navbar-currency-coins').text
                a_coins = int((a_coins0.replace(',','')).replace(' ',''))
                print('on a : ',a_coins,'|')
            buy_players(web) #
            buy_players2(web) #
            time.sleep(random.randint(10,60))
            sell_players(web)
        except:
            continue
except:
    print('erreur lors du buy')
        


