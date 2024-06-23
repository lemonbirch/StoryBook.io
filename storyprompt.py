
import random

class buildPrompt: 
    def __init__(self) -> None:
        self.children_story_themes = [
                'A lonely cloud befriends a lost kite and helps it find its way back home', 'A group of shy woodland creatures start a talent show to overcome their stage fright', 'A curious pair of shoes embark on an adventure after they get separated from their owner', 'A grumpy old troll learns the importance of kindness when a lost puppy wanders into his cave', 'A group of misfit toys team up to save Christmas when Santa forgets his important bag', 'A talking garden gnome helps a young child learn about the magic of growing their own food', 'A lost firefly searches for its light with the help of a wise old moonbeam', 'A timid bookworm overcomes its fear of heights to climb a giant bookshelf', 'A mischievous group of raindrops cause chaos in a city, then learn to work together to water a thirsty park', 'A grumpy thunderstorm and a gentle spring breeze learn to appreciate each others differences', 'A group of talking crayons accidentally draw themselves into their own fantastical adventure', 'A lost sock searches the laundry basket for its missing partner, encountering all sorts of lost treasures', 'A group of neighborhood children build a magnificent clubhouse out of recycled materials', 'A shy firefly uses its light to help a nocturnal animal navigate the forest at night', 'A grumpy old bridge learns the importance of teamwork when a big storm threatens to wash it away', 'A curious puppy discovers a secret world hidden inside a grandfather clock', 'A group of friendly butterflies help a lost caterpillar find its perfect chrysalis', 'A family of mice goes on a daring adventure to steal cheese from a grumpy chefs kitchen', 'A lonely lighthouse longs for adventure until a brave little boat needs its guidance in a storm', 'A group of playful puppies use their teamwork to outsmart a mischievous squirrel who keeps stealing their toys', 'A lost backpack embarks on a journey through a busy airport searching for its owner', 'A group of musical instruments learn how to harmonize and create a beautiful symphony together', 'A shy dandelion puff embarks on a journey across the wind to find a new place to grow', 'A group of friendly forest animals team up to build a winter wonderland for all the creatures', 'A curious raindrop travels from the clouds down to the earth, learning about the water cycle', 'A grumpy old cactus learns the joy of friendship when a lost desert creature needs its help', 'A mischievous group of bubbles cause chaos at a birthday party, then learn to entertain the children', 'A shy bookworm overcomes its fear of words and discovers the joy of storytelling', 'A brave little ladybug helps a lost group of ants find their way back to their anthill', 'A group of mismatched socks learn to embrace their differences and become the best of friends', 'A grumpy old rocking horse learns the joy of sharing when a group of children come to play', 'A lost pair of glasses embarks on an adventure through a busy library searching for its owner', 'A curious group of snowflakes learn about the different shapes and sizes they can take during a snowfall', 'A grumpy old scarecrow learns the importance of friendship when a lost baby bird falls from its nest', 'A mischievous group of fireflies use their light to create a dazzling display during a summer night', 'A lost mitten searches through the lost and found box for its missing partner', 'A shy little seed overcomes its fear of growing and discovers the beauty of blooming', 'A group of friendly forest creatures team up to clean up a polluted stream', 'A curious group of stars learn about the constellations and the stories they tell', 'A grumpy old swing set learns the joy of laughter when a group of children come to play', 'A lost seashell travels across the ocean floor, encountering all sorts of fascinating sea creatures', 'A shy little ghost overcomes its fear of darkness and learns to make friends with the other spooky creatures', 'A brave little ladybug helps a lost group of caterpillars find their way back to their favorite food source', 'A mischievous group of dewdrops use their sparkle to create a beautiful rainbow in the morning sky', 'A lost pair of sunglasses embarks on an adventure through a bustling beach, searching for its owner', 'A curious group of pebbles learn about the different shapes and sizes they can be after a river journey']
        

        self.children_story_names = ["Amelia", "Benjamin", "Cedric", "Daisy", "Elliot", "Finley", "Gloria", "Henry", "Isaac", "Jasper", "Juniper", "Kai", "Luna", "Mateo", "Nora", "Olivia", "Penelope", "Quinn", "Rory", "Stella", "Theodore", "Uma", "Vincent", "Willow", "Xavier", "Yasmin", "Zachariah", "Alice", "Bear", "Clementine", "Daniel", "Everly", "Fox", "Graham", "Hazel", "Iris", "Jasper", "Kingsley", "Milo", "Nova", "Oliver", "Penelope", "Ruby", "Silas", "Theodore", "Uma", "Violet", "Wesley", "Xavier", "Yolanda", "Zane"]
           
    def generateTheme(self): 
        theme = random.choice(self.children_story_themes)
        return theme


    def generateName(self): 
        name = random.choice(self.children_story_names)
        return name
    def contentPrompt(self, user_input, name, theme):
        if user_input == None: 
            user_input_prompt = f"""Please use the following default name and theme: {name}, {theme}"""
            print(f"this shows that None is activated: {user_input}")
        else: 
            print(f"this shows that else is activated: {user_input}")
            user_input_prompt = f"""First validate that this is a valid name and theme: {user_input} if this valid, use this name and theme for your story and continue to section 1. Otherwise, use the following default name and theme: {name}, {theme}"""
        return [f"""Create a unique, short 5-page book for children aged 4-5 years old. {user_input_prompt}.
    
    1. Each page should follow this format:

    story: [Write a simple and engaging story for young children. Ensure each story section contributes to a coherent narrative with a clear beginning, middle, and end. Include elements such as introduction, build-up, climax, and resolution appropriate for a children's book.]
    choices: [Provide three short and simple choices of what can happen next. These choices should be logical and engaging, leading to different potential story developments.]

    The story should be age-appropriate, fun, and easy to understand. Make sure to provide three short and simple choices after each story section. Here is the structure:

    Page 1:
    story: [Start the story, introducing the main character and setting the scene.]
    choices: [Provide three choices that determine the next part of the story.]

    Page 2:
    story: [Continue the story based on the choice from Page 1, building up the plot.]
    choices: [Provide three choices that determine the next part of the story.]

    Page 3:
    story: [Further develop the story or introduce a climax based on the choice from Page 2.]
    choices: [Provide three choices that determine the next part of the story.]

    Page 4:
    story: [Move towards resolving the story based on the choice from Page 3.]
    choices: [Provide three choices that determine the next part of the story.]

    Page 5:
    story: [Conclude the story with a satisfying ending based on the choice from Page 4.]
    choices: The end

    Ensure that the story follows a typical children's book structure and reaches a satisfying conclusion by the fifth page. The stories should be unique and imaginative, providing a delightful experience for young readers.

    Make sure to only output the first page first so the user can make a choice that will affect the second page.
    Add relevent emojies to each choice so the user can easily identify them. 
    """]

    