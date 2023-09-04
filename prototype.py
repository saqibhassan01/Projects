import random
from colorama import Fore, Style
from art import text2art
import time
from playsound import playsound
from tabulate import tabulate
import threading

class Character:
    def __init__(self, name, gender, age = 0, gold = 25, prestige = 0):
        self.name = name
        self.age = age
        self.gender = gender
        self.career = None
        self.gold = gold
        self.prestige = prestige
        self.stats = {
            "health" : random.randint(20,100),
            "looks" : random.randint(20,100),
            "martial": 0,
            "diplomacy": 0,
            "intrigue": 0,
        }

    @classmethod
    def get(cls):
        try:
            name = input(Fore.RED + Style.BRIGHT + "Name: " + Style.RESET_ALL).title()
            gender = input(Fore.RED + Style.BRIGHT + "Gender: " + Style.RESET_ALL).title()
            while gender not in ("Male", "Female"):
                gender = input(Fore.RED + Style.BRIGHT + "Gender: " + Style.RESET_ALL).title()
            return cls(name, gender)
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def print_info(self):
        print("<----------------------------------->\n")
        print(Fore.RED + Style.BRIGHT + "Name: " + Style.RESET_ALL + Style.BRIGHT + self.name + Style.RESET_ALL)
        print(Fore.RED + Style.BRIGHT + "Age:" + Style.RESET_ALL + Style.BRIGHT ,self.age , Style.RESET_ALL)
        print(Fore.RED + Style.BRIGHT + "Gold:" + Style.RESET_ALL+ Style.BRIGHT ,self.gold , Style.RESET_ALL)
        print(Fore.RED + Style.BRIGHT + "Prestige:" + Style.RESET_ALL+ Style.BRIGHT ,self.prestige ,Style.RESET_ALL)
        print( Fore.RED + Style.BRIGHT + "Attributes: " + Style.RESET_ALL )
        print(f"❤️" + Style.BRIGHT + Fore.GREEN + "  Health:",self.stats['health'],"%" + Style.RESET_ALL)
        print(f"🔥" + Style.BRIGHT + Fore.YELLOW + "Looks:",self.stats['looks'],"%" + Style.RESET_ALL)
        print(Fore.RED + Style.BRIGHT + "Stats: " + Style.RESET_ALL + Style.BRIGHT +
              f"⚔️  Martial:{self.stats['martial']}  ✍️  Diplo:{self.stats['diplomacy']}  🕵️  Intrigue{self.stats['intrigue']}" + Style.RESET_ALL)
        print("\n<----------------------------------->")

    

