import os

answer_A = ["A", "a"]
answer_B = ["B", "b"]

#def clear():
 #   os.system('clear')

def intro():
    print("Choose Your Own Haunting!!!")
    #clear()
    print("You are an abandoned house in rural Hanover, NH. \n"
      "It is a warm night in the middle of August, and it \n"
      "just so happens to be Friday the 13th. A group of \n"
      "Dartmouth students are out for an evening woccom. \n"
      "Currently enrolled in summer school and taking Haunted \n"
      "Houses with Professor Clark, the group of students decided \n"
      "it would be a good idea to apply what they have learned in \n"
      "their class to a haunting experience and seek you, the infamous \n"
      "Hanover Haunted House, out. ")

    print("Like the houses depicted in the literature the students \n"
      "studied in their class, what makes you so terrifying is \n"
      "the fact that you, the Hanover Haunted House, are alive. \n"
      "You can choose how to best haunt your inhabitants. Will you be \n"
      "a Hungry House, a Stay Away House, or some combination of both….. \n"
      "(press the key of the option you want to pursue for each prompt)")

    print("Press 'a' to begin the adventure")

    choice = input(">>>>>") #Here is first choice
    if choice in answer_A:
      one()

def one():
    #prompt
    print("Guided by the light of the full moon, the Dartmouth students slip \n"
        "through the opening in the rusted metal gate protecting the property. \n"
        "Once through, they cautiously hike up the graveled pathway to the front \n"
        "of the house and approach the front porch. One brave soul steps closer to \n"
        "the warped wooden door, a sage green color that is more chipped than painted.\n"
        "A bronze lion head knocker decorates the door, and the student reaches out \n"
        "and knocks on it. You will…..")
    print("\n")
    #bright red
    print("A: With an unnerving loud, slow creak, you swing open the door, \n"
        "inviting them into you.")
    print("B: You make the entire house shudder and audibly lock the front door \n"
        "as the lion knocker comes alive, roaring at the students.")

    choice = input(">>>>>") #Here is first choice
    if choice in answer_A:
        one_a()
    elif choice in answer_B:
        one_b()


def one_a():
    #prompt
    print("After you open the door, the students nervously enter. It is pitch black \n"
          "inside and the slight breeze from outside follows the students in. They stand \n"
          " frozen in the entryway, their eyes large and absorbing as much of their \n"
          "surroundings as possible. They have yet to move further into the space, as if \n"
          "they are waiting for you to beckon them in or turn them away, so you…..")
    print("\n")
    print("A: Turn on the light in the chandelier that floats above the top step of \n"
          "the grand staircase, thereby inviting them up.")
    print("B: A ghostly voice repeatedly screeches “GET OUT GET OUT NOW” ")

    choice = input(">>>>>") #Here is first choice
    if choice in answer_A:
        two_a()
    elif choice in answer_B:
        two_b()

def one_b():
    #prompt; bright red B
    print("Frightened, the students begin to run away from the front door, \n"
          "quickly realizing that this was not the best decision. As they sprint \n"
          "back down the gravel pathway….")
    print("\n")
    #hot pink
    print("A: The antique metal gate eerily rolls shut, locking the students in")
    print("B: An old man hobbles in front of them, blocking their path")

    choice = input(">>>>>") #Here is first choice
    if choice in answer_A:
        three_a()
    elif choice in answer_B:
        final_one()

def two_a():
    #prompt; light red A
    print("The students follow your lead and ascend the 100 year old grand staircase, \n"
          "each step creaking under their feet. Upon reaching the second floor landing….")
    print("\n")

    #bright orange
    print("A: A black cat prances in front of the students and leads them \n"
          "ahead to a door on their right at the top of the stairs.")
    print("B: The top step splinters as the entire staircase rumbles beneath \n"
          "their feet, causing the students to somersault back down the stairs. ")

    choice = input(">>>>>")
    if choice in answer_A:
        four_a()
    elif choice in answer_B:
        four_b()

def four_b():
    print("Disoriented and sore, they get up and compose themselves. \n"
          "Unsure of exactly what just happened, they are not fully frightened \n"
          "enough to run out of their own will. Do you scare them away or entice them to stay?")

    print("\n")
    print("A: Scare them away")
    print("B:Entice them to stay")

    choice = input(">>>>>")
    if choice in answer_A:
        print("These students have no place here, so you decide to scare them away.")
        final_three()
    elif choice in answer_B:
        final_seven()

