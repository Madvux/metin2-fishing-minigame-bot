# metin2-fishing-minigame-bot

> [!NOTE]
**NEEDS ADMIN PRIVILEGES**

> [!IMPORTANT]
**Console application**

> [!WARNING]
> __I do not take responsibility of any illegal use of game bot__

Bot compares screenshot from __img__ directory and based on number - clicks __space__ number of times. 
Top run bot open console with admin privileges, go to project directory using __cd **path**__ command and run __img_recognition.py__.
Bot starts working after putting bait on fishing rod, when first image bubble shows up.
Using many randomized time functions in bot, and not injecting anything into the game simulates real player actions.

To work correctly configuration is needed.
Default bait in game position should be at **1**  in action bar (Can be changed in code).
To check right region of screen and make screenshots use **regionscreenshotsaver.py**, after making screenshot change it's name to __**number**.png__ where **number** is times that __space__ is needed to be be clicked, and paste it into __img__ directory.
Randomized sleep() functions might need adjustment, this worked for me.

Bot compares images so make sure while running the bot conditions, should be the same as while configuring it.
For example max-zoomed in, character facing north, camera directly over the head.
