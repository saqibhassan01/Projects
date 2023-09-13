import random
from colorama import Fore, Style
from art import text2art
from playsound import playsound
from tabulate import tabulate


class Character:
    def __init__(self, name = "",age = 0, gold = 25, prestige = 0):
        self.name = name
        self.age = age
        self.career = None
        self.gold = gold
        self.prestige = prestige
        self.stats = {
            "health" : random.randint(20,100),
            "looks" : random.randint(20,100),
            "smart" : random.randint(20,100),
            "martial": random.randint(2,5),
            "diplomacy": random.randint(2,5),
            "intrigue": random.randint(2,5),
        }


    @classmethod
    def get(cls):
        try:
            name = input(Fore.RED + Style.BRIGHT + "Name: " + Style.RESET_ALL).title()
            return cls(name)
        except ValueError:
            print("Invalid Name")
            pass

    def print_info(self):
        print("<----------------------------------->\n")
        print(Fore.RED + Style.BRIGHT + "Name: " + Style.RESET_ALL + Style.BRIGHT + self.name + Style.RESET_ALL)
        print(Fore.RED + Style.BRIGHT + "Age:" + Style.RESET_ALL + Style.BRIGHT ,self.age , Style.RESET_ALL)
        print(Fore.RED + Style.BRIGHT + "Dinars:" + Style.RESET_ALL+ Style.BRIGHT ,self.gold , Style.RESET_ALL)
        print(Fore.RED + Style.BRIGHT + "Prestige:" + Style.RESET_ALL+ Style.BRIGHT ,self.prestige ,Style.RESET_ALL)
        print( Fore.RED + Style.BRIGHT + "Attributes: " + Style.RESET_ALL )
        print(f"❤️" + Style.BRIGHT + Fore.GREEN + "  Health:",self.stats['health'],"%" + Style.RESET_ALL)
        print(f"🔥" + Style.BRIGHT + Fore.YELLOW + "Looks:",self.stats['looks'],"%" + Style.RESET_ALL)
        print(f"🎓" + Style.BRIGHT + Fore.YELLOW + "Looks:",self.stats['smart'],"%" + Style.RESET_ALL)
        print(Fore.RED + Style.BRIGHT + "Stats: " + Style.RESET_ALL + Style.BRIGHT +
              f"⚔️  Martial:{self.stats['martial']}  ✍️  Diplo:{self.stats['diplomacy']}  🕵️  Intrigue{self.stats['intrigue']}" + Style.RESET_ALL)
        print("\n<----------------------------------->")
    
    def regulate(self):
        #To keep health and looks under 100% and not lower then 0%
        while True:
            if self.stats['health'] >= 100:
                self.stats['health'] = 100
            elif self.stats['health'] <= 0:
                self.stats['health'] = 0
            if self.stats['looks'] >= 100:
                self.stats['looks'] = 100
            elif self.stats['looks'] <= 0:
                self.stats['looks'] = 0
            if self.stats['smart'] >= 100:
                self.stats['smart'] = 100
            elif self.stats['smart'] <= 0:
                self.stats['smart'] = 0


