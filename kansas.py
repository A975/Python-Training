from random import choice

capital = "Topeka"

bird = "Western Meadowlark"

flower = "Sunflower"

song = "Home on the Range"

def randomfunfact():

    funfacts = [
        "Kansas City sits on Missouri's western edge, straddling the border with Kansas."
        "It's known for its barbecue, jazz heritage and fountains. Downtown, the" 
        "American Jazz Museum shares a building with the Negro Leagues Baseball Museum" 
        "in the historic 18th & Vine Jazz District. The Nelson-Atkins Museum of Art, with" 
        "giant shuttlecocks out front, houses nearly 40,000 works of art, from ancient to contemporary collections"
    ]

    index  = choice("0123")

    print(funfacts[int(index)])

if __name__ == "__main__":
    randomfunfact()