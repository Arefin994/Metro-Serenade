# Define characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Coral", color="#ffcccc")
define k = Character("Kirin", color="#ccffcc")

# Define custom positions for the characters
define coral_left = Position(xalign=0.3, yalign=1.0)
define kirin_right = Position(xalign=0.7, yalign=1.0)

# Define scaled images
image coral_happy = im.Scale("coral_happy.png", 500, 800) # Adjust size as necessary
image coral_sad = im.Scale("coral_sad.png", 500, 800) # Adjust size as necessary
image coral_surprised = im.Scale("coral_surprised.png", 500, 800) # Adjust size as necessary
image kirin_happy = im.Scale("kirin_happy.png", 700, 700) # Adjust size as necessary
image kirin_sad = im.Scale("kirin_sad.png", 700, 700) # Adjust size as necessary
image kirin_surprised = im.Scale("kirin_surprised.png", 700, 700) # Adjust size as necessary

# The game starts here.

label start:

    # Show a background with a fade transition.
    scene bg train with fade

    # Play background music
    play music "Day1 Master.mp3" loop

    # Introduce the setting

    c "Welcome aboard the Love Express! This train ride is going to be special."
    k "Indeed! Who knows what kind of stories will unfold?"

    # Show Coral and Kirin separately

    c "Hey, I'm Coral. It's great to meet you!"
    k "And I'm Kirin. Ready for an adventure?"

    # Offer a choice of who to spend time with
    menu:
        "Spend time with Coral":
            jump spend_time_coral
        "Spend time with Kirin":
            jump spend_time_kirin

label spend_time_coral:

    # Focus on Coral
    show coral happy at center with dissolve
    hide kirin with dissolve

    c "I'm really into exploring new places. Do you like traveling?"

    menu:
        "Yes, I love it!":
            $ renpy.sound.play("StingerVictory1 Master.mp3")
            jump coral_love_travel
        "Not really, I prefer staying home.":
            $ renpy.sound.play("StingerDefeat1 Master.mp3")
            jump coral_no_travel

label coral_love_travel:

    play music "Dramatic1 Master.mp3" loop

    show coral happy at center with dissolve
    c "That's awesome! Traveling opens up so many new experiences."
    c "What's your favorite type of place to visit?"

    menu:
        "Mountains":
            $ renpy.sound.play("StingerVictory1 Master.mp3")
            jump coral_mountains
        "Beaches":
            $ renpy.sound.play("StingerVictory1 Master.mp3")
            jump coral_beaches

label coral_no_travel:

    play music "Dramatic2 Master.mp3" loop

    show coral sad at center with dissolve
    c "Oh, I see. Staying home can be nice too. What do you like to do at home?"

    menu:
        "Reading books":
            $ renpy.sound.play("StingerVictory1 Master.mp3")
            jump coral_books
        "Watching movies":
            $ renpy.sound.play("StingerVictory1 Master.mp3")
            jump coral_movies

label coral_mountains:

    play music "Night1 Master.mp3" loop

    show coral happy at center with dissolve
    c "Mountains are amazing! The fresh air, the stunning views... it's magical."
    c "We should plan a hiking trip sometime. It'd be so much fun!"

    c "Thanks for chatting with me. Let's enjoy the rest of the ride!"

    show coral neutral with dissolve

    return

label coral_beaches:

    play music "Night1 Master.mp3" loop

    show coral happy at center with dissolve
    c "Beaches are wonderful! The sound of the waves, the feeling of sand under your feet..."
    c "We should definitely go to a beach together. It'd be a great day out!"

    c "Thanks for chatting with me. Let's enjoy the rest of the ride!"

    show coral neutral with dissolve

    return

label coral_books:

    play music "Dramatic1 Master.mp3" loop

    show coral happy at center with dissolve
    c "Reading is a great way to escape into another world. What's your favorite genre?"

    # End the scene with a nice conversation
    c "Thanks for sharing. Maybe we can exchange book recommendations!"

    show coral neutral with dissolve

    return

label coral_movies:

    play music "Dramatic1 Master.mp3" loop

    show coral curious at center with dissolve
    c "Movies are awesome! They can make you laugh, cry, and everything in between."
    c "Do you have a favorite movie?"

    # End the scene with a positive note
    c "Thanks for chatting with me about movies. Maybe we can watch one together sometime!"

    show coral neutral with dissolve

    return

label spend_time_kirin:

    # Focus on Kirin
    show kirin happy at center with dissolve
    hide coral with dissolve

    k "I'm a bit of an adventurer. Do you like exploring new things?"

    menu:
        "Yes, absolutely!":
            $ renpy.sound.play("StingerVictory1 Master.mp3")
            jump kirin_love_adventure
        "Not really, I prefer familiarity.":
            $ renpy.sound.play("StingerDefeat1 Master.mp3")
            jump kirin_no_adventure

label kirin_love_adventure:

    play music "Dramatic1 Master.mp3" loop

    show kirin happy at center with dissolve
    k "That's great! Adventures can be so thrilling. What's the most adventurous thing you've done?"

    menu:
        "Skydiving":
            $ renpy.sound.play("StingerVictory1 Master.mp3")
            jump kirin_skydiving
        "Scuba diving":
            $ renpy.sound.play("StingerVictory1 Master.mp3")
            jump kirin_scuba_diving

label kirin_no_adventure:

    play music "Dramatic2 Master.mp3" loop

    show kirin sad at center with dissolve
    k "I get that. Sometimes comfort and familiarity are the best."
    k "What's something you enjoy doing in your comfort zone?"

    menu:
        "Reading":
            $ renpy.sound.play("StingerVictory1 Master.mp3")
            jump kirin_reading
        "Cooking":
            $ renpy.sound.play("StingerVictory1 Master.mp3")
            jump kirin_cooking

label kirin_skydiving:

    play music "Night1 Master.mp3" loop

    show kirin happy at center with dissolve
    k "Skydiving is so exhilarating! The rush of the wind, the view from above... It's incredible."
    k "I'd love to try it someday. Maybe we could go together!"

    k "Thanks for sharing your adventure stories with me!"

    show kirin happy with dissolve

    return

label kirin_scuba_diving:

    play music "Night1 Master.mp3" loop

    show kirin happy at center with dissolve
    k "Scuba diving sounds amazing! The underwater world is so beautiful and mysterious."
    k "I'd love to explore it more. Maybe we could go diving together!"

    k "Thanks for sharing your adventure stories with me!"

    show kirin happy with dissolve

    return

label kirin_reading:

    play music "Dramatic1 Master.mp3" loop

    show kirin surprised at center with dissolve
    k "Reading is a wonderful way to explore new worlds from the comfort of your home."
    k "What's your favorite book?"

    # End the scene with a nice conversation
    k "Thanks for chatting with me about books. Maybe we can discuss more sometime!"

    show kirin happy with dissolve

    return

label kirin_cooking:

    play music "Dramatic1 Master.mp3" loop

    show kirin happy at center with dissolve
    k "Cooking is a great way to unwind and enjoy delicious food. Do you have a favorite dish to cook?"

    # End the scene with a positive note
    k "Thanks for chatting with me about cooking. Maybe we can share recipes sometime!"

    show kirin happy with dissolve

    return
