import sys
from recipes import Forecast, Nutrition, SimilarRecipe

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python nutrionist.py ingredient1 ingredient2 ...")
        return

    ingredients = sys.argv[1:]

   
    forecaster = Forecast()
    forecaster.print_forecast(ingredients)

    print()
    nutrition = Nutrition()
    print(nutrition.summarize(ingredients))

    query = " ".join(ingredients)
    similar = SimilarRecipe(query)
    print(similar.print_the_recipe())



if __name__ == "__main__":
    main()
