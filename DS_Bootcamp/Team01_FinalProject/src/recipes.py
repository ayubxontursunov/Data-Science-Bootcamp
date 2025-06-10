import pandas as pd
import joblib
from bs4 import BeautifulSoup
import requests


whitelist = {
    'milk', 'sugar', 'egg', 'butter', 'salt', 'pepper', 'carrot', 'onion',
    'chicken', 'beef', 'pork', 'fish', 'rice', 'bread', 'flour', 'water',
    'garlic', 'honey', 'jam', 'tomato', 'cheese', 'cream', 'spinach',
    'yogurt', 'zucchini', 'potato', 'almond', 'banana', 'apple', 'lemon',
    'lime', 'orange', 'cucumber', 'celery', 'parsley', 'basil', 'oregano',
    'thyme', 'rosemary', 'cinnamon', 'nutmeg', 'ginger', 'vanilla', 'chocolate',
    'coffee', 'tea', 'vinegar', 'oil', 'olive oil', 'vegetable oil', 'buttermilk',
    'mayonnaise', 'ketchup', 'mustard', 'soy sauce', 'tofu', 'lentils',
    'beans', 'peas', 'corn', 'pumpkin', 'mushroom', 'onion powder', 'garlic powder',
    'paprika', 'cumin', 'coriander', 'turmeric', 'chili', 'cabbage', 'lettuce',
    'broccoli', 'cauliflower', 'eggplant', 'sweet potato', 'maple syrup',
    'molasses', 'baking powder', 'baking soda', 'yeast', 'sour cream',
    'coconut', 'pineapple', 'strawberry', 'blueberry', 'raspberry',
    'blackberry', 'peach', 'pear', 'plum', 'apricot', 'fig', 'date',
    'walnut', 'pecan', 'cashew', 'pistachio', 'hazelnut', 'sesame',
    'chia', 'quinoa', 'barley', 'oats', 'buckwheat', 'rye', 'spelt',
    'mustard seed', 'clove', 'anise', 'cardamom', 'star anise', 'bay leaf',
    'dill', 'chives', 'scallion', 'shallot', 'leek', 'coriander leaf',
    'capsicum', 'bell pepper', 'jalapeno', 'habanero', 'chili powder',
    'brown sugar', 'powdered sugar', 'cornstarch', 'arrowroot', 'gelatin',
    'almond milk', 'coconut milk', 'rice milk', 'cashew milk',
    'maple syrup', 'agave', 'sesame oil', 'peanut', 'peanut butter',
    'beef broth', 'chicken broth', 'vegetable broth', 'mayo',
    'whipped cream', 'cream cheese', 'feta', 'mozzarella', 'parmesan',
    'cheddar', 'swiss', 'gouda', 'brie', 'ricotta', 'blue cheese',
    'tofu', 'tempeh', 'seitan', 'black beans', 'kidney beans',
    'chickpeas', 'edamame', 'seaweed', 'wasabi', 'sriracha',
    'tahini', 'miso', 'salsa', 'guacamole', 'curry powder',
    'curry paste', 'lemongrass', 'galangal', 'kaffir lime leaf',
    'ginger powder', 'cocoa powder', 'dark chocolate', 'white chocolate',
    'matcha', 'espresso', 'espresso powder', 'coconut sugar',
    'brown rice', 'wild rice', 'basmati rice', 'jasmine rice',
    'zucchini noodles', 'pasta', 'noodles', 'breadcrumbs',
    'chicken breast', 'ground beef', 'ground turkey',
    'bacon', 'sausage', 'ham', 'salami', 'prosciutto', 'shrimp',
    'crab', 'lobster', 'salmon', 'tuna', 'cod', 'tilapia', 'trout',
    'scallops', 'oysters', 'mussels', 'clams', 'octopus',
    'egg yolk', 'egg white', 'quail egg', 'duck egg',
    'butternut squash', 'acorn squash', 'spaghetti squash',
    'sweet corn', 'baby corn', 'edible flowers', 'microgreens',
    'arugula', 'kale', 'collard greens', 'bok choy',
    'brussels sprouts', 'artichoke', 'asparagus',
    'beets', 'fennel', 'turnip', 'parsnip', 'radish', 'rutabaga',
    'watercress', 'endive', 'chicory', 'dandelion greens',
    'mustard greens', 'pea shoots', 'snap peas', 'snow peas',
    'tomatillo', 'avocado', 'plantain', 'cassava', 'yam',
    'sorghum', 'teff', 'amaranth', 'millet',
}


