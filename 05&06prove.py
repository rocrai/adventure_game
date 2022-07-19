print('You wake up and realize that you are suddenly teleported to a strange unfamiliar place what will you do HIDE or EXPLORE')
choose_one = input('')
print()


while choose_one.lower() not in ['hide','explore']:
    print("This is not a valid input, please try again")
    print('You wake up and realize that you are suddenly teleported to a strange place what will you do HIDE or EXPLORE')
    choose_one = input('')
    print()
if choose_one.lower() == 'hide':
    print('You hid for a few hours and saw a bizzare creature. It doesnt seem to look dangerous, but be careful looks can be deceiving. RUN or APPROACH')
    choose_two = input('')
    print()
    while choose_two.lower() not in ['run','approach']:
        print("This is not a valid input, please try again")
        print('You hid for a few hours and saw a bizzare creature. It doesnt seem to look dangerous, but be careful looks can be deceiving. RUN or APPROACH')
        choose_two = input('')
        print()
    if choose_two.lower() == 'run':
        print('You ran away from it saying to yourself "better safe than sorry". You waited for hours till it became dark. What will you do? LIGHT a campfire or STAY in darkness.')
        choose_three = input('')
        print()
        while choose_three.lower() not in ['light','stay']:
            print("This is not a valid input, please try again")
            print('You ran away from it saying to yourself "better safe than sorry". You waited for hours till it became dark. What will you do? LIGHT a campfire or STAY in darkness.')
            choose_three = input('')
            print()
        if choose_three.lower() == 'light':
            print('You lit your campfire and after a few minutes multiple eyes are staring at you through the darkness. You quickly turned off the light but it\'s too late now they already know where you are. You patiently sat as it is the only thing you can do. You hear their footsteps getting closer and closer. You can see the silhouette of the creatures, they don\'t seem to resemble the shape of a human. You only hope that they are not hostile.')
        elif choose_three.lower() == 'stay':
            print('You stayed in the dark not making any noise. You are lucky that this place doesnt feel cold at all even though it\'s night-time. After a few minutes you hear strange noises that you have never heard before in your life. You quietly uttered to yourself "I want to go home". Suddenly something behind you said "This is your home now".')
        else :
            print('That\'s not one of the choices.. Try Again')
    elif choose_two.lower() == 'approach':
        print('You approach the creature, it doesnt seem to be hostile. But it seems to be going back to its home. Will you FOLLOW it or LEAVE it alone.')
        choose_three = input('')
        print()
        while choose_three.lower() not in ['follow','leave']:
            print("This is not a valid input, please try again")
            print('You approach the creature, it doesnt seem to be hostile. But it seems to be going back to its home. Will you FOLLOW it or LEAVE it alone.')
            choose_three = input('')
            print()
        if choose_three.lower() == 'follow':
            print('You followed the creature to its home which resembles a cave. You entered it and found a safe place to rest for the day. But are you really safe?')
        elif choose_three.lower() == 'leave':
            print('You left it alone and went the opposite way. You found a strange looking cave and tried to enter it, as you went deeper the cave you found some bones. You suddenly want to leave now but you felt a piece of debris drop on you, you look up and saw something sinister.')
        else :
            print('That\'s not one of the choices.. Try Again')
    else :
            print('That\'s not one of the choices.. Try Again')
    
elif choose_one.lower() == 'explore':
    print('You explored and found an empty village. You entered in one of the houses and found a comfortable place to stay for the night. Will you STAY or LEAVE the place.')
    choose_two = input('')
    print()
    while choose_two.lower() not in ['stay','leave']:
        print("This is not a valid input, please try again")
        print('You explored and found an empty village. You entered in one of the houses and found a comfortable place to stay for the night. Will you STAY or LEAVE the place.')
        choose_two = input('')
        print()
    if choose_two.lower() == 'stay':
        print('You decided to stay in this strange place since you dont want to sleep outside. It\'s a huge house with many rooms Would you sleep in a HIDDEN place or a more COMFORTABLE place.')
        choose_three = input('')
        print()
        while choose_three.lower() not in ['hidden','comfortable']:
            print("This is not a valid input, please try again")
            print('You decided to stay in this strange place since you dont want to sleep outside. It\'s a huge house with many rooms Would you sleep in a HIDDEN place or a more COMFORTABLE place.')
            choose_three = input('')
            print()
        if choose_three.lower() == 'hidden':
            print('You purposely slept on a place where you are completely hidden. You slept peacefully but a sudden noise woke you up. You were near the window so you checked out what that is. You opend the curtains just barely enough to see whats happening. You saw multiple human like creatures. Even though you are completely hidden they all looked your way staring at you. You closed the curtains and sat in the corner, wondering what will happen to you. ')
        elif choose_three.lower() == 'comfortable':
            print('You found and slept on the most comfortable bed you could find in the house. You woke up the next day feeling refreshed. You continued exploring this unfamiliar place once more hoping you can find your way home. You went on your day and found food from some trees, as you were exploring for the entire day it was now time for you to sleep. You slept and woke up the next morning feeling refreshed. You look around and was confused because you were in the same comfortable bed you slept the other day. The night came by again and just ignored the fact that you woke up in that bed, you went far this day sleeping next to a tree. The next morning you woke up horrified because you woke up in the comfortable bed again. You realize that you were stuck in an endless loop, was it because you chose to sleep in that bed?')
        else :
            print('That\'s not one of the choices.. Try Again')
    elif choose_two.lower() == 'leave':
        print('You left this strange village because you thought that it was too creepy. You found two different path\'s that leads to different places. Which path will you choose LEFT or RIGHT.')
        choose_three = input('')
        print()
        while choose_three.lower() not in ['left','right']:
            print("This is not a valid input, please try again")
            print('You left this strange village because you thought that it was too creepy. You found two different path\'s that leads to different places. Which path will you choose LEFT or RIGHT.')
            choose_three = input('')
            print()
        if choose_three.lower() == 'left':
            print('You went to the left path. You found an ocean and decided to go for a swim. You heard someone singing on some sort of rock and thought that they can probably help you go home. You swam closer to them but they werent what you expected them to be. Filled with terror you hurriedly swam to nearby land. You were getting closer to the land but felt something pulling your feet. You tried to resist but they were stronger than you, you realize that you cant do anything as you sank into the dark abyss.')
        elif choose_three.lower() == 'right':
            print('You went to right path and saw a huge tree. You went closer to the tree and found that it had fruits hanging from it. You werent hungry yet and there were more important things to do like going home. As you were about to leave the tree, someone said "psst". You looked back to the tree and found nothing so you ignored it, as you were about to leave again you heard the same thing again. You looked back but this time you saw a snake. "This snake cant possibly be the source of that sound right?" you thought to yourself. The snake spoke and you were shocked, it mysteriously convinced you to eat of the fruit. After you ate the fruit you passed out. You had a weird dream where you saw every other option that you could possibly make. You then woke up and was thankful that you didn\'t choose the other options. You hoped that you would have waken up in your home but you were still here in this unfamiliar place with the snake in front of you. The snake then proclaimed that it can lead you back home. Wll you trust this mysterious snake? ')
        else :
            print('That\'s not one of the choices.. Try Again')
    else :
            print('That\'s not one of the choices.. Try Again')
else :
            print('That\'s not one of the choices.. Try Again')


#I think I get a 5. I added a while loop to my code so that it asks the user again for an input if they put an incorrect answer.





