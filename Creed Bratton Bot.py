import praw  # Reddit's API wrapper.
import random  # To randomly choose a quote.
import time  # To put the bot to sleep.

reddit = praw.Reddit(  # All the information that goes here will be unique, given to you by Reddit.
    client_id="clientId",
    client_secret="clientSecret",
    user_agent="userAgent",
    username="userName",
    password="passWord"
)

creedQuotes = ["Just pretend like we’re talking until the cops leave.",  # An array of quotes by Creed Bratton.
               "Every week, I’m supposed to take four hours and do a quality spot-check at the paper mill. And of "
               "course, the one year I blow it off, this happens.", "Animals can’t feel pain.",
               "He was drunk as a skunk. He was flying down Route 6. He slides under an 18-wheeler. ",
               "Not bad for a day in the life of a dog food company.",
               "You should see how many supplies I’ve taken from this place. Honestly, I love stealing.",
               "Everywhere I look, it’s Betty White this and Betty White that. Finally, a kid who is not talking "
               "about Betty White. Of course, I follow him.",
               "You’re paying way too much for your worms, man. Who’s your worm guy?", "That wasn't a tape worm",
               "Ohm, I steal things all the time. It’s just something I do. I stopped caring a long time ago.",
               "I wanna do a cartwheel. But real casual like, not make a bit deal out of it, but I "
               "know everyone saw it. Just one stunning gorgeous cartwheel.",
               "It’s pirate code. It means he wants to meet. I understand pirate code. I can’t speak it.",
               "Hello, Creed Bratton, Quality Assurance, Dunder Mifflin, Scranton. I was supposed to meet with one of "
               "your floor managers last week for a quality inspection, and he or she wasn't there. I’m trying to "
               "remember who it was. Who wasn't there last week?",
               "Oh really, what kind? Codeine, Vicodin, Percocet, Fentanyl, Oxycontin, Palladone?",
               "You’re over 40; that’s the cut-off. Are you listening to what he’s saying? Re-training. New system. "
               "Youth. I’m telling you, this kid is the grim reaper.",
               "What is wrong with this woman? She’s asking about stuff that’s nobody’s business. What do I do? "
               "Really, what do I do here? I should’ve written it down. Qua something, uh…qua…quar…quibo, "
               "qual…quir-qubity. Uabity assurance! No, no, no, no, no, but I’m getting close.",
               "It’s pronounced Ker-nell. It’s the highest rank in the army.”, “I can bring these to my shelter.",
               "All right, all right. Say no more. So, this is how I got Squeaky Fromme. No small talk. Just show "
               "her who’s the boss. Just go right in and kiss her.",
               "Be cool, Michael. I saw this guy kill a bunch of people.",
               "My tombstone has been already made, thank you.",
               "Two eyes, two ears, a chin, a mouth, 10 fingers, two nipples, a butt, two kneecaps, a penis. I have "
               "just described to you the Loch Ness Monster and the reward for its capture…all the riches in Scotland. "
               "So I have one question, why are you here?",
               "Let’s keep this on the QT, okay? I want to be a dead mama JAMA.",
               "It’s Creed. FYI I’m starting my own paper company looking to poach some chumps. You in?",
               "I sprout mung beans on a damp paper towel in my desk drawer. Very nutritious, "
               "but they smell like death.",
               "You deal with this, or you, me Sammy, Phyllis, the chick you hit with the car…we’re goners.",
               "We should hang out by the quarry and thrown things down there.",
               "Hey, brah. I have been meaning to ask you. Can we get some Red Bull for these things? "
               "Sometimes your guy’s gotta rude the bull. Later skater.",
               "You know a human can go on living for several hours after being decapitated.",
               "I already won the lottery. I was born in the US of A baby! And as a backup, I have a Swiss passport.",
               "A beautiful morning at Dunder Mifflin, or like I like to call it, Great Bratton.",
               "Guys, I’m starting to think Pam’s not even pregnant.", "I’ve never owned a refrigerator before",
               "He’s been trashing us relentlessly on Twitter. Now it’s funny stuff, but mean.",
               "The only difference between me and a homeless man is this job. I will do whatever it takes to survive, "
               "just like I did when I was a homeless man.",
               "I run a small fake I.D. company from my car with a laminating machine that I swiped from the sheriff’s "
               "station.", "Did one of you tell Stanley that I have asthma? Cause I don’t. If this gets out, they "
                           "won’t let me scuba. And if I can’t scuba, what am I working towards?"]

subreddit = reddit.subreddit("DunderMifflin")  # You pass the name of the subreddit as an argument.

for post in subreddit.hot(limit=10):  # Here I choose ten posts from the 'hot' section of the subreddit.
    for comment in post.comments:  # Here I parse the comments.
        if hasattr(comment, "body"):  # Checking if the comment has a body, if not, the code would've thrown an error.
            commentLower = comment.body.lower()  # We convert the comment to lower case.
            if "creed bratton" in commentLower:  # We check if the comment mentions Creed Bratton.
                quoteToPrint = creedQuotes[random.randint(0, len(creedQuotes) - 1)]
                # A quote is chosen at random from the array.
                comment.reply(quoteToPrint)  # The quote is replied with.
                time.sleep(700)  # The bot is put to sleep for 700 seconds.