class Forecast:
    def __init__(self, model_path='./data/balanced_random_forest.pkl', columns_path='./data/ingredient_columns.pkl'):
        self.model=joblib.load(model_path)
        self.columns=joblib.load(columns_path)
        
        
    def predict(self, ingridients):
        df=pd.read_csv('./data/epi_r.csv')
        ingredient_columns = [col for col in df.columns if col.lower() in whitelist]
        df_ingredients = df[ingredient_columns]
        zero_vector = pd.DataFrame(0, index=[0], columns=self.columns)
        
        
        for ingr in ingridients:
            ingr=ingr.lower()
            if ingr in self.columns:
                zero_vector.at[0,ingr]=1.0
        return self.model.predict(zero_vector)[0]
    
    def print_forecast(self, ingredients):
        result = self.predict(ingredients)
        print("I. HEALTH FORECAST")
        if result == 'great':
            print("Awesome choice! This combination of ingredients is considered highly nutritious.")
        elif result == 'so-so':
            print("This dish is somewhat balanced. It's not the healthiest, but not the worst either.")
        elif result == 'bad':
            print("You might find it tasty, but in our opinion, it's a bad idea to have a dish with that list of ingredients.")


class Nutrition:
    def __init__(self, csv_path='./data/new_daily_nutrients.csv'):
        self.df=pd.read_csv(csv_path)
        
        self.df['Unnamed: 0']=self.df['Unnamed: 0'].str.lower()
        self.df.set_index('Unnamed: 0', inplace=True)
        
    def summarize(self, ingredients):
        ingredients = [ing.lower() for ing in ingredients]
        matched = self.df.loc[self.df.index.intersection(ingredients)]

        if matched.empty:
            return "No nutrition data found for the given ingredients."

        output = "II. NUTRITION FACTS"
        for ing in ingredients:
            if ing in matched.index:
                output += f"\n{ing.title()}\n"
                ing_data = matched.loc[ing]
                ing_data = ing_data[ing_data > 0]
                for nutrient, percent in ing_data.items():
                    output += f"{nutrient} - {percent:.2f}% of Daily Value\n"
            else:
                output += f"\n{ing.title()} - No data available\n"

        return output.strip()


class SimilarRecipe:
    headers = {
    "User-Agent": "Mozilla/5.0"
    }
    
    def __init__(self, query):
        self.search_url = f"https://www.epicurious.com/search?q={query.replace(' ', '+')}"
        response = requests.get(self.search_url, headers=self.headers)
        self.soup = BeautifulSoup(response.text, 'html.parser')
    
    def get_rating(self):
        rating_divs = self.soup.find_all('div', class_='RatingFormWrapper-WFRur kQaRnK')
        ratings = []
        count = 0
        for div in rating_divs:
            if count >= 3:
                break
            rating_tags = div.find_all('p') 
            for tag in rating_tags:
                text = tag.get_text(strip=True)
                if text.startswith("(") and text.endswith(")"):
                    ratings.append(text.strip("()"))  
                    break  
            count += 1
        return ratings
    def get_recipe_info(self):
        info = []
        count = 0
        recipe_divs = self.soup.find_all('div', class_='ClampContent-hilPkr fvKowN')
        for div in recipe_divs:
            if count >= 3:
                break

            a_tag = div.find('a', href=True)
            if not a_tag:
                continue
            url = "https://www.epicurious.com" + a_tag['href']
            title = a_tag.get_text(strip=True)
            parts = {'title': title, 'url': url}
            info.append(parts)
            count += 1

        return info
    
    def print_the_recipe(self):
        output = "\nIII. TOP-3 SIMILAR RECIPES:"
        recipes = self.get_recipe_info()
        ratings = self.get_rating()
        for i in range(min(3, len(recipes), len(ratings))):
            title = recipes[i]['title']
            url = recipes[i]['url']
            rating = ratings[i]
            output += f"\n- {title}, rating: {rating} , URL:\n{url}"
        return output
        
        
    
    

finder = SimilarRecipe("egg jam almond milk")
finder.print_the_recipe()