class Event:
    def __init__(self, shaykh = "", qari = "", shaykh_trust = 0, qari_trust = 0):
        self.shaykh = shaykh
        self.shaykh_trust = shaykh_trust
        self.qari = qari
        self.qari_trust = qari_trust
    def event(self,character):
        main_menu = Player()
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

        zero_year_old_events = {
    "event1": [
        "First steps",
        "At the age of one, you take your first unsteady steps, supported by the loving hands of your parents."
    ],
    "event2": [
        "Naming ceremony",
        "Your family holds a naming ceremony, and you are officially given your name, a source of pride and identity."
    ],
    "event3": [
        "First words",
        "You utter your first words, bringing joy and laughter to your family as they celebrate this milestone."
    ],
    "event4": [
        "Family gathering",
        "Your extended family gathers to celebrate your first birthday, showering you with blessings and gifts."
    ],
    "event5": [
        "Exploring the world",
        "You begin to explore your immediate surroundings, touching objects and experiencing the world with curiosity."
    ],
}

        selected_event_key = random.choice(list(zero_year_old_events.keys()))
        selected_event = zero_year_old_events[selected_event_key]

        

        character.age += 1
        print("\n" + Fore.YELLOW + Style.BRIGHT + "Age 0: A New Beginning" + Style.RESET_ALL)
        print(Style.BRIGHT + event0)
        print(f"" + Style.BRIGHT + "At the age of one year, ",selected_event[0].lower(), selected_event[1])

        # Event 1: First Birthday Celebration
        while True:
            if character.age == 1:
                event_chance = random.randint(1, 10)
                if event_chance <= 5:
                    print(Style.BRIGHT + "\nToday, your parents celebrate your first birthday with a small family gathering.")
                    character.stats['looks'] += random.randint(1, 3)
                    print(f"Looks: {character.stats['looks']}")
                    break
                else:
                    print(Style.BRIGHT + "\nIt's just an ordinary day in your life as you are now a one-year-old.")
                    break

        # Main game loop
        while True:
            print("\n" + Style.BRIGHT + "What would you like to do?" + Style.RESET_ALL)
            print(Fore.RED + Style.BRIGHT + "1." + Style.RESET_ALL + " Eat")
            print(Fore.RED + Style.BRIGHT + "2." + Style.RESET_ALL + " Take a nap")
            print(Fore.RED + Style.BRIGHT + "3." + Style.RESET_ALL + " Play")
            print(Fore.RED + Style.BRIGHT + "4." + Style.RESET_ALL + " Age up")

            choice = input(Style.BRIGHT + "Enter your choice (1/2/3/4): " + Style.RESET_ALL)

            if choice == "1":
                character.stats['health'] += random.randint(1, 2)
                character.stats['looks'] += random.randint(-2, 1)
                print(Style.BRIGHT + "You eat some baby food.")
            elif choice == "2":
                character.stats['health'] += random.randint(2, 4)
                print(Style.BRIGHT + "You take a nap.")
            elif choice == "3":
                character.stats['looks'] += random.randint(1, 2)
                print(Style.BRIGHT + "You play with your toys.")
            elif choice == "4":
                print(Style.BRIGHT + "You decide to rest for now.")
            else:
                continue
            break
            
        character.age += 1
        
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
        
        two_year_old_events = {
    "event1": [
        "A Blessing from the Imam",
        "The local Imam visits your home and bestows a blessing upon you, wishing you a life filled with wisdom and kindness."
    ],
    "event2": [
        "A Precious Family Heirloom",
        "Your family gifts you a treasured heirloom, a beautifully crafted silver rattle, which you grasp with delight."
    ],
    "event3": [
        "An Unexpected Companion",
        "You find a stray kitten in your home, and it becomes your constant source of joy as you giggle and play together."
    ],
    "event4": [
        "A Taste of Sweet Dates",
        "Your parents introduce you to the sweetness of dates, and your face lights up as you savor the delicious flavor."
    ],
    "event5": [
        "A Lullaby from Grandma",
        "Your grandmother sings a soothing lullaby to put you to sleep, filling your dreams with visions of a bright future."
    ],
}

        selected_event_key = random.choice(list(two_year_old_events.keys()))
        selected_event = two_year_old_events[selected_event_key]

        # Age 2: A Year of Discovery
        print("\n" + Fore.YELLOW + Style.BRIGHT + "Age 2: A Year of Discovery" + Style.RESET_ALL)
        print(Style.BRIGHT +event2)
        print(f"At the age of two year, {selected_event[0].lower()}. {selected_event[1]}")

        # Event 1: Second Birthday Celebration
        while True:
            if character.age == 2:
                event_chance = random.randint(1, 10)
                if event_chance <= 5:
                    print(Style.BRIGHT + "\nYour parents celebrate your second birthday with a small gathering, showering you with affection and gifts.")
                    character.stats['looks'] += random.randint(1, 3)
                    print(f"Looks: {character.stats['looks']}")
                    break
                else:
                    print(Style.BRIGHT + "\nIt's just an ordinary day as you turn 2 years old.")
                    break

        # Main game loop
        while True:
            print("\n" + Style.BRIGHT + "What would you like to do?" + Style.RESET_ALL)
            print(Fore.RED + Style.BRIGHT + "1." + Style.RESET_ALL + " Explore the house")
            print(Fore.RED + Style.BRIGHT + "2." + Style.RESET_ALL + " Mimic your parents")
            print(Fore.RED + Style.BRIGHT + "3." + Style.RESET_ALL + " Play with toys")
            print(Fore.RED + Style.BRIGHT + "4." + Style.RESET_ALL + " Age up")

            choice = input(Style.BRIGHT + "Enter your choice (1/2/3/4): " + Style.RESET_ALL)

            if choice == "1":
                character.stats['looks'] += random.randint(1, 2)
                print(Style.BRIGHT + "You explore your home in Edirne, discovering new corners and objects.")
            elif choice == "2":
                character.stats['looks'] += random.randint(1, 3)
                print(Style.BRIGHT + "You try to mimic your parents' actions and words, showing early signs of learning.")
            elif choice == "3":
                character.stats['looks'] += random.randint(1, 2)
                print(Style.BRIGHT + "You have fun playing with your toys, showcasing your creativity.")
            elif choice == "4":
                print(Style.BRIGHT + "You decide to rest for now.")
            else:
                continue
            break
            
        character.age += 1
        
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
        three_year_old_events = {
    "event1": [
        "A Visit to the Grand Mosque",
        "Your family takes you to the magnificent Grand Mosque of Edirne, and you're awestruck by its grandeur and serenity."
    ],
    "event2": [
        "An Artistic Discovery",
        "You discover your love for drawing and painting when you create your first colorful artwork with the help of your family."
    ],
    "event3": [
        "A Playful Day at the Riverside",
        "You spend a delightful day by the riverside, skipping stones and watching boats go by with your family."
    ],
    "event4": [
        "A Taste of Exotic Spices",
        "Your parents introduce you to the flavors of exotic spices, and you develop a fondness for the rich, aromatic cuisine."
    ],
    "event5": [
        "A Visit from a Jester",
        "A jester entertains you with funny tricks and jokes, leaving you in fits of giggles and wonder."
    ],
}

        selected_event_key = random.choice(list(three_year_old_events.keys()))
        selected_event = three_year_old_events[selected_event_key]

        print("\n" + Fore.YELLOW + Style.BRIGHT + "Age 3: A Year of Exploration" + Style.RESET_ALL)
        print(Style.BRIGHT + event3)
        print(f"At the age of three years, {selected_event[0].lower()}. {selected_event[1]}")

        # Event 1: Third Birthday Celebration
        while True:
            if character.age == 3:
                event_chance = random.randint(1, 10)
                if event_chance <= 5:
                    print(Style.BRIGHT + "\nYour parents celebrate your third birthday with a grand gathering in Edirne, inviting friends and family.")
                    character.stats['looks'] += random.randint(1, 3)
                    print(f"🎉 Happy 3rd Birthday! Looks: {character.stats['looks']}")
                    break
                else:
                    print(Style.BRIGHT + "\nIt's just an ordinary day as you turn 3 years old.")
                    break

        # Main game loop
        while True:
            print("\n" + Style.BRIGHT + "What would you like to do?" + Style.RESET_ALL)
            print(Fore.RED + Style.BRIGHT + "1." + Style.RESET_ALL + " Explore the blacksmith's tools")
            print(Fore.RED + Style.BRIGHT + "2." + Style.RESET_ALL + " Ask your parents questions")
            print(Fore.RED + Style.BRIGHT + "3." + Style.RESET_ALL + " Play with your friends")
            print(Fore.RED + Style.BRIGHT + "4." + Style.RESET_ALL + " Age up")

            choice = input(Style.BRIGHT + "Enter your choice (1/2/3/4): " + Style.RESET_ALL)

            if choice == "1":
                character.stats['looks'] += random.randint(1, 2)
                print(Style.BRIGHT + "You explore your father's friend's blacksmithing tools, fascinated by the shiny metals.")
                print("While exploring, you accidentally cut your finger on a sharp edge.")
                print("Your parents rush to comfort you and bandage your finger.")
            elif choice == "2":
                character.stats['looks'] += random.randint(1, 3)
                print(Style.BRIGHT + "You ask your parents countless questions, eager to learn about the world.")
                print("Your parents patiently answer your questions, sparking your curiosity.")
                print("You continue to ask more questions and gain knowledge.")
            elif choice == "3":
                character.stats['looks'] += random.randint(1, 2)
                print(Style.BRIGHT + "You have a great time playing with your friends in the streets of Edirne.")
                print("You develop strong bonds with your playmates and enjoy their company.")
            elif choice == "4":
                print(Style.BRIGHT + "You decide to rest for now.")
            else:
                continue
            break
        character.age += 1
        
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
        
        while True:
            if character.age == 4:
                event_chance = random.randint(1, 10)
            if event_chance <= 5:
                print( Style.BRIGHT +"\nUnder the starry Edirne sky, laughter filled the air as friends and family gathered to celebrate a joyous fourth birthday.")
                character.stats['looks'] += random.randint(1, 3) 
                print(f""+ Style.BRIGHT +"🎉 Happy 4th Birthday! Looks:" + Style.RESET_ALL ,character.stats['looks'])
                break
            else:
                print( Style.BRIGHT +"\nIt's just an ordinary day as you turn 4 years old.")
                break


        while True:
            # Age 4: Introduction
            print("\n" + Fore.YELLOW + Style.BRIGHT + "Age 4: A New Beginning" + Style.RESET_ALL)
            print(Style.BRIGHT +event4)

            # Event 1: Ask for a Wooden Sword
            print("\n" + Fore.YELLOW + Style.BRIGHT + "Event 1: Ask for a Wooden Sword" + Style.RESET_ALL)
            print("You've always admired the brave knights in stories and want to become one.")
            print("You ask your father for a wooden sword, hoping to start your training as a young knight.")

            # Event 2: Sneak into Father's Study
            print("\n" + Fore.YELLOW + Style.BRIGHT + "Event 2: Sneak into Father's Study" + Style.RESET_ALL)
            print("Your father's study is filled with books and mysterious objects. You're curious about what he keeps there.")
            print("You decide to sneak into your father's study to uncover its secrets.")

            # Event 3: Help Your Mother with Her Guests
            print("\n" + Fore.YELLOW + Style.BRIGHT + "Event 3: Help Your Mother with Her Guests" + Style.RESET_ALL)
            print("A grand feast is being held at your home, and your mother is busy attending to the guests.")
            print("You want to be helpful and decide to assist your mother during the feast.")

            print("\n" + Style.BRIGHT + "What would you like to do?" + Style.RESET_ALL)
            print(Fore.RED + Style.BRIGHT + "1." + Style.RESET_ALL + " Ask your father for a wooden sword")
            print(Fore.RED + Style.BRIGHT + "2." + Style.RESET_ALL + " Sneak into your father's study")
            print(Fore.RED + Style.BRIGHT + "3." + Style.RESET_ALL + " Help your mother with her guests")
            print(Fore.RED + Style.BRIGHT + "4." + Style.RESET_ALL + " Age up")

            choice = input(Style.BRIGHT + "Enter your choice (1/2/3/4): " + Style.RESET_ALL)

            if choice == "1":
                character.stats['martial'] += 2
                print(Style.BRIGHT + "You ask your father for a wooden sword. He smiles and agrees, handing you a finely crafted wooden sword.")
                print("You begin training with it, improving your martial skills.")
            elif choice == "2":
                character.stats['intrigue'] += 2
                print(Style.BRIGHT + "You decide to sneak into your father's study, intrigued by the secrets it holds.")
                print("You carefully open the door and explore the room, discovering hidden scrolls and documents.")
                print("Your intrigue skills grow as you uncover valuable knowledge.")
            elif choice == "3":
                character.stats['diplomacy'] += 2
                print(Style.BRIGHT + "You choose to help your mother with her guests during the grand feast.")
                print("You gracefully interact with the guests, making them feel welcomed and appreciated.")
                print("Your mother smiles at your diplomatic skills, and you learn more about the art of diplomacy and negotiation.")
            elif choice == "4":
                print(Style.BRIGHT + "You decide to rest for now.")
            else:
                continue
            break
        character.age += 1
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
        events5 = random.choice(events5)

        

        # Age 5: A Year of Exploration
        print("\n" + Fore.YELLOW + Style.BRIGHT + "Age 5: A Year of Exploration" + Style.RESET_ALL)
        print(Style.BRIGHT ,events5)

        # Event 1: Fifth Birthday Celebration
        while True:
            if character.age == 5:
                event_chance = random.randint(1, 10)
                if event_chance <= 5:
                    print(Style.BRIGHT + "\nThe aroma of delicious Turkish cuisine wafted through the evening breeze, making the grand feast in Edirne an unforgettable celebration of the youngster's fifth birthday.")
                    character.stats['looks'] += random.randint(1, 3)
                    print(f"🎉 Happy 5th Birthday! Looks: {character.stats['looks']}")
                    break
                else:
                    print(Style.BRIGHT + "\nIt's just an ordinary day as you turn 5 years old.")
                    break

        # Main game loop
        while True:
            print("\n" + Style.BRIGHT + "What would you like to do?" + Style.RESET_ALL)
            print(Fore.RED + Style.BRIGHT + "1." + Style.RESET_ALL + " Spend time with friends")
            print(Fore.RED + Style.BRIGHT + "2." + Style.RESET_ALL + " Explore the city of Edirne")
            print(Fore.RED + Style.BRIGHT + "3." + Style.RESET_ALL + " Read a historical book")
            print(Fore.RED + Style.BRIGHT + "4." + Style.RESET_ALL + " Age up")

            choice = input(Style.BRIGHT + "Enter your choice (1/2/3/4): " + Style.RESET_ALL)

            if choice == "1":
                print(Style.BRIGHT + "You spend time with friends, playing games.")
                character.stats['health'] += random.randint(2,5)
            elif choice == "2":
                print(Style.BRIGHT + "You explore the city of Edirne, discovering new places and making new acquaintances.")
                character.stats['smart'] += random.randint(2,5)
            elif choice == "3":
                print(Style.BRIGHT + "You read a historical book, learning about the great figures of the past.")
                character.stats['smart'] += random.randint(2,5)
            elif choice == "4":
                print(Style.BRIGHT + "You decide to rest for now.")
            else:
                continue
            break
        character.age += 1
        
        character.print_info()

        # Age 6: A Special Celebration
        print("\n" + Fore.YELLOW + Style.BRIGHT + "Age 6: A Special Celebration" + Style.RESET_ALL)
        print("You are now 6 years old, and this year's celebration holds a significant event in your culture: your circumcision.")

        # Event 1: Sixth Birthday and Circumcision Celebration
        while True:
            if character.age == 6:
                event_chance = random.randint(1, 10)
                if event_chance <= 5:
                    print(Style.BRIGHT + "\nYour parents celebrate your sixth birthday with a grand gathering in Edirne, inviting friends and family. It's a special occasion that marks not only your age but also a significant event in your culture: your circumcision.")
                    character.stats['looks'] += random.randint(1, 3)
                    print(f"🎉 Happy 6th Birthday and Circumcision Celebration! Looks: {character.stats['looks']}")
                    break
                else:
                    print(Style.BRIGHT + "\nIt's just an ordinary day as you turn 6 years old.")
                    break

        # Main game loop
        while True:
            print("\n" + Style.BRIGHT + "What would you like to do?" + Style.RESET_ALL)
            print(Fore.RED + Style.BRIGHT + "1." + Style.RESET_ALL + " Celebrate your circumcision with a feast")
            print(Fore.RED + Style.BRIGHT + "2." + Style.RESET_ALL + " Participate in a traditional dance")
            print(Fore.RED + Style.BRIGHT + "3." + Style.RESET_ALL + " Receive blessings from elders")
            print(Fore.RED + Style.BRIGHT + "4." + Style.RESET_ALL + " Age up")

            choice = input(Style.BRIGHT + "Enter your choice (1/2/3/4): " + Style.RESET_ALL)

            if choice == "1":
                print(Style.BRIGHT + "You celebrate your circumcision with a grand feast. The delicious food and joyful atmosphere boost your health and looks.")
                character.stats['health'] += random.randint(2,5)
                character.stats['looks'] += random.randint(2,5)
            elif choice == "2":
                print(Style.BRIGHT + "You participate in a traditional dance, showcasing your cultural heritage. It's a joyful experience that enhances your health and looks.")
                character.stats['health'] += random.randint(2,5)
                character.stats['looks'] += random.randint(2,5)
            elif choice == "3":
                print(Style.BRIGHT + "You receive blessings from the elders, who wish you a prosperous and healthy future. The blessings have a positive impact on your health and looks.")
                character.stats['health'] += random.randint(2,5)
                character.stats['looks'] += random.randint(2,5)
            elif choice == "4":
                print(Style.BRIGHT + "You decide to rest for now.")
                break
            else:
                continue
        character.age += 1
        
        character.print_info()
        # Age 7: A New Beginning
        print("\n" + Fore.YELLOW + Style.BRIGHT + "Age 7: A New Beginning" + Style.RESET_ALL)
        print("You have reached the age of 7, and exciting adventures await you.")

        # Event 1: Seventh Birthday Celebration
        while True:
            if character.age == 7:
                event_chance = random.randint(1, 10)
                if event_chance <= 5:
                    print(Style.BRIGHT + "\nSurrounded by loved ones, your eyes sparkled with excitement as you blew out the candles on your seventh birthday cake, creating cherished memories in Edirne.")
                    character.stats['looks'] += random.randint(1, 3)
                    print(f"🎉 Happy 7th Birthday! Looks: {character.stats['looks']}")
                    break
                else:
                    print(Style.BRIGHT + "\nIt's just an ordinary day as you turn 7 years old.")
                    break

        # Event 2: First Day at Madrassah
        while True:
            if character.age == 7:
                print(Fore.RED + Style.BRIGHT + "\nAge 7:" + Style.RESET_ALL + Style.BRIGHT + " First Day at Madrassah\n" + Style.RESET_ALL)
                print(Style.BRIGHT + "\nIn the bustling city of Istanbul, during the 15th century Ottoman Empire, you were about to embark on a life-changing journey. It was your first day at the prestigious Madrassah, a center of learning and scholarship where young minds were shaped to serve the empire.")
                print(Style.BRIGHT + "\nToday is your first day at the local madrassah, a place of both religious and general education. You stand outside the magnificent mosque, its minarets reaching for the heavens. The bustling courtyard is filled with children of various ages, and you can't help but feel a mix of excitement and apprehension.")
                print(Fore.RED + "1." + Style.RESET_ALL + Style.BRIGHT + " You could approach a group of fellow students who were engaged in animated conversation. They seemed friendly, and you hoped to make new friends.")
                print(Fore.RED + "2." + Style.RESET_ALL + Style.BRIGHT + " You could choose to explore the Madrassah on your own, taking in the architecture and the sense of history that surrounded you.")
                print(Fore.RED + "3." + Style.RESET_ALL + Style.BRIGHT + " You could inquire about the Madrassah's martial training program. The Ottoman Empire valued both scholarly pursuits and martial skills.")
                break
        while True:
            choice = input(Style.BRIGHT + "Enter your choice (1/2/3/4): " + Style.RESET_ALL)

            if choice == "1":
                print(Style.BRIGHT + "You decided to approach the group of students. They welcomed you warmly and introduced themselves. You made instant friends who would later become your closest companions throughout your time at the Madrassah. You shared your experiences and received valuable advice on how to navigate the rigorous curriculum.")
                character.stats['diplomacy'] += random.randint(2,5)
                break
            elif choice == "2":
                print(Style.BRIGHT + "You embarked on a solo exploration of the Madrassah. You marveled at the beautifully adorned hallways, the expansive library filled with ancient manuscripts, and the peaceful courtyard gardens. Your independent spirit helped you develop a deep appreciation for the history and culture of the Ottoman Empire.")
                character.stats['intrigue'] += random.randint(2,5)
                break
            elif choice == "3":
                print(Style.BRIGHT + "You began your martial training alongside your academic pursuits. You learned the art of Ottoman martial arts, which emphasized discipline, honor, and self-defense. These skills would later serve you well in defending the empire and its values.")
                character.stats['martial'] += random.randint(2,5)
                break
            else:
                continue
            
            break
        
        character.age += 1
        character.print_info()
        madrassah = Madrassah()
        madrassah.main_menu(character)
        while True:
            print("\n" + Fore.YELLOW + Style.BRIGHT + "Age 8: A Magical Journey Begins" + Style.RESET_ALL)
            print("You are now 8 years old, embarking on your second year at the Madrassah.")
            event_chance = random.randint(1, 10)
            if event_chance <= 5:
                print(Style.BRIGHT + "\nAs you celebrate your eighth birthday, you reflect on your time at the Madrassah. Each day has been a journey of learning and discovery, and you feel a growing sense of purpose and knowledge.")
                character.stats['looks'] += random.randint(1, 3) 
                print(f""+ Style.BRIGHT +"🎉 Happy 8th Birthday! Looks:" + Style.RESET_ALL ,character.stats['looks'])
                break
            else:
                print("\nIt's just an ordinary day as you turn 8 years old.")
                break
        while True:
            if character.age == 8:
                print(Fore.RED + Style.BRIGHT + "\nAge 8:" + Style.RESET_ALL + Style.BRIGHT + " Progress at the Madrassah\n" + Style.RESET_ALL)
                print(Style.BRIGHT + "\nThe Madrassah courtyard bustles with life, just as it did a year ago. Young minds, each with unique dreams and aspirations, fill the air with a palpable sense of ambition. The towering minarets of the nearby mosque remind you of the profound importance of this place." + Style.RESET_ALL)
                print(Style.BRIGHT + "\nYou've thrived during this year of learning and spiritual growth, and now it's time to make a decision that will shape your destiny. As you reflect on the path that calls to your heart, a sense of gravity fills the air.\n\nThree distinct groups await you, each offering a different journey and purpose:" + Style.RESET_ALL)
                print(Style.BRIGHT+  Fore.RED + "This is the most Important Decision Until Now,So Choose Wisely")
                print(Fore.RED + "1." + Style.RESET_ALL + Style.BRIGHT + " Join Talib al-Ilm\nThe pursuit of wisdom and intellectual growth beckons you. To choose this path is to embrace the scholarly life, to delve deep into the mysteries of faith and philosophy. If you join Talib al-Ilm, you will embark on a journey of academic rigor, honing your critical thinking and knowledge-seeking abilities. Scholarly pursuits and intellectual debates will be your companions.")
                print(Fore.RED + "2." + Style.RESET_ALL + Style.BRIGHT + " \nEmbrace Hafiz-e-Quran\nThe sacred verses of the Quran have captured your heart. To choose this path is to dedicate your life to preserving and spreading the divine teachings. If you join Hafiz-e-Quran, you will become a guardian of the holy scripture, with a focus on memorization, recitation, and interpretation of the Quran. Your deep connection to the Quran will guide your spiritual journey.")
                print(Fore.RED + "3." + Style.RESET_ALL + Style.BRIGHT + " \nEmbark on the path of Sufi Müritler\nYour soul longs for a deeper, more spiritual understanding of the world. To choose this path is to embark on a mystical journey that transcends the boundaries of ordinary existence. If you join Sufi Müritler, you will immerse yourself in spiritual practices, Sufi poetry, and the pursuit of divine love and enlightenment. Your path will be marked by moments of deep spiritual insight.")

            choice = input(Style.BRIGHT + "Enter your choice (1/2/3/4): ")

            if choice == "1":
                print(Style.BRIGHT + "You embrace the path of knowledge with enthusiasm. Your dedication to scholarship earns you the respect of your teachers and peers. As you delve deeper into the world of Islamic studies, your critical thinking skills sharpen, and you become a formidable thinker. Your journey is marked by academic challenges, theological debates, and the pursuit of wisdom.")
                madrassah.join_group_talib()
                while True:
                    if character.age == 8:
                        print("\n" + Fore.RED + Style.BRIGHT + "Age 8: The Journey of Knowledge Begins" + Style.RESET_ALL)
                        print("You are 8 years old and have just joined the Talib al-Ilm group at the Madrassah.")
                        print("Your journey towards the pursuit of wisdom, knowledge, and intellectual growth begins.")

                        # Event 1: The Scholarly Mentor
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Scholarly Mentor" + Style.RESET_ALL)
                        print("You meet your scholarly mentor, a learned and inquisitive teacher dedicated to nurturing young minds.")
                        print("Your mentor introduces you to the world of academic study and intellectual exploration.")
                        character.stats['diplomacy'] += random.randint(2,5)                        
                        # Event 2: The Library of Knowledge
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Library of Knowledge" + Style.RESET_ALL)
                        print("You are led to the Madrassah's vast library, a treasure trove of ancient texts and knowledge.")
                        print("The books within inspire your curiosity and fuel your passion for learning.")
                        character.stats['intrigue'] += random.randint(2,5)
                        # Event 3: The First Intellectual Challenge
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The First Intellectual Challenge" + Style.RESET_ALL)
                        print("You are presented with your first intellectual challenge, a puzzle that requires critical thinking.")
                        print("You approach the challenge with curiosity and determination.")
                        character.stats['smart'] += random.randint(2,5)
                        # Choices
                        print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                        print("1. Dedicate Yourself to the Pursuit of Knowledge")
                        print("2. Explore the Vast Library Further")
                        print("3. Embrace the Intellectual Challenge")

                        
                        choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                        if choice == "1":
                            print("\nYou choose to dedicate yourself to the pursuit of knowledge, embracing the scholarly path.")
                            print("Your knowledge and curiosity begin to grow as you dive deeper into academic studies.")
                            # Implement character growth and story progression for the pursuit of knowledge
                            character.stats['smart'] += random.randint(2,5)
                        elif choice == "2":
                            print("\nYou decide to explore the vast library further, immersing yourself in the world of books and texts.")
                            print("The knowledge contained within inspires you and broadens your intellectual horizons.")
                            # Implement character growth and story progression for exploring the library
                            character.stats['intrigue'] += random.randint(2,5)
                        elif choice == "3":
                            print("\nYou choose to embrace the intellectual challenge, solving it with curiosity and determination.")
                            print("This experience strengthens your critical thinking skills and your passion for intellectual pursuits.")
                            # Implement character growth and story progression for embracing challenges
                            character.stats['smart'] += random.randint(2,5)
                        else:
                            continue
    
                        break
                character.age += 1
                character.print_info()
                madrassah.main_menu(character)
                while True:
                    if character.age == 9:
                        event_chance = random.randint(1, 10)
                    if event_chance <= 5:
                        print(Style.BRIGHT + "\nAs you celebrate your ninth birthday, you reflect on your time at the Madrassah. Each day has been a journey of learning and discovery, and you feel a growing sense of purpose and knowledge.")
                        character.stats['looks'] += random.randint(1, 3) 
                        print(f""+ Style.BRIGHT +"🎉 Happy 9th Birthday! Looks:" + Style.RESET_ALL ,character.stats['looks'])
                        break
                    else:
                        print("\nIt's just an ordinary day as you turn 9 years old.")
                        break
                while True:
                    if character.age == 9:
                        print(Fore.RED + Style.BRIGHT + "\nAge 9:" + Style.RESET_ALL + Style.BRIGHT + " The Scholar's Path\n" + Style.RESET_ALL)
                        print(Style.BRIGHT + "\nAs you take your first steps down the path of Talib al-Ilm, the Madrassah welcomes you with open arms. The yearning for knowledge burns brightly within you, and you're eager to delve deeper into the world of scholarship." + Style.RESET_ALL)
                        print(Style.BRIGHT + "\nYour days are filled with rigorous study, guided by devoted mentors who impart wisdom with every lesson. Books become your trusted companions, and the corridors of the Madrassah echo with intellectual debates and discussions." + Style.RESET_ALL)
                        print(Style.BRIGHT + "\nIn the library, a treasure trove of ancient texts awaits your exploration. Here, you uncover the works of renowned philosophers, scholars, and theologians. You immerse yourself in their writings, gaining insights into the complexities of faith and the universe." + Style.RESET_ALL)
                        print(Style.BRIGHT + Fore.RED + "This is a year of profound learning and growth. Your dedication to scholarship shapes your character and the path ahead.")
                        print(Fore.RED + "1." + Style.RESET_ALL + Style.BRIGHT + " Assist a fellow student with a challenging passage\nYou offer your help, explaining the passage patiently. Your act of kindness strengthens friendships and earns you the respect of your peers. Your reputation as a knowledgeable and helpful student grows.")
                        print(Fore.RED + "2." + Style.RESET_ALL + Style.BRIGHT + " Continue your intense studies\nYou choose to focus on your own studies, recognizing the importance of academic excellence. Your dedication to scholarship leads to remarkable progress in your intellectual pursuits.")
                        print(Fore.RED + "3." + Style.RESET_ALL + Style.BRIGHT + " Suggest studying together\nYou suggest studying together to tackle difficult subjects. Collaborative learning deepens your bonds with fellow students, and together, you conquer academic challenges.")

                        choice = input(Style.BRIGHT + "Enter your choice (1/2/3): ")

                        if choice == "1":
                            print(Style.BRIGHT + "You offer your assistance to the struggling student, patiently explaining the challenging passage. Your act of kindness strengthens the bonds of friendship and earns you the respect of your peers. Your reputation as a knowledgeable and helpful student grows.")
                            character.stats["diplomacy"] += random.randint(2,5)
                        elif choice == "2":
                            print(Style.BRIGHT + "You choose to focus on your own studies, recognizing the importance of academic excellence. Your dedication to scholarship leads to remarkable progress in your intellectual pursuits.")
                            character.stats["smart"] += random.randint(2,5)
                        elif choice == "3":
                            print(Style.BRIGHT + "You suggest studying together with your fellow students to tackle difficult subjects. Collaborative learning deepens your bonds with your peers, and together, you conquer academic challenges.")
                            character.stats["diplomacy"] += random.randint(1,3)
                            character.stats["smart"] += random.randint(1,3)
                        else:
                            continue
                        break
                character.age += 1
                character.print_info()
                madrassah.main_menu(character)
                while True:
                    if character.age == 10:
                        event_chance = random.randint(1, 10)
                        if event_chance <= 5:
                            print(Style.BRIGHT + "\nAs you celebrate your tenth birthday, the weight of knowledge rests comfortably upon your shoulders. Each day at the Madrassah deepens your commitment to the path of wisdom, and you stand on the threshold of a new year filled with intellectual promise.")
                            character.stats['looks'] += random.randint(1, 3) 
                            print(f""+ Style.BRIGHT +"🎉 Happy 10th Birthday! Looks:" + Style.RESET_ALL ,character.stats['looks'])
                            break
                        else:
                            print("\nIt's just an ordinary day as you turn 10 years old.")
                            break
                while True:
                    if character.age == 10:
                        print(Fore.RED + Style.BRIGHT + "\nAge 10:" + Style.RESET_ALL + Style.BRIGHT + " Pursuit of Knowledge Deepens\n" + Style.RESET_ALL)
                        print(Style.BRIGHT + "\nAs you enter your tenth year at the Madrassah, your commitment to the path of Talib al-Ilm deepens. The corridors of learning have become your second home, and the pursuit of knowledge has become a part of your very being." + Style.RESET_ALL)
                        print(Style.BRIGHT + "\nYour teachers recognize your thirst for knowledge and have entrusted you with more challenging texts and assignments. The weight of responsibility rests on your young shoulders, but you face it with determination." + Style.RESET_ALL)
                        print(Style.BRIGHT + "\nIn the hushed library, you encounter a rare manuscript, a treasure trove of ancient wisdom. The book, weathered by time, reveals secrets that stir your soul. You dedicate countless hours to its study, unearthing profound insights that few have ever beheld." + Style.RESET_ALL)
                        print(Style.BRIGHT + Fore.RED + "This year, your scholarly pursuits reach new heights. Your commitment to wisdom and learning defines you, setting you on a path of profound intellectual growth.")
                        print(Fore.RED + "1." + Style.RESET_ALL + Style.BRIGHT + " Assist in teaching younger students\nYou share your knowledge with younger students, helping them grasp complex concepts. Your role as a mentor strengthens your teaching and leadership skills, and you gain the respect of your peers and teachers.")
                        print(Fore.RED + "2." + Style.RESET_ALL + Style.BRIGHT + " Engage in a theological debate\nYou participate in a spirited debate on a complex theological topic. Your eloquence and reasoning skills shine during the discussion, earning you recognition as a formidable scholar.")
                        print(Fore.RED + "3." + Style.RESET_ALL + Style.BRIGHT + " Undertake an ambitious research project\nYou embark on an ambitious research project, diving deep into a subject that has fascinated you. Your dedication to this scholarly endeavor pushes the boundaries of your knowledge.")

                        choice = input(Style.BRIGHT + "Enter your choice (1/2/3): ")

                    if choice == "1":
                        print(Style.BRIGHT + "You take on the role of a mentor, assisting younger students in grasping complex concepts. Your teaching and leadership skills flourish, and you earn the admiration of both your peers and teachers.")
                        character.stats["diplomacy"] += random.randint(2,5)
                    elif choice == "2":
                        print(Style.BRIGHT + "You engage in a spirited theological debate, showcasing your eloquence and reasoning skills. Your performance during the discussion gains you recognition as a formidable scholar.")
                        character.stats["smart"] += random.randint(2,5)
                    elif choice == "3":
                        print(Style.BRIGHT + "You embark on an ambitious research project, delving deep into a subject that has captivated your interest. Your dedication to this scholarly endeavor pushes the boundaries of your knowledge.")
                        character.stats["smart"] += random.randint(2,5)
                    else:
                        continue
                    break
                character.age += 1
                character.print_info()
                madrassah.main_menu(character)
                while True:
                    if character.age == 11:
                        print("\n" + Fore.RED + Style.BRIGHT + "Age 11: The Enlightenment Beckons" + Style.RESET_ALL)
                        print(Style.BRIGHT +"As you celebrate your 11th birthday within the hallowed walls of the Madrassah, you're acutely aware of the responsibilities and expectations that come with each passing year.")
                        print(Style.BRIGHT +"The pursuit of wisdom has etched its mark upon you, shaping your character and defining your path.")

                        # Choices
                        print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: New Friendships" + Style.RESET_ALL)
                        print(Style.BRIGHT +"This year, you form deep bonds with like-minded students who share your passion for learning. Together, you engage in lively discussions, debate complex philosophical questions, and explore the nuances of faith.")
                        print(Fore.RED + "1." + Style.RESET_ALL + Style.BRIGHT +"Stand Up for Justice")
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Secret of the Old Library" + Style.RESET_ALL)
                        print(Style.BRIGHT +"During one of your late-night visits to the Madrassah's library, you stumble upon a hidden chamber filled with ancient texts. These manuscripts, hidden away for centuries, hold secrets and wisdom that few have ever glimpsed. This discovery opens up new avenues of learning and exploration.")
                        print(Fore.RED + "2." + Style.RESET_ALL + Style.BRIGHT +"Navigate a Middle Path")
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Challenge of Ethics" + Style.RESET_ALL)
                        print(Style.BRIGHT +"As you delve deeper into your studies, you encounter a profound ethical dilemma. A fellow student faces unjust accusations, and you must decide whether to speak out and risk your own reputation or remain silent. Your choice will shape not only your character but also the moral fabric of the Madrassah.")
                        print(Fore.RED + "3." + Style.RESET_ALL + Style.BRIGHT +"Uphold Tradition")

                    choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                    if choice == "1":
                        print("\nYou choose to defend your fellow student, even if it means facing consequences yourself. Your unwavering commitment to justice earns you the respect and admiration of both your peers and teachers.")
                        character.stats['smart'] += random.randint(2,5)
                    elif choice == "2":
                        print("\nYou decide to investigate the accusations discreetly, seeking a balanced solution that doesn't jeopardize your own position. Your actions ultimately lead to a fair resolution that maintains harmony within the Madrassah.")
                        character.stats['intrigue'] += random.randint(2,5)
                    elif choice == "3":
                        print("\nYou opt to follow the advice of your mentors and prioritize maintaining the Madrassah's reputation. While you avoid any personal repercussions, you can't help but feel a pang of guilt for not taking a more active stand.")
                        character.stats['diplomacy'] += random.randint(2,5)
                    else:
                        continue
                    break
                character.age += 1
                character.print_info()
                madrassah.main_menu(character)
                while True:
                    if character.age == 12:
                        print("\n" + Fore.RED + Style.BRIGHT + "Age 12: A Crucial Decision" + Style.RESET_ALL)
                        print("As you stand on the threshold of your final year at the Madrassah, you find yourself at a crossroads of destiny.")
                        print("The years of learning and discovery have brought you to this pivotal moment.")
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Pursue Higher Scholarship" + Style.RESET_ALL)
                        print("The path of the scholar beckons you once more, this time leading to the highest levels of academic achievement.")
                        print("You have the opportunity to enroll in advanced courses, engage in profound research, and earn the title of a renowned scholar in your chosen field.")
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Choose a Career Beyond Madrassah" + Style.RESET_ALL)
                        print("Alternatively, you may decide that your destiny lies beyond the walls of the Madrassah.")
                        print("This choice allows you to explore career opportunities outside the realm of academia, using the knowledge and values you've gained to make a difference in the world.")
                        print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                        print("1. Pursue Higher Scholarship")

                    choice = input(Style.BRIGHT + "Enter your choice (1): " + Style.RESET_ALL)

                    if choice == "1":
                        print("\nYou decide to pursue higher scholarship, dedicating yourself to advanced studies and research.")
                        print("Your journey as a scholar continues, and you aim to make significant contributions to your field of expertise.")
                        character.age += 1
                        character.print_info()
                        while True:
                            if character.age == 13:
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 13: Journey to Istanbul" + Style.RESET_ALL)
                                print("You are now 13 years old and have embarked on a journey to Istanbul, a city filled with history, culture, and newfound opportunities.")
                                print("Your family, like many others, has moved to the newly conquered city of Istanbul in 1453, seeking a better life and education for you.")

                                # Event 1: The Road to Istanbul
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Road to Istanbul" + Style.RESET_ALL)
                                print("As your family travels to Istanbul, you witness the changing landscapes and meet fellow travelers along the way.")
                                print("The journey is long and filled with both challenges and moments of wonder.")

                                # Event 2: Arrival in Istanbul
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Arrival in Istanbul" + Style.RESET_ALL)
                                print("Finally, you arrive in Istanbul, a city that resonates with history and promise.")
                                print("The echoes of the recent conquest by Mehmet the Conqueror can still be felt in the air, and you are eager to begin your new life here.")

                                # Event 3: Settling In
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Settling In" + Style.RESET_ALL)
                                print("Your family finds a place to settle in Istanbul, and you start to explore your new surroundings.")
                                print("Istanbul is a melting pot of cultures and traditions, and you are excited to discover what it has to offer.")

                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Focus on your Islamic studies and the path of knowledge")
                                print("2. Make friends and explore Istanbul's history and culture")
                                print("3. Balance your studies and exploration of the city")

                                choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                if choice == "1":
                                    print("\nYou choose to prioritize your Islamic studies and your path to seeking knowledge.")
                                    print("Your commitment to your pursuit of knowledge remains unwavering.")
                                    
                                    # Outcome 1: Continuing the Path of Knowledge
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Outcome: Continuing the Path of Knowledge" + Style.RESET_ALL)
                                    print("Your days are filled with rigorous Islamic studies, including Quranic studies, Hadith, and Islamic jurisprudence.")
                                    print("Your quest to become a scholar continues.")
                                    
                                    # Choices for Outcome 1
                                    print("\n" + Fore.CYAN + Style.BRIGHT + "Choices for Continuing the Path of Knowledge:" + Style.RESET_ALL)
                                    print("1. Attend additional Islamic classes")
                                    print("2. Dedicate more time to Quranic studies")
                                    sub_choice = input(Style.BRIGHT + "Enter your choice (1/2): " + Style.RESET_ALL)
                                    if sub_choice == "1":
                                        print("\nYou choose to attend additional Islamic classes, deepening your understanding of Islamic sciences.")
                                        print("Your dedication to your studies impresses your instructors and fellow students.")
                                        character.stats['smart'] += random.randint(2, 5)
                                    elif sub_choice == "2":
                                        print("\nYou decide to focus on Quranic studies, dedicating more time to understanding and memorizing the Quran.")
                                        print("Your Quranic knowledge improves significantly as you dedicate yourself to this task.")
                                        character.stats['health'] += random.randint(2, 5)
                                    else:
                                        continue
                                    break

                                elif choice == "2":
                                    print("\nWhile dedicated to your Islamic studies, you also make friends and immerse yourself in Istanbul's rich history and culture.")
                                    print("Your understanding of Islam is complemented by the diverse experiences you gain in the city.")
                                    
                                    # Outcome 2: Exploring Istanbul's Culture
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Outcome: Exploring Istanbul's Culture" + Style.RESET_ALL)
                                    print("You make friends with local children and together you explore the vibrant streets of Istanbul.")
                                    print("Your knowledge of the city's history and culture grows.")
                                    
                                    # Choices for Outcome 2
                                    print("\n" + Fore.CYAN + Style.BRIGHT + "Choices for Exploring Istanbul's Culture:" + Style.RESET_ALL)
                                    print("1. Visit historical landmarks")
                                    print("2. Learn about the diverse traditions of Istanbul")
                                    sub_choice = input(Style.BRIGHT + "Enter your choice (1/2): " + Style.RESET_ALL)
                                    if sub_choice == "1":
                                        print("\nYou choose to visit historical landmarks, marveling at the rich history of Istanbul.")
                                        print("Each visit deepens your appreciation for the city's cultural heritage.")
                                        character.stats['diplomacy'] += random.randint(2, 5)
                                    elif sub_choice == "2":
                                        print("\nYou decide to learn about the diverse traditions of Istanbul by immersing yourself in its cultural experiences.")
                                        print("Your understanding of the city's unique traditions and practices expands.")
                                        character.stats['intrigue'] += random.randint(2, 5)
                                    else:
                                        continue
                                    break

                                elif choice == "3":
                                    print("\nYou decide to strike a balance between your Islamic studies and your exploration of Istanbul.")
                                    print("This balance allows you to deepen your Islamic knowledge while appreciating the city's heritage.")
                                    
                                    # Outcome 3: Balancing Studies and Exploration
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Outcome: Balancing Studies and Exploration" + Style.RESET_ALL)
                                    print("You divide your time between Islamic studies and exploring the city.")
                                    print("Your ability to manage your time and priorities improves.")
                                    
                                    # Choices for Outcome 3
                                    print("\n" + Fore.CYAN + Style.BRIGHT + "Choices for Balancing Studies and Exploration:" + Style.RESET_ALL)
                                    print("1. Attend Islamic classes regularly and explore in your free time")
                                    print("2. Establish a study routine that allows for cultural exploration")
                                    sub_choice = input(Style.BRIGHT + "Enter your choice (1/2): " + Style.RESET_ALL)
                                    if sub_choice == "1":
                                        print("\nYou choose to attend Islamic classes regularly and explore Istanbul in your free time.")
                                        character.stats['smart'] += random.randint(2, 5)
                                    elif sub_choice == "2":
                                        print("\nYou decide to establish a study routine that allows for cultural exploration.")
                                        character.stats['diplomacy'] += random.randint(2, 5)
                                    else:
                                        continue
                                    break
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()
                        while True:
                            if character.age == 14:
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 14: Advancing in Knowledge" + Style.RESET_ALL)
                                print("You are now 14 years old, and your pursuit of knowledge in the vibrant city of Istanbul continues.")
                                print("The city's rich history and intellectual environment have contributed to your growth as a student of knowledge.")

                                # Event 1: Expanding Your Studies
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Expanding Your Studies" + Style.RESET_ALL)
                                print("You enroll in advanced Islamic studies, delving deeper into subjects like Islamic jurisprudence (Fiqh) and theology (Aqeedah).")
                                print("Your dedication to learning is recognized by your teachers and peers.")

                                # Event 2: Mentorship Opportunity
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Mentorship Opportunity" + Style.RESET_ALL)
                                print("One of your professors offers to mentor you in the study of Islamic philosophy and critical thinking.")
                                print("This mentorship presents a unique opportunity to broaden your horizons.")

                                # Event 3: Community Engagement
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Community Engagement" + Style.RESET_ALL)
                                print("You become involved in community service, helping to organize events and provide support to those in need.")
                                print("Your sense of responsibility towards the community grows stronger.")

                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Focus on advanced Islamic studies and deepen your knowledge")
                                print("2. Embrace the mentorship opportunity in Islamic philosophy")
                                print("3. Continue community engagement and service")

                                choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                if choice == "1":
                                    print("\nYou choose to focus on advanced Islamic studies, dedicating yourself to deepening your knowledge.")
                                    print("Your commitment to your studies and understanding of Islamic sciences continues to grow.")
                                    character.stats['smart'] += random.randint(2, 5)

                                elif choice == "2":
                                    print("\nYou embrace the mentorship opportunity in Islamic philosophy, exploring critical thinking and deepening your understanding.")
                                    print("Your mentor guides you through complex subjects, broadening your horizons.")
                                    character.stats['diplomacy'] += random.randint(2, 5)

                                elif choice == "3":
                                    print("\nYou continue your community engagement and service, supporting events and helping those in need.")
                                    print("Your involvement in the community deepens your sense of responsibility and compassion.")
                                    character.stats['health'] += random.randint(2, 5)

                                else:
                                    continue
                                break
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()
                        while True:
                            if character.age == 15:
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 15: Navigating Scholarly Challenges" + Style.RESET_ALL)
                                print("You are now 15 years old, and your pursuit of knowledge continues to present new challenges and opportunities.")
                                print("The academic rigor of your studies in Istanbul has honed your intellect and determination.")

                                # Event 1: Research Project
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Research Project" + Style.RESET_ALL)
                                print("You are assigned a complex research project on a topic of Islamic history and civilization.")
                                print("This project demands in-depth research and scholarly analysis.")

                                # Event 2: Scholarly Debates
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Scholarly Debates" + Style.RESET_ALL)
                                print("You engage in lively debates with fellow students and scholars on matters of theology and philosophy.")
                                print("These debates challenge your thinking and sharpen your intellectual skills.")

                                # Event 3: Invitation to Lecture
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Invitation to Lecture" + Style.RESET_ALL)
                                print("Your professors recognize your academic excellence and invite you to deliver a lecture on Islamic jurisprudence.")
                                print("This is an opportunity to share your knowledge with others.")

                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Dedicate yourself to the demanding research project")
                                print("2. Engage in scholarly debates and discussions")
                                print("3. Accept the invitation to deliver a lecture")

                                choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                if choice == "1":
                                    print("\nYou decide to dedicate yourself to the demanding research project, immersing yourself in extensive research and analysis.")
                                    print("Your commitment to scholarship and academic excellence shines through.")
                                    character.stats['smart'] += random.randint(2, 5)

                                elif choice == "2":
                                    print("\nYou actively engage in scholarly debates and discussions, further refining your intellectual skills.")
                                    print("Your ability to articulate and defend your views improves significantly.")
                                    character.stats['diplomacy'] += random.randint(2, 5)

                                elif choice == "3":
                                    print("\nYou accept the invitation to deliver a lecture on Islamic jurisprudence, sharing your knowledge with others.")
                                    print("Your lecture is well-received, and you gain recognition as a scholar.")
                                    character.stats['intrigue'] += random.randint(2, 5)

                                else:
                                    continue
                                break
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()
                        while True:
                            if character.age == 16:
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 16: Expanding Horizons" + Style.RESET_ALL)
                                print("At 16 years old, you continue to flourish as a dedicated student of knowledge in Istanbul.")
                                print("Your passion for learning and academic excellence drives you to explore new horizons.")

                                # Event 1: Scholarly Conferences
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Scholarly Conferences" + Style.RESET_ALL)
                                print("You attend scholarly conferences that bring together intellectuals and scholars from various regions.")
                                print("These conferences broaden your understanding of diverse perspectives.")

                                # Event 2: Multilingual Studies
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Multilingual Studies" + Style.RESET_ALL)
                                print("To deepen your scholarly pursuits, you begin to study classical Islamic texts in multiple languages, including Arabic, Persian, and Turkish.")
                                print("This multilingual approach enhances your access to primary sources.")

                                # Event 3: Mentorship Opportunity
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Mentorship Opportunity" + Style.RESET_ALL)
                                print("A renowned scholar offers to become your mentor, guiding your intellectual growth and research.")
                                print("This mentorship presents a unique chance for further academic development.")

                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Actively participate in scholarly conferences")
                                print("2. Focus on multilingual studies to access more texts")
                                print("3. Accept the mentorship opportunity")

                                choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                if choice == "1":
                                    print("\nYou choose to actively participate in scholarly conferences, where you engage with intellectuals and broaden your horizons.")
                                    print("Your presence and contributions are recognized at these gatherings.")
                                    character.stats['diplomacy'] += random.randint(2, 5)

                                elif choice == "2":
                                    print("\nYou focus on multilingual studies, allowing you to delve deeper into classical Islamic texts from various linguistic perspectives.")
                                    print("Your expanded language skills open doors to a wider range of sources.")
                                    character.stats['intrigue'] += random.randint(2, 5)

                                elif choice == "3":
                                    print("\nYou accept the mentorship opportunity, benefiting from the wisdom and guidance of a renowned scholar.")
                                    print("Your mentor helps shape your research direction and scholarly career.")
                                    character.stats['smart'] += random.randint(2, 5)

                                else:
                                    continue
                                break
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()
                        while True:
                            if character.age == 17:
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 17: Research and Revelations" + Style.RESET_ALL)
                                print("At 17, your scholarly journey in Istanbul continues with renewed vigor.")
                                print("You are on the cusp of making significant contributions to your field of study.")

                                # Event 1: Breakthrough Research
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Breakthrough Research" + Style.RESET_ALL)
                                print("Your dedicated research on a complex topic leads to a groundbreaking discovery.")
                                print("Your work garners recognition from both peers and mentors.")

                                # Event 2: Academic Publications
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Academic Publications" + Style.RESET_ALL)
                                print("You publish your research findings in prestigious academic journals.")
                                print("These publications establish your reputation as a promising scholar.")

                                # Event 3: Scholarly Network
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Scholarly Network" + Style.RESET_ALL)
                                print("You expand your scholarly network by collaborating with experts in your field.")
                                print("This network provides opportunities for collaboration and shared learning.")

                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Continue to focus on in-depth research")
                                print("2. Dedicate time to publishing more academic work")
                                print("3. Nurture and strengthen your scholarly network")

                                choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                if choice == "1":
                                    print("\nYou decide to continue focusing on in-depth research, delving deeper into your chosen area of expertise.")
                                    print("Your commitment to scholarship remains unwavering, leading to further discoveries.")
                                    character.stats['smart'] += random.randint(2, 5)

                                elif choice == "2":
                                    print("\nYou dedicate time to publishing more academic work, contributing valuable insights to your field.")
                                    print("Your publications continue to earn respect and recognition.")
                                    character.stats['intrigue'] += random.randint(2, 5)

                                elif choice == "3":
                                    print("\nYou nurture and strengthen your scholarly network, fostering collaborations with esteemed experts.")
                                    print("Your network becomes a source of support and knowledge exchange.")
                                    character.stats['diplomacy'] += random.randint(2, 5)
                                else:
                                    continue
                                break
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()
                        while True:
                            if character.age == 18:
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 18: Academic Pursuits" + Style.RESET_ALL)
                                print("As you turn 18, your pursuit of knowledge and scholarly achievements reaches new heights.")
                                print("The academic world eagerly anticipates your contributions.")

                                # Event 1: Research Symposium
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Research Symposium" + Style.RESET_ALL)
                                print("You are invited to present your research at a prestigious international symposium.")
                                print("Your presentation captivates the audience and earns accolades.")

                                # Event 2: Teaching Opportunity
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Teaching Opportunity" + Style.RESET_ALL)
                                print("A renowned educational institution offers you a position as a lecturer.")
                                print("You embark on a journey of sharing your knowledge with aspiring students.")

                                # Event 3: Scholarly Recognition
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Scholarly Recognition" + Style.RESET_ALL)
                                print("Your consistent dedication to scholarship leads to recognition by your peers.")
                                print("You receive an award for your outstanding contributions to your field.")

                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Continue to participate in international research events")
                                print("2. Focus on your role as a lecturer and mentor")
                                print("3. Expand your research portfolio and seek further recognition")

                                choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                if choice == "1":
                                    print("\nYou choose to continue participating in international research events, broadening your horizons.")
                                    print("Your global presence in the academic community continues to grow.")
                                    character.stats['smart'] += random.randint(2, 5)

                                elif choice == "2":
                                    print("\nYou decide to focus on your role as a lecturer and mentor, shaping the next generation of scholars.")
                                    print("Your students admire your guidance, and you become a respected educator.")
                                    character.stats['diplomacy'] += random.randint(2, 5)

                                elif choice == "3":
                                    print("\nYou opt to expand your research portfolio and seek further recognition for your scholarly work.")
                                    print("Your dedication to your field results in more prestigious awards and recognition.")
                                    character.stats['looks'] += random.randint(2, 5)

                                else:
                                    continue
                                break
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()
                        while True:
                            if character.age == 19:
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 19: The Path to Philosophy" + Style.RESET_ALL)
                                print("At 19, your intellectual pursuits have led you to the threshold of philosophy, where profound questions and wisdom await.")

                                # Event 1: Encounter with a Philosopher
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Encounter with a Philosopher" + Style.RESET_ALL)
                                print("You cross paths with a renowned philosopher known for their wisdom and insights.")
                                print("This meeting sparks your interest in the world of philosophy.")

                                # Event 2: Delving into Philosophical Texts
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Delving into Philosophical Texts" + Style.RESET_ALL)
                                print("You immerse yourself in the works of ancient and contemporary philosophers.")
                                print("The profound ideas and philosophical debates fuel your desire to explore further.")

                                # Event 3: Mentorship Offer
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Mentorship Offer" + Style.RESET_ALL)
                                print("A respected philosopher offers to become your mentor in the realm of philosophy.")
                                print("You contemplate accepting their mentorship to deepen your understanding.")

                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Accept the philosopher's mentorship and fully commit to philosophy")
                                print("2. Continue your academic pursuits, balancing philosophy with your other interests")
                                print("3. Politely decline the mentorship and explore philosophy independently")

                                choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                if choice == "1":
                                    print("\nYou decide to accept the philosopher's mentorship and fully commit to the path of philosophy.")
                                    print("Under their guidance, you delve deeper into the world of profound ideas and philosophical debates.")
                                    character.stats['smart'] += random.randint(2, 5)

                                elif choice == "2":
                                    print("\nYou choose to continue your academic pursuits while balancing your exploration of philosophy.")
                                    print("You find harmony in combining various fields of knowledge.")
                                    character.stats['diplomacy'] += random.randint(2, 5)

                                elif choice == "3":
                                    print("\nYou politely decline the mentorship and opt to explore philosophy independently.")
                                    print("Your journey into philosophy takes a self-directed and adventurous path.")
                                    character.stats['intrigue'] += random.randint(2, 5)

                                else:
                                    continue
                                break
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()
                        while True:
                            if character.age == 20:
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 20: The Culmination of Knowledge" + Style.RESET_ALL)
                                print("At 20, you stand at the culmination of your quest for knowledge and wisdom.")
                                print("Your journey has been a remarkable one, filled with learning and self-discovery.")

                                # Event: The Philosopher's Legacy
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Philosopher's Legacy" + Style.RESET_ALL)
                                print("Your dedication to philosophy has led you to a profound realization.")
                                print("You reflect on the legacy you wish to leave behind.")

                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Share your wisdom by becoming a philosopher and teaching others")
                                print("2. Write philosophical works to inspire future generations")
                                print("3. Continue your own pursuit of knowledge, exploring new horizons")

                                choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                if choice == "1":
                                    print("\nYou choose to share your wisdom by becoming a philosopher and teaching others.")
                                    print("Your passion for philosophy inspires and enlightens future generations.")
                                    print("\nCongratulations! You have reached the culmination of your journey as a seeker of knowledge and wisdom.")
                                    character.stats['smart'] += random.randint(4,5)
                                    character.prestige += 100
                                elif choice == "2":
                                    print("\nYou decide to write philosophical works to inspire and guide future generations.")
                                    print("Your writings become renowned for their depth and insight, leaving a lasting legacy.")
                                    print("\nCongratulations! You have reached the culmination of your journey as a seeker of knowledge and wisdom.")
                                    character.stats['looks'] += random.randint(4, 5)
                                    character.prestige += 100
                                elif choice == "3":
                                    print("\nYou opt to continue your own pursuit of knowledge, exploring new horizons and expanding your understanding.")
                                    print("Your journey into the realms of knowledge continues, and the future is full of possibilities.")
                                    print("\nCongratulations! You have reached the culmination of your journey as a seeker of knowledge and wisdom.")
                                    character.stats['intrigue'] += random.randint(4, 5)
                                    character.prestige += 100
                                else:
                                    continue
                                # End the game
                                print("\n" + Fore.GREEN + Style.BRIGHT + "End of the Game" + Style.RESET_ALL)
                                print("Your journey as a seeker of knowledge and wisdom has come to a close.")
                                print("Thank you for playing!")

                                break
                    else:
                        continue
                    break
                