def two_b():
    #prompt; light red B
    print("Terrified, the students turn to leave")
    print("\n")

    #bright purple
    print("A: You lock the front door from the inside, trapping them in. ")
    print("B: The front door swings open, and the students rush out. ")

    choice = input(">>>>>")
    if choice in answer_A:
        final_two()
    elif choice in answer_B:
        five_a()

def five_a():
    #prompt; bright purple B
    print("Frightened, the students begin to run away from the front door, \n"
          "quickly realizing that this was not the best decision. As they \n"
          "sprint back down the gravel pathway…")

    print("\n")

    one_b()


def three_a():
    #prompt, hot pink A
    print("Realizing they are trapped, the students nervously look around, surveying \n"
          "their surroundings. A light turns on in a second story room catching the \n"
          "students’ eyes and they see a figure move about the room. Suddenly, the \n"
          "figure’s hand slaps the window and slowly slides down, leaving a bloody \n"
          "handprint. Worried about the person, the students look for a way in the house....")

    print("\n")
    #light purple
    print("A: The front door swings open and the front porch light turns on, beckoning them inside ")
    print("B: The figure reappears in the window and yells, “SAVE YOURSELF. LEAVE NOW” ")

    choice = input(">>>>>")
    if choice in answer_A:
        one_a()
    elif choice in answer_B:
        final_one()


def four_a():
    #prompt; bright orange A
    print("The students gingerly follow behind the cat as they approach the \n"
          "door. Hissing, the cat claws at the door, signaling for the students \n"
          "to open it up, so…..")
    print("\n")
    #light orange
    print("A: A key appears around the cat’s collar that will unlock the door")
    print("B: Blood slowly drips from the ceiling down the front of the door. \n"
          "A message in all capital letters appears: “LEAVE” ")

    choice = input(">>>>>")
    if choice in answer_A:
        six_a()
    elif choice in answer_B:
        final_three()

def six_a():
    #prompt; light orange A
    print("The silver key catches the students’ attention. They reach down \n"
          "and unclip it from the cat’s collar, insert it into the keyhole \n"
          "and unlock the door. The door swings open to reveal a large, \n"
          "magnificent ballroom, similar to the unused one the students \n"
          "saw when they watched The Shining.")
    print("\n")

    #bright yellow
    print("A: At the far side of the room, there is a bar. \n"
          "Behind the bar, a man dressed in a tuxedo waves them over saying “Come. Come here ")
    print("B: The lights in the ballroom flicker on and off and the entire room starts to shake. ")

    choice = input(">>>>>")
    if choice in answer_A:
        seven_a()
    elif choice in answer_B:
        seven_b()

def seven_a():
    #prompt; bright yellow A
    print("The students walk across the room and approach the bar. \n"
          "They ask him his name and why he is in the house, but \n"
          "he does not respond. Instead he asks them to come \n"
          "behind the bar and shows them a trap door that opens to a staircase…. ")
    print("\n")

    print("A: He pushes the students down the staircase")
    print("B: He asks them to follow him downstairs.")
    choice = input(">>>>>")
    if choice in answer_A:
        final_four()
    elif choice in answer_B:
        final_five()


def seven_b():
    #prompt; bright yellow B
    print("Afraid, the students aren’t sure what to do and if they \n"
          "should leave or stay. You help them decide…")
    print("\n")

    print("A: The lights turn back on and the room stops shaking. \n"
          "Twin 8 year old girls appear in front of the students \n"
          "and say “Welcome homeeeee” as they slowly walk towards the students. ")
    print("B: The lights turn back on and the room stops shaking. \n"
          "Twin 8 year old girls appear in front of the students and \n"
          "say “This isn’t your home. You need to leave” ")

    choice = input(">>>>>")
    if choice in answer_A:
        final_six()
    elif choice in answer_B:
        print("The twins start to slowly and creepily approach the students.")
        final_three()

