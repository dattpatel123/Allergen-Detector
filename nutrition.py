    

import requests 
from bs4 import BeautifulSoup 
foodList = []
ingredientList = []
allergens=[]
allergicFoods=[]
nonAllergicFoods=[]

class Python:
    
    def menu(link):
        r = requests.get(link)        
        soup = BeautifulSoup(r.content, 'html.parser')    
        lines = soup.find_all('div') 
        mydivs = soup.findAll("div", {"class": "col-3"})
        
        for div in mydivs:
   
            y = 'http://menuportal23.dining.rutgers.edu/FoodPro/' + div.find('a').get('href')
            r = requests.get(y)   
            souped_soup = BeautifulSoup(r.content, 'html.parser') 
            foods = souped_soup.find_all('h2')  
            lines = souped_soup.find_all('p') 
            i=0
            
            for line in lines: 
                if i == 6:
                    foodList.append(foods[2].text)
                    ingredientList.append([line.text[14:len(line.text)-1]])
                    break
                i+=1
          
    
    print('Enter Hall (Livingston, Busch, College Ave, Cook/Douglass): ')
    hall = input()
    link = ''
    
    if(hall == 'Livingston'):
        link = 'http://menuportal23.dining.rutgers.edu/FoodPro/pickmenu.asp?locationNum=04&locationName=Livingston+Dining+Hall&mealName='
    if(hall == 'Busch'):
        link = 'http://menuportal23.dining.rutgers.edu/FoodPro/pickmenu.asp?locationNum=04&locationName=Busch+Dining+Hall&mealName='
    if(hall == 'College Ave'):
        link = 'http://menuportal23.dining.rutgers.edu/FoodPro/pickmenu.asp?locationNum=13&locationName=The+Atrium&mealName='
    if(hall == 'Cook/Douglass'):
        link = 'http://menuportal23.dining.rutgers.edu/FoodPro/pickmenu.asp?locationNum=04&locationName=Neilson+Dining+Hall&mealName='
    print('What Meal (Breakfast, Lunch, Dinner): ')    
    meal = input()
    if(hall == 'College Ave'):
        if(meal == 'Breakfast'):
            link = link + 'Breakfast+Entree'
        if(meal == 'Lunch'):
            link = link + 'Lunch+Entree'
        if(meal == 'Dinner'):
            link = link + 'Dinner+Entree'
    else:
        if(meal == 'Lunch'):
            link = link + 'Lunch'
        if(meal == 'Dinner'):
            link = link + 'Dinner'
    menu(link)
    
    
    print('How many allergies do you have?')
    n = int(input())
    
    print("Enter Allergens:")
    for i in range (n):
        x = input()
        allergens.append(x)
        
    for allergen in allergens: 
            for i in range(len(ingredientList)):
                for ingredient in ingredientList[i]:    
                    if(allergen.upper() in ingredient):
                        allergicFoods.append(foodList[i])
                    else:
                        nonAllergicFoods.append(foodList[i])
    print("You cannot eat: ")            
    print(allergicFoods)
    print("You can eat:")
    print(nonAllergicFoods)
    