class Event:
    def event(self,character):
        events0 = [
            "Your father, Iskender Demir, a skilled blacksmith, and your mother, Ayşe Yilmaz, a talented rug weaver, welcome you into the world in Edirne.",
            "Born in Edirne, you are the child of Hüseyin Bey, a respected olive oil merchant, and your mother, Zehra Öztürk, an expert herbalist.",
            "Your father, Mustafa Efendi, a wise judge in Edirne's court, and your mother, Leyla Kaya, a gifted storyteller, celebrate your birth.",
            "Edirne's bustling bazaar sees the birth of another soul as your father, Mehmet Ağa, a renowned spice trader, and your mother, Fatma Şahin, a skilled carpet seller, become parents.",
            "As you enter the world in Edirne, your father, Yusuf Bey, a respected calligrapher, and your mother, Nurcan Güler, a talented jewelry maker, look upon you with joy.",
            "Born in the heart of the Ottoman Empire, your father, İsmail Ağa, a skilled leatherworker, and your mother, Selma Karadeniz, a masterful silk weaver, welcome you into their world.",
            "Your father, Osman Efendi, a skilled ceramicist, and your mother, Aylin Aksoy, an expert henna artist, proudly announce your birth in Edirne.",
            "In Edirne, you come into the world as the child of Mehmet Bey, a respected judge, and your mother, Şehrazat Karabulut, a gifted storyteller and poet.",
            "Born to parents steeped in Ottoman culture, your father, Ali Ağa, a well-known calligrapher, and your mother, Emine Koç, a talented rug weaver, celebrate your arrival.",
            "Your father, Ahmet Bey, a respected olive oil merchant, and your mother, Esma Şahin, a skilled carpet seller, welcome you into the bustling city of Edirne.",
            "In Edirne, your birth is celebrated by your father, Hasan Efendi, a wise scholar, and your mother, Zübeyde Kiliç, a renowned herbalist and healer.",
            "Born into an artisan family in Edirne, your father, Mehmet Efendi, a skilled ceramicist, and your mother, Selin Demirci, a masterful silk weaver, cherish your arrival.",
            "Your father, Mustafa Bey, a well-known spice trader, and your mother, Şerife Altin, a gifted jewelry maker, greet you with love and pride in Edirne.",
            "As you are born in Edirne, your father, Halil Ağa, a respected leatherworker, and your mother, Sema Kiliç, an expert henna artist, celebrate your birth.",
            "Born in Edirne, you come into the world as the child of Ali Efendi, a wise judge, and your mother, Lale Temiz, a talented storyteller and poet, sharing the richness of Ottoman culture."
]
        event0 = random.choice(events0)
        print(event0)
        character.age += 1
        while True:
            if character.age == 1:
                event_chance = random.randint(1, 10)
            if event_chance <= 5:
                print( Style.BRIGHT +"\nToday, your parents celebrate your first birthday with a small family gathering.")
                character.stats['looks'] += random.randint(1, 3)  
                print(f""+Style.BRIGHT +"Looks:"+ Style.RESET_ALL ,character.stats['looks'])
                break
            else:
                print( Style.BRIGHT +"\nIt's just an ordinary day in your life as you are now a one-year-old.")
                break
        
        while True:
            print( Style.BRIGHT +"\nWhat would you like to do?")
            print(Fore.RED + Style.BRIGHT +"1."+ Style.RESET_ALL +  Style.BRIGHT +"Eat")
            print(Fore.RED + Style.BRIGHT +"2."+ Style.RESET_ALL +  Style.BRIGHT +"Take a nap")
            print(Fore.RED + Style.BRIGHT +"3."+ Style.RESET_ALL +  Style.BRIGHT +"Play")
            print(Fore.RED + Style.BRIGHT +"4."+ Style.RESET_ALL +  Style.BRIGHT +"Age up")

            choice = input("Enter your choice (1/2/3/4): ")

            if choice == "1":
                # Simulate eating
                character.stats['health'] += random.randint(1, 2)  # Eating improves health
                character.stats['looks'] += random.randint(-2, 1)  # Eating may have a slight impact on looks
                print( Style.BRIGHT +"You eat some baby food.")
            elif choice == "2":
                # Simulate taking a nap
                character.stats['health'] += random.randint(2, 4)  # Napping improves health
                print( Style.BRIGHT +"You take a nap.")
            elif choice == "3":
                # Simulate playing
                character.stats['looks'] += random.randint(1, 2)  # Playing may improve looks
                print( Style.BRIGHT +"You play with your toys.")
            elif choice == "4":
                print( Style.BRIGHT +"You decide to rest for now.")
            else:
                continue
            break
        character.age += 1
        time.sleep(3)
        character.print_info()
        events2 = [
            "At age 2, you begin to show an interest in your surroundings, especially in the colorful patterns of the rugs woven by your mother.",
            "As a 2-year-old, you start babbling and trying to mimic words, much to the amusement of your parents.",
            "You turn 2 years old, and your parents notice your curiosity as you explore your home in Edirne, touching everything in sight.",
            "At age 2, you take your first steps, wobbling as you navigate the rooms of your home in Edirne.",
            "Your second birthday arrives, and your parents celebrate your growth with a special family meal in the heart of the Ottoman Empire.",
            "At age 2, you show a fascination with the calligraphy pens your father uses, often attempting to mimic his strokes.",
            "Your parents notice your love for storytelling at the age of 2, as you eagerly listen to your mother's tales of Ottoman legends.",
            "As you reach age 2, you start to exhibit a strong bond with your parents, seeking comfort and affection from them.",
            "You turn 2, and your parents, both skilled artisans, introduce you to the basics of their crafts, hoping to pass on their skills.",
            "At age 2, your parents notice your developing artistic talents as you create your first colorful drawings.",
            "Your second birthday is marked by your fascination with the bustling bazaars of Edirne, where you accompany your parents on their business ventures.",
            "As you reach age 2, you display a knack for negotiation, often trying to strike deals with your parents in playful exchanges.",
            "At the age of 2, you show an affinity for nature, spending time with your parents in the beautiful gardens of Edirne.",
            "You celebrate your second birthday with a joyful family picnic along the tranquil banks of the Meriç River in Edirne.",
            "As you turn 2, your parents introduce you to the rich musical traditions of the Ottoman Empire, playing soothing melodies on traditional instruments.",
            "Your second birthday is marked by your growing love for animals, especially the cats that roam the streets of Edirne."
        ]
        event2 = random.choice(events2)
        print(event2)
        while True:
            if character.age == 2:
                event_chance = random.randint(1, 10)
            if event_chance <= 5:
                print( Style.BRIGHT +"\nYour parents celebrate your second birthday with a small gathering, showering you with affection and gifts.")
                character.stats['looks'] += random.randint(1, 3)  # Event may improve looks
                print(f"" + Style.BRIGHT + "Looks:" + Style.RESET_ALL ,character.stats['looks'])
                break
            else:
                print( Style.BRIGHT +"\nIt's just an ordinary day as you turn 2 years old.")
                break

        while True:
            print( Style.BRIGHT +"\nWhat would you like to do?")
            print(Fore.RED + Style.BRIGHT + "1." + Style.RESET_ALL + "Explore the house")
            print(Fore.RED + Style.BRIGHT + "2." + Style.RESET_ALL + "Mimic your parents")
            print(Fore.RED + Style.BRIGHT + "3." + Style.RESET_ALL + "Play with toys")
            print(Fore.RED + Style.BRIGHT + "4." + Style.RESET_ALL + "Age up")

            choice = input( Style.BRIGHT +"Enter your choice (1/2/3/4): ")

            if choice == "1":
                # Simulate exploring the house
                character.stats['looks'] += random.randint(1, 2)  # Exploring may improve looks
                print( Style.BRIGHT +"You explore your home in Edirne, discovering new corners and objects.")
            elif choice == "2":
                # Simulate mimicking your parents
                character.stats['looks'] += random.randint(1, 3)  # Mimicking may improve looks
                print( Style.BRIGHT +"You try to mimic your parents' actions and words, showing early signs of learning.")
            elif choice == "3":
                # Simulate playing with toys
                character.stats['looks'] += random.randint(1, 2)  # Playing may improve looks
                print( Style.BRIGHT +"You have fun playing with your toys, showcasing your creativity.")
            elif choice == "4":
                print( Style.BRIGHT +"You decide to rest for now.")
            else:
                continue
            break
        character.age += 1
        time.sleep(3)
        character.print_info()
        events3 = [
            "At age 3, you continue to explore your surroundings, now showing a keen interest in your father's blacksmithing tools.",
            "As you turn 3, your vocabulary expands, and you start forming sentences, impressing your parents with your communication skills.",
            "At the age of 3, you become increasingly independent, attempting to dress yourself and tie your tiny shoes.",
            "You celebrate your third birthday, and your parents notice your growing confidence and assertiveness in Edirne.",
            "As you reach age 3, you become more inquisitive, asking your parents endless questions about the world around you.",
            "At age 3, you develop a fascination with your mother's rug-weaving loom, often trying to mimic her intricate patterns.",
            "Your third birthday is marked by your love for storytelling, as you create imaginative tales for your family to enjoy.",
            "As you turn 3, your parents introduce you to the world of art, teaching you the basics of calligraphy.",
            "At age 3, you demonstrate a growing sense of empathy, often comforting others when they are upset.",
            "Your third birthday arrives, and you exhibit an early interest in diplomacy, mediating disputes among your playmates.",
            "As you reach age 3, you start to display a preference for certain colors, particularly those found in the vibrant bazaars of Edirne.",
            "At age 3, you become more adventurous, eagerly exploring the markets of Edirne with your parents.",
            "Your third birthday is filled with musical joy as you learn to play simple tunes on traditional Ottoman instruments.",
            "As you turn 3, your love for animals grows, and you begin caring for stray cats that visit your home.",
            "At age 3, you start to show a talent for haggling, often accompanying your parents to bargain for goods.",
            "Your third birthday celebration includes a visit to the serene Meriç River, where you release colorful paper lanterns into the evening sky."
        ]
        event3 = random.choice(events3)
        print(event3)
        while True:
            if character.age == 3:
                event_chance = random.randint(1, 10)
            if event_chance <= 5:
                print( Style.BRIGHT +"\nYour parents celebrate your third birthday with a grand gathering in Edirne, inviting friends and family.")
                character.stats['looks'] += random.randint(1, 3)  # Event may improve looks
                print(f""+ Style.BRIGHT +"🎉 Happy 3rd Birthday! Looks:" + Style.RESET_ALL ,character.stats['looks'])
                break
            else:
                print( Style.BRIGHT +"\nIt's just an ordinary day as you turn 3 years old.")
                break

        while True:
            print( Style.BRIGHT +"\nWhat would you like to do?")
            print(Fore.RED + Style.BRIGHT + "1." + Style.RESET_ALL + "Explore the blacksmith's tools")
            print(Fore.RED + Style.BRIGHT + "2." + Style.RESET_ALL + "Ask your parents questions")
            print(Fore.RED + Style.BRIGHT + "3." + Style.RESET_ALL + "Play with your friends")
            print(Fore.RED + Style.BRIGHT + "4." + Style.RESET_ALL + "Age up")

            choice = input( Style.BRIGHT +"Enter your choice (1/2/3/4): ")

            if choice == "1":
                # Simulate exploring the blacksmith's tools
                character.stats['looks'] += random.randint(1, 2)  # Exploring may improve looks
                print( Style.BRIGHT +"You explore your father's friend blacksmithing tools, fascinated by the shiny metals.\nWhile exploring, you accidentally cut your finger on a sharp edge.\nYour parents rush to comfort you and bandage your finger.")
            elif choice == "2":
                # Simulate asking questions
                character.stats['looks'] += random.randint(1, 3)  # Asking questions may improve looks
                print( Style.BRIGHT +"You ask your parents countless questions, eager to learn about the world.\nYour parents patiently answer your questions, sparking your curiosity.\nYou continue to ask more questions and gain knowledge.")
            elif choice == "3":
                # Simulate playing with friends
                character.stats['looks'] += random.randint(1, 2)  # Playing may improve looks
                print( Style.BRIGHT +"You have a great time playing with your friends in the streets of Edirne.\nYou develop strong bonds with your playmates and enjoy their company.")
            elif choice == "4":
                print( Style.BRIGHT +"You decide to rest for now.")
            else:
                continue
            break
        character.age += 1
        time.sleep(4)
        character.print_info()
        events4 =[
    "At age 4, you can't contain your excitement when you discover a family of playful kittens in the courtyard, and you spend hours giggling and playing with them.",
    "As you turn 4, you proudly show off your ability to climb trees, impressing your family with your newfound sense of adventure.",
    "At the age of 4, you become a little chef, helping your parents in the kitchen by stirring ingredients and tasting cookie dough.",
    "You celebrate your fourth birthday with a homemade kite your father crafted, and you joyfully watch it soar high in the clear skies.",
    "As you reach age 4, you develop a fascination with bugs and spend your days exploring the garden, observing tiny creatures with wonder.",
    "At age 4, you eagerly participate in games of 'hide and seek' with your friends, giggling uncontrollably when you find a clever hiding spot.",
    "Your fourth birthday is marked by your love for storytelling, as you create imaginative tales about knights and dragons for your family to enjoy.",
    "As you turn 4, you discover your artistic side, creating colorful finger paintings that decorate the walls of your home.",
    "At age 4, you enjoy helping your parents in the garden, carefully planting seeds and watching in awe as flowers bloom.",
    "Your fourth birthday celebration includes a visit to a local pond, where you excitedly feed the ducks and watch their playful antics."
]

        event4 = random.choice(events4)
        print(event4)
        while True:
            if character.age == 4:
                event_chance = random.randint(1, 10)
            if event_chance <= 5:
                print( Style.BRIGHT +"\nUnder the starry Edirne sky, laughter filled the air as friends and family gathered to celebrate a joyous fourth birthday.")
                character.stats['looks'] += random.randint(1, 3)  # Event may improve looks
                print(f""+ Style.BRIGHT +"🎉 Happy 4th Birthday! Looks:" + Style.RESET_ALL ,character.stats['looks'])
                break
            else:
                print( Style.BRIGHT +"\nIt's just an ordinary day as you turn 4 years old.")
                break


        while True:
            print( Style.BRIGHT +"\nWhat would you like to do?")
            print(Fore.RED + Style.BRIGHT + "1." + Style.RESET_ALL + "Ask your father for a wooden sword")
            print(Fore.RED + Style.BRIGHT + "2." + Style.RESET_ALL + "Sneak into your father's study")
            print(Fore.RED + Style.BRIGHT + "3." + Style.RESET_ALL + "Help your mother with her guests")
            print(Fore.RED + Style.BRIGHT + "4." + Style.RESET_ALL + "Age up")

            choice = input( Style.BRIGHT +"Enter your choice (1/2/3/4): ")

            if choice == "1":
                # Ask for a wooden sword (Martial +2)
                character.stats['martial'] += 2
                print( Style.BRIGHT +"You ask your father for a wooden sword. He smiles and agrees, handing you a finely crafted wooden sword.\nYou begin training with it, improving your martial skills.")
            elif choice == "2":
                # Sneak into your father's study (Intrigue +2)
                character.stats['intrigue'] += 2
                print( Style.BRIGHT +"You decide to sneak into your father's study, intrigued by the secrets it holds.\nYou carefully open the door and explore the room, discovering hidden scrolls and documents. Your intrigue skills grow as you uncover valuable knowledge.")
            elif choice == "3":
                # Help your mother with her guests (Diplomacy +2)
                character.stats['diplomacy'] += 2
                print( Style.BRIGHT +"You choose to help your mother with her guests during the grand feast.You gracefully interact with the guests,\nMaking them feel welcomed and appreciated. \nYour mother smiles at your diplomatic skills, and you learn more about the art of diplomacy and negotiation.")
            elif choice == "4":
                print( Style.BRIGHT +"You decide to rest for now.")
            else:
                continue
            break
        character.age += 1
        time.sleep(3)
        character.print_info()
        events5 = [
            "At age 5, you continue to explore your surroundings, now showing a keen interest in history and stories.",
            "As you turn 5, your vocabulary expands, and you become an eloquent speaker, impressing your family.",
            "At the age of 5, you become increasingly independent, dressing yourself and helping with chores.",
            "You celebrate your fifth birthday, and your parents notice your growing confidence and assertiveness in Edirne.",
            "As you reach age 5, you become more inquisitive, asking your parents endless questions about the world around you.",
            "At age 5, you develop a fascination with the stories of great historical figures, inspiring you to learn more.",
            "Your fifth birthday is marked by your love for storytelling, as you create imaginative tales for your family to enjoy.",
            "As you turn 5, your parents introduce you to the world of art, teaching you the basics of calligraphy.",
            "At age 5, you demonstrate a growing sense of empathy, often comforting others when they are upset.",
            "Your fifth birthday arrives, and you exhibit an early interest in diplomacy, mediating disputes among your playmates."
        ]

        print(random.choice(events5))

        while True:
            if character.age == 5:
                event_chance = random.randint(1, 10)
            if event_chance <= 5:
                print( Style.BRIGHT +"\nThe aroma of delicious Turkish cuisine wafted through the evening breeze, making the grand feast in Edirne an unforgettable celebration of the youngster's fifth birthday.")
                character.stats['looks'] += random.randint(1, 3)  # Event may improve looks
                print(f""+ Style.BRIGHT +"🎉 Happy 5th Birthday! Looks:" + Style.RESET_ALL ,character.stats['looks'])
                break
            else:
                print( Style.BRIGHT +"\nIt's just an ordinary day as you turn 5 years old.")
                break

        while True:
            print( Style.BRIGHT +"\nWhat would you like to do?")
            print(Fore.RED + Style.BRIGHT + "1." + Style.RESET_ALL + "Spend time with friends")
            print(Fore.RED + Style.BRIGHT + "2." + Style.RESET_ALL + "Explore the city of Edirne")
            print(Fore.RED + Style.BRIGHT + "3." + Style.RESET_ALL + "Read a historical book")
            print(Fore.RED + Style.BRIGHT + "4." + Style.RESET_ALL + "Age up")

            choice = input( Style.BRIGHT +"Enter your choice (1/2/3/4): ")

            if choice == "1":
                print( Style.BRIGHT +"You spend time with friends, playing games and having a blast.")
            elif choice == "2":
                print( Style.BRIGHT +"You explore the city of Edirne, discovering new places and making new acquaintances.")
            elif choice == "3":
                print( Style.BRIGHT +"You read a historical book, learning about the great figures of the past.")
            elif choice == "4":
                print( Style.BRIGHT +"You decide to rest for now.")
                time.sleep(3)  # Introduce a delay before aging up
            else:
                continue
            break
        character.age += 1
        time.sleep(2)
        character.print_info()

        print( Style.BRIGHT +"\nYour parents celebrate your sixth birthday with a grand gathering in Edirne, inviting friends and family. It's a special occasion that marks not only your age but also a significant event in your culture: your circumcision.")
        character.stats['looks'] += random.randint(1, 3)  # Event may improve looks
        print(f"" +  Style.BRIGHT +"🎉 Happy 6th Birthday and Circumcision Celebration! Looks: ",character.stats['looks'])

        while True:
            print( Style.BRIGHT +"\nWhat would you like to do?")
            print(Fore.RED + Style.BRIGHT + "1." + Style.RESET_ALL + "Celebrate your circumcision with a feast")
            print(Fore.RED + Style.BRIGHT + "2." + Style.RESET_ALL + "Participate in a traditional dance")
            print(Fore.RED + Style.BRIGHT + "3." + Style.RESET_ALL + "Receive blessings from elders")
            print(Fore.RED + Style.BRIGHT + "4." + Style.RESET_ALL + "Age up")

            choice = input( Style.BRIGHT +"Enter your choice (1/2/3/4): ")

            if choice == "1":
                print( Style.BRIGHT +"You celebrate your circumcision with a grand feast. The delicious food and joyful atmosphere boost your health and looks.")
                character.stats['health'] += 3  # Feast improves health
                character.stats['looks'] += 3 # Feast improves looks
            elif choice == "2":
                print( Style.BRIGHT +"You participate in a traditional dance, showcasing your cultural heritage. It's a joyful experience that enhances your health and looks.")
                character.stats['health'] += 2  # Dance improves health
                character.stats['looks'] += 3 # Dance improves looks
            elif choice == "3":
                print( Style.BRIGHT +"You receive blessings from the elders, who wish you a prosperous and healthy future. The blessings have a positive impact on your health and looks.")
                character.stats['health'] += 3 # Blessings improve health
                character.stats['looks'] += 2  # Blessings improve looks
            elif choice == "4":
                print( Style.BRIGHT +"You decide to rest for now.")
                time.sleep(3)  # Introduce a delay before aging up
            else:
                continue
            break
        character.age += 1
        time.sleep(3)
        character.print_info()
        while True:
            if character.age == 7:
                event_chance = random.randint(1, 10)
                if event_chance <= 5:
                    print( Style.BRIGHT +"\nSurrounded by loved ones, the little one's eyes sparkled with excitement as they blew out the candles on their seventh birthday cake, creating cherished memories in Edirne.")
                    character.stats['looks'] += random.randint(1, 3)  # Event may improve looks
                    print(f""+ Style.BRIGHT +"🎉 Happy 4th Birthday! Looks:" + Style.RESET_ALL ,character.stats['looks'])
                    break
                else:
                    print("\nIt's just an ordinary day as you turn 7 years old.")
                    break
        while True:
            if character.age == 7:
                print(Fore.RED + Style.BRIGHT + "\nAge 7:" + Style.RESET_ALL + Style.BRIGHT + " First Day at Madrassah\n"+ Style.RESET_ALL)
                print(Style.BRIGHT +  Style.BRIGHT +"\nIn the bustling city of Istanbul, during the 15th century Ottoman Empire, you were about to embark on a life-changing journey. It was your first day at the prestigious Madrassah, a center of learning and scholarship where young minds were shaped to serve the empire." + Style.RESET_ALL)
                print(Style.BRIGHT +  Style.BRIGHT +"\nToday is your first day at the local madrassah, a place of both religious and general education. You stand outside the magnificent mosque, its minarets reaching for the heavens. The bustling courtyard is filled with children of various ages, and you can't help but feel a mix of excitement and apprehension." +Style.RESET_ALL)
                print(Fore.RED + "1." + Style.RESET_ALL +  Style.BRIGHT +" You could approach a group of fellow students who were engaged in animated conversation. They seemed friendly, and you hoped to make new friends.")
                print(Fore.RED + "2." + Style.RESET_ALL + Style.BRIGHT + " You could choose to explore the Madrassah on your own, taking in the architecture and the sense of history that surrounded you.")
                print(Fore.RED + "3." + Style.RESET_ALL +  Style.BRIGHT +"You could inquire about the Madrassah's martial training program. The Ottoman Empire valued both scholarly pursuits and martial skills.")
                print(Fore.RED + Style.BRIGHT + "4." + Style.RESET_ALL + Style.BRIGHT + "Age up")

            choice = input( Style.BRIGHT +"Enter your choice (1/2/3/4): ")

            if choice == "1":
                print( Style.BRIGHT +"You decided to approach the group of students. They welcomed you warmly and introduced themselves. You made instant friends who would later become your closest companions throughout your time at the Madrassah. You shared your experiences and received valuable advice on how to navigate the rigorous curriculum..")
                character.stats['diplomacy'] += 3  
            elif choice == "2":
                print( Style.BRIGHT +"You embarked on a solo exploration of the Madrassah. You marveled at the beautifully adorned hallways, the expansive library filled with ancient manuscripts, and the peaceful courtyard gardens. Your independent spirit helped you develop a deep appreciation for the history and culture of the Ottoman Empire.")
                character.stats['intrigue'] += 3  
            elif choice == "3":
                print( Style.BRIGHT +"You began your martial training alongside your academic pursuits. You learned the art of Ottoman martial arts, which emphasized discipline, honor, and self-defense. These skills would later serve you well in defending the empire and its values.")
                character.stats['martial'] += 3  
            elif choice == "4":
                print( Style.BRIGHT +"You decide to rest for now.")
                time.sleep(3)  # Introduce a delay before aging up
            else:
                continue
            break
        madrassah = Madrassah()
        madrassah.main_menu()
        #Implementing MAdrassah System