######################################################


            elif choice == "2":
                print(Style.BRIGHT + "You commit to safeguarding the Quran with unwavering devotion. Your days are filled with recitations, memorization, and discussions of the sacred text. As a Hafiz-e-Quran, you gain deep insights into the Quran's teachings and its role in guiding the faithful. You become a trusted figure in your community, revered for your knowledge of the holy scripture.")
                madrassah.join_group_hafiz()
                while True:
                    if character.age == 8:
                        print("\n" + Fore.RED + Style.BRIGHT + "Age 8: The Journey Begins" + Style.RESET_ALL)
                        print("You are 8 years old and have just joined the Hafiz-e-Quran group at the Madrassah.")
                        print("Your journey to become a guardian of the holy Quran has just begun.")

                        # Event 1: The Quranic Teacher
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Quranic Teacher" + Style.RESET_ALL)
                        print("You meet your Quranic teacher, a wise and patient scholar dedicated to teaching the sacred Quran.")
                        print("The teacher begins your lessons in Quranic memorization and recitation.")

                        # Event 2: The First Surah
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The First Surah" + Style.RESET_ALL)
                        print("After months of diligent practice, you successfully memorize your first Surah (chapter) from the Quran.")
                        print("The sense of accomplishment and reverence for the Quran fills your heart.")

                        # Event 3: A Lesson in Faith
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: A Lesson in Faith" + Style.RESET_ALL)
                        print("Your teacher imparts a valuable lesson on faith, emphasizing the importance of sincerity and devotion in your journey.")
                        print("You gain a deeper understanding of the spiritual significance of your path.")

                        # Choices
                        print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                        print("1. Dedicate Yourself to Quranic Memorization")
                        print("2. Focus on Improving Your Recitation")
                        print("3. Embrace the Lesson in Faith")

                        choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                        if choice == "1":
                            print("\nYou wholeheartedly dedicate yourself to Quranic memorization, striving to become a Hafiz of the Quran.")
                            print("Each day, you commit more verses to memory, inching closer to your goal.")
                            character.stats['smart'] += random.randint(2, 5)
                        elif choice == "2":
                            print("\nYou focus on improving your Quranic recitation, working on the melodic and precise pronunciation of verses.")
                            print("Your recitation becomes more beautiful and melodious with each practice session.")
                            character.stats['health'] += random.randint(2, 5)
                        elif choice == "3":
                            print("\nYou embrace the lesson in faith, understanding that your journey as a Hafiz-e-Quran is not just about memorization.")
                            print("You approach your studies with sincerity and devotion, seeking a deeper connection with the Quran.")
                            character.stats['smart'] += random.randint(2, 5)
                        else:
                            continue
                        break
                character.age += 1
                character.print_info()
                madrassah.main_menu(character)
                while True:
                    if character.age == 9:
                        print("\n" + Fore.RED + Style.BRIGHT + "Age 9: Deepening Quranic Knowledge" + Style.RESET_ALL)
                        print("You are 9 years old and have spent one year as a member of the Hafiz-e-Quran group.")
                        print("Your dedication to the Quranic studies has continued to grow, and you are becoming more proficient in memorization and recitation.")

                        # Event 1: A New Surah Memorized
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: A New Surah Memorized" + Style.RESET_ALL)
                        print("After a year of diligent practice, you successfully memorize a new Surah from the Quran.")
                        print("Your ability to retain and recite Quranic verses is improving.")

                        # Event 2: Recitation Competition
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Recitation Competition" + Style.RESET_ALL)
                        print("A friendly recitation competition is held among the Hafiz-e-Quran group members.")
                        print("You participate and receive praise for your beautiful and accurate recitation.")

                        # Event 3: The Quranic Teacher's Guidance
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Quranic Teacher's Guidance" + Style.RESET_ALL)
                        print("Your Quranic teacher offers you valuable guidance on the importance of preserving the Quran.")
                        print("Their words inspire you to continue your journey as a guardian of the holy scripture.")

                        # Choices
                        print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                        print("1. Continue Focusing on Memorization")
                        print("2. Further Improve Your Recitation Skills")
                        print("3. Seek More Guidance from Your Quranic Teacher")

                        choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                        if choice == "1":
                            print("\nYou decide to continue focusing on Quranic memorization, aiming to memorize more Surahs.")
                            print("Your dedication to memorization continues to strengthen.")
                            character.stats['smart'] += random.randint(2, 5)
                        elif choice == "2":
                            print("\nYou choose to further improve your recitation skills, aiming for even more beautiful and accurate recitation.")
                            print("Your recitation becomes increasingly melodious and precise.")
                            character.stats['smart'] += random.randint(2, 5)
                        elif choice == "3":
                            print("\nYou seek more guidance from your Quranic teacher, eager to learn and preserve the Quran's teachings.")
                            print("Your teacher provides you with additional insights and encouragement.")
                            character.stats['diplomacy'] += random.randint(2, 5)
                        else:
                            continue
                        break
                # Progress character age and continue the game loop
                character.age += 1
                character.print_info()
                madrassah.main_menu(character)
                while True:
                    if character.age == 10:
                        print("\n" + Fore.RED + Style.BRIGHT + "Age 10: Progress in Quranic Mastery" + Style.RESET_ALL)
                        print("You are 10 years old and have spent two years as a member of the Hafiz-e-Quran group.")
                        print("Your dedication to the Quranic arts continues to grow, and you strive for excellence.")

                        # Event 1: Memorizing New Surahs
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Memorizing New Surahs" + Style.RESET_ALL)
                        print("You successfully memorize new Surahs from the Quran.")
                        print("Your ability to memorize complex Quranic verses improves, and you feel a sense of accomplishment.")

                        # Event 2: Leading Group Recitations
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Leading Group Recitations" + Style.RESET_ALL)
                        print("You are chosen to lead group Quranic recitations during Madrassah gatherings.")
                        print("Your leadership skills and beautiful recitations inspire others in the group.")

                        # Event 3: Seeking Spiritual Guidance
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Seeking Spiritual Guidance" + Style.RESET_ALL)
                        print("You seek guidance from a spiritual mentor within the Hafiz-e-Quran group.")
                        print("Their wisdom deepens your spiritual connection with the Quran and the divine.")

                        # Choices
                        print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                        print("1. Focus on Memorizing More Surahs")
                        print("2. Continue Leading Group Recitations")
                        print("3. Deepen Your Spiritual Connection")

                        choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                        if choice == "1":
                            print("\nYou decide to focus on memorizing more Surahs, aiming to expand your Quranic knowledge.")
                            print("Your dedication to memorization grows, and you continue to impress with your memory.")
                            character.stats['smart'] += random.randint(2, 5)
                        elif choice == "2":
                            print("\nYou choose to continue leading group Quranic recitations, inspiring others with your leadership.")
                            print("Your reputation as a skilled reciter and leader within the Hafiz-e-Quran group flourishes.")
                            character.stats['diplomacy'] += random.randint(2, 5)
                        elif choice == "3":
                            print("\nYou opt to deepen your spiritual connection with the Quran and the divine.")
                            print("Your spirituality deepens, and you find solace and inspiration in your connection.")
                            character.stats['health'] += random.randint(2, 5)
                        else:
                            continue
                        break
                character.age += 1
                character.print_info()
                madrassah.main_menu(character)
                while True:
                    if character.age == 11:
                        print("\n" + Fore.RED + Style.BRIGHT + "Age 11: Advancing in Quranic Mastery" + Style.RESET_ALL)
                        print("You are 11 years old and have spent three years as a member of the Hafiz-e-Quran group.")
                        print("Your mastery of the Quranic arts continues to flourish, and your spirituality deepens.")

                        # Event 1: Completion of Quran Memorization
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Completion of Quran Memorization" + Style.RESET_ALL)
                        print("After years of dedication, you successfully memorize the entire Quran.")
                        print("This achievement is celebrated by your peers and teachers, and your spirituality soars.")

                        # Event 2: Leading Quranic Recitations
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Leading Quranic Recitations" + Style.RESET_ALL)
                        print("You are chosen to lead Quranic recitations during special gatherings at the Madrassah.")
                        print("Your recitations are admired for their beauty and precision, and you inspire others with your devotion.")

                        # Event 3: Guidance from the Elder Scholar
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Guidance from the Elder Scholar" + Style.RESET_ALL)
                        print("An elder Quranic scholar recognizes your dedication and offers you guidance.")
                        print("Their wisdom enriches your understanding of the Quran and your spiritual journey.")

                        # Choices
                        print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                        print("1. Continue Leading Quranic Recitations")
                        print("2. Deepen Your Spiritual Connection")
                        print("3. Learn Advanced Quranic Interpretation from the Elder Scholar")

                        choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                        if choice == "1":
                            print("\nYou choose to continue leading Quranic recitations, inspiring others with your beautiful recitations.")
                            print("Your reputation as a skilled and devout Hafiz-e-Quran grows.")
                            character.stats['smart'] += random.randint(2, 5)
                        elif choice == "2":
                            print("\nYou decide to deepen your spiritual connection, spending more time in reflection and prayer.")
                            print("Your spirituality deepens, and you feel a profound sense of connection with the divine.")
                            character.stats['martial'] += random.randint(2, 5)
                        elif choice == "3":
                            print("\nYou opt to learn advanced Quranic interpretation from the elder scholar, delving into the deeper meanings of the Quran.")
                            print("Your understanding of the Quran becomes enriched, and you gain insights into its profound teachings.")
                            character.stats['diplomacy'] += random.randint(2, 3)
                            character.stats['smart'] += random.randint(2, 3)
                        else:
                            continue
                        break
                # Progress character age and continue the game loop
                character.age += 1
                character.print_info()
                madrassah.main_menu(character)
                while True:
                    if character.age == 12:
                        print("\n" + Fore.RED + Style.BRIGHT + "Age 12: The Final Year" + Style.RESET_ALL)
                        print("You are 12 years old and have reached the final year of your journey as a member of the Hafiz-e-Quran group.")
                        print("Your mastery of the Quran is renowned, and your spirituality is profound.")

                        # Event 1: The Decision Approaches
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Decision Approaches" + Style.RESET_ALL)
                        print("You stand at a crossroads. It is time to make a decision that will shape your future.")
                        print("Do you wish to continue your Quranic studies or choose a new career path?")

                        # Choices
                        print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                        print("1. Continue Your Quranic Studies and Become a Quranic Scholar")

                        choice = input(Style.BRIGHT + "Enter your choice (1/2): " + Style.RESET_ALL)

                    if choice == "1":
                        print("\nYou decide to continue your Quranic studies and to become a Quranic scholar.")
                        print("Your dedication to preserving and spreading the Quranic teachings becomes your life's purpose.")
    
                        character.age += 1
                        character.print_info()
                        while True:
                            if character.age == 13:
                                character.prestige += 100
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 13: Journey to Istanbul" + Style.RESET_ALL)
                                print("You are now 13 years old and have embarked on a journey to Istanbul, a city filled with history, culture, and newfound opportunities.")
                                print("Your family, like many others, has moved to the newly conquered city of Istanbul in 1453, seeking a better life and education for you.")

                                # Event 1: The Road to Istanbul
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Road to Istanbul" + Style.RESET_ALL)
                                print("As your family travels to Istanbul, you witness the changing landscapes and meet fellow travelers along the way.")
                                print("The journey is long and filled with both challenges and moments of wonder.")

                                # Event 2: Arrival in Istanbul
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Arrival in Istanbul" + Style.RESET_ALL)
                                print("Finally, you arrive in Istanbul, a city that resonates with history and promise.")
                                print("The echoes of the recent conquest by Mehmet the Conqueror can still be felt in the air, and you are eager to begin your new life here.")

                                # Event 3: Settling In
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Settling In" + Style.RESET_ALL)
                                print("Your family finds a place to settle in Istanbul, and you start to explore your new surroundings.")
                                print("Istanbul is a melting pot of cultures and traditions, and you are excited to discover what it has to offer.")

                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Focus on Quranic studies and your Hafiz-e-Quran path")
                                print("2. Make friends and explore Istanbul's history and culture")
                                print("3. Balance your studies and exploration of the city")

                                choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                if choice == "1":
                                    print("\nYou choose to prioritize your Quranic studies and your path to becoming a Hafiz-e-Quran.")
                                    print("Your commitment to your spiritual journey remains unwavering.")
                                    
                                    # Outcome 1: Continuing the Hafiz-e-Quran Path
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Outcome: Continuing the Hafiz-e-Quran Path" + Style.RESET_ALL)
                                    print("Your days are filled with rigorous Quranic studies and memorization.")
                                    print("Your quest to become a Hafiz-e-Quran continues.")
                                    
                                    # Choices for Outcome 1
                                    print("\n" + Fore.CYAN + Style.BRIGHT + "Choices for Continuing the Hafiz-e-Quran Path:" + Style.RESET_ALL)
                                    print("1. Attend additional Quranic classes")
                                    print("2. Memorize Quranic verses diligently")
                                    
                                    sub_choice = input(Style.BRIGHT + "Enter your choice (1/2): " + Style.RESET_ALL)
                                    
                                    if sub_choice == "1":
                                        print("\nYou choose to attend additional Quranic classes, deepening your understanding of the Quran.")
                                        print("Your dedication to your studies impresses your instructors and fellow students.")
                                        character.stats['smart'] += random.randint(2, 5)
                                        break
                                    elif sub_choice == "2":
                                        print("\nYou decide to focus on memorizing Quranic verses with diligence and devotion.")
                                        print("Your memorization skills improve significantly as you dedicate yourself to this task.")
                                        character.stats['smart'] += random.randint(2, 5)
                                        break
                                    character.stats['smart'] += random.randint(2, 5)

                                elif choice == "2":
                                    print("\nWhile dedicated to your Quranic studies, you also make friends and immerse yourself in Istanbul's rich history and culture.")
                                    print("Your understanding of the Quran is complemented by the diverse experiences you gain in the city.")
                                    
                                    # Outcome 2: Exploring Istanbul's Culture
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Outcome: Exploring Istanbul's Culture" + Style.RESET_ALL)
                                    print("You make friends with local children and together you explore the vibrant streets of Istanbul.")
                                    print("Your knowledge of the city's history and culture grows.")
                                    
                                    # Choices for Outcome 2
                                    print("\n" + Fore.CYAN + Style.BRIGHT + "Choices for Exploring Istanbul's Culture:" + Style.RESET_ALL)
                                    print("1. Visit historical landmarks")
                                    print("2. Learn about the diverse traditions of Istanbul")
                                    
                                    sub_choice = input(Style.BRIGHT + "Enter your choice (1/2): " + Style.RESET_ALL)
                                    
                                    if sub_choice == "1":
                                        print("\nYou choose to visit historical landmarks, marveling at the rich history of Istanbul.")
                                        print("Each visit deepens your appreciation for the city's cultural heritage.")
                                        character.stats['smart'] += random.randint(2, 5)
                                        break
                                    elif sub_choice == "2":
                                        print("\nYou decide to learn about the diverse traditions of Istanbul by immersing yourself in its cultural experiences.")
                                        print("Your understanding of the city's unique traditions and practices expands.")
                                        character.stats['smart'] += random.randint(2, 5)
                                        break
                                    character.stats['smart'] += random.randint(2, 5)

                                elif choice == "3":
                                    print("\nYou decide to strike a balance between your Quranic studies and your exploration of Istanbul.")
                                    print("This balance allows you to deepen your Quranic knowledge while appreciating the city's heritage.")
                                    
                                    # Outcome 3: Balancing Studies and Exploration
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Outcome: Balancing Studies and Exploration" + Style.RESET_ALL)
                                    print("You divide your time between Quranic studies and exploring the city.")
                                    print("Your ability to manage your time and priorities improves.")
                                    
                                    # Choices for Outcome 3
                                    print("\n" + Fore.CYAN + Style.BRIGHT + "Choices for Balancing Studies and Exploration:" + Style.RESET_ALL)
                                    print("1. Attend Quranic classes regularly and explore in your free time")
                                    print("2. Establish a study routine that allows for cultural exploration")
                                    
                                    sub_choice = input(Style.BRIGHT + "Enter your choice (1/2): " + Style.RESET_ALL)
                                    
                                    if sub_choice == "1":
                                        print("\nYou choose to attend Quranic classes regularly and explore Istanbul in your free time.")
                                        print("Your dedication to both your studies and exploration helps you grow as an individual.")
                                        character.stats['smart'] += random.randint(2, 5)
                                        break
                                    elif sub_choice == "2":
                                        print("\nYou decide to establish a study routine that allows for cultural exploration.")
                                        print("Your efficient time management skills enable you to excel in both areas.")
                                        character.stats['smart'] += random.randint(2, 5)
                                        break
                                    character.stats['smart'] += random.randint(2, 5)

                                else:
                                    continue
                                break
    
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()
                        
                        while True:
                            if character.age == 14:
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 14: Choosing a Quranic Teacher" + Style.RESET_ALL)
                                print("You are now 14 years old, and your dedication to the Quranic path has brought you to a crucial crossroads.")
                                print("It's time to choose a Quranic teacher, a Qari, who will guide you in the art of Quranic recitation and Tajweed.")

                                # Event: The Choices
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Choices" + Style.RESET_ALL)
                                print("You have two prominent Qaris to choose from, both highly respected in the world of Quranic recitation.")

                                # Choice 1: Sheikh Zainuddin al-Amasi
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Choice 1: Sheikh Zainuddin al-Amasi" + Style.RESET_ALL)
                                print("Sheikh Zainuddin al-Amasi (died c. 1469) was a highly regarded Quranic reciter and teacher during the Ottoman period.")
                                print("He was known for his mastery of Quranic recitation, including the proper pronunciation (Tajweed) and melodious rendering of the Quranic verses.")
                                print("Sheikh Zainuddin al-Amasi's expertise in Quranic recitation earned him a reputation as one of the leading Qari of his time.")
                                print("He was not only recognized for his beautiful recitation but also for his dedication to teaching the art of Quranic recitation to students.")
                                print("Do you choose Sheikh Zainuddin al-Amasi as your Quranic teacher?")

                                # Choice 2: Sheikh Hamdullah Efendi
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Choice 2: Sheikh Hamdullah Efendi" + Style.RESET_ALL)
                                print("Sheikh Hamdullah Efendi (c. 1436-1520) was a prominent Islamic scholar, calligrapher, and Quranic reciter who lived during the 15th and 16th centuries.")
                                print("Although he was primarily known for his contributions to Islamic calligraphy, he was also recognized for his expertise in Quranic recitation and Tajweed (proper pronunciation).")
                                print("Sheikh Hamdullah Efendi is remembered for his role in advancing the art of Islamic calligraphy in the Ottoman Empire, particularly the Naskh and Thuluth script styles.")
                                print("His calligraphic works and copies of the Quran have been preserved in various collections and museums.")
                                print("Do you choose Sheikh Hamdullah Efendi as your Quranic teacher?")

                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Choose Sheikh Zainuddin al-Amasi")
                                print("2. Choose Sheikh Hamdullah Efendi")

                                choice_qari = input(Style.BRIGHT + "Enter your choice (1/2): " + Style.RESET_ALL)

                                if choice_qari == "1":
                                    print("\nYou choose to be guided by the expertise of Sheikh Zainuddin al-Amasi.")
                                    print("His mastery of Quranic recitation and dedication to teaching will be your path to becoming a skilled Qari.")

                                    # Outcome: Choosing Sheikh Zainuddin al-Amasi
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Outcome: Choosing Sheikh Zainuddin al-Amasi" + Style.RESET_ALL)
                                    print("Under the guidance of Sheikh Zainuddin al-Amasi, your Quranic recitation skills flourish.")
                                    print("You delve deep into the art of Tajweed and the melodious rendering of Quranic verses.")
                                    print("Your journey as a dedicated Qari begins.")
                                    self.qari = "Sheikh Zainuddin al-Amasi"
                                    character.stats['smart'] += random.randint(2, 5)
                                    self.qari_trust += 5
                                    character.stats['smart'] += random.randint(2, 5)
                                elif choice_qari == "2":
                                    print("\nYou choose to learn from the versatile Sheikh Hamdullah Efendi.")
                                    print("His expertise in both Quranic recitation and Islamic calligraphy promises a unique and enriching experience.")

                                    # Outcome: Choosing Sheikh Hamdullah Efendi
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Outcome: Choosing Sheikh Hamdullah Efendi" + Style.RESET_ALL)
                                    print("Under the guidance of Sheikh Hamdullah Efendi, you embark on a journey of Quranic mastery and calligraphic artistry.")
                                    print("You explore the intricacies of Quranic recitation and the elegance of Islamic calligraphy.")
                                    print("Your path as a well-rounded scholar and artist begins.")
                                    self.qari = "Sheikh Hamdullah Efendi"
                                    character.stats['smart'] += random.randint(2, 5)
                                    self.qari_trust += 5
                                    character.stats['smart'] += random.randint(2, 5)
                                else:
                                    continue
                                break
    
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()
                        
                        while True:
                            if character.age == 15 and self.qari == "Sheikh Zainuddin al-Amasi":
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 15: Quranic Scholar's Journey with Sheikh Zainuddin al-Amasi" + Style.RESET_ALL)
                                print("At the age of 15, you have firmly embarked on your journey as a Quranic scholar under the guidance of Sheikh Zainuddin al-Amasi.")
                                print("The path of knowledge and spirituality stretches ahead of you, offering new horizons to explore.")

                                # Event 1: Intensive Quranic Studies
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Intensive Quranic Studies" + Style.RESET_ALL)
                                print("Sheikh Zainuddin al-Amasi guides you in intensive Quranic studies, focusing on the depth of Quranic knowledge.")
                                print("Your understanding of the Quran's profound verses deepens significantly.")

                                # Event 2: Tajweed Mastery
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Tajweed Mastery" + Style.RESET_ALL)
                                print("Under Sheikh Zainuddin al-Amasi's mentorship, you dedicate yourself to mastering Tajweed.")
                                print("Your recitation of the Quran becomes a melodious symphony, capturing the hearts of those who hear it.")

                                # Event 3: Spiritual Retreat
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Spiritual Retreat" + Style.RESET_ALL)
                                print("Sheikh Zainuddin al-Amasi arranges a spiritual retreat in a serene natural setting.")
                                print("The retreat allows you to experience profound spiritual moments and deepens your connection to the Quran.")

                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Continue your intensive Quranic studies")
                                print("2. Dedicate more time to mastering Tajweed")
                                print("3. Embrace the spiritual path with Sheikh Zainuddin al-Amasi")

                                choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                if choice == "1":
                                    print("\nYou choose to continue your intensive Quranic studies, delving even deeper into the Quran's wisdom.")
                                    print("Your commitment to scholarship remains unwavering.")
                                    
                                    # Outcome 1: Continuing Quranic Studies
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Outcome: Continuing Quranic Studies" + Style.RESET_ALL)
                                    print("Your days are filled with extensive Quranic studies, guided by Sheikh Zainuddin al-Amasi's wisdom.")
                                    print("Your dedication to becoming a Quranic scholar grows stronger.")
                                    character.stats['smart'] += random.randint(2, 5)
                                    character.stats['smart'] += random.randint(2, 5)
                                    self.qari_trust += 3

                                elif choice == "2":
                                    print("\nYou decide to dedicate more time to mastering Tajweed, perfecting the art of Quranic pronunciation.")
                                    print("Your efforts are focused on achieving the highest standards of recitation.")
                                    
                                    # Outcome 2: Mastery of Tajweed
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Outcome: Mastery of Tajweed" + Style.RESET_ALL)
                                    print("Your diligence in mastering Tajweed results in flawless Quranic recitation.")
                                    print("Your ability to convey the beauty and essence of the Quranic verses is unparalleled.")
                                    character.stats['smart'] += random.randint(2, 5)
                                    self.qari_trust += 3
                                    character.stats['martial'] += random.randint(2, 5)

                                elif choice == "3":
                                    print("\nYou choose to embrace the spiritual path under the guidance of Sheikh Zainuddin al-Amasi.")
                                    print("His mentorship leads you to a deeper spiritual understanding of the Quran and its significance.")
                                    
                                    # Outcome 3: Embracing the Spiritual Path
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Outcome: Embracing the Spiritual Path" + Style.RESET_ALL)
                                    print("You embark on a spiritual journey that transcends the realm of Quranic knowledge.")
                                    print("Your connection to the divine and your spiritual growth become the focal points of your life.")
                                    character.stats['smart'] += random.randint(2, 5)
                                    self.qari_trust += 5
                                    character.stats['health'] += random.randint(2, 5)

                                else:
                                    continue
                                break
    
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()
                        
                        while True:
                            if character.age == 16 and self.qari == "Sheikh Zainuddin al-Amasi":
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 16: Quranic Mastery with Sheikh Zainuddin al-Amasi" + Style.RESET_ALL)
                                print("At the age of 16, you have devoted yourself to Quranic mastery under the guidance of Sheikh Zainuddin al-Amasi.")
                                print("Your days are filled with intensive Quranic studies and the pursuit of perfecting your recitation.")

                                # Event 1: Intensive Quranic Studies
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Intensive Quranic Studies" + Style.RESET_ALL)
                                print("Sheikh Zainuddin al-Amasi leads you through rigorous Quranic studies, focusing on Tajweed (proper pronunciation) and melodious recitation.")
                                print("You find yourself immersed in the beauty and intricacy of the Quranic verses.")

                                # Event 2: The Art of Tajweed
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Art of Tajweed" + Style.RESET_ALL)
                                print("Your mentor places significant emphasis on Tajweed, ensuring every letter and word is recited with precision and beauty.")
                                print("Your mastery over Tajweed grows under his watchful eye.")

                                # Event 3: Recitation Competitions
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Recitation Competitions" + Style.RESET_ALL)
                                print("You participate in Quranic recitation competitions, where your skills are put to the test.")
                                print("Your heartfelt renditions of the Quranic verses leave a lasting impression on the audience.")

                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Dedicate yourself to perfecting Tajweed")
                                print("2. Focus on deepening your understanding of Quranic interpretation")
                                print("3. Continue participating in recitation competitions")

                                choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                if choice == "1":
                                    print("\nYou choose to dedicate yourself to perfecting Tajweed, focusing on the precise pronunciation and intonation of Quranic verses.")
                                    print("Your recitation becomes more melodious and awe-inspiring.")
                                    self.qari_trust += 5  # Increase trust in your Qari
                                    character.stats['smart'] += random.randint(2, 5)
                                    
                                    # Outcome 1: Mastery of Tajweed
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Outcome: Mastery of Tajweed" + Style.RESET_ALL)
                                    print("Your mastery of Tajweed brings you recognition among scholars and peers alike.")
                                    print("Your recitations leave a profound impact on the hearts of those who listen.")
                                    character.stats['smart'] += random.randint(2, 5)

                                elif choice == "2":
                                    print("\nYou decide to focus on deepening your understanding of Quranic interpretation, delving into the meanings and nuances of the verses.")
                                    print("Your quest for profound Quranic knowledge becomes your primary goal.")
                                    self.qari_trust += 3  # Increase trust in your Qari
                                    character.stats['smart'] += random.randint(2, 5)
                                    
                                    # Outcome 2: Deep Quranic Understanding
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Outcome: Deep Quranic Understanding" + Style.RESET_ALL)
                                    print("Your deep understanding of Quranic interpretation allows you to share profound insights with others.")
                                    print("Your reputation as a Quranic scholar continues to grow.")
                                    character.stats['smart'] += random.randint(2, 5)

                                elif choice == "3":
                                    print("\nYou continue participating in recitation competitions, showcasing your refined skills and heartfelt recitations.")
                                    print("Your passion for Quranic recitation fuels your competitive spirit.")
                                    self.qari_trust += 3  # Increase trust in your Qari
                                    
                                    # Outcome 3: Recitation Champion
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Outcome: Recitation Champion" + Style.RESET_ALL)
                                    print("You become a champion of Quranic recitation, winning competitions and earning accolades.")
                                    print("Your recitations inspire others to excel in their own Quranic studies.")
                                    character.stats['smart'] += random.randint(2, 5)
                                    character.stats['health'] += random.randint(2, 5)

                                else:
                                    continue
                                break
    
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()
                        
                        while True:
                            if character.age == 17 and self.qari == "Sheikh Zainuddin al-Amasi":
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 17: Deepening Quranic Expertise" + Style.RESET_ALL)
                                print("At 17, your journey in the art of Quranic recitation continues under the tutelage of Sheikh Zainuddin al-Amasi.")
                                print("The expertise you have gained from your Qari has transformed you into a skilled Quranic reciter.")
                                
                                # Event 1: Reciting at the Mosque
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Reciting at the Mosque" + Style.RESET_ALL)
                                print("You are given the opportunity to recite Quranic verses at the local mosque during a special gathering.")
                                print("The congregation is moved by the beauty and precision of your recitation.")
                                
                                # Event 2: Teaching Quranic Recitation
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Teaching Quranic Recitation" + Style.RESET_ALL)
                                print("Recognizing your mastery of Quranic recitation, you are entrusted with teaching young students.")
                                print("You pass on the knowledge and skill you've acquired, becoming a respected Quranic teacher.")
                                
                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Continue reciting at the mosque and inspire the congregation")
                                print("2. Dedicate more time to teaching Quranic recitation to the next generation")
                                print("3. Seek to further perfect your own recitation skills")
                                
                                choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)
                                
                                if choice == "1":
                                    print("\nYou choose to continue reciting at the mosque, becoming a source of inspiration for the congregation.")
                                    print("Your recitation touches the hearts of those who listen, leaving a lasting impact.")
                                    character.stats['smart'] += random.randint(2, 5)
                                elif choice == "2":
                                    print("\nYou dedicate more time to teaching Quranic recitation to the next generation of students.")
                                    print("Your commitment to passing on the knowledge you've gained ensures a legacy of skilled reciters.")
                                    character.stats['smart'] += random.randint(2, 5)
                                elif choice == "3":
                                    print("\nYou decide to seek further perfection in your own recitation skills.")
                                    print("Your dedication to improvement leads to an even higher level of mastery in Quranic recitation.")
                                    character.stats['diplomacy'] += random.randint(2, 5)
                                else:
                                    continue
                                break
    
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()
                        
                        while True:
                            # Age 18: Mastery of Quranic Recitation
                            if character.age == 18 and self.qari == "Sheikh Zainuddin al-Amasi":
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 18: Mastery of Quranic Recitation" + Style.RESET_ALL)
                                print("Having studied under the esteemed guidance of Sheikh Zainuddin al-Amasi for years, your Quranic recitation skills have reached new heights.")

                                # Event 1: Recitation Mastery
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Recitation Mastery" + Style.RESET_ALL)
                                print("Your Qari, Sheikh Zainuddin al-Amasi, acknowledges your mastery of Quranic recitation.")
                                print("He commends your impeccable Tajweed (proper pronunciation) and melodious rendering of Quranic verses.")

                                # Event 2: A Special Gift
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: A Special Gift" + Style.RESET_ALL)
                                print("As a token of his appreciation, Sheikh Zainuddin al-Amasi presents you with a beautifully handwritten Quran.")
                                print("This Quran is not only a testament to your achievements but also a symbol of your spiritual journey.")

                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Continue your journey of Quranic mastery")
                                print("2. Explore opportunities to teach and share your knowledge")
                                print("3. Reflect on your future path")

                                choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                if choice == "1":
                                    print("\nYou choose to continue your journey of Quranic mastery, further perfecting your recitation and Tajweed.")
                                    print("Your dedication to the Quran remains unwavering, and you delve deeper into its divine verses.")
                                    character.stats['martial'] += random.randint(2, 5)
                                elif choice == "2":
                                    print("\nRecognizing your expertise, you decide to explore opportunities to teach and share your Quranic knowledge.")
                                    print("You become a respected Quranic teacher, imparting your skills and spiritual insights to eager students.")
                                    character.stats['diplomacy'] += random.randint(2, 5)
                                elif choice == "3":
                                    print("\nYou take a moment to reflect on your future path, considering the impact of your Quranic journey.")
                                    print("While you have achieved mastery, you contemplate how your skills can best serve your community and faith.")
                                    character.stats['smart'] += random.randint(2, 5)
                                else:
                                    continue
                                break
    
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()
                        
                        while True:
                            # Age 19: Spreading Quranic Knowledge
                            if character.age == 19 and self.qari == "Sheikh Zainuddin al-Amasi":
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 19: Spreading Quranic Knowledge" + Style.RESET_ALL)
                                print("With your mastery of Quranic recitation and the guidance of Sheikh Zainuddin al-Amasi, you stand as a beacon of Quranic knowledge and spirituality.")

                                # Event 1: Teaching Quranic Recitation
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Teaching Quranic Recitation" + Style.RESET_ALL)
                                print("Recognizing your expertise, you begin teaching Quranic recitation to eager students from diverse backgrounds.")
                                print("Your classes are filled with a sense of reverence for the Quran and a thirst for understanding its verses.")

                                # Event 2: A Spiritual Gathering
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: A Spiritual Gathering" + Style.RESET_ALL)
                                print("You organize a spiritual gathering where individuals come to listen to your beautiful Quranic recitation.")
                                print("The event becomes a source of inspiration for those seeking a deeper connection with the Quran.")

                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Continue teaching and mentoring students")
                                print("2. Organize larger Quranic events and gatherings")
                                print("3. Embark on a journey to explore other regions and share your knowledge")

                                choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                if choice == "1":
                                    print("\nYou choose to continue teaching and mentoring students in the art of Quranic recitation.")
                                    print("Your commitment to nurturing the next generation of Quranic scholars is deeply appreciated.")
                                    character.stats['smart'] += random.randint(2, 5)
                                elif choice == "2":
                                    print("\nYou decide to organize larger Quranic events and gatherings, drawing in even more participants.")
                                    print("These gatherings become a means of fostering unity and spirituality within the community.")
                                    character.stats['diplomacy'] += random.randint(2, 5)
                                elif choice == "3":
                                    print("\nFeeling a calling to share your knowledge beyond your current surroundings, you embark on a journey.")
                                    print("You travel to different regions, spreading the beauty of Quranic recitation and spirituality.")
                                    character.stats['smart'] += random.randint(2, 5)
                                else:
                                    continue
                                break
    
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()
                        
                        while True:
                            # Age 20: Becoming the Mosque's Ulama
                            if character.age == 20 and self.qari == "Sheikh Zainuddin al-Amasi":
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 20: Becoming the Mosque's Ulama" + Style.RESET_ALL)
                                print("As the culmination of your journey to become a Hafiz-e-Quran and the guidance of Sheikh Zainuddin al-Amasi, you receive a prestigious invitation.")

                                # Event: Qari's Blessing and the Invitation
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Qari's Blessing and the Invitation" + Style.RESET_ALL)
                                print("Sheikh Zainuddin al-Amasi, your beloved Qari, recognizes your dedication and mastery of Quranic recitation.")
                                print("He offers his blessings and presents you with an invitation to become an Ulama of a prominent mosque in the Ottoman city of Bursa.")

                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Accept the invitation and deliver your first Khutbah (sermon)")
                                print("2. Express gratitude to your Qari and seek his guidance")
                                print("3. Reflect on the invitation and seek divine guidance")

                                choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                if choice == "1":
                                    print("\nWith great honor, you accept the invitation and prepare to deliver your first Khutbah at the mosque in Bursa.")
                                    print("Your heartfelt sermon touches the hearts of the congregation, leaving a lasting impact.")
                                    character.stats['diplomacy'] += random.randint(2, 5)
                                    character.prestige += 100
                                elif choice == "2":
                                    print("\nRecognizing the importance of your Qari's guidance, you express your gratitude and seek his wisdom.")
                                    print("Sheikh Zainuddin al-Amasi imparts valuable advice and blessings for your new role.")
                                    character.stats['martial'] += random.randint(2, 5)
                                elif choice == "3":
                                    print("\nYou decide to reflect on the invitation and seek divine guidance through prayer and contemplation.")
                                    print("You spend time in deep reflection, seeking clarity on the path that lies ahead.")
                                    character.stats['diplomacy'] += random.randint(2, 5)
                                else:
                                    continue
                                break



