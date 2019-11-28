#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:57:40 2019

@author: philipreiche
"""
#This program uses the requests function to retrieve the data from a url, in our case the exchange rate API.

import requests

#We import the latest currency rates (quoted against the dollar) and store them under the name "data".

url = "https://api.exchangerate-api.com/v4/latest/USD"
    
response = requests.get(url)
data = response.json()
    
#Introduction to the program, what it can do, how to use it, and which currencies are supported.

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

#Use while True to which at the end of the program asks the user if they want to run the program again.

while True:
    
#Ask the user if he would like to convert current currencies, if No the program will skip to the next option.
    
    choice = input("Would you like to convert current currencies? (Yes/No) ")
    
    if choice == "Yes":
        
        print("You can convert a maximum of 4 currencies at a time!")

#Use the try function so that if there is a ValueError or KeyError the program tells the user what went wrong.

        try:

            n = int(input("How many currencies would you like to convert? "))

#Ask the user how many currencies to convert, supports up to 4 currencies.
#The process for converting currencies is the same no matter how many currencies are to be converted. We simply add more inputs and the conversion formula becomes longer, however, they all use the same principal.

            if n == 1:
                
#Ask the user for 3 inputs, an input currency and amount, and a final currency that the user wants to convert to.      
#If the user wanted to convert 2 currencies, we would need an additional currency input and amount input.
                
                cur1 = input("Which currency would you like to convert? ")
                amm1 = int(input("How much of this currency would you like to convert? "))
                
                finalcur = input("What currency would you like the convert this currency to? ")
                
#We retreive the corresponding exchange rates from "data". First we specify that we want to retrieve something from "rates" and then use the user input to specifiy the specific rate which we want to retrieve. 

                rate1 = (data["rates"][cur1])
                finalrate = (data["rates"][finalcur])
    
#We do the exchange rate calculation using the exchange rates we retrieved and the amounts which the user entered.
#For multiple currencies we simply repeat the same calculation for the second currency.
#The dataset uses USD as the base rate, so if the user wants to exchange something other than USD we will have to calculate the exchange rates ourselves.
#We do this by dividing the initial exchange rate by the final exchange rate, so a if the user wants to convert 10 EUR to CHF we would have to calculate how many dollars 10 EUR is, and then multiply this by the CHF/USD rate to get the CHF amount.
#This is what we do in the function below, first we divide the amount by the exchange rate and then multiply it be the final exchange rate.             
                print("")
                print(amm1, cur1,"=", 
                      ((amm1/rate1)*finalrate),finalcur,"!")
                
            elif n == 2:

#As seen below, if the user wants to convert 2 currencies we have 2 sets of currency/amount inputs.
#The conversion formula is the same as above, except we repeat the formula for the second currency and get the sum of the two. 
#The same goes for 3 and 4 formula, we simply add more inputs and extend the formula.
                
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
    
#This try function at the beginning ends here where the except(KeyError, ValueError) tells the user to input valud currencies or numbers since unsupported currencies or worsd entered instead of numbers will cause the program to not work.
    
        except (KeyError, ValueError):
            print("Please make sure you entered a valid currency or number!")

#Use elif so that if the user enters "No" to the first question they are taken here. 
         
    elif choice == "No":
    
        choice2 = input("Would you like to check your gains/losses from previous exchanges? (Yes/No) ")    
        
#Give them the choice to check gains/losses, uses the same principal as the first if function so when they say no they skip this part and are brought to the final option without further choices.

        if choice2 == "Yes":
        
            try:
            
                print("You can now check if saved or lost money on previous exchanges. WE DO NOT ADJUST FOR INFLATION!")
                print("Choose any date from 2000 onwards.")
                print("")
                date = input("Please enter a date in the form %Y-%m-%d, ex. 2010-12-20. ")
              
#Ask the user to input the date of their previous exchange in the specific format so that we can add their input to the URL in order to retreive the exchange rates for that day.
#The data retreival is the same as in the beginning simply the URL has been changed and we store the data under dataold.        
        
                urlold = "https://api.exchangeratesapi.io/"+date
                response = requests.get(urlold)
                dataold = response.json()
                
                curold = input("What currency did you exchange? " )
                finalcurold = input("What currency did you exchange it to? ")
                ammold = int(input("How much did you exchange? "))
              
#The older datasets have a different format where the base currency is not included, so we have to add the if functions in case the user wants to convert EUR. Since in the dataset there will be no value associated with EUR so we need to tell the program that the value of the base currency is always 1 since 1 EUR = 1 EUR.             
                
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
                
#If the user does not want to exchange from/to EUR we can retreive the exchange rates normally.
#Just as before, we go to the list named dataold, specify that we want the rates and then specifix which rates we want.
#We calculate the outcome of the old conversion the same way in which we calculated the conversions before and we call the "convertold".
#We also need to calculate what the outcome of that conversion would have been if it was done today, so we retreive the same currencies but this time using the first data set which included the current exchange rates.
#We calculate the outcome of the conversion and call it "convertnew", we use the if function to check if convertnew is more than convertold or vice versa and print the difference between the two.
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
           
#Again we use a try except function in case an invalid currency was entered, an integer was entered instead of a string or vice versa.
            
            except (ValueError, KeyError):
                print("Make sure you entered a valid currency/number.")
 
#If the user answered No at choice2 we can deduce that they want to check the spot rate since no other options remain.
               
        else:
            print("")    
            print("You can now check the spot rate for a currency.")
            print("")
            base = input("What is the base currency? (ex. EUR): " )
            quote = input("What is the quote currency? (ex. CHF): ")
            
#Calculating the spot rate is easy, we again retreive the exchange rates from the data set and transform them into the spot rate.
#Since the exchange rates all use USD as the base rate we have to divide the exchange rates corresponding to the currencies which the user wants in the spot rate.
#If the user wanted the EUR/CHF rate we would have to calculate: (EUR/USD)/(CHF/USD), this gives us the EUR/CHF rate.
            
            baserate = (data["rates"][base])
            quoterate = (data["rates"][quote])
                
            print("Currently 1",base,"=",(quoterate/baserate),quote)

#If the user did not enter Yes/No then the first if and elif are not true and the user ends up here at the final part of the if/else function. We know that he did not enter Yes or No as instructed so we remind him to enter yes or no.
    
    else:
        print("")
        print("Please enter either Yes or No.")

#This corresponds to our first while True loop:, if the user completes the program they are asked if they want to go again, if they answer "Yes" the loop continues, otherwise it finishes.

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