class Madrassah:
    def __init__(self, num_npcs=10):
        self.num_npcs = num_npcs
        self.male_names = [
            "Mehmet", "Ahmed", "Mustafa", "Selim", "Ibrahim", "Osman", "Orhan", "Bayezid", "Murad", "Suleiman",
            "Hasan", "Husayn", "Abdullah", "Ali", "Yusuf", "Ismail", "Faruk", "Halil", "Huseyin", "Cem",
            "Mehmed", "Ahmed Pasha", "Ahmed Bey", "Mustafa Bey", "Selim Bey", "Ibrahim Efendi", "Osman Bey", "Orhan Bey", "Bayezid Pasha", "Murad Bey",
            "Suleiman Efendi", "Hasan Bey", "Husayn Pasha", "Abdullah Efendi", "Ali Bey", "Yusuf Bey", "Ismail Pasha", "Faruk Efendi", "Halil Bey", "Huseyin Pasha", "Cem Bey",
            "Mehmed Efendi", "Ahmed Bey", "Mustafa Pasha", "Selim Efendi", "Ibrahim Bey", "Osman Pasha", "Orhan Efendi", "Bayezid Bey", "Murad Pasha", "Suleiman Bey",
            "Hasan Efendi", "Husayn Bey", "Abdullah Pasha", "Ali Efendi", "Yusuf Bey", "Ismail Bey", "Faruk Bey", "Halil Pasha", "Huseyin Bey", "Cem Pasha",
            "Mehmed Bey", "Ahmed Efendi", "Mustafa Bey", "Selim Pasha", "Ibrahim Efendi", "Osman Bey", "Orhan Pasha", "Bayezid Efendi", "Murad Bey", "Suleiman Pasha",
            "Hasan Efendi", "Husayn Bey", "Abdullah Pasha", "Ali Efendi", "Yusuf Bey", "Ismail Efendi", "Faruk Bey", "Halil Bey", "Huseyin Pasha", "Cem Pasha",
            "Mehmed Pasha", "Ahmed Efendi", "Mustafa Bey", "Selim Bey", "Ibrahim Pasha", "Osman Efendi", "Orhan Bey", "Bayezid Pasha", "Murad Bey", "Suleiman Efendi",
            "Hasan Efendi", "Husayn Bey", "Abdullah Pasha", "Ali Efendi", "Yusuf Bey", "Ismail Bey", "Faruk Efendi", "Halil Bey", "Huseyin Efendi", "Cem Bey" # List of male names (same as before)
        ]
        self.randomize_names()
        self.npcs = self.generate_npcs()
        self.friends = []
        self.complimented_npcs = []
        self.insulted_npcs =[]


        # Class attributes
        self.brawl_attacks = [
            {"name": "Punch", "description": "A straightforward punch to the opponent's face.", "damage": 5},
            {"name": "Kick", "description": "A powerful kick aimed at the opponent's legs.", "damage": 7},
            {"name": "Slap", "description": "A quick and humiliating slap across the opponent's cheek.", "damage": 3},
        ]

    def randomize_names(self):
        random.shuffle(self.male_names)

    def generate_npcs(self):
        npcs = [{"name": self.male_names[i], "relationship": random.randint(1, 100)} for i in range(self.num_npcs)]
        return npcs

    def display_relationship_table(self):
        data = []
        for i, npc in enumerate(self.npcs, start=1):
            data.append([i, npc["name"], npc["relationship"]])

        headers = ["Number", "Name", "Relationship"]
        table = tabulate(data, headers=headers, tablefmt="grid")
        print("\nRelationship Table:")
        print(table)

    def display_friends_list(self):
        data = []
        for i, friend in enumerate(self.friends, start=1):
            data.append([i, friend])

        headers = ["Number", "Friend's Name"]
        table = tabulate(data, headers=headers, tablefmt="grid")
        print("\nFriends List:")
        print(table)

    def interact_with_npc(self, npc_index):
        npc = self.npcs[npc_index]

        print(f"\nYou are interacting with {npc['name']}.")

        while True:
            print("\nInteraction Options:")
            print("1. Compliment")
            print("2. Have a Conversation")
            print("3. Insult")
            print("4. Brawl")
            print("5. Befriend")
            print("6. Back to Main Menu")

            choice = input("Choose an option (1-6): ")

            if choice == '1':
                # Check if the NPC has already been complimented
                if npc["name"] not in self.complimented_npcs:
                    compliment = self.choose_compliment(npc_name=npc["name"])
                    print(compliment)
                    npc["relationship"] += 5
                    self.complimented_npcs.append(npc["name"])  # Add NPC to the complimented list
                else:
                    print(f"You have already complimented {npc['name']}.")

            elif choice == '2':
                conversation = self.choose_conversation()
                print(conversation)

                # Implement conversation logic and update the relationship
                npc["relationship"] += 3
            elif choice == '3':
                # Check if the NPC is already a friend
                if npc["name"] not in self.friends and npc["name"] not in self.insulted_npcs:
                    insult = self.choose_insult(npc_name=npc["name"])
                    print(insult)
                    npc["relationship"] -= 5
                else:
                    print(f"You cannot insult {npc['name']} until you are friend with them.")
                

            elif choice == '4':
                # Implement brawl logic and update the relationship
                if npc["name"] not in self.friends:
                    brawl = self.choose_brawl()
                    print(brawl)
                    npc["relationship"] -= 10
                else:
                    print(print(f"You cannot brawl with {npc['name']} until you are friend with them."))
            elif choice == '5':
                # Check if the NPC meets the friendship requirement
                if npc["relationship"] >= 80:
                    if npc["name"] not in self.friends:
                        befriend = self.choose_befriend()
                        print(befriend)
                        self.friends.append(npc["name"])
                    else:
                        print(f"You are already friends with {npc['name']}.")
                else:
                    print(f"You need at least 80 relationship points to befriend {npc['name']}.")

            elif choice == '6':
                break
            else:
                print("Invalid choice. Please select a valid option (1-6).")

    def choose_compliment(self, npc_name):
        compliment_lines = [
        "You called {npc_name} quite dashing today!",
        "You said to {npc_name}, 'Your wisdom and wit are truly admirable.'",
        "You mentioned to {npc_name}, 'Your kindness and generosity are unmatched.'",
        "You commented to {npc_name}, 'I must say, you have impeccable taste.'",
        "You remarked to {npc_name}, 'Your presence brightens up the room.'",
        "You complimented {npc_name} on their strength and courage, 'You inspire me.'",
        "You told {npc_name}, 'You have a heart of gold.'",
        "You praised {npc_name} for their eloquence in speech, 'It's impressive.'",
        "You said to {npc_name}, 'You are a true gem among men.'",
        "You expressed to {npc_name}, 'Your friendship means the world to me.'"
        ]
        return random.choice(compliment_lines).format(npc_name=npc_name)

    def choose_insult(self, npc_name):
        insult_lines = [
        "You called {npc_name} nothing but a coward!",
        "You accused {npc_name}, 'Your arrogance knows no bounds.'",
        "You told {npc_name}, 'You lack honor and integrity.'",
        "You condemned {npc_name}, 'Your actions are a disgrace to your name.'",
        "You remarked about {npc_name}, 'You are a blight upon this world.'",
        "You insulted {npc_name}, 'I've met more intelligent rocks than you.'",
        "You mentioned to {npc_name}, 'Your presence is repulsive.'",
        "You stated to {npc_name}, 'You are a pitiful excuse for a human being.'",
        "You declared to {npc_name}, 'You will never amount to anything.'",
        "You expressed, 'I can't stand the sight of you.' to {npc_name}"
        ]
        return random.choice(insult_lines).format(npc_name=npc_name)

    def choose_conversation(self):
        conversation_lines = [
        "Have you heard the latest news from the Ottoman court? There are rumors of an impending alliance with a powerful neighboring kingdom.",
        "The bazaars are bustling with traders from distant lands, offering exotic goods and spices that fill the air with their rich aroma.",
        "I wonder what the future holds for our great empire. The sultan's vision for expansion and prosperity is truly inspiring.",
        "The call to prayer from the minarets is truly enchanting. It's a reminder of our faith and the beauty of our culture.",
        "I've been reading the works of Rumi lately; his poetry is profound and speaks to the depths of the human soul.",
        "The sultan's viziers are known for their wisdom and counsel, guiding the empire with their unparalleled expertise.",
        "I hear the Ottoman army is preparing for a grand campaign to secure new territories and protect our homeland.",
        "The architecture of the Hagia Sophia is awe-inspiring, with its majestic domes and intricate mosaics that tell stories of our history.",
        "Let us discuss philosophy and the nature of existence. Contemplating life's mysteries can lead to profound insights.",
        "Ah, the aroma of spices from the Silk Road! It's a testament to the trade routes that connect our empire to the world."
        ]
        return random.choice(conversation_lines)

    def choose_brawl(self):
        brawl_lines = [
        "You square up for a fight, fists clenched.",
        "A heated argument escalates into a physical confrontation.",
        "Punches are thrown as tempers flare.",
        "The madrassah courtyard becomes a chaotic battleground.",
        "Shouting and shoving quickly turn into a brawl."
        ]
        return random.choice(brawl_lines)

    def choose_befriend(self,npc_name):
        befriend_lines =[
        "Congratulations! You've formed a strong bond with {npc_name}.",
        "Your efforts have paid off, and {npc_name} now considers you a true friend.",
        "You've won {npc_name}'s trust and friendship.",
        "Through your kindness and actions, you've gained {npc_name}'s friendship.",
        "You and {npc_name} have become fast friends.",
        "It's official {npc_name} is now your friend.",
        "Your friendship with {npc_name} deepens as you continue to help them.",
        "A strong friendship has blossomed between you and {npc_name}.",
        "You can count {npc_name} as one of your closest friends now.",
        "{npc_name} smiles warmly at you, solidifying your friendship."
        ]
        return random.choice(befriend_lines).format(npc_name=npc_name)

    def handle_brawl(self, character, opponent):
        print(f"\nYou are in a brawl with {opponent['name']}.")

        # Display brawl attack options
        print("Choose your attack:")
        for i, attack in enumerate(self.brawl_attacks, start=1):
            print(f"{i}. {attack['name']} - {attack['description']}")

        choice = int(input("Enter the number of your chosen attack: ")) - 1  # Subtract 1 to match list indexing
        player_attack = self.brawl_attacks[choice]

        # Randomly select opponent's attack
        opponent_attack = random.choice(self.brawl_attacks)

        # Calculate damage
        player_damage = player_attack["damage"]
        opponent_damage = opponent_attack["damage"]

        # Update health
        character.stats["health"] -= opponent_damage
        print(character.stats["health"])

        print(f"\nYou used {player_attack['name']} and dealt {player_damage} damage.")
        print(f"{opponent['name']} used {opponent_attack['name']} and dealt {opponent_damage} damage.")

        # Function to handle brawls with simplified outcomes
        print(f"\nYou are in a brawl with {opponent['name']}.")

        # Randomly determine the outcome (50% chance of winning)
        outcome = random.choice(["win", "lose"])

        if outcome == "win":
            print(f"You landed a powerful hit on {opponent['name']} and won the brawl!")
            # Implement consequences for winning (e.g., improved relationship)
        else:
            print(f"{opponent['name']} landed a strong blow on you, and you lost the brawl.")

    def main_menu(self,character):
        while True:
            print("\nMain Menu:")
            print("1. View Relationship Table")
            print("2. List of Friends")
            print("3. Interact with an NPC")
            print("4. Quit")

            main_choice = input("Choose an option (1-4): ")

            if main_choice == '1':
                self.display_relationship_table()
            elif main_choice == '2':
                self.display_friends_list()
            elif main_choice == '3':
                self.display_relationship_table()
                try:
                    npc_number = int(input("Enter the number of the NPC you want to interact with (1-10): "))
                    if 1 <= npc_number <= 10:
                        self.interact_with_npc(npc_number - 1)  # Subtract 1 to match list indexing
                    else:
                        print("Invalid NPC number. Please enter a number between 1 and 10.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif main_choice == '4':
                character.age += 1
                print("Thanks for playing! Goodbye.")
                break
            else:
                print("Invalid choice. Please select a valid option (1-4).")

        
        


class GameEngine:
    def __init__(self):
        self.characters = []
        self.stats = []
        self.events = [Event]  
        madrassah = Madrassah()

        
    
    def start_game(self):
        print(text2art("Tales of Heritage"))
        print(Fore.GREEN + Style.BRIGHT + "Hello, Adventurer! Welcome to 'Tales of Heritage,' a realm where you're the author of your destiny.\nEmbark on an epic journey through time, navigating the twists and turns of history.\nAs you shape your character's path, prepare to witness the tapestry of the Renaissance era unfurl before you.\nCraft your legacy, make daring choices, and let your name echo through the ages in this immersive tale.\n" + Style.RESET_ALL)
        print(Style.BRIGHT + "Shape your protagonist and embark on a Renaissance odyssey within the vibrant tapestry of the Ottoman Empire—where your choices shape not only your destiny but the fate of an empire.\n")
        # Call the get method to create a character
        character = Character.get()
        # Add the character to the list of characters
        if character:
            self.characters.append(character)
        character.print_info()
        event_instance = Event()
        event_instance.event(character)

        #To keep health and looks under 100%
        while True:
            if character.stats['health'] >= 100:
                character.stats['health'] = 100
            elif character.stats['health'] <= 0:
                character.stats['health'] = 0
            if character.stats['looks'] >= 100:
                character.stats['looks'] = 100
            elif character.stats['looks'] <= 0:
                character.stats['looks'] = 0

# Play a sound effect
def play_sound_effect(sound_file):
    playsound(sound_file)

# Create a separate thread to play the sound
sound_thread = threading.Thread(target=play_sound_effect, args=('EU4_Domination.wav',))

# Start the thread
sound_thread.start()



# Create a game engine instance and start the game
game_engine = GameEngine()
game_engine.start_game()