####################################################################


    
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()
                        
                        while True:
                            if character.age == 15 and self.qari == "Sheikh Hamdullah Efendi":
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 15: Quranic Scholar's Journey with Sheikh Hamdullah Efendi" + Style.RESET_ALL)
                                print("At the age of 15, you have embarked on your journey as a Quranic scholar under the guidance of Sheikh Hamdullah Efendi.")
                                print("The city of Istanbul, with its rich history and culture, becomes the backdrop of your continued quest for knowledge.")

                                # Event 1: Quranic Studies with a Scholar
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Quranic Studies with a Scholar" + Style.RESET_ALL)
                                print("Sheikh Hamdullah Efendi initiates you into advanced Quranic studies, emphasizing both understanding and recitation.")
                                print("His deep insights into the Quranic verses inspire your pursuit of knowledge.")

                                # Event 2: Exploring Calligraphy and Quran
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Exploring Calligraphy and Quran" + Style.RESET_ALL)
                                print("You accompany Sheikh Hamdullah Efendi in his exploration of Islamic calligraphy, combining the art with Quranic study.")
                                print("Your appreciation for the intricate relationship between the two deepens.")

                                # Event 3: Calligraphy Exhibition
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Calligraphy Exhibition" + Style.RESET_ALL)
                                print("Under Sheikh Hamdullah Efendi's guidance, you participate in a calligraphy exhibition, showcasing your work.")
                                print("Your contributions to Islamic calligraphy gain recognition and admiration.")

                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Continue your advanced Quranic studies")
                                print("2. Dedicate more time to Islamic calligraphy")
                                print("3. Balance both Quranic studies and calligraphy")

                                choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                if choice == "1":
                                    print("\nYou choose to continue your advanced Quranic studies, delving deeper into the Quran's profound teachings.")
                                    print("Your dedication to understanding and interpreting the Quran grows stronger.")
                                    
                                    # Outcome 1: Continuing Quranic Studies
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Outcome: Continuing Quranic Studies" + Style.RESET_ALL)
                                    print("You immerse yourself in advanced Quranic studies, guided by Sheikh Hamdullah Efendi's wisdom.")
                                    print("Your journey as a Quranic scholar advances with each passing day.")
                                    character.stats['smart'] += random.randint(2, 5)

                                elif choice == "2":
                                    print("\nYou decide to dedicate more time to Islamic calligraphy, honing your skills in the art of beautiful script.")
                                    print("Your calligraphy work becomes a reflection of your spiritual connection with the Quran.")
                                    
                                    # Outcome 2: Dedication to Islamic Calligraphy
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Outcome: Dedication to Islamic Calligraphy" + Style.RESET_ALL)
                                    print("Your dedication to Islamic calligraphy leads you to create stunning pieces inspired by Quranic verses.")
                                    print("Your work captivates those who see it, celebrating the beauty of Quranic art.")
                                    character.stats['smart'] += random.randint(2, 5)

                                elif choice == "3":
                                    print("\nYou choose to balance both your Quranic studies and your dedication to Islamic calligraphy.")
                                    print("This balance allows you to explore the depth of Quranic knowledge while continuing your artistic pursuits.")
                                    
                                    # Outcome 3: Balancing Studies and Calligraphy
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Outcome: Balancing Studies and Calligraphy" + Style.RESET_ALL)
                                    print("You divide your time effectively between advanced Quranic studies and Islamic calligraphy.")
                                    print("Your ability to manage both disciplines grows, enriching your life in profound ways.")
                                    character.stats['intrigue'] += random.randint(2, 5)

                                else:
                                    continue
                                break
    
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()
                        
                        while True:
                            if character.age == 16 and self.qari == "Sheikh Hamdullah Efendi":
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 16: Quranic Artistry with Sheikh Hamdullah Efendi" + Style.RESET_ALL)
                                print("At the age of 16, you have chosen Sheikh Hamdullah Efendi as your mentor in the art of Quranic recitation.")
                                print("Under his guidance, you explore the world of Islamic calligraphy and continue refining your Quranic recitation.")

                                # Event 1: The World of Islamic Calligraphy
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The World of Islamic Calligraphy" + Style.RESET_ALL)
                                print("Sheikh Hamdullah Efendi introduces you to the intricate world of Islamic calligraphy, particularly Naskh and Thuluth scripts.")
                                print("His expertise in calligraphy leaves you in awe.")

                                # Event 2: Combining Recitation and Calligraphy
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Combining Recitation and Calligraphy" + Style.RESET_ALL)
                                print("You learn to merge Quranic recitation with the art of calligraphy, creating visually stunning and spiritually rich pieces.")
                                print("This unique combination becomes a hallmark of your work.")

                                # Event 3: Preserving Islamic Heritage
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Preserving Islamic Heritage" + Style.RESET_ALL)
                                print("Sheikh Hamdullah Efendi emphasizes the importance of preserving Islamic heritage through art and recitation.")
                                print("You realize that your work can contribute significantly to this noble cause.")

                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Dedicate yourself to mastering Islamic calligraphy")
                                print("2. Continue refining your Quranic recitation skills")
                                print("3. Focus on using art and recitation to preserve Islamic heritage")

                                choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                if choice == "1":
                                    print("\nYou choose to dedicate yourself to mastering Islamic calligraphy, focusing on the Naskh and Thuluth scripts.")
                                    print("Under Sheikh Hamdullah Efendi's guidance, your calligraphic skills become exceptional.")
                                    self.qari_trust += 3  # Increase trust in your Qari

                                    # Outcome 1: Mastering Islamic Calligraphy
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Outcome: Mastering Islamic Calligraphy" + Style.RESET_ALL)
                                    print("Your mastery of Islamic calligraphy earns you recognition as a calligrapher of great skill.")
                                    print("You produce beautiful Quranic verses and calligraphic pieces cherished by many.")
                                    character.stats['smart'] += random.randint(2, 5)

                                elif choice == "2":
                                    print("\nYou decide to continue refining your Quranic recitation skills, working on proper pronunciation and melodious rendering.")
                                    print("Your recitation becomes more profound and mesmerizing under Sheikh Hamdullah Efendi's guidance.")
                                    self.qari_trust += 5  # Increase trust in your Qari

                                    # Outcome 2: Quranic Recitation Mastery
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Outcome: Quranic Recitation Mastery" + Style.RESET_ALL)
                                    print("Your Quranic recitations are celebrated for their beauty and spiritual depth.")
                                    print("You inspire others with your heartfelt renditions of the Quranic verses.")
                                    character.stats['martial'] += random.randint(2, 5)

                                elif choice == "3":
                                    print("\nYou choose to focus on using art and recitation to preserve Islamic heritage, working on projects that combine both.")
                                    print("Your creations become a means of educating and inspiring others about Islamic culture and spirituality.")
                                    self.qari_trust += 3  # Increase trust in your Qari

                                    # Outcome 3: Preserving Islamic Heritage
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Outcome: Preserving Islamic Heritage" + Style.RESET_ALL)
                                    print("Your art and recitations contribute significantly to the preservation of Islamic heritage.")
                                    print("You are admired for your dedication to this noble cause.")
                                    character.stats['intrigue'] += random.randint(2, 5)

                                else:
                                    continue
                                break
    
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()
                        
                        while True:
                            if character.age == 17 and self.qari == "Sheikh Hamdullah Efendi":
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 17: Advancing in Quranic Artistry with Sheikh Hamdullah Efendi" + Style.RESET_ALL)
                                print("At the age of 17, your journey in Quranic artistry under the guidance of Sheikh Hamdullah Efendi continues to flourish.")
                                print("You have honed your skills in calligraphy and Quranic recitation, and now it's time to take your talents to new heights.")

                                # Event 1: Mastering the Art of Naskh and Thuluth
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Mastering the Art of Naskh and Thuluth" + Style.RESET_ALL)
                                print("Under the mentorship of Sheikh Hamdullah Efendi, you delve deep into the intricate world of Naskh and Thuluth calligraphy.")
                                print("Your strokes become more precise, and your compositions reach new levels of sophistication.")

                                # Event 2: Quranic Recitation and Tajweed
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Quranic Recitation and Tajweed" + Style.RESET_ALL)
                                print("You continue to improve your Quranic recitation, ensuring each word is pronounced with precision and melody.")
                                print("Sheikh Hamdullah Efendi's guidance refines your recitation skills, making them harmonious and deeply moving.")

                                # Event 3: Preserving Quranic Artistry
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Preserving Quranic Artistry" + Style.RESET_ALL)
                                print("Sheikh Hamdullah Efendi emphasizes the importance of preserving Quranic artistry for future generations.")
                                print("You take up the responsibility of teaching calligraphy and Quranic recitation to young students, passing on the legacy.")

                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Dedicate yourself to mastering Naskh and Thuluth calligraphy")
                                print("2. Focus on perfecting Quranic recitation and Tajweed")
                                print("3. Embrace the role of a teacher and mentor for young students")

                                choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                if choice == "1":
                                    print("\nYou choose to dedicate yourself to mastering Naskh and Thuluth calligraphy.")
                                    print("Your work becomes recognized for its artistic excellence, and you contribute to the preservation of this Quranic art form.")
                                    character.stats['smart'] += random.randint(2, 5)

                                elif choice == "2":
                                    print("\nYou decide to focus on perfecting Quranic recitation and Tajweed.")
                                    print("Your recitations touch the hearts of those who listen, and you become known for your moving Quranic renditions.")
                                    character.stats['smart'] += random.randint(2, 5)

                                elif choice == "3":
                                    print("\nYou embrace the role of a teacher and mentor for young students, imparting your knowledge of calligraphy and Quranic recitation.")
                                    print("Your dedication to teaching ensures the continuation of Quranic artistry for generations to come.")
                                    character.stats['diplomacy'] += random.randint(2, 5)

                                else:
                                    continue
                                break
    
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()
                        
                        while True:
                            if character.age == 18 and self.qari == "Sheikh Hamdullah Efendi":
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 18: A Flourishing Legacy with Sheikh Hamdullah Efendi" + Style.RESET_ALL)
                                print("At the age of 18, your journey with Sheikh Hamdullah Efendi has matured into a flourishing legacy of Quranic artistry.")
                                print("Your skills in calligraphy and Quranic recitation have reached their zenith, and you are recognized as a master in your craft.")

                                # Event 1: International Recognition
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: International Recognition" + Style.RESET_ALL)
                                print("Your mastery of Naskh and Thuluth calligraphy and your soul-stirring Quranic recitations gain international acclaim.")
                                print("Your works are sought after by collectors, and you receive invitations to exhibit your artistry in renowned galleries.")

                                # Event 2: Preservation of Manuscripts
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Preservation of Manuscripts" + Style.RESET_ALL)
                                print("Sheikh Hamdullah Efendi entrusts you with the preservation of valuable Quranic manuscripts.")
                                print("You painstakingly restore and protect these ancient manuscripts, ensuring their continued existence.")

                                # Event 3: Teaching the Elite
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Teaching the Elite" + Style.RESET_ALL)
                                print("You are invited to teach Quranic artistry to the elite of the Ottoman Empire, including princes and scholars.")
                                print("Your students hold great respect for you, and your teachings shape the future of Quranic artistry.")

                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Continue to produce exceptional calligraphic masterpieces")
                                print("2. Dedicate yourself to the preservation of ancient Quranic manuscripts")
                                print("3. Nurture the next generation of Quranic artists and scholars")

                                choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                if choice == "1":
                                    print("\nYou choose to continue producing exceptional calligraphic masterpieces.")
                                    print("Your artistry becomes legendary, and your works are collected by connoisseurs worldwide.")
                                    character.stats['smart'] += random.randint(2, 5)

                                elif choice == "2":
                                    print("\nYou decide to dedicate yourself to the preservation of ancient Quranic manuscripts.")
                                    print("Your meticulous work ensures the survival of these invaluable treasures for generations to come.")
                                    character.stats['martial'] += random.randint(2, 5)

                                elif choice == "3":
                                    print("\nYou opt to nurture the next generation of Quranic artists and scholars.")
                                    print("Your students go on to become renowned in their own right, and you leave an indelible mark on Quranic artistry.")
                                    character.stats['diplomacy'] += random.randint(2, 5)

                                else:
                                    continue
                                break
    
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()
                        
                        while True:
                            if character.age == 19 and self.qari == "Sheikh Hamdullah Efendi":
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 19: Mastery of the Quran and Hadiths" + Style.RESET_ALL)
                                print("At the age of 19, you have achieved a profound mastery of the Quran and the Hadiths.")
                                print("Your journey to become a Hafiz-e-Quran is now complete, and your knowledge is widely respected.")

                                # Event 1: Recitation Mastery
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Recitation Mastery" + Style.RESET_ALL)
                                print("Your Quranic recitations are unparalleled in their beauty and precision.")
                                print("You are frequently invited to lead prayers and recitations in prestigious mosques and gatherings.")

                                # Event 2: Hadith Scholarship
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Hadith Scholarship" + Style.RESET_ALL)
                                print("Your scholarship in Hadiths is highly regarded, and you have become a respected authority in Islamic jurisprudence.")
                                print("Your insights into the Hadiths guide scholars and students in understanding Islamic traditions.")

                                # Event 3: Spiritual Leadership
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Spiritual Leadership" + Style.RESET_ALL)
                                print("You are acknowledged as a spiritual leader, providing guidance and solace to those seeking enlightenment.")
                                print("People from all walks of life seek your counsel, and you help them on their spiritual journeys.")

                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Continue to lead Quranic recitations in prestigious settings")
                                print("2. Dedicate yourself to furthering the study of Hadiths and Islamic jurisprudence")
                                print("3. Embrace your role as a spiritual leader and guide")

                                choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                if choice == "1":
                                    print("\nYou choose to continue leading Quranic recitations in prestigious settings.")
                                    print("Your captivating recitations resonate with the faithful, drawing them closer to their faith.")
                                    character.stats['health'] += random.randint(2, 5)

                                elif choice == "2":
                                    print("\nYou decide to dedicate yourself to furthering the study of Hadiths and Islamic jurisprudence.")
                                    print("Your scholarly works continue to guide future generations in understanding Islamic traditions.")
                                    character.stats['smart'] += random.randint(2, 5)

                                elif choice == "3":
                                    print("\nYou embrace your role as a spiritual leader and guide to those seeking enlightenment.")
                                    print("Your wisdom and compassion provide solace and inspiration to countless individuals.")
                                    character.stats['diplomacy'] += random.randint(2, 5)

                                else:
                                    continue
                                break
    
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()
                        print(Fore.RED +"Qari" + Style.BRIGHT + Style.RESET_ALL + Style.BRIGHT + Fore.CYAN , self.qari , Style.RESET_ALL+ Style.BRIGHT ,":", self.qari_trust ,Style.RESET_ALL)
                        while True:
                            if character.age == 20 and self.qari == "Sheikh Hamdullah Efendi":
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 20: Becoming an Ulema" + Style.RESET_ALL)
                                print("You have reached the age of 20, and your remarkable knowledge of the Quran and Hadiths has not gone unnoticed.")
                                print("You receive an invitation to serve as an Ulema in a prominent mosque in the thriving Ottoman city of Bursa, a center of Islamic culture and learning.")

                                # Event: Congratulations from Sheikh Hamdullah Efendi
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Congratulations from Sheikh Hamdullah Efendi" + Style.RESET_ALL)
                                print("Sheikh Hamdullah Efendi, your former Qari, sends you a heartfelt letter of congratulations.")
                                print("He expresses his pride in your achievements and wishes you success in your new role as an Ulema in Bursa.")

                                # Event 1: Arrival in Bursa
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Arrival in Bursa" + Style.RESET_ALL)
                                print("As you arrive in Bursa, you are greeted with warmth and respect by the local community.")
                                print("The city's rich Islamic heritage surrounds you, inspiring your sense of purpose.")

                                # Event 2: Offer to Lead Friday Sermons
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Offer to Lead Friday Sermons" + Style.RESET_ALL)
                                print("The elders of the mosque invite you to lead the Friday sermons (Khutbah) in the grand mosque of Bursa.")
                                print("This is a significant honor and responsibility, marking the beginning of your role as an Ulema.")

                                # Event 3: Community Engagement
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Community Engagement" + Style.RESET_ALL)
                                print("You engage with the local Muslim community, providing spiritual guidance, resolving disputes, and teaching.")
                                print("Your presence becomes a source of inspiration, and people look up to you for wisdom and leadership.")

                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Accept the offer to lead Friday sermons and establish yourself as an Ulema")
                                print("2. Focus on community engagement and support, prioritizing the needs of the local Muslims")
                                print("3. Balance your responsibilities, ensuring both the sermons and community engagement receive attention")

                                choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                if choice == "1":
                                    print("\nYou wholeheartedly accept the offer to lead Friday sermons, cementing your position as an Ulema.")
                                    print("Your eloquent sermons resonate with the congregation, and your reputation as a spiritual leader grows.")
                                    character.stats['diplomacy'] += random.randint(2, 5)

                                elif choice == "2":
                                    print("\nYou choose to focus on community engagement and support, prioritizing the needs of the local Muslims.")
                                    print("Your dedication to the community's well-being strengthens the bond between you and the people of Bursa.")
                                    character.stats['smart'] += random.randint(2, 5)

                                elif choice == "3":
                                    print("\nYou decide to balance your responsibilities, ensuring both the sermons and community engagement receive attention.")
                                    print("Your ability to manage your duties reflects your commitment to serving both God and the community.")
                                    character.stats['intrigue'] += random.randint(2, 5)

                                else:
                                    continue
                                break
    
                        character.age += 1
                        character.print_info()
                        print("Thanks for playing!!!!!")
                        quit()


####################################################################


                    elif choice == "2":
                        print("\nYou choose to embark on a new career path, exploring opportunities beyond the Madrassah.")
                        print("Your decision opens doors to a different future filled with possibilities.")
                        # Implement character growth and story progression for choosing a new career
                    else:
                        continue
                    break

            elif choice == "3":
                print(Style.BRIGHT + "You embark on a mystical journey that transcends the boundaries of ordinary existence. In the company of Sufi Müritler, you engage in spiritual practices, immerse yourself in Sufi poetry, and explore the inner dimensions of faith. Your path is filled with moments of spiritual ecstasy and profound insights. You seek to find divine love and meaning in all aspects of life.")
                madrassah.join_group_sufi()
                while True:
                    if character.age == 8:
                        print("\n" + Fore.RED + Style.BRIGHT + "Age 8: The Sufi Journey Begins" + Style.RESET_ALL)
                        print("You are 8 years old and have just joined the Sufi group at the Madrassah.")
                        print("Your journey towards spiritual enlightenment and a deeper understanding of faith begins.")

                        # Event 1: The Sufi Mentor
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Sufi Mentor" + Style.RESET_ALL)
                        print("You meet your Sufi mentor, a wise and kind-hearted guide who welcomes you into the Sufi order.")
                        print("Your mentor introduces you to the principles of Sufism and the path of spiritual awakening.")

                        # Event 2: The Mystical Teachings
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Mystical Teachings" + Style.RESET_ALL)
                        print("You begin your journey into the mystical teachings of Sufism, exploring the poetry and wisdom of Sufi saints.")
                        print("These teachings inspire you to seek a deeper connection with the divine.")

                        # Event 3: The Sufi Rituals
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Sufi Rituals" + Style.RESET_ALL)
                        print("Your mentor introduces you to the sacred Sufi rituals, including the mesmerizing Whirling Dervishes dance.")
                        print("You experience moments of spiritual ecstasy during these rituals.")

                        # Choices
                        print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                        print("1. Dedicate Yourself to Sufi Wisdom")
                        print("2. Explore the Mystical Teachings Further")
                        print("3. Deepen Your Connection Through Sufi Rituals")

                        choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                        if choice == "1":
                            print("\nYou choose to dedicate yourself to Sufi wisdom, seeking to understand the deeper philosophical aspects of Sufism.")
                            print("Your wisdom and spirituality begin to grow as you delve into Sufi literature.")
                            character.stats['martial'] += random.randint(2, 5)
                        elif choice == "2":
                            print("\nYou decide to explore the mystical teachings of Sufism further, immersing yourself in the poetry and wisdom of Sufi saints.")
                            print("Your connection with the divine deepens as you contemplate the profound teachings.")
                            character.stats['smart'] += random.randint(2, 5)
                        elif choice == "3":
                            print("\nYou choose to deepen your connection through Sufi rituals, participating in the mesmerizing Whirling Dervishes dance.")
                            print("During these rituals, you experience moments of spiritual ecstasy and oneness with the divine.")
                            character.stats['looks'] += random.randint(2, 5)
                        else:
                            continue
    
                        break
                character.age += 1
                character.print_info()
                madrassah.main_menu(character)
                while True:
                    if character.age == 9:
                        print("\n" + Fore.RED + Style.BRIGHT + "Age 9: The Journey Continues" + Style.RESET_ALL)
                        print(f"You are now 9 years old and have spent 1 year as a member of the Sufi group in the Madrassah.")
                        print("Your mystical journey guided by faith and spirituality continues to unfold.")

                        # Event 1: The Sufi Mentor's Guidance
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Sufi Mentor's Guidance" + Style.RESET_ALL)
                        print("Your Sufi mentor, a source of spiritual wisdom and guidance, continues to nurture your spiritual growth.")
                        print("They impart deeper teachings about Sufism, emphasizing the importance of inner reflection and connection with the divine.")

                        # Event 2: The Spiritual Retreat
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Spiritual Retreat" + Style.RESET_ALL)
                        print("The Sufi group embarks on a spiritual retreat, where you spend days in quiet contemplation, meditation, and prayer.")
                        print("During this retreat, you have a profound spiritual experience that deepens your connection to the divine.")

                        # Event 3: The Quest for Wisdom
                        print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Quest for Wisdom" + Style.RESET_ALL)
                        print("Your mentor assigns you a quest to seek wisdom and knowledge. You must engage in the study of sacred texts, Sufi poetry, and philosophy to attain higher levels of understanding.")
                        print("Your journey for wisdom begins.")

                        # Choices
                        print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                        print("1. Continue Embracing the Mentor's Teachings")
                        print("2. Reflect on the Spiritual Retreat Experience")
                        print("3. Embark on the Quest for Wisdom")

                        choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                        if choice == "1":
                            print("\nYou continue to wholeheartedly embrace your Sufi mentor's teachings, absorbing their wisdom and spiritual guidance.")
                            print("Your wisdom and spirituality continue to flourish under their mentorship.")
                            character.stats['smart'] += random.randint(2, 5)
                        elif choice == "2":
                            print("\nYou reflect deeply on the profound spiritual experience during the retreat, seeking to integrate its lessons into your daily life.")
                            print("Your connection to the divine deepens as you carry the retreat's essence with you.")
                            character.stats['smart'] += random.randint(2, 5)
                        elif choice == "3":
                            print("\nYou embark on the quest for wisdom, dedicating yourself to the study of sacred texts and Sufi philosophy.")
                            print("As you delve deeper into the realm of knowledge, your understanding of the spiritual and philosophical aspects of Sufism grows.")
                            character.stats['smart'] += random.randint(2, 5)
                        else:
                            continue
                        break
            # Progress character age and continue the game loop
            
            character.age += 1
            character.print_info()
            madrassah.main_menu(character)
            while True:
                if character.age == 10:
                    print("\n" + Fore.RED + Style.BRIGHT + "Age 10: Deepening the Connection" + Style.RESET_ALL)
                    print(f"You are now 10 years old and have spent 2 year(s) as a member of the Sufi group in the Madrassah.")
                    print("Your mystical journey guided by faith and spirituality continues to deepen.")

                    # Event 1: The Sufi Gathering
                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Sufi Gathering" + Style.RESET_ALL)
                    print("The Sufi group gathers for a spiritual gathering, where you listen to Sufi poetry and engage in heartfelt discussions.")
                    print("The sense of unity and spiritual connection among the group members grows stronger.")

                    # Event 2: The Sufi Music and Dance
                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Sufi Music and Dance" + Style.RESET_ALL)
                    print("You are introduced to the mesmerizing world of Sufi music and dance, a form of expression that transcends the mundane.")
                    print("Participating in these spiritual practices elevates your soul and draws you closer to the divine.")

                    # Event 3: The Challenge of Patience
                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Challenge of Patience" + Style.RESET_ALL)
                    print("Your mentor assigns you a challenge—to cultivate patience and forbearance in the face of adversity.")
                    print("You must face various trials and tribulations that test your ability to remain patient and steadfast.")

                    # Choices
                    print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                    print("1. Embrace the Unity of the Sufi Gathering")
                    print("2. Explore the Spiritual Depths of Sufi Music and Dance")
                    print("3. Take on the Challenge of Patience")

                    choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                    if choice == "1":
                        print("\nYou wholeheartedly embrace the unity and spiritual connection of the Sufi gathering, fostering deeper bonds with your fellow Sufi members.")
                        print("The collective energy of the group continues to uplift your soul.")
                        character.stats['diplomacy'] += random.randint(2, 5)
                    elif choice == "2":
                        print("\nYou immerse yourself in the world of Sufi music and dance, allowing these spiritual practices to elevate your consciousness.")
                        print("Your experiences with music and dance become a profound source of spiritual inspiration.")
                        character.stats['looks'] += random.randint(2, 5)
                    elif choice == "3":
                        print("\nYou accept the challenge of patience, facing trials with resilience and calmness.")
                        print("Through these challenges, you cultivate a deep sense of inner peace and patience.")
                        character.stats['martial'] += random.randint(2, 5)
                    else:
                        continue
                    break
            # Progress character age and continue the game loop
            
            character.age += 1
            character.print_info()
            madrassah.main_menu(character)
            while True:
                if character.age == 11:
                    print("\n" + Fore.RED + Style.BRIGHT + "Age 11: The Path of Illumination" + Style.RESET_ALL)
                    print(f"You are now 11 years old and have spent 3 year(s) as a member of the Sufi group in the Madrassah.")
                    print("Your mystical journey guided by faith and spirituality continues to lead you toward illumination.")

                    # Event 1: The Sufi Meditation Retreat
                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Sufi Meditation Retreat" + Style.RESET_ALL)
                    print("The Sufi group embarks on a deep meditation retreat in a serene natural setting.")
                    print("During this retreat, you experience moments of profound inner peace and divine connection.")

                    # Event 2: The Sufi Poetry and Philosophy
                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Sufi Poetry and Philosophy" + Style.RESET_ALL)
                    print("You delve into the world of Sufi poetry and philosophy, exploring the writings of renowned Sufi mystics.")
                    print("The poetic verses and profound teachings resonate with your soul, leading to spiritual insights.")

                    # Event 3: The Call to Service
                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Call to Service" + Style.RESET_ALL)
                    print("Your mentor conveys a message: it is time to apply your spiritual wisdom in service to others.")
                    print("You embark on a journey to help those in need, demonstrating the compassion and love you have cultivated.")

                    # Choices
                    print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                    print("1. Embrace the Tranquility of the Meditation Retreat")
                    print("2. Dive Deeper into Sufi Poetry and Philosophy")
                    print("3. Answer the Call to Service")

                    choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                    if choice == "1":
                        print("\nYou fully embrace the tranquility of the meditation retreat, experiencing moments of profound inner peace.")
                        print("The retreat deepens your spiritual connection and brings you closer to the illumination you seek.")
                        character.stats['smart'] += random.randint(2, 5)
                    elif choice == "2":
                        print("\nYou immerse yourself in the world of Sufi poetry and philosophy, finding profound meaning in the verses and teachings.")
                        print("Your understanding of the mystical aspects of Sufism continues to expand.")
                        character.stats['smart'] += random.randint(2, 5)
                    elif choice == "3":
                        print("\nYou answer the call to service, dedicating yourself to helping those in need with compassion and love.")
                        print("Through your acts of service, you shine as a beacon of light and inspiration to others.")
                        character.stats['martial'] += random.randint(2, 5)
                    else:
                        continue
                    break
            # Progress character age and continue the game loop
            
            character.age += 1
            character.print_info()
            madrassah.main_menu(character)
            while True:
                if character.age == 12:
                    print("\n" + Fore.RED + Style.BRIGHT + "Age 12: A Turning Point" + Style.RESET_ALL)
                    print(f"You are now 12 years old and have spent 4 year(s) as a member of the Sufi group in the Madrassah.")
                    print("Your mystical journey has brought you to a significant turning point in your life.")

                    # Event 1: The Revelation
                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Revelation" + Style.RESET_ALL)
                    print("During a moment of deep meditation and reflection, you experience a profound revelation.")
                    print("The revelation fills you with a sense of purpose and clarity about your path.")

                    # Choices
                    print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                    print("1. Embrace the Path of Sufism")

                    choice = input(Style.BRIGHT + "Enter your choice (1): " + Style.RESET_ALL)

                    if choice == "1":
    
                        character.age += 1
                        character.print_info()
                        if character.age == 13:
                            print("\nYou choose to wholeheartedly embrace the path of Sufism, continuing your spiritual journey with unwavering dedication.")
                            print("Your wisdom and spirituality continue to grow as you seek deeper mystical experiences.")
                            # Implement character growth and story progression for continuing Sufism
                            # Age 13: Journey to Istanbul
                            print("\n" + Fore.RED + Style.BRIGHT + "Age 13:"  + Fore.YELLOW + " Journey to Istanbul\n")
                            
                            # Decision 1
                            print("As the year is 1453, you and your family have decided to embark on a journey to Istanbul, a city of great importance in the Ottoman Empire. Your family has joined a caravan for safety and companionship.")
                            print("Before setting off, you have some choices to make.")

                            print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                            print(Fore.RED +Style.BRIGHT + "1." + Style.RESET_ALL +Style.BRIGHT + " Help your family load the caravan with supplies and belongings.")
                            print(Fore.RED +Style.BRIGHT + "2." + Style.RESET_ALL +Style.BRIGHT + " Visit the local mosque to seek blessings for a safe journey.")
                            print(Fore.RED +Style.BRIGHT + "3." + Style.RESET_ALL +Style.BRIGHT + " Spend time with your friends one last time before leaving.")

                            choice_1 = input("Enter your choice (1/2/3): ")

                            if choice_1 == "1":
                                print("\nYou decided to help your family load the caravan. Working together, you strengthen your family bonds.")
                                character.stats['looks'] += random.randint(2, 5)
                            elif choice_1 == "2":
                                print("\nYou chose to visit the local mosque for blessings. You feel a sense of divine protection surrounding you.")
                                character.stats['smart'] += random.randint(2, 5)
                            elif choice_1 == "3":
                                print("\nYou spent time with your friends, cherishing the moments before your journey. Your bonds with them grew stronger.")
                                character.stats['diplomacy'] += random.randint(2, 5)
                            else:
                                print("\nInvalid choice. Please enter 1, 2, or 3.")

                            # Decision 2
                            print("\nAs you journey to Istanbul, you can't help but think of Mehmet the Conqueror, who captured the city in 1453, marking a significant moment in history.")
                            print("\nAs you travel with the caravan, you encounter travelers from diverse backgrounds. One evening, you sit by the campfire, and a group of travelers begins sharing stories and wisdom.")

                            print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                            print(Fore.RED +Style.BRIGHT + "1." + Style.RESET_ALL +Style.BRIGHT + " Strike up a conversation with them to learn from their experiences." )
                            print(Fore.RED +Style.BRIGHT + "2." + Style.RESET_ALL + Style.BRIGHT +" Listen quietly and observe, taking in their stories.")

                            choice_2 = input("Enter your choice (1/2): ")

                            if choice_2 == "1":
                                print("\nYou decided to strike up a conversation with the travelers. Their stories enriched your wisdom.")
                            elif choice_2 == "2":
                                print("\nYou chose to listen quietly and observe. The stories of the travelers left a lasting impact on your wisdom.")
                            else:
                                print("\nInvalid choice. Please enter 1 or 2.")

                            # Decision 3
                            print("\nDuring your journey, you come across a wounded animal on the path. It appears to be in pain and needs help.")

                            print(Fore.RED +Style.BRIGHT + "1." + Style.RESET_ALL + Style.BRIGHT +" Approach the animal cautiously to see if you can assist it." )
                            print(Fore.RED +Style.BRIGHT + "2." + Style.RESET_ALL + Style.BRIGHT +" Stay back and observe the animal from a distance.")
                            print(Fore.RED + Style.BRIGHT +"3." + Style.RESET_ALL + Style.BRIGHT +" Pray for the animal's well-being." )

                            choice_3 = input("Enter your choice (1/2/3): ")

                            if choice_3 == "1":
                                print("\nYou cautiously approached the wounded animal and offered assistance. Your act of compassion made a difference in its well-being.")
                                character.stats['martial'] += random.randint(2, 5)
                            elif choice_3 == "2":
                                print("\nYou chose to stay back and observe the animal from a distance. It eventually limped away, and you continued your journey.")
                                character.stats['intrigue'] += random.randint(2, 5)
                            elif choice_3 == "3":
                                print("\nYou offered a prayer for the animal's well-being. You felt a sense of divine protection surrounding you.")
                                character.stats['health'] += random.randint(2, 5)
                            else:
                                print("\nInvalid choice. Please enter 1, 2, or 3.")
    
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()
                        while True:
                            if character.age == 14:
                                print(Style.BRIGHT + Fore.RED + "\nAge 14:" + Fore.YELLOW + " Seeking Guidance in Istanbul" + Style.RESET_ALL)
                                print(Style.BRIGHT + "\nAs you set foot in the magnificent city of Istanbul, the grandeur of its architecture, bustling markets, and diverse culture overwhelms your senses. You find yourself standing at a crossroads, not only in this great city but in your spiritual journey as well." + Style.RESET_ALL)
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print(Fore.RED + Style.BRIGHT +"1." + Style.RESET_ALL + Style.BRIGHT +" Seek guidance from Murshid Shams al-Din Sivasi")
                                print(Fore.RED + Style.BRIGHT +"2." + Style.RESET_ALL + Style.BRIGHT +" Choose to study under Shaykh Akshamsaddin")

                                choice_shaykh = input(Style.BRIGHT + "Enter your choice (1/2): ")

                                if choice_shaykh == "1":
                                    self.shaykh = "Murshid Shams al-Din Sivasi"
                                    print("\nYou decide to seek guidance from Murshid Shams al-Din Sivasi, a trusted adviser of Mehmet the Conqueror himself. His wisdom and close association with the ruler make him an appealing choice for your spiritual journey.")
                                    print("You make your way to his humble abode in Istanbul, where you find him in deep meditation. With great respect, you request to be his disciple, and after a long silence, he agrees to take you under his wing. Your journey into Sufism begins under the guidance of this esteemed Murshid.")

                                    # Create an event to earn trust from Murshid Shams al-Din Sivasi
                                    print(Style.BRIGHT + "\nAge 14: Earning Trust with Murshid Shams al-Din Sivasi" + Style.RESET_ALL)
                                    print(Style.BRIGHT + "You spend your initial days with Murshid Shams al-Din Sivasi in silent contemplation and prayer. He observes your dedication and commitment to the path of Sufism." + Style.RESET_ALL)
                                    
                                    # Create two options to earn trust, one with more trust than the other
                                    print("\n" + Fore.CYAN + Style.BRIGHT  + Style.BRIGHT +"Choices:" + Style.RESET_ALL)
                                    print(Fore.RED +Style.BRIGHT +"1." + Style.RESET_ALL + Style.BRIGHT +" Diligently follow his teachings and practices")
                                    print(Fore.RED + Style.BRIGHT + "2." + Style.RESET_ALL + Style.BRIGHT +" Show initiative by assisting him in daily tasks")

                                    trust_choice = input(Style.BRIGHT + "Choose how you will earn the Murshid's trust (1/2): ")

                                    if trust_choice == "1":
                                        print("\nYou choose to diligently follow Murshid Shams al-Din Sivasi's teachings and practices. Your commitment and discipline impress him, and he begins to share deeper insights into Sufism with you. Your trust with the Murshid grows significantly.")
                                        self.shaykh_trust += 5
                                        break
                                    elif trust_choice == "2":
                                        print("\nYou decide to show initiative by assisting Murshid Shams al-Din Sivasi in his daily tasks. Your willingness to help and your humility earn his appreciation. Your trust with the Murshid increases.")
                                        self.shaykh_trust += 3
                                        break
                                    else:
                                        continue
        
                            character.age += 1
                            character.print_info()
                            main_menu.main_menu()
                            self.shaykh_trust += 5

                            while True:
                                # Age 15: Sufi Journey with Murshid Shams al-Din Sivasi
                                if character.age == 15 and self.shaykh == "Murshid Shams al-Din Sivasi":
                                    print("\n" + Fore.RED + Style.BRIGHT + "Age 15: Sufi Journey with Murshid Shams al-Din Sivasi" + Style.RESET_ALL)
                                    print("Having embraced the guidance of Murshid Shams al-Din Sivasi, your Sufi journey has deepened.")
                                    print("You are now 15 years old and stand at the threshold of further spiritual exploration under his mentorship.")

                                    # Event 1: A Sufi Retreat
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Event 1: A Sufi Retreat" + Style.RESET_ALL)
                                    print("Murshid Shams al-Din Sivasi organizes a Sufi retreat in a serene natural setting.")
                                    print("This retreat is designed to deepen your connection to the divine and to foster spiritual growth.")

                                    # Decision 1: Choose to immerse yourself in silent contemplation or active service
                                    print("\n" + Fore.CYAN + Style.BRIGHT + "Decision 1:" + Style.RESET_ALL)
                                    print("1. Immerse yourself in silent contemplation and meditation")
                                    print("2. Engage in active service and help fellow Sufis during the retreat")

                                    choice1 = input(Style.BRIGHT + "Enter your choice (1/2): " + Style.RESET_ALL)

                                    if choice1 == "1":
                                        print("\nYou choose to immerse yourself in silent contemplation and meditation during the retreat.")
                                        print("The retreat deepens your spiritual connection and inner peace.")
                                        character.stats['smart'] += random.randint(2, 5)
                                    elif choice1 == "2":
                                        print("\nYou decide to engage in active service during the retreat, assisting fellow Sufis in various tasks.")
                                        print("Your acts of service are well-received, fostering a sense of unity and harmony within the group.")
                                        character.stats['diplomacy'] += random.randint(2, 5)

                                    # Event 2: Delving into Sufi Poetry
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Event 2: Delving into Sufi Poetry" + Style.RESET_ALL)
                                    print("Murshid Shams al-Din Sivasi introduces you to the world of Sufi poetry and philosophy.")
                                    print("You explore the writings of renowned Sufi mystics, finding profound meaning in their verses.")

                                    # Decision 2: Choose to focus on the mystical aspects or philosophical discussions
                                    print("\n" + Fore.CYAN + Style.BRIGHT + "Decision 2:" + Style.RESET_ALL)
                                    print("1. Immerse yourself in the mystical aspects of Sufi poetry")
                                    print("2. Engage in profound philosophical discussions with fellow Sufis")

                                    choice2 = input(Style.BRIGHT + "Enter your choice (1/2): " + Style.RESET_ALL)

                                    if choice2 == "1":
                                        print("\nYou choose to immerse yourself in the mystical aspects of Sufi poetry, experiencing divine love and unity.")
                                        print("The verses resonate with your soul, deepening your spiritual understanding.")
                                        character.stats['smart'] += random.randint(2, 5)
                                    elif choice2 == "2":
                                        print("\nYou decide to engage in profound philosophical discussions with fellow Sufis, exploring the depths of Sufi philosophy.")
                                        print("Your keen intellect and curiosity contribute to enriching the discussions.")
                                        character.stats['diplomacy'] += random.randint(2, 5)
                                    else:
                                        continue

                                    # Event 3: The Sufi Call to Service
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Event 3: The Sufi Call to Service" + Style.RESET_ALL)
                                    print("Murshid Shams al-Din Sivasi conveys a message: it is time to apply your spiritual wisdom in service to others.")
                                    print("You embark on a journey to help those in need, demonstrating the compassion and love you have cultivated.")

                                    # Decision 3: Choose to dedicate more time to service or to further study and meditation
                                    print("\n" + Fore.CYAN + Style.BRIGHT + "Decision 3:" + Style.RESET_ALL)
                                    print("1. Dedicate more time to selfless service and helping others")
                                    print("2. Prioritize further study and meditation to deepen your spiritual knowledge")

                                    choice3 = input(Style.BRIGHT + "Enter your choice (1/2): " + Style.RESET_ALL)

                                    if choice3 == "1":
                                        print("\nYou decide to dedicate more time to selfless service, helping those in need with compassion and love.")
                                        print("Through your acts of service, you shine as a beacon of light and inspiration to others.")
                                        character.stats['smart'] += random.randint(2, 5)
                                    elif choice3 == "2":
                                        print("\nYou choose to prioritize further study and meditation, delving deeper into the realms of spiritual knowledge.")
                                        print("Your commitment to inner growth continues to deepen your understanding of Sufism.")
                                        character.stats['intrigue'] += random.randint(2, 5)
                                    else:
                                        continue
                                    break
        
                            character.age += 1
                            character.print_info()
                            main_menu.main_menu()
                            self.shaykh_trust += 5

                            while True:
                                # Age 16: Continuing the Sufi Journey
                                if character.age == 16 and self.shaykh == "Murshid Shams al-Din Sivasi":
                                    print("\n" + Fore.RED + Style.BRIGHT + "Age 16: Continuing the Sufi Journey" + Style.RESET_ALL)
                                    print("With each passing year under the guidance of Murshid Shams al-Din Sivasi, your Sufi journey deepens.")
                                    print("You are now 16 years old and have grown in wisdom and spirituality through his mentorship.")

                                    # Event 1: The Sufi Meditation Retreat
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Event 1: The Sufi Meditation Retreat" + Style.RESET_ALL)
                                    print("Once again, Murshid Shams al-Din Sivasi organizes a Sufi meditation retreat, building upon your previous experiences.")
                                    print("The retreat offers an opportunity for profound inner peace and divine connection.")

                                    # Decision 1: Choose to deepen your meditation practice or to assist in organizing the retreat
                                    print("\n" + Fore.CYAN + Style.BRIGHT + "Decision 1:" + Style.RESET_ALL)
                                    print("1. Deepen your meditation practice, seeking to connect more deeply with the divine")
                                    print("2. Assist in organizing and facilitating the retreat to help fellow Sufis")

                                    choice1 = input(Style.BRIGHT + "Enter your choice (1/2): " + Style.RESET_ALL)

                                    if choice1 == "1":
                                        print("\nYou choose to deepen your meditation practice, dedicating yourself to seeking a profound connection with the divine.")
                                        print("The retreat allows you to experience moments of spiritual transcendence.")
                                        character.stats['smart'] += random.randint(2, 5)
                                    elif choice1 == "2":
                                        print("\nYou decide to assist in organizing and facilitating the retreat, ensuring a harmonious and spiritually enriching experience for fellow Sufis.")
                                        print("Your dedication to service contributes to the success of the retreat.")
                                        character.stats['diplomacy'] += random.randint(2, 5)

                                    # Event 2: Sufi Music and Chants
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Event 2: Sufi Music and Chants" + Style.RESET_ALL)
                                    print("During this phase of your journey, Murshid Shams al-Din Sivasi introduces you to the mystical world of Sufi music and chants.")
                                    print("You explore the power of music as a means of connecting with the divine and reaching higher states of consciousness.")

                                    # Decision 2: Choose to immerse yourself in Sufi music or to learn the art of chanting and spiritual songs
                                    print("\n" + Fore.CYAN + Style.BRIGHT + "Decision 2:" + Style.RESET_ALL)
                                    print("1. Immerse yourself in the melodies and rhythms of Sufi music")
                                    print("2. Learn the art of chanting and singing spiritual songs with devotion")

                                    choice2 = input(Style.BRIGHT + "Enter your choice (1/2): " + Style.RESET_ALL)

                                    if choice2 == "1":
                                        print("\nYou choose to immerse yourself in the melodies and rhythms of Sufi music, using it as a medium for spiritual expression.")
                                        print("The enchanting music elevates your soul and deepens your connection to the divine.")
                                        character.stats['smart'] += random.randint(2, 5)
                                    elif choice2 == "2":
                                        print("\nYou decide to learn the art of chanting and singing spiritual songs with unwavering devotion.")
                                        print("Your soulful chants and songs resonate with the hearts of those who listen, creating a spiritual atmosphere.")
                                        character.stats['intrigue'] += random.randint(2, 5)

                                    # Event 3: The Call to Sufi Leadership
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Event 3: The Call to Sufi Leadership" + Style.RESET_ALL)
                                    print("Murshid Shams al-Din Sivasi recognizes your growth and dedication to the Sufi path.")
                                    print("He shares with you his vision of you becoming a Sufi leader and guide to others.")

                                    # Decision 3: Choose to accept the call to leadership or to continue your personal journey
                                    print("\n" + Fore.CYAN + Style.BRIGHT + "Decision 3:" + Style.RESET_ALL)
                                    print("1. Accept the call to Sufi leadership and guide others on their spiritual journeys")
                                    print("2. Continue your personal journey, focusing on your own spiritual growth")

                                    choice3 = input(Style.BRIGHT + "Enter your choice (1/2): " + Style.RESET_ALL)

                                    if choice3 == "1":
                                        print("\nYou wholeheartedly accept the call to Sufi leadership, ready to guide and mentor others on their spiritual journeys.")
                                        print("Your journey now includes helping fellow Sufis find their path to divine love and unity.")
                                        character.stats['smart'] += random.randint(2, 5)
                                    elif choice3 == "2":
                                        print("\nYou choose to continue your personal journey, focusing on your own spiritual growth and exploration.")
                                        print("You believe that by deepening your own understanding, you can better serve others in the future.")
                                        character.stats['smart'] += random.randint(2, 5)
                                    else:
                                        continue
                                    break
        
                            character.age += 1
                            character.print_info()
                            main_menu.main_menu()
                            self.shaykh_trust += 5

                            while True:
                                # Age 17: Advancing on the Sufi Path
                                if character.age == 17 and self.shaykh == "Murshid Shams al-Din Sivasi":
                                    print("\n" + Fore.RED + Style.BRIGHT + "Age 17: Advancing on the Sufi Path" + Style.RESET_ALL)
                                    print("Your journey under the guidance of Murshid Shams al-Din Sivasi continues to evolve.")
                                    print("At the age of 17, you stand as a beacon of spiritual wisdom and devotion among your fellow Sufis.")

                                    # Event 1: The Sufi Gathering
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Event 1: The Sufi Gathering" + Style.RESET_ALL)
                                    print("A grand Sufi gathering is organized, bringing together Sufis from different regions.")
                                    print("The gathering is a celebration of unity and spiritual enlightenment.")

                                    # Decision 1: Choose to share your spiritual experiences or to listen and learn from other Sufis
                                    print("\n" + Fore.CYAN + Style.BRIGHT + "Decision 1:" + Style.RESET_ALL)
                                    print("1. Share your own spiritual experiences and insights with the Sufi community")
                                    print("2. Listen and learn from the experiences and teachings of other Sufis")

                                    choice1 = input(Style.BRIGHT + "Enter your choice (1/2): " + Style.RESET_ALL)

                                    if choice1 == "1":
                                        print("\nYou choose to share your own spiritual experiences and insights with the Sufi community.")
                                        print("Your words resonate deeply with fellow Sufis, inspiring them on their own journeys.")
                                        character.stats['smart'] += random.randint(2, 5)
                                    elif choice1 == "2":
                                        print("\nYou decide to listen and learn from the experiences and teachings of other Sufis.")
                                        print("The diverse perspectives and wisdom you encounter enrich your spiritual understanding.")
                                        character.stats['martial'] += random.randint(2, 5)

                                    # Event 2: Sufi Artistry and Expression
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Event 2: Sufi Artistry and Expression" + Style.RESET_ALL)
                                    print("In this phase of your Sufi journey, Murshid Shams al-Din Sivasi encourages you to explore the realm of Sufi artistry.")
                                    print("You discover how art, including calligraphy, poetry, and music, can be a path to divine connection.")

                                    # Decision 2: Choose to specialize in a particular form of Sufi art or to explore multiple forms
                                    print("\n" + Fore.CYAN + Style.BRIGHT + "Decision 2:" + Style.RESET_ALL)
                                    print("1. Specialize in a particular form of Sufi art, such as calligraphy or music")
                                    print("2. Explore multiple forms of Sufi art, allowing creativity to flow freely")

                                    choice2 = input(Style.BRIGHT + "Enter your choice (1/2): " + Style.RESET_ALL)

                                    if choice2 == "1":
                                        print("\nYou choose to specialize in a particular form of Sufi art, dedicating yourself to its mastery.")
                                        print("Your chosen art form becomes a channel for expressing divine beauty and truth.")
                                        character.stats['smart'] += random.randint(2, 5)
                                    elif choice2 == "2":
                                        print("\nYou decide to explore multiple forms of Sufi art, allowing your creativity to flow freely.")
                                        print("Your artistic expressions capture the essence of Sufi mysticism, inspiring others.")
                                        character.stats['martial'] += random.randint(2, 5)

                                    # Event 3: The Sufi's Inner Quest
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Event 3: The Sufi's Inner Quest" + Style.RESET_ALL)
                                    print("As you advance on the Sufi path, you face profound questions about your own spiritual journey.")
                                    print("Murshid Shams al-Din Sivasi encourages you to embark on a deep inner quest for self-realization.")

                                    # Decision 3: Choose to embark on a solitary retreat or to seek guidance from Murshid Shams al-Din Sivasi
                                    print("\n" + Fore.CYAN + Style.BRIGHT + "Decision 3:" + Style.RESET_ALL)
                                    print("1. Embark on a solitary retreat, seeking self-realization through introspection")
                                    print("2. Seek guidance and mentorship from Murshid Shams al-Din Sivasi in your inner quest")

                                    choice3 = input(Style.BRIGHT + "Enter your choice (1/2): " + Style.RESET_ALL)

                                    if choice3 == "1":
                                        print("\nYou choose to embark on a solitary retreat, delving deep into introspection and self-realization.")
                                        print("The solitude and silence of the retreat lead you to profound spiritual insights.")
                                        character.stats['smart'] += random.randint(2, 5)
                                    elif choice3 == "2":
                                        print("\nYou decide to seek guidance and mentorship from Murshid Shams al-Din Sivasi in your inner quest.")
                                        print("Under his wise counsel, you navigate the complexities of the Sufi's inner journey.")
                                        character.stats['martial'] += random.randint(2, 5)
                                    else:
                                        continue
                                    break
        
                            character.age += 1
                            character.print_info()
                            main_menu.main_menu()
                            self.shaykh_trust += 5

                            while True:
                                # Age 18: Deepening the Sufi Journey
                                if character.age == 18 and self.shaykh == "Murshid Shams al-Din Sivasi":
                                    print("\n" + Fore.RED + Style.BRIGHT + "Age 18: Deepening the Sufi Journey" + Style.RESET_ALL)
                                    print("Your dedication to the Sufi path under the guidance of Murshid Shams al-Din Sivasi continues to deepen.")
                                    print("You are now 18 years old and have experienced profound spiritual growth.")

                                    # Event 1: The Sufi Retreat
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Event 1: The Sufi Retreat" + Style.RESET_ALL)
                                    print("A transformative Sufi retreat is organized, drawing Sufis from different regions.")
                                    print("The retreat offers a rare opportunity for spiritual awakening and enlightenment.")

                                    # Decision 1: Choose to lead a meditation session or to participate actively in the retreat
                                    print("\n" + Fore.CYAN + Style.BRIGHT + "Decision 1:" + Style.RESET_ALL)
                                    print("1. Take on the responsibility of leading a meditation session during the retreat")
                                    print("2. Actively participate in the various activities and teachings of the Sufi retreat")

                                    choice1 = input(Style.BRIGHT + "Enter your choice (1/2): " + Style.RESET_ALL)

                                    if choice1 == "1":
                                        print("\nYou choose to take on the responsibility of leading a meditation session during the retreat.")
                                        print("Your guidance leads participants to profound states of inner peace and divine connection.")
                                        character.stats['diplomacy'] += random.randint(2, 5)
                                    elif choice1 == "2":
                                        print("\nYou decide to actively participate in the various activities and teachings of the Sufi retreat.")
                                        print("The retreat deepens your understanding of Sufism and strengthens your spiritual bond with fellow Sufis.")
                                        character.stats['diplomacy'] += random.randint(2, 5)

                                    # Event 2: The Sufi Poetry and Music
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Event 2: The Sufi Poetry and Music" + Style.RESET_ALL)
                                    print("The exploration of Sufi poetry and music becomes a central theme in your Sufi journey.")
                                    print("You discover how these artistic expressions serve as pathways to divine love and mysticism.")

                                    # Decision 2: Choose to focus on composing Sufi poetry or to master Sufi music
                                    print("\n" + Fore.CYAN + Style.BRIGHT + "Decision 2:" + Style.RESET_ALL)
                                    print("1. Channel your creativity into composing Sufi poetry")
                                    print("2. Dedicate yourself to mastering the art of Sufi music")

                                    choice2 = input(Style.BRIGHT + "Enter your choice (1/2): " + Style.RESET_ALL)

                                    if choice2 == "1":
                                        print("\nYou choose to channel your creativity into composing Sufi poetry, expressing divine love through verses.")
                                        print("Your poetry resonates deeply with fellow Sufis and becomes a source of inspiration.")
                                        character.stats['looks'] += random.randint(2, 5)
                                    elif choice2 == "2":
                                        print("\nYou decide to dedicate yourself to mastering the art of Sufi music, creating soul-stirring melodies.")
                                        print("Your musical talents bring a profound sense of ecstasy to Sufi gatherings.")
                                        character.stats['intrigue'] += random.randint(2, 5)

                                    # Event 3: The Sufi's Pilgrimage
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Event 3: The Sufi's Pilgrimage" + Style.RESET_ALL)
                                    print("You receive a call from within to embark on a Sufi pilgrimage to a sacred destination.")
                                    print("This journey is not only a physical one but a symbolic reflection of your inner spiritual quest.")

                                    # Decision 3: Choose to undertake the pilgrimage alone or to invite fellow Sufis to join you
                                    print("\n" + Fore.CYAN + Style.BRIGHT + "Decision 3:" + Style.RESET_ALL)
                                    print("1. Undertake the Sufi pilgrimage alone, seeking solitude and spiritual solitude")
                                    print("2. Invite fellow Sufis to join you on this sacred pilgrimage")

                                    choice3 = input(Style.BRIGHT + "Enter your choice (1/2): " + Style.RESET_ALL)

                                    if choice3 == "1":
                                        print("\nYou choose to undertake the Sufi pilgrimage alone, seeking solitude and spiritual solitude.")
                                        print("The journey takes you deep into contemplation and self-discovery.")
                                        character.stats['intrigue'] += random.randint(2, 5)
                                    elif choice3 == "2":
                                        print("\nYou decide to invite fellow Sufis to join you on this sacred pilgrimage.")
                                        print("The collective journey strengthens the bonds of brotherhood among Sufis.")
                                        character.stats['diplomacy'] += random.randint(2, 5)
                                    else:
                                        continue
                                    break
        
                            character.age += 1
                            character.print_info()
                            main_menu.main_menu()
                            self.shaykh_trust += 5

                            while True:
                            # Age 19: Deepening the Sufi Connection
                                if character.age == 19 and self.shaykh == "Murshid Shams al-Din Sivasi":
                                    print("\n" + Fore.RED + Style.BRIGHT + "Age 19: Deepening the Sufi Connection" + Style.RESET_ALL)
                                    print("You are now 19 years old, and your journey on the Sufi path under the guidance of Murshid Shams al-Din Sivasi continues to evolve.")
                                    print("The bond between you and your Murshid deepens with each passing day.")

                                    # Event 1: The Sufi Retreat
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Sufi Retreat" + Style.RESET_ALL)
                                    print("Your Sufi group organizes a retreat in a tranquil natural setting, away from the bustling city.")
                                    print("The retreat is a time for reflection, meditation, and deepening your connection with the divine.")

                                    # Event 2: The Whirling Dervishes
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Whirling Dervishes" + Style.RESET_ALL)
                                    print("You are introduced to the mesmerizing practice of the Whirling Dervishes.")
                                    print("The spinning dance becomes a part of your spiritual routine, helping you attain a state of ecstasy and spiritual awakening.")

                                    # Event 3: The Teachings of Murshid Shams al-Din Sivasi
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Teachings of Murshid Shams al-Din Sivasi" + Style.RESET_ALL)
                                    print("Your Murshid imparts profound wisdom and insights into the mystical aspects of Sufism.")
                                    print("His teachings revolve around love, unity, and the oneness of the divine.")

                                    # Choices
                                    print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                    print("1. Immerse yourself in the Sufi retreat experience")
                                    print("2. Embrace the practice of the Whirling Dervishes")
                                    print("3. Dive deeper into the teachings of Murshid Shams al-Din Sivasi")

                                    choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                    if choice == "1":
                                        print("\nYou fully immerse yourself in the Sufi retreat experience, finding profound moments of inner peace.")
                                        print("The retreat deepens your spiritual connection and brings you closer to the divine.")
                                        character.stats['smart'] += random.randint(2, 5)
                                    elif choice == "2":
                                        print("\nYou embrace the practice of the Whirling Dervishes, finding a unique form of spiritual expression.")
                                        print("The spinning dance leads you to states of ecstasy and spiritual awakening.")
                                        character.stats['smart'] += random.randint(2, 5)
                                    elif choice == "3":
                                        print("\nYou choose to dive deeper into the teachings of Murshid Shams al-Din Sivasi, absorbing his wisdom.")
                                        print("His teachings about love, unity, and the oneness of the divine resonate deeply with you.")
                                        character.stats['smart'] += random.randint(2, 5)
                                    else:
                                        continue
                                    break
        
                            character.age += 1
                            character.print_info()
                            main_menu.main_menu()
                            self.shaykh_trust += 5

                            while True:
                                # Age 20: Embracing the Sufi Path
                                if character.age == 20 and self.shaykh == "Murshid Shams al-Din Sivasi":
                                    print("\n" + Fore.RED + Style.BRIGHT + "Age 20: Embracing the Sufi Path" + Style.RESET_ALL)
                                    print("At the age of 20, you have completed your training as a Sufi under the guidance of Murshid Shams al-Din Sivasi.")
                                    print("Now, it is time for you to officially embrace the Sufi path and contribute to the spiritual community.")

                                    # Event 1: The Sufi Gathering
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Sufi Gathering" + Style.RESET_ALL)
                                    print("Sufis from various regions gather for a spiritual event, seeking to connect with the divine and share their insights.")
                                    print("You are invited to participate in this sacred gathering, representing your Sufi lineage.")

                                    # Event 2: Leading Dhikr and Meditation
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Leading Dhikr and Meditation" + Style.RESET_ALL)
                                    print("You are entrusted with the responsibility of leading a Dhikr session and meditation for fellow Sufis.")
                                    print("This is a significant moment as you guide others on their spiritual journey.")

                                    # Event 3: Guidance for Seekers
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Guidance for Seekers" + Style.RESET_ALL)
                                    print("People from the community, drawn by your reputation as a Sufi, seek your guidance.")
                                    print("You offer counsel, share Sufi wisdom, and help individuals on their path toward spiritual enlightenment.")

                                    # Choices
                                    print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                    print("1. Embrace the Sufi Gathering and connect with fellow Sufis")
                                    print("2. Lead the Dhikr and meditation session with devotion")
                                    print("3. Offer guidance and support to seekers on their spiritual journey")

                                    choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                    if choice == "1":
                                        print("\nYou fully embrace the Sufi gathering, connecting deeply with fellow Sufis from various regions.")
                                        print("The shared spiritual experience reaffirms your commitment to the Sufi path.")
                                        character.stats['smart'] += random.randint(2, 5)
                                    elif choice == "2":
                                        print("\nYou lead the Dhikr and meditation session with unwavering devotion, guiding others toward inner peace.")
                                        print("Your ability to inspire others through your leadership is evident.")
                                        character.stats['martial'] += random.randint(2, 5)
                                    elif choice == "3":
                                        print("\nYou offer guidance and support to seekers, sharing Sufi wisdom and helping them on their spiritual journey.")
                                        print("Your role as a spiritual guide becomes more prominent within the community.")
                                        character.stats['smart'] += random.randint(2, 5)
                                    else:
                                        continue
                                    character.prestige += 100
                                    # Congratulations
                                    print("\n" + Fore.YELLOW + Style.BRIGHT + "Congratulations!" + Style.RESET_ALL)
                                    print(f"You have officially embraced the Sufi path and become a respected Sufi within the community.")
                                    print(f"Your journey of spiritual growth and enlightenment continues as you inspire others to follow the path of Sufism.")
                                    print(f"{self.shaykh}, your beloved Murshid, congratulates you on this significant milestone, and your heart is filled with gratitude.")
                                    break


                                    
