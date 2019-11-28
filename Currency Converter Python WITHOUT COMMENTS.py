#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:45:29 2019

@author: philipreiche
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:57:40 2019

@author: philipreiche
"""

import requests

url = "https://api.exchangerate-api.com/v4/latest/USD"
    
response = requests.get(url)
data = response.json() 

print("Welcome to the currency converter!")
print("")
print("This converter allows you to convert 1 or more currencies.")
print("")
print("It is able to check if you are better/worse off from previous exchanges.")
print("")
print("It can also give you the current spot rates.")
print("")
print("Please keep in mind that everything is case sensitive!")
print("")
currencies = ["AED", "ARS", "AUD", "BGN", "BRL", "BSD", "CAD", "CHF", "CLP", "CNY", "COP", "CZK", "DKK", "DOP", "EGP", "EUR", "FJD", "GBP", "GTQ", "HKD", "HRK", "HUF", "IDR", "KRW", "KZT", "MXN", "MYR", "NOK", "NZD", "PAB", "PEN", "PHP", "PKR", "PLN", "PYG", "RON", "RUB", "SAR", "SEK", "SGD", "THB", "TRY", "TWD", "UAH", "USD", "UYU", "VND", "ZAR"]
print("These are the currencies we support: ",currencies)

while True:
        
    choice = input("Would you like to convert current currencies? (Yes/No) ")
    
    if choice == "Yes":
        
        print("You can convert a maximum of 4 currencies at a time!")

        try:

            n = int(input("How many currencies would you like to convert? "))

            if n == 1:
                                
                cur1 = input("Which currency would you like to convert? ")
                amm1 = int(input("How much of this currency would you like to convert? "))
                
                finalcur = input("What currency would you like the convert this currency to? ")
                
                rate1 = (data["rates"][cur1])
                finalrate = (data["rates"][finalcur])

                print("")
                print(amm1, cur1,"=", 
                      ((amm1/rate1)*finalrate),finalcur,"!")
                
            elif n == 2:
                
                cur1 = input("What is the first currency? ")
                amm1 = int(input("How much of this currency would you like to convert? "))
                
                cur2 = input("What is the second currency? ")
                amm2 = int(input("How much of this currency would you like to convert? "))
                
                finalcur = input("What currency would you like the convert these currencies to? ")
                
                rate1 = (data["rates"][cur1])
                rate2 = (data["rates"][cur2]) 
                finalrate = (data["rates"][finalcur])
            
                print("")
                print(amm1, cur1, "+", amm2, cur2, "=", 
                      ((amm1/rate1)*finalrate)+((amm2/rate2)*finalrate),finalcur,"!")
                
            elif n == 3:
                
                cur1 = input("What is the first currency? ")
                amm1 = int(input("How much of this currency would you like to convert? "))
                
                cur2 = input("What is the second currency? ")
                amm2 = int(input("How much of this currency would you like to convert? "))
                
                cur3 = input("What is the third currency? ")
                amm3 = int(input("How much of this currency would you like to convert? "))
                
                finalcur = input("What currency would you like the convert these currencies to? ")
                
                rate1 = (data["rates"][cur1])
                rate2 = (data["rates"][cur2])
                rate3 = (data["rates"][cur3])
                finalrate = (data["rates"][finalcur])
                
                print("")
                print(amm1, cur1, "+", amm2, cur2, "+", amm3, cur3, "=", 
                      ((amm1/rate1)*finalrate)+((amm2/rate2)*finalrate)+((amm3/rate3)*finalrate),finalcur,"!")
                
            elif n == 4:
                
                cur1 = input("What is the first currency? ")
                amm1 = int(input("How much of this currency would you like to convert? "))
                
                cur2 = input("What is the second currency? ")
                amm2 = int(input("How much of this currency would you like to convert? "))
                
                cur3 = input("What is the third currency? ")
                amm3 = int(input("How much of this currency would you like to convert? "))
                
                cur4 = input("What is the fourth currency? ")
                amm4 = int(input("How much of this currency would you like to convert? "))
                
                finalcur = input("What currency would you like the convert these currencies to? ")
                
                rate1 = (data["rates"][cur1])
                rate2 = (data["rates"][cur2])
                rate3 = (data["rates"][cur3])
                rate4 = (data["rates"][cur4])
                finalrate = (data["rates"][finalcur])
                
                print("")
                print(amm1, cur1, "+", amm2, cur2, "+", amm3, cur3, "+", amm3, cur4, "=", 
                      ((amm1/rate1)*finalrate)+((amm2/rate2)*finalrate)+((amm3/rate3)*finalrate)
                      +((amm4/rate4)*finalrate),finalcur,"!")  
        
        except (KeyError, ValueError):
            print("Please make sure you entered a valid currency or number!")
         
    elif choice == "No":
    
        choice2 = input("Would you like to check your gains/losses from previous exchanges? (Yes/No) ")    
        
        if choice2 == "Yes":
        
            try:
            
                print("You can now check if saved or lost money on previous exchanges. WE DO NOT ADJUST FOR INFLATION!")
                print("Choose any date from 2000 onwards.")
                print("")
                date = input("Please enter a date in the form %Y-%m-%d, ex. 2010-12-20. ")
              
                urlold = "https://api.exchangeratesapi.io/"+date
                response = requests.get(urlold)
                dataold = response.json()
                
                curold = input("What currency did you exchange? " )
                finalcurold = input("What currency did you exchange it to? ")
                ammold = int(input("How much did you exchange? "))
                              
                if finalcurold == "EUR":
                
                    rateold = (dataold["rates"][curold])
                    finalrateold = 1
                    
                    convertold = ((ammold/rateold)*finalrateold)
                    
                    rate = (data["rates"][curold])
                    finalrate = (data["rates"][finalcurold])
                    
                    convertnew = ((ammold/rate)*finalrate)
                    
                    if convertnew > convertold:
                        print("You lost money, had you converted your money today you would've gotten",(convertnew-convertold),"more.")
                        
                    else:
                        print("You made money, had you converted your money today you would've gotten", (convertold-convertnew),"less.")
                    
                elif curold == "EUR":
                    rateold = 1
                    finalrateold = (dataold["rates"][finalcurold])
                    
                    convertold = ((ammold/rateold)*finalrateold)
                    
                    rate = (data["rates"][curold])
                    finalrate = (data["rates"][finalcurold])
                    
                    convertnew = ((ammold/rate)*finalrate)
                    
                    if convertnew > convertold:
                        print("You lost money, had you converted your money today you would've gotten",(convertnew-convertold),"more.")
                        
                    else:
                        print("You made money, had you converted your money today you would've gotten", (convertold-convertnew),"less.")
                
                else:
                    rateold = (dataold["rates"][curold])
                    finalrateold = (dataold["rates"][finalcurold])
                    
                    convertold = ((ammold/rateold)*finalrateold)
                    
                    rate = (data["rates"][curold])
                    finalrate = (data["rates"][finalcurold])
                    
                    convertnew = ((ammold/rate)*finalrate)
                    
                    if convertnew > convertold:
                        print("You lost money, had you converted your money today you would've gotten",(convertnew-convertold),"more.")
                        
                    else:
                        print("You made money, had you converted your money today you would've gotten", (convertold-convertnew),"less.")
           
            
            except (ValueError, KeyError):
                print("Make sure you entered a valid currency/number/date.")
                
        else:
            print("")    
            print("You can now check the spot rate for a currency.")
            print("")
            base = input("What is the base currency? (ex. EUR): " )
            quote = input("What is the quote currency? (ex. CHF): ")
                        
            baserate = (data["rates"][base])
            quoterate = (data["rates"][quote])
                
            print("Currently 1",base,"=",(quoterate/baserate),quote)
    
    else:
        print("")
        print("Please enter either Yes or No.")

    while True:
        answer = input("Would you like to run it again? (Yes/No): ")
        if answer in ("Yes", "No"):
            break
        print("Invalid input.")
    if answer == "Yes":
        continue
    else:
        print("Goodbye!")
        break