def final_seven():
    print("he lights suddenly flicker on and an old woman appears, \n"
          "“Welcome, I’m sorry I was not here to greet you earlier” \n"
          "she says to the students. “We have a feast prepared for you. Come along.” \n"
          "And she leads them through a long hallway that opens into an \n"
          "exquisite dining hall. A long mahogany table is set with \n"
          "multiple gold place settings and is adorned with dishes of \n"
          "enticing meals. The students sit down and begin eating. \n"
          "As they enjoy the feast, they are unaware that the old \n"
          "woman has left the room, and that any and all doors and \n"
          "windows have disappeared, thus creating an inescapable \n"
          "space; they are too absorbed in the meal to notice or \n"
          "even care. Hours pass but the students are unphased. \n"
          "The more time that passes, the more disconnected the students \n"
          "become from their previous lives. All they now know is \n"
          "that they feel so welcomed and happy in this room and \n"
          "that they never want to leave, not that they even could \n"
          "if they wanted to…..END OF HAUNTING")

#twins
def final_six():
    print("3 more pairs of twins appear and they surround the group of students. \n"
          "Grabbing onto the students the twins drag them out of the room into \n"
          "a dimly lit hallway chanting, “Welcome home. Welcome home.” \n"
          "The hallway seems to last forever and eventually the Dartmouth \n"
          "students enter a trance and join in on the chant. \n"
          "“We are home. We are home” They haven’t been seen since. END OF HAUNTING ")

def final_five():
    print("The students gingerly follow him into an emptied wine cellar. \n"
          "“I’m so glad you decided to join us,” the man says. \n"
          "“The house has been in need of some young, new blood.” \n"
          "The trap door above them slams closed and locks from the outside. \n"
          "There is no escape, they are part of the house now. END OF HAUNTING")

#trapped in cellar
def final_four():
    print("The students tumble down the stairs and the trap door is \n"
          "closed above them. There is a single light bulb illuminating the room. \n"
          "Left alone in an emptied cellar, they have no way to escape. \n"
          "An ominous voice calls out to them, “You should have left \n"
          "when you had the chance.” The lightbulb turns off. A \n"
          "distant laugh fills the room, growing louder and louder. \n"
          "They never should have entered the house….END OF HAUNTING")


#chased out by bats
def final_three():
    print("Terrified, the students run down the stairs. A ghostly figure appears \n"
          "in the foyer, dripping with blood and screams “RUNNNNNN” as thousands of \n"
          "bats flit around the house, screeching and flying towards the students.\n"
          "The front door swings open and the students sprint out, being chased \n"
          "by the bats, all the way down the gravel pathway. As they approach \n"
          "the metal gate, an old man hobbles in front of them, stops the \n"
          "students, and hoarsely warns, “You should not be here. This is \n"
          "private property and college kids like you have no place here. \n"
          "Too many things have happened within the walls of this house, \n"
          "and if you value your lives, you will leave and never come back. \n"
          "The house might not be as forgiving next time…..” With that \n"
          "ominous warning, the students run away into the night. END OF HAUNTING ")

#trapped in feast
def final_two():
    print("Standing in the darkness of the foyer, the students stand frozen, \n"
          "waiting for something to happen. The lights suddenly flicker on \n"
          "and an old woman appears, “Welcome,” she says to the students. \n"
          "“We have a feast prepared for you. Come along.” And she leads \n"
          "them through a long hallway that opens into an exquisite dining \n"
          "hall. A long mahogany table is set with multiple gold place \n"
          "settings and is adorned with dishes of enticing meals.  The \n"
          "students sit down and begin eating. As they enjoy the feast, \n"
          "they are unaware that the old woman has left the room, and \n"
          "that any and all doors and windows have disappeared, thus \n"
          "creating an inescapable space; they are too absorbed in \n"
          "the meal to notice or even care. Hours pass but the \n"
          "students are unphased. The more time that passes, the \n"
          "more disconnected the students become from their previous \n"
          "lives. All they now know is that they feel so welcomed and \n"
          "happy in this room and that they never want to leave, \n"
          "not that they even could if they wanted to…..END OF HAUNTING")

#old man ask to leave final
def final_one():
    print("At that moment, the old metal gate rolls open. An old man appears out \n"
          "of the thicket of landscape on the property and calls out to the students, \n"
          " “You should not be here. This is private property and college kids like \n"
          "you have no place here. Too many things have happened within the walls \n"
          "of this house, and if you value your lives, you will leave and never \n"
          "come back. The house might not be as forgiving next time…..” With that \n"
          "ominous warning, the students run away into the night. END OF HAUNTING")

intro()