################################################################################################

                                elif choice_shaykh == "2":
                                    self.shaykh = "Shaykh Akshamsaddin"
                                    print("\nYou are drawn to the enigmatic figure of Shaykh Akshamsaddin, known for his profound spiritual experiences and deep connection to the divine. His reputation as a Gwath and his mystic aura make him an intriguing choice for your spiritual path.")
                                    print("You seek out Shaykh Akshamsaddin in Istanbul, and after a long and profound conversation, he agrees to accept you as his student. Your journey into the depths of Sufi mysticism begins under the tutelage of this spiritual giant.")

                                    # Create an event to earn trust from Shaykh Akshamsaddin
                                    print(Style.BRIGHT + Fore.RED + "\nAge 14: " + Fore.YELLOW + " Earning Trust with Shaykh Akshamsaddin" + Style.RESET_ALL)
                                    print(Style.BRIGHT + "Under Shaykh Akshamsaddin's guidance, you are introduced to the mystical aspects of Sufism. His teachings emphasize the inner journey and connection to the divine." + Style.RESET_ALL)
                                    
                                    # Create two options to earn trust, one with more trust than the other
                                    print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                    print(Fore.RED + Style.BRIGHT + "1." + Style.RESET_ALL + Style.BRIGHT +" Immerse yourself in deep meditation and spiritual practices")
                                    print(Fore.RED + Style.BRIGHT +"2." + Style.RESET_ALL + Style.BRIGHT + " Engage in profound philosophical discussions with the Shaykh")

                                    trust_choice = input(Style.BRIGHT + "Choose how you will earn Shaykh Akshamsaddin's trust (1/2): ")

                                    if trust_choice == "1":
                                        print("\nYou choose to immerse yourself in deep meditation and spiritual practices as per Shaykh Akshamsaddin's guidance. Your dedication to the inner journey impresses him, and he begins to share profound spiritual insights with you. Your trust with the Shaykh grows significantly.")
                                        self.shaykh_trust += 5
                                        break
                                    elif trust_choice == "2":
                                        print("\nYou engage in profound philosophical discussions with Shaykh Akshamsaddin, exploring the depths of Sufi philosophy and mysticism. Your keen intellect and curiosity earn his respect. Your trust with the Shaykh increases.")
                                        self.shaykh_trust += 3
                                        break
    
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()   
                        while True:
                            if character.age == 15 and self.shaykh == "Shaykh Akshamsaddin":
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 15: The Path of Illumination" + Style.RESET_ALL)
                                print(f"You are now 15 years old and have spent several years learning Sufism")
                                print("Your mystical journey guided by faith and spirituality continues to lead you toward illumination.")

                                # Event 1: The Sufi Meditation Retreat
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Sufi Meditation Retreat" + Style.RESET_ALL)
                                print("The Sufi group embarks on a deep meditation retreat in a serene natural setting.")
                                print("During this retreat, you experience moments of profound inner peace and divine connection.")

                                # Event 2: The Sufi Poetry and Philosophy
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Sufi Poetry and Philosophy" + Style.RESET_ALL)
                                print("You delve into the world of Sufi poetry and philosophy, exploring the writings of renowned Sufi mystics.")
                                print("The poetic verses and profound teachings resonate with your soul, leading to spiritual insights.")

                                # Event 3: The Call to Service
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Call to Service" + Style.RESET_ALL)
                                print("Your mentor conveys a message: it is time to apply your spiritual wisdom in service to others.")
                                print("You embark on a journey to help those in need, demonstrating the compassion and love you have cultivated.")

                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Embrace the Tranquility of the Meditation Retreat")
                                print("2. Dive Deeper into Sufi Poetry and Philosophy")
                                print("3. Answer the Call to Service")

                                choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                if choice == "1":
                                    print("\nYou fully embrace the tranquility of the meditation retreat, experiencing moments of profound inner peace.")
                                    print("The retreat deepens your spiritual connection and brings you closer to the illumination you seek.")
                                    character.stats['smart'] += random.randint(2, 5)
                                    self.shaykh_trust += 4
                                elif choice == "2":
                                    print("\nYou immerse yourself in the world of Sufi poetry and philosophy, finding profound meaning in the verses and teachings.")
                                    print("Your understanding of the mystical aspects of Sufism continues to expand.")
                                    character.stats['smart'] += random.randint(2, 5)
                                    self.shaykh_trust += 3
                                elif choice == "3":
                                    print("\nYou answer the call to service, dedicating yourself to helping those in need with compassion and love.")
                                    print("Through your acts of service, you shine as a beacon of light and inspiration to others.")
                                    character.stats['martial'] += random.randint(2, 5)
                                    self.shaykh_trust += 5
                                else:
                                    continue
                                break
    
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()  
                        while True:
                            if character.age == 16 and self.shaykh == "Shaykh Akshamsaddin":
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 16: The Inner Journey Continues" + Style.RESET_ALL)
                                print(f"You are now 16 years old and have been dedicated to the Sufi path for a significant part of your life.")
                                print("Your journey towards inner illumination and spiritual growth continues with unwavering determination.")

                                # Event 1: The Night of Visions
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Night of Visions" + Style.RESET_ALL)
                                print("One night, as you engage in deep meditation, you experience a series of vivid and meaningful visions.")
                                print("These visions offer insights into your own spiritual journey and the interconnectedness of all beings.")

                                # Event 2: Guiding Fellow Seekers
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Guiding Fellow Seekers" + Style.RESET_ALL)
                                print("You are approached by other Sufi students who seek your guidance and wisdom.")
                                print("You find yourself taking on the role of a mentor, helping others navigate the path of Sufism.")

                                # Event 3: The Test of Faith
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Test of Faith" + Style.RESET_ALL)
                                print("You face a challenging situation that tests your faith and commitment to the Sufi path.")
                                print("Through unwavering belief and inner strength, you overcome this test and emerge stronger in your faith.")

                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Reflect on the Meaning of the Night of Visions")
                                print("2. Embrace the Role of a Mentor to Fellow Seekers")
                                print("3. Share Your Experience of the Test of Faith")

                                choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                if choice == "1":
                                    print("\nYou choose to reflect deeply on the meaning of the Night of Visions, seeking further understanding.")
                                    print("These insights lead you to profound spiritual realizations and a deeper connection to the divine.")
                                    self.shaykh_trust += 3
                                    character.stats['smart'] += random.randint(2, 5)
                                elif choice == "2":
                                    print("\nYou wholeheartedly embrace the role of a mentor to your fellow seekers, guiding them on their own spiritual journeys.")
                                    print("Through teaching and sharing, you find fulfillment in nurturing the spiritual growth of others.")
                                    self.shaykh_trust += 5
                                    character.stats['diplomacy'] += random.randint(2, 5)
                                elif choice == "3":
                                    print("\nYou decide to share your experience of the Test of Faith with your Sufi community.")
                                    print("Your story inspires others and strengthens the collective faith of your Sufi brothers and sisters.")
                                    self.shaykh_trust += 4
                                    character.stats['smart'] += random.randint(2, 5)
                                else:
                                    continue
                                break
    
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()
                        while True:
                            if character.age == 17 and self.shaykh == "Shaykh Akshamsaddin":
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 17: The Quest for Unity" + Style.RESET_ALL)
                                print(f"You have now reached the age of 17 and continue your devoted journey along the Sufi path.")
                                print("Your pursuit of unity with the divine intensifies as you seek to transcend the worldly realm.")

                                # Event 1: The Sufi Retreat in Nature
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Sufi Retreat in Nature" + Style.RESET_ALL)
                                print("You embark on a profound retreat in the heart of nature with your Sufi companions.")
                                print("Surrounded by the beauty of the natural world, you delve deep into meditation and contemplation.")

                                # Event 2: The Revelation of Unity
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Revelation of Unity" + Style.RESET_ALL)
                                print("During your retreat, you experience a profound revelation of unity with the divine.")
                                print("You feel a sense of oneness with all creation, transcending the boundaries of the material world.")

                                # Event 3: The Call to Teach
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Call to Teach" + Style.RESET_ALL)
                                print("You receive a calling from your Shaykh to take on a new role as a teacher and spiritual guide.")
                                print("This responsibility involves sharing the wisdom of Sufism with others and leading by example.")

                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Contemplate the Revelation of Unity")
                                print("2. Embrace the Role of a Teacher and Guide")
                                print("3. Answer the Call to Teach and Share Your Revelation")

                                choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                if choice == "1":
                                    print("\nYou choose to contemplate the revelation of unity, deepening your understanding of oneness with the divine.")
                                    print("This profound experience continues to influence your spiritual journey and quest for unity.")
                                    self.shaykh_trust += 3
                                    character.stats['diplomacy'] += random.randint(2, 5)
                                elif choice == "2":
                                    print("\nYou wholeheartedly embrace the role of a teacher and guide, accepting the responsibility bestowed upon you by your Shaykh.")
                                    print("Your teachings and guidance help others along their own paths of spiritual illumination.")
                                    self.shaykh_trust += 5
                                    character.stats['smart'] += random.randint(2, 5)
                                elif choice == "3":
                                    print("\nYou answer the call to teach and share your revelation of unity with others.")
                                    print("Your teachings inspire a sense of unity and divine connection among your students and Sufi community.")
                                    self.shaykh_trust += 4
                                    character.stats['diplomacy'] += random.randint(2, 5)
                                else:
                                    continue
                                break
    
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()
                        while True:
                            # Age 18: Deepening Your Connection with Shaykh Akshamsaddin
                            if character.age == 18 and self.shaykh == "Shaykh Akshamsaddin":
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 18: Deepening Your Connection with Shaykh Akshamsaddin" + Style.RESET_ALL)
                                print("Over the years, your journey with Shaykh Akshamsaddin has been transformative. The bond between you and your Shaykh has grown stronger, and your understanding of Sufism has deepened.")

                                # Event: Profound Spiritual Discussion
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Profound Spiritual Discussion" + Style.RESET_ALL)
                                print("One evening, Shaykh Akshamsaddin invites you for a special spiritual discussion.")
                                print("You engage in a profound conversation about the mysteries of the soul, divine love, and the oneness of existence.")

                                # Event: An Inner Journey
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: An Inner Journey" + Style.RESET_ALL)
                                print("Under Shaykh Akshamsaddin's guidance, you embark on a deep inner journey through meditation and contemplation.")
                                print("You experience moments of spiritual ecstasy and a sense of closeness to the Divine that words cannot express.")

                                # Event: Serving the Sufi Community
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Serving the Sufi Community" + Style.RESET_ALL)
                                print("Shaykh Akshamsaddin encourages you to actively serve the Sufi community and spread the message of love and spirituality.")
                                print("You begin to assist in organizing Sufi gatherings and events, sharing the teachings of Sufism with others.")

                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Continue deepening your understanding through spiritual discussions")
                                print("2. Dedicate more time to inner meditation and contemplation")
                                print("3. Focus on serving the Sufi community by organizing events")

                                choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                if choice == "1":
                                    print("\nYou choose to continue deepening your understanding through spiritual discussions with Shaykh Akshamsaddin.")
                                    print("The wisdom and insights you gain from these discussions are invaluable.")
                                    character.stats['smart'] += random.randint(2, 5)
                                elif choice == "2":
                                    print("\nYou decide to dedicate more time to inner meditation and contemplation, seeking a deeper connection with the Divine.")
                                    print("These moments of spiritual contemplation become the foundation of your spiritual journey.")
                                    character.stats['smart'] += random.randint(2, 5)
                                elif choice == "3":
                                    print("\nYou focus on serving the Sufi community by actively organizing Sufi gatherings and events.")
                                    print("Your efforts help spread the message of Sufism and love to a wider audience.")
                                    character.stats['diplomacy'] += random.randint(2, 5)
                                else:
                                    continue
                                break
    
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()
                        self.shaykh_trust += 5
                        while True:
                            # Age 19: The Essence of Sufism
                            if character.age == 19 and self.shaykh == "Shaykh Akshamsaddin":
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 19: The Essence of Sufism" + Style.RESET_ALL)
                                print("Your journey with Shaykh Akshamsaddin has taken you to new heights of spiritual understanding. Sufism's essence unfolds before you, revealing the secrets of the heart and the divine connection.")

                                # Event: The Heart's Longing
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: The Heart's Longing" + Style.RESET_ALL)
                                print("You find yourself overwhelmed by a deep longing for the Divine, a yearning that stirs your soul.")
                                print("Shaykh Akshamsaddin guides you on the path of divine love, teaching you how to embrace and channel this longing.")

                                # Event: Mystical Experiences
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Mystical Experiences" + Style.RESET_ALL)
                                print("Your spiritual practices lead you to mystical experiences, where you witness the unity of all existence.")
                                print("These moments of divine revelation and ecstasy leave an indelible mark on your soul.")

                                # Event: Becoming a Guide
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event: Becoming a Guide" + Style.RESET_ALL)
                                print("Shaykh Akshamsaddin recognizes your deep spiritual insight and encourages you to guide others on their Sufi journey.")
                                print("You begin mentoring younger Sufis, sharing your wisdom and experiences.")

                                # Choices
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Choices:" + Style.RESET_ALL)
                                print("1. Embrace the longing for the Divine and delve deeper into the mysteries of love")
                                print("2. Continue exploring mystical experiences and revelations")
                                print("3. Dedicate yourself to mentoring and guiding other Sufis")

                                choice = input(Style.BRIGHT + "Enter your choice (1/2/3): " + Style.RESET_ALL)

                                if choice == "1":
                                    print("\nYou choose to embrace the longing for the Divine and delve deeper into the mysteries of love.")
                                    print("Your heart becomes a vessel of divine love, and your spiritual journey is marked by profound devotion.")
                                    character.stats['diplomacy'] += random.randint(2, 5)
                                elif choice == "2":
                                    print("\nYou decide to continue exploring mystical experiences and revelations, seeking to unravel the secrets of existence.")
                                    print("Your path is illuminated by the light of divine knowledge and mystical insights.")
                                    character.stats['smart'] += random.randint(2, 5)
                                elif choice == "3":
                                    print("\nYou dedicate yourself to mentoring and guiding other Sufis on their spiritual journey.")
                                    print("Your role as a guide and mentor becomes a source of spiritual fulfillment and service to the Sufi community.")
                                    character.stats['intrigue'] += random.randint(2, 5)
                                else:
                                    continue
                                character.prestige += 100
                                break
    
                        character.age += 1
                        character.print_info()
                        main_menu.main_menu()
                        self.shaykh_trust += 5
                        while True:
                        # Age 21: Embracing Sufi Mastery
                            if character.age == 20 and self.shaykh == "Shaykh Akshamsaddin":
                                print("\n" + Fore.RED + Style.BRIGHT + "Age 20: Embracing Sufi Mastery" + Style.RESET_ALL)
                                print("Having spent years under the guidance of Shaykh Akshamsaddin, you have become a dedicated and enlightened Sufi.")
                                print("You stand at the threshold of your spiritual journey, ready to share the wisdom you have acquired or to embark on new adventures as a Sufi.")

                                # Event 1: The Call to Serve
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event 1: The Call to Serve" + Style.RESET_ALL)
                                print("Shaykh Akshamsaddin recognizes your spiritual growth and calls upon you to serve the Sufi community.")
                                print("You are faced with a choice: to become a Sufi teacher and guide others on their path or to embark on a personal journey of spiritual exploration.")

                                # Decision 1: Choose to become a Sufi teacher
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Decision 1:" + Style.RESET_ALL)
                                print("1. Accept the role of a Sufi teacher and share your knowledge")
                                print("2. Embark on a personal spiritual journey of exploration")

                                choice1 = input(Style.BRIGHT + "Enter your choice (1/2): " + Style.RESET_ALL)

                                if choice1 == "1":
                                    print("\nYou wholeheartedly accept the role of a Sufi teacher, embracing the responsibility to guide others.")
                                    print("Your wisdom and spiritual depth will now benefit those who seek enlightenment.")
                                    character.stats['smart'] += random.randint(2, 5)
                                elif choice1 == "2":
                                    print("\nYou decide to embark on a personal spiritual journey of exploration, seeking new depths of Sufi wisdom.")
                                    print("The path ahead is unknown, but you are eager to uncover the hidden truths of the Sufi mysticism.")
                                    character.stats['smart'] += random.randint(2, 5)

                                # Event 2: A Farewell Gathering
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event 2: A Farewell Gathering" + Style.RESET_ALL)
                                print("As you contemplate your decision, Shaykh Akshamsaddin organizes a farewell gathering in your honor.")
                                print("Sufi brothers and sisters gather to celebrate your journey and seek your blessings for their own paths.")

                                # Decision 2: Choose to give a final discourse or not
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Decision 2:" + Style.RESET_ALL)
                                print("1. Deliver a final discourse, imparting your wisdom and blessings")
                                print("2. Participate in the gathering as a humble observer")

                                choice2 = input(Style.BRIGHT + "Enter your choice (1/2): " + Style.RESET_ALL)

                                if choice2 == "1":
                                    print("\nYou decide to deliver a final discourse, sharing your wisdom and blessings with the Sufi community.")
                                    print("Your words resonate deeply with those present, and your blessings are received with gratitude.")
                                    character.stats['smart'] += random.randint(2, 5)
                                elif choice2 == "2":
                                    print("\nYou choose to participate in the gathering as a humble observer, allowing others to share their experiences.")
                                    print("Your presence is a source of inspiration for those who have walked alongside you on this Sufi journey.")
                                    character.stats['smart'] += random.randint(2, 5)

                                # Event 3: The Path Ahead
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Event 3: The Path Ahead" + Style.RESET_ALL)
                                print("With the gathering concluding, you stand at a crossroads, ready to embrace the path ahead.")
                                print("Whether as a Sufi teacher or as a solitary seeker, your journey continues with a heart full of devotion.")

                                # Decision 3: Choose to continue as a teacher or seeker
                                print("\n" + Fore.CYAN + Style.BRIGHT + "Decision 3:" + Style.RESET_ALL)
                                print("1. Continue your role as a Sufi teacher and guide")
                                print("2. Embark on a solitary spiritual journey of deeper discovery")

                                choice3 = input(Style.BRIGHT + "Enter your choice (1/2): " + Style.RESET_ALL)

                                if choice3 == "1":
                                    print("\nYou embrace your role as a Sufi teacher, committed to guiding others on their spiritual journeys.")
                                    print("Your path is clear as you illuminate the way for those seeking the light of Sufism.")
                                    character.stats['diplomacy'] += random.randint(2, 5)
                                elif choice3 == "2":
                                    print("\nYou choose to embark on a solitary spiritual journey, driven by the thirst for deeper spiritual discovery.")
                                    print("The mystic path unfolds before you, and you step into the realm of profound self-realization.")
                                    character.stats['smart'] += random.randint(2, 5)
                                else:
                                    continue
                                print("\n" + Fore.YELLOW + Style.BRIGHT + "Congratulations!" + Style.RESET_ALL)
                                print(f"You have officially embraced the Sufi path and become a respected Sufi within the community.")
                                print(f"Your journey of spiritual growth and enlightenment continues as you inspire others to follow the path of Sufism.")
                                print(f"{self.shaykh}, your beloved Murshid, congratulates you on this significant milestone, and your heart is filled with gratitude.")

                                   # End the game
                                print("\n" + Fore.GREEN + Style.BRIGHT + "End of the Sufi Journey" + Style.RESET_ALL)
                                print("Your Sufi journey has come to its culmination, and you have embraced a life of spiritual depth and devotion.")
                                print("Thank you for embarking on this profound journey!")
                    



####################################################################
                    else:
                        continue
                    break
            else:
                continue
                


        
#Implementing Madrassah System
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
        self.has_executed = False

        # Fighting attributes choose a new career path
        self.brawl_attacks = [
            {"name": "Lick", "description": "Lick the opponent's face, to show you really are mental.", "damage": 1},
            {"name": "Punch", "description": "A straightforward punch to the opponent's face.", "damage": 5},
            {"name": "Kick", "description": "A powerful kick aimed at the opponent's legs.", "damage": 7},
            {"name": "Slap", "description": "A quick and humiliating slap across the opponent's cheek.", "damage": 3},
            {"name": "Trip", "description": "Swiftly sweep the opponent's legs, causing them to stumble and fall.", "damage": 1},
            {"name":"Trash Talk","description":"Engage in verbal taunts and insults to demoralize the opponent.", "damage": 1},
            {"name": "Sucker Punch", "description": "Deliver a quick and unexpected punch to catch the opponent off guard.", "damage": 5},
            {"name": "Low Blow", "description": "A swift kick aimed at the opponent's groin, causing discomfort.", "damage": 2},
            {"name": "Spit", "description": "Spit in the opponent's face, humiliating and enraging them.", "damage": 1},
            {"name": "Shoulder Check", "description": "Ram into the opponent with your shoulder, pushing them back.", "damage": 2},
            {"name": "Headbutt", "description": "Perform a headbutt to stun the opponent momentarily.", "damage": 3},
            {"name": "Distracting Dance", "description": "Bust out a comical dance to confuse and distract the opponent.", "damage": 1},
            {"name": "Thumb War", "description": "Engage in a thumb war to test the opponent's thumb strength.", "damage": 1},
            {"name": "Face Palm", "description": "Slap your hand on the opponent's face in disbelief, causing minimal damage.", "damage": 1}
        ]

        self.female_names = [
            "Ayşe Hanim", "Fatma Sultan", "Emine Hatun", "Hatice Kizi", "Sultan Begüm",
            "Zeynep Hanim", "Nurbanu Sultan", "Mihrimah Sultan", "Esma Hatun", "Gülbahar Hatun",
            "Safiye Sultan", "Hafsa Sultan", "Raziye Hatun", "Dilşad Hatun", "Aslihan Hanim",
            "Melek Hatun", "Mahpeyker Sultan", "Nakşidil Sultan", "Esin Hatun", "Şehzade Kizi",
            "Şahika Sultan", "Cemile Hatun", "Nazli Hanim", "Perihan Hatun", "Fahriye Hatun",
            "Selma Sultan", "Şehvar Hatun", "Aygül Hanim", "Saadet Hatun", "Cevriye Hatun",
            "Ferah Hatun", "Neslihan Hanim", "Şükriye Hatun", "Melike Sultan", "Hatice Sultan",
            "Gülizar Hatun", "Mehtap Hatun", "Şahsenem Sultan", "İlhan Hatun", "Esengül Hatun",
            "Feryal Hatun", "Nilgün Hatun", "Müberra Hatun", "Serap Sultan", "Nebahat Hatun",
            "Sevim Hatun", "Zekiye Hanim", "Gönül Hatun", "Ebru Hatun", "Figen Hatun"
        ]

        # Create a dictionary to store both male and female names
        self.turkish_names_dict = {
            "male_names": self.male_names,
            "female_names": self.female_names
        }
        self.groups = {
            "Talib al-Ilm": [],
            "Hafiz-e-Quran": [],
            "Süfi Müritler": []
        }
        self.assign_npcs_to_groups()

    def randomize_names(self):
        random.shuffle(self.male_names)

    def generate_npcs(self):
        self.randomize_names()
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
        character = Character
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
                # Checking if the NPC has already been complimented
                if npc["name"] not in self.complimented_npcs:
                    compliment = self.choose_compliment(npc_name=npc["name"])
                    print(compliment)
                    npc["relationship"] += 5
                    self.complimented_npcs.append(npc["name"]) 
                else:
                    print(f"You have already complimented {npc['name']}.")

            elif choice == '2':
                conversation = self.choose_conversation()
                print(conversation)
                npc["relationship"] += 3
            elif choice == '3':
                # Checking if the NPC is already a friend
                if npc["name"] not in self.friends and npc["name"] not in self.insulted_npcs:
                    insult = self.choose_insult(npc_name=npc["name"])
                    print(insult)
                    npc["relationship"] -= 5
                else:
                    print(f"You cannot insult {npc['name']} until you are friend with them.")
                

            elif choice == '4':
                # Implemented brawl logic and updated the relationship
                if npc["name"] not in self.friends:
                    brawl = self.choose_brawl()
                    print(brawl)
                    self.handle_brawl(character)
                    npc["relationship"] -= 10
                else:
                    print(print(f"You cannot brawl with {npc['name']} until you are friend with them."))
            elif choice == '5':
                # Checking if the NPC meets the friendship requirement
                if npc["relationship"] >= 80:
                    if npc["name"] not in self.friends:
                        befriend = self.choose_befriend(npc_name=npc["name"])
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

    def handle_brawl(self, character):
        print(f"\nYou are in a brawl with a fellow.")

        # Displaying brawl attack options
        print("Choose your attack:")
        for i, attack in enumerate(self.brawl_attacks, start=1):
            print(f"{i}. {attack['name']} - {attack['description']}")

        choice = int(input("Enter the number of your chosen attack: "))
        choice -= 1  # Subtract 1 to match list indexing
        player_attack = self.brawl_attacks[choice]

        # Randomly selecting opponent's attack
        opponent_attack = random.choice(self.brawl_attacks)

        # Calculating damage
        player_damage = player_attack["damage"]
        opponent_damage = opponent_attack["damage"]

        print(f"\nYou used {player_attack['name']} and dealt {player_damage} damage.")
        print(f"Your Opponent used {opponent_attack['name']} and dealt {opponent_damage} damage.")

        if player_damage > opponent_damage:
            print(f"You landed a powerful hit on your enemy and won the brawl!")
        else:
            print(f"Your opponent landed a strong blow on you, and you lost the brawl.")
    def main_menu(self,character):
        while True:
            print("\nMadrassah:")
            print("1. View Fellow Students")
            print("2. List of Friends")
            print("3. Interact with Fellow Students")
            print("4. Groups")
            print("5. Aged up")

            main_choice = input("Choose an option (1-5): ")

            if main_choice == '1':
                self.display_relationship_table()
            elif main_choice == '2':
                self.display_friends_list()
            elif main_choice == '3':
                self.display_relationship_table()
                try:
                    npc_number = int(input("Enter the number of the Student you want to interact with (1-10): "))
                    if 1 <= npc_number <= 10:
                        self.interact_with_npc(npc_number - 1)  # Subtract 1 to match list indexing
                    else:
                        print("Invalid NPC number. Please enter a number between 1 and 10.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif main_choice == '4':
                self.manage_groups()  # Call the method to manage groups
            elif main_choice == '5':
                print("You decided to rest for now.")
                break
            else:
                print("Invalid choice. Please select a valid option (1-5).")
                continue

    def manage_groups(self):
        while True:
            print("\nGroups Menu:")
            print("1. View Groups and Members")
            print("2. Back to Main Menu")

            groups_choice = input("Choose an option (1-3): ")

            if groups_choice == '1':
                self.view_groups_and_members()
                  # Call the method to display groups and members
            elif groups_choice == '2':
                break
            else:
                print("Invalid choice. Please select a valid option (1-3).")


    def view_groups_and_members(self):
        data = []
        for group_num, group_info in enumerate(self.groups, start=1):
            group_name = group_info
            members = ', '.join(self.groups[group_info])
            data.append([group_num, group_name, members])

        headers = ["Group", "Group Name", "Members"]
        table = tabulate(data, headers=headers, tablefmt="grid")
        print("\nGroups and Members:")
        print(table)


    def assign_npcs_to_groups(self):
        if not self.has_executed:
            # Shuffle the list of male names to randomize group assignments
            random.shuffle(self.male_names)

            for group_name in self.groups.keys():
                if len(self.groups[group_name]) < 3:
                    while len(self.groups[group_name]) < 3:
                        if len(self.male_names) > 0:
                            npc_name = self.male_names.pop()
                            self.groups[group_name].append(npc_name)
                        else:
                            break  # No more NPCs to assign
                    if len(self.male_names) == 0:
                        self.has_executed = True
                        break

    #Some more functions
    def join_group_talib(self):
        print("You Joined Tali al-Ilm")
        self.groups["Talib al-Ilm"].append("Player")
    def join_group_hafiz(self):
        print("You Joined Hafiz-e-Quran")
        self.groups["Hafiz-e-Quran"].append("Player")
    def join_group_sufi(self):
        print("You Joined Süfi Müritler")
        self.groups["Süfi Müritler"].append("Player")


        

class Player:
    def __init__(self,num_npcs = 10):
        madrassah = Madrassah()
        character = Character()
        self.male = madrassah.male_names
        self.female = madrassah.female_names
        self.compliment = madrassah.choose_compliment
        self.insult = madrassah.choose_insult
        self.conversation = madrassah.choose_conversation
        self.befriend = madrassah.choose_befriend
        self.names = {
            "male_names": self.male,
            "female_names": self.female
        }
        self.attacks = madrassah.brawl_attacks
        self.friends = madrassah.friends
        self.randomize_names()
        self.complimented_npcs = []
        self.insulted_npcs =[]
        self.num_npcs = num_npcs
        
        self.npcs = self.generate_npcs()
        
        self.character = Character()
        
        
        self.available_gigs = {
            "Tier 3": [
                {"name": "Animal Care", "requirements": {}, "reward": 35},
                {"name": "Hunting", "requirements": {}, "reward": 35},
                {"name": "Fishing", "requirements": {}, "reward": 30},
            ],
            "Tier 2": [
                {"name": "Agricultural Labor", "requirements": {}, "reward": 20},
            ],
            "Tier 1": [
                {"name": "Babysitting", "requirements": {}, "reward": 15},
            ],
        }
        self.completed_gigs = []

        self.items = [
            {"name": "Humble Ottoman Abode", "type": "House", "price":25, "prestige_effect": 5},
            {"name": "Traditional Ottoman House", "type": "House", "price":50, "prestige_effect": 10},
            {"name": "Grand Ottoman Residence", "type": "House", "price":75, "prestige_effect": 15},
            {"name": "Noble Ottoman Villa", "type": "House", "price":125, "prestige_effect": 25},
            {"name": "Royal Ottoman Mansion", "type": "House", "price":200, "prestige_effect": 40},
            {"name": "The Wisdom of Rumi", "type": "Book", "price":10, "attribute_effect": "wisdom"},
            {"name": "Ottoman Diplomacy Handbook", "type": "Book", "price":15, "attribute_effect": "diplomacy"},
            {"name": "The Art of Intrigue", "type": "Book", "price":12, "attribute_effect": "intrigue"},
            {"name": "Sword of the Janissary", "type": "Armory", "price":20, "attribute_effect": "martial"},
            {"name": "Ottoman Warrior's Armor", "type": "Armory", "price":30, "attribute_effect": "martial"},
            {"name": "Jeweled Scimitar", "type": "Armory", "price":25, "attribute_effect": "martial"},
            {"name": "Sultan's Robe", "type": "Clothes", "price":15, "attribute_effect": "looks", "prestige_effect": 5},
            {"name": "Ottoman Shawl", "type": "Clothes", "price":10, "attribute_effect": "looks", "prestige_effect": 3},
            {"name": "Janissary Uniform", "type": "Clothes", "price":20, "attribute_effect": "looks", "prestige_effect": 8},
            {"name": "Baklava Delight", "type": "Food", "price":5, "attribute_effect": "health"},
            {"name": "Sultan's Feast", "type": "Food", "price":12, "attribute_effect": "health"},
            {"name": "Ottoman Spices", "type": "Food", "price":8, "attribute_effect": "health"},
        ]
        

        # Create an inventory dictionary to store player's items
        self.inventory = []

        self.hookah_conversations = [
    "As you enjoy your hookah, {npc} shares tales of the bustling Ottoman bazaar, where vibrant colors and enchanting aromas greet all who enter.",
    "The sweet scent of hookah smoke fills the air as {npc} recounts the opulent Ottoman weddings, where celebrations last for days on end.",
    "Amidst the curling smoke, {npc} speaks of the Ottoman Empire's unmatched military prowess, conquering new lands with remarkable ease.",
    "With a puff of your hookah, {npc} recommends savoring the famed Ottoman baklava, a culinary masterpiece that leaves one longing for more.",
    "The swirl of hookah smoke seems to dance as {npc} mentions the Grand Vizier's tireless efforts to enact vital reforms, strengthening the empire.",
    "With a contemplative exhale, {npc} admires the breathtaking Ottoman architecture, domes and minarets soaring high in artistic splendor.",
    "As you inhale the fragrant hookah, {npc} transports you to the Ottoman bazaar, where vibrant colors and exotic aromas create an enchanting tapestry.",
    "A cloud of smoke accompanies {npc} as they sing praises to the fearless Ottoman Janissaries, steadfast in their loyalty to the Sultan.",
    "With every puff, {npc} paints a picture of their encounter with a dervish, who whispered tales of Sufi mysticism and spiritual enlightenment.",
    "Amidst the wafting smoke, {npc} shares verses from a famous Ottoman poet, invoking emotions of love and longing that touch the soul.",
    "With a contemplative exhale, {npc} speaks of Ottoman calligraphy, where each brushstroke carries deep meaning and artistic significance.",
    "The hookah's embers glow as {npc} recalls a recent visit to an Ottoman music performance, where hauntingly beautiful melodies filled the air.",
    "Amidst the soothing haze of hookah smoke, {npc} hints at the intrigue and power struggles within the enigmatic Ottoman harem.",
    "With each inhale, {npc} underscores the pivotal role of diplomatic relations in the Ottoman Empire's enduring success.",
    "As you enjoy your hookah, {npc} imparts wisdom about Ottoman herbal medicine, known for its effective and holistic remedies.",
    "The hookah's ember flickers like the flames of history as {npc} delves into the Ottoman military campaigns in Europe, shaping destiny.",
    "In the midst of swirling smoke, {npc} encourages you to explore Ottoman carpet shops, where intricate designs and skilled craftsmanship await.",
    "With every puff, {npc} conveys the awe-inspiring strength and skill displayed by Ottoman wrestlers, a testament to their discipline.",
    "Amidst the enchanting haze of hookah, {npc} weaves captivating stories of ancient Ottoman heroes and the legends that endure.",
    "With a final contemplative exhale, {npc} reflects on the unparalleled power and authority vested in the hands of the Ottoman Sultan."
]

    def otto_conver(self, npc):
        ottoman_conversations = [
    "As you enjoy your hookah, {names} shares tales of the bustling Ottoman bazaar, where vibrant colors and enchanting aromas greet all who enter.",
    "The sweet scent of hookah smoke fills the air as {names} recounts the opulent Ottoman weddings, where celebrations last for days on end.",
    "Amidst the curling smoke, {names} speaks of the Ottoman Empire's unmatched military prowess, conquering new lands with remarkable ease.",
    "With a puff of your hookah, {names} recommends savoring the famed Ottoman baklava, a culinary masterpiece that leaves one longing for more.",
    "The swirl of hookah smoke seems to dance as {names} mentions the Grand Vizier's tireless efforts to enact vital reforms, strengthening the empire.",
    "With a contemplative exhale, {names} admires the breathtaking Ottoman architecture, domes and minarets soaring high in artistic splendor.",
    "As you inhale the fragrant hookah, {names} transports you to the Ottoman bazaar, where vibrant colors and exotic aromas create an enchanting tapestry.",
    "A cloud of smoke accompanies {names} as they sing praises to the fearless Ottoman Janissaries, steadfast in their loyalty to the Sultan.",
    "With every puff, {names} paints a picture of their encounter with a dervish, who whispered tales of Sufi mysticism and spiritual enlightenment.",
    "Amidst the wafting smoke, {names} shares verses from a famous Ottoman poet, invoking emotions of love and longing that touch the soul.",
    "With a contemplative exhale, {names} speaks of Ottoman calligraphy, where each brushstroke carries deep meaning and artistic significance.",
    "The hookah's embers glow as {names} recalls a recent visit to an Ottoman music performance, where hauntingly beautiful melodies filled the air.",
    "Amidst the soothing haze of hookah smoke, {names} hints at the intrigue and power struggles within the enigmatic Ottoman harem.",
    "With each inhale, {names} underscores the pivotal role of diplomatic relations in the Ottoman Empire's enduring success.",
    "As you enjoy your hookah, {names} imparts wisdom about Ottoman herbal medicine, known for its effective and holistic remedies.",
    "The hookah's ember flickers like the flames of history as {names} delves into the Ottoman military campaigns in Europe, shaping destiny.",
    "In the midst of swirling smoke, {names} encourages you to explore Ottoman carpet shops, where intricate designs and skilled craftsmanship await.",
    "With every puff, {names} conveys the awe-inspiring strength and skill displayed by Ottoman wrestlers, a testament to their discipline.",
    "Amidst the enchanting haze of hookah, {names} weaves captivating stories of ancient Ottoman heroes and the legends that endure.",
    "With a final contemplative exhale, {names} reflects on the unparalleled power and authority vested in the hands of the Ottoman Sultan."
]
        return random.choice(ottoman_conversations).format(names=npc["name"])
    
    def choose_brawl(self):
        brawl_lines = [
        "You square up for a fight, fists clenched.",
        "A heated argument escalates into a physical confrontation.",
        "Punches are thrown as tempers flare.",
        "The madrassah courtyard becomes a chaotic battleground.",
        "Shouting and shoving quickly turn into a brawl."
        ]
        return random.choice(brawl_lines)
    
    def randomize_names(self):
        random.shuffle(self.male)
        random.shuffle(self.female)

    def generate_npcs(self):
        npcs = [{"name": random.choice(self.names["male_names" if i % 2 == 0 else "female_names"]), "relationship": random.randint(1,100)} for i in range(self.num_npcs)]
        return npcs

    def randomize_names(self):
        random.shuffle(self.male)
        random.shuffle(self.female)

    # Function to display the Marketplace items
    def list_items(self):
        print("Welcome to the Ottoman Marketplace. What would you like to purchase?")
        headers = ["Option", "Item Name", "Type", "Price (Dinars)", "Attribute Effect", "Prestige Effect"]
        item_data = []
        for i, item in enumerate(self.items, start=1):
            item_data.append([i, item["name"], item["type"], item["price"],
                              item.get("attribute_effect", "-"), item.get("prestige_effect", "-")])
        print(tabulate(item_data, headers=headers, tablefmt="grid"))

    def purchase_item(self, item_number,character):
        if item_number < 1 or item_number > len(self.items):
            print("Invalid item number. Please select a valid item.")
            return

        selected_item = self.items[item_number - 1]
        item_name = selected_item["name"]
        item_type = selected_item["type"]
        item_price = int(selected_item["price"])

        while True:
            if character.gold < item_price:
                print(f"You don't have enough Dinars to purchase the {item_name}.")
                break
            elif item_name in self.inventory:
                print(f"You have already bought {item_name}.")
                break
            else:
                character.gold -= item_price
                if item_type == "House":
                    character.prestige += selected_item.get("prestige_effect", 0)
                elif "attribute_effect" in selected_item:
                    attribute = selected_item["attribute_effect"]
                    if attribute in character.stats:
                        character.stats[attribute] += 10 
                if "prestige_effect" in selected_item:
                    character.prestige += selected_item["prestige_effect"]
                print(f"You have purchased the {item_name} for {item_price} Dinars.")
                self.inventory.append(item_name)
                break

    def visit_marketplace(self, character):
        while True:
            self.list_items()
            print("0. Exit Marketplace")
            choice = input("Enter the number of the item you want to purchase: ")
            if choice == "0":
                break
            try:
                choice = int(choice)
                self.purchase_item(choice, character)
            except ValueError:
                print("Invalid input. Please enter a valid item number.")
        

    def view_inventory(self):
        if not self.inventory:
            print("Your inventory is empty.")
        else:
            print("Inventory:")
            for item in self.inventory:
                print(item)
    def visit_coffee_house(self,character):
        print("You find yourself in a bustling Coffee House in Ottoman Istanbul. The air is filled with the rich aroma of freshly brewed Turkish coffee.")
        print("The place is alive with animated conversations, soft strains of traditional music, and the gentle bubbling of hookahs.")
        print("What would you like to do?")
        print("1. Sip Turkish Coffee (-10 Dinars)")
        print("2. Strike up a Conversation with Patrons")
        print("3. Enjoy the Hookah (10 Dinars)")
        coffee_choice = input("Enter your choice: ")

        if coffee_choice == "1":
            character.gold -= 10
            character.stats["health"] += 2
        elif coffee_choice == "2":
            self.interact_with_npcs_in_coffee_house()
        elif coffee_choice == "3":
            print(self.hookah_conversations)

        else:
            print("Invalid choice. Please select a valid option.")

    def interact_with_npcs_in_coffee_house(self):
        print("You are in the Coffee House. Who would you like to interact with?")

        npc_table = []
        for i, npc in enumerate(self.npcs, start=1):
            npc_table.append([i, npc["name"], npc["relationship"]])

        print(tabulate(npc_table, headers=["Number", "Name","Opinion"], tablefmt="grid"))

        choice = input("Enter the number of the NPC you want to interact with (0 to exit): ")

        if choice == "0":
            return

        try:
            choice = int(choice)
            if 1 <= choice <= len(self.npcs):
                npc_index = choice - 1
                self.interact_with_npc(npc_index)
            else:
                print("Invalid choice. Please select a valid NPC to interact with.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def work(self, character):
        print("You are looking for gigs to earn Dinars.")
        
        # Create a table to display gig names and rewards
        gig_data = []
        for _, gigs in self.available_gigs.items():
            for gig in gigs:
                gig_data.append([gig["name"], gig["reward"]])

        print(tabulate(gig_data, headers=["Gig Name", "Gig Reward (Dinars)"], tablefmt="grid"))
        
        choice = input("Enter the number of the gig you want to work on (0 to cancel): ")

        if choice == "0":
            return  

        try:
            choice = int(choice)
            total_gigs = sum(len(gigs) for gigs in self.available_gigs.values())
            if 1 <= choice <= total_gigs:
                selected_gig = None
                current_option_counter = 1

                # Find the selected gig based on the chosen option
                for _, gigs in self.available_gigs.items():
                    for gig in gigs:
                        if current_option_counter == choice:
                            selected_gig = gig
                            break
                        current_option_counter += 1
                    if selected_gig:
                        break
                random1 = random.randint(0,10)
                if selected_gig and random1 >= 5:
                    reward = selected_gig["reward"]
                    character.gold += reward
                    self.completed_gigs.append(selected_gig["name"])
                    print(f"You have completed the {selected_gig['name']} gig and earned {reward} Dinars.")
                else:
                    print("No one requires your services for this gig.")
            else:
                print("Invalid choice. Please select a gig from the list.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")



    
    def interact_with_npc(self, npc_index):
        madrassah = Madrassah()
        character = Character()
        npc = self.npcs[npc_index]

        print(f"\nYou are interacting with" , npc['name'])

        while True:
            print("\nInteraction Options:")
            print("1. Compliment")
            print("2. Have a Conversation")
            print("3. Insult")
            print("4. Brawl")
            print("5. Befriend")
            print("6. Have Coffee")
            print("7. Back to Coffee House Menu")

            choice = input("Choose an option (1-7): ")

            if choice == '1':
                # Checking if the NPC has already been complimented
                if npc["name"] not in self.complimented_npcs:
                    compliment = self.compliment(npc_name=npc["name"])
                    print(compliment)
                    npc["relationship"] += 5
                    self.complimented_npcs.append(npc["name"]) 
                else:
                    print(f"You have already complimented {npc['name']}.")

            elif choice == '2':
                conversation = self.otto_conver(npc)
                print(conversation)
                npc["relationship"] += 3
            elif choice == '3':
                # Checking if the NPC is already a friend
                if npc["name"] not in self.friends and npc["name"] not in self.insulted_npcs:
                    insult = self.insult(npc_name=npc["name"])
                    print(insult)
                    npc["relationship"] -= 5
                else:
                    print(f"You cannot insult {npc['name']} until you are friend with them.")
                

            elif choice == '4':
                # Implemented brawl logic and updated the relationship
                if npc["name"] not in self.friends:
                    brawl = self.choose_brawl()
                    print(brawl)
                    madrassah.handle_brawl(character)
                    npc["relationship"] -= 10
                else:
                    print(print(f"You cannot brawl with {npc['name']} until you are friend with them."))
            elif choice == '5':
                # Checking if the NPC meets the friendship requirement
                if npc["relationship"] >= 80:
                    if npc["name"] not in self.friends:
                        self.friends.append(npc["name"])
                    else:
                        print(f"You are already friends with {npc['name']}.")
                else:
                    print(f"You need at least 80 relationship points to befriend {npc['name']}.")

            elif choice == '6':
                print(f"You have a cup of Turkish coffee with {npc['name']}.")
            elif choice == '7':
                break
            else:
                print("Invalid choice. Please select a valid option (1-7).")
    def activities_menu(self, character):
        while True:
            print("\nActivities Menu:")
            print("1. Roam the City")
            print("2. Visit Public Baths")
            print("3. Listen to the Hakawatis")
            print("4. Back to Main Menu")

            activities_choice = input("Choose an activity (1-4): ")

            if activities_choice == '1':
                self.roam_the_city()
            elif activities_choice == '2':
                self.visit_public_baths(character)
            elif activities_choice == '3':
                self.listen_to_hakawatis()
            elif activities_choice == '4':
                break
            else:
                print("Invalid choice. Please select a valid activity (1-4).")

    def roam_the_city(self):
        # Implement roaming the city and display a random text
        city_texts = [
            "As you roam the bustling streets of the Ottoman city, you admire the vibrant markets filled with exotic spices and colorful textiles.",
            "The call to prayer echoes through the winding alleys as you explore the ancient architecture of the city.",
            "You witness a group of traders haggling over prices, their voices filling the air with a lively energy.",
            "Children play in the narrow streets, their laughter a testament to the joy of everyday life in the city.",
            "You stumble upon a hidden tea house, where locals gather to share stories and enjoy aromatic cups of tea.",
            "The city's bazaars are a sensory delight, with the aroma of spices and the colors of fabrics and ceramics.",
            "You come across a street performer playing traditional Ottoman music, drawing a crowd with their melodies.",
            "In a quiet corner, you find a calligrapher creating intricate designs, a testament to the city's rich artistic heritage.",
            "As you explore, you stumble upon an ancient mosque, its stunning architecture a testament to Ottoman craftsmanship.",
            "You discover a small shop selling finely crafted Ottoman jewelry, each piece a work of art.",
            "The city's bustling harbor is filled with ships from distant lands, a reminder of the empire's global reach.",
            "You visit a local café and savor a cup of Turkish coffee, its rich flavor warming your soul.",
            "The city's streets are alive with the sights and sounds of daily life, a reflection of the diverse cultures within the empire.",
            "As you walk along the city walls, you marvel at the breathtaking view of the surrounding countryside.",
            "You join a group of children flying colorful kites in an open square, experiencing the simple joys of youth."
        ]
        random_text = random.choice(city_texts)
        print(random_text)

    def visit_public_baths(self, character):
        # Increase character's health and display a random text about taking a bath
        health_increase = random.randint(5, 15)
        character.stats["health"] += health_increase
        print(f"You visit the public baths and immerse yourself in the soothing waters. Your health improves by {health_increase} points.")
        bath_texts = [
            "The steam envelops you, relaxing your muscles as you soak in the warm waters.",
            "You feel rejuvenated as you cleanse yourself in the communal baths, a cherished tradition in Ottoman culture.",
            "Surrounded by fellow bathers, you share stories and laughter while enjoying the healing properties of the baths.",
            "The attendants scrub your skin with fragrant soap, leaving you feeling invigorated and refreshed.",
            "The sound of splashing water and friendly chatter fills the baths, creating a sense of unity among the visitors.",
            "You float in the bath's soothing waters, feeling the day's stresses melt away.",
            "The baths are adorned with intricate mosaics, each tile a work of art that tells a story.",
            "As you soak, you hear snippets of conversations in various languages, a testament to the city's diversity.",
            "A traditional Ottoman musician plays soothing melodies by the baths, adding to the ambiance.",
            "You enjoy a massage by one of the skilled bath attendants, feeling tension release from your body.",
            "The baths are a place of reflection, where you ponder life's mysteries as you soak in the ancient waters.",
            "You watch as bath attendants prepare fragrant oils and scents, infusing the air with a pleasant aroma.",
            "The baths provide a welcome respite from the bustling city, offering a moment of tranquility.",
            "You notice intricate patterns in the bath's architecture, a testament to Ottoman craftsmanship.",
            "In the baths, you strike up a conversation with a fellow bather, exchanging stories and experiences."
        ]
        random_text = random.choice(bath_texts)
        print(random_text)

    def listen_to_hakawatis(self):
        # Implement listening to Hakawatis and display a random story text
        hakawati_stories = [
            "The Hakawati narrates a thrilling tale of adventure on the high seas, with pirates and hidden treasures. The hero's courage knows no bounds as they face formidable challenges.",
            "You are captivated by the Hakawati's storytelling as he weaves a story of star-crossed lovers in a distant land. Their love defies all odds, and their sacrifices resonate with your heart.",
            "The story unfolds with a heroic quest to defeat a fearsome dragon that threatens a peaceful village. The hero's determination and bravery inspire all who hear the tale.",
            "The Hakawati's words transport you to a world of magic and wonder, where mythical creatures roam ancient forests. You can almost feel the enchantment in the air.",
            "You listen intently as the Hakawati shares a story of wisdom, teaching valuable lessons about honor and kindness. The tale's moral resonates with the audience, leaving them with food for thought.",
            "The Hakawati's story takes you on a journey through time, recounting epic battles and legendary warriors. Each battle is filled with valor and sacrifice, reminding you of the empire's history.",
            "As the Hakawati continues, you become immersed in a tale of political intrigue and secret alliances. The plot thickens with each revelation, keeping you on the edge of your seat.",
            "The story's protagonist embarks on a quest for knowledge, traveling to distant lands and seeking the wisdom of sages. Their pursuit of enlightenment is a testament to the human spirit.",
            "The Hakawati narrates a heartwarming story of friendship that transcends boundaries. The bonds between the characters remind you of the importance of camaraderie.",
            "You find yourself in a world of dreams and fantasy as the Hakawati spins a tale of magical realms and mythical creatures. The line between reality and imagination blurs, captivating your senses.",
            "The Hakawati's storytelling skill shines as he recounts historical events with vivid detail. The past comes alive through his words, offering a deeper understanding of the empire's heritage.",
            "You listen to a story of perseverance and resilience, where the protagonist overcomes adversity with unwavering determination. The tale leaves you with a sense of hope and inspiration.",
            "The Hakawati's narrative takes unexpected twists and turns, keeping the audience engaged and eager to discover the story's resolution. Each revelation is met with anticipation and wonder.",
            "As the Hakawati shares a tale of love and sacrifice, you can't help but be moved by the characters' devotion to one another. Their sacrifices tug at your heartstrings.",
            "The story's climax is a breathtaking spectacle of courage and heroism. The hero faces their greatest challenge yet, and the outcome hangs in the balance, leaving the audience in suspense."
        ]
        random_story = random.choice(hakawati_stories)
        print("You sit down to listen to the Hakawati:")
        print(random_story)

    def main_menu(self):
        character = Character()
        while True:
            print("Main Menu:")
            print("1. Visit Ottoman Bazaar")
            print("2. Visit Coffee House")
            print("3. Serve the Empire")
            print("4. View Inventory")
            print("5. Activities")
            print("6. Aged up")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.visit_marketplace(character)
            elif choice == "2":
                self.visit_coffee_house(character)
            elif choice == "3":
                self.work(character)
            if choice == "4":
                self.view_inventory()
            elif choice == '5':
                self.activities_menu(character)
            elif choice == '6':
                print("You decided to rest for now.")
                break
            

#Main Engine to handle everything
class GameEngine:
    def __init__(self):
        self.characters = []
        self.stats = []
        self.events = [Event()]  

        
    def start_game(self):
        print(text2art("Tales of Heritage"))
        print(Fore.GREEN + Style.BRIGHT + "Hello, Adventurer! Welcome to 'Tales of Heritage,' a realm where you're the author of your destiny.\nEmbark on an epic journey through time, navigating the twists and turns of history.\nAs you shape your character's path, prepare to witness the tapestry of the Renaissance era unfurl before you.\nCraft your legacy, make daring choices, and let your name echo through the ages in this immersive tale.\n" + Style.RESET_ALL)
        print(Style.BRIGHT + "Shape your protagonist and embark on a Renaissance odyssey within the vibrant tapestry of the Ottoman Empire—where your choices shape not only your destiny but the fate of an empire.\n")
        # Calling the get method to create a character
        character = Character.get()
        # Adding the character to the list of characters
        if character:
            self.characters.append(character)
        character.print_info()
        character.regulate()
        event_instance = Event()
        event_instance.event(character)
        madrassah = Madrassah()
        madrassah.assign_npcs_to_groups()
        



# Creating a game engine instance and start the game
game_engine = GameEngine()
game_engine.start_game()
