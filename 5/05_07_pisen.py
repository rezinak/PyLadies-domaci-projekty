lyrics = """One pill makes you larger, and one pill makes you small
And the ones that mother gives you, don't do anything at all
Go ask Alice, when she's ten feet tall

And if you go chasing rabbits, and you know you're going to fall
Tell 'em a hookah-smoking caterpillar has given you the call

And call Alice, when she was just small

When the men on the chessboard get up and tell you where to go
And you've just had some kind of mushroom, and your mind is moving low

Go ask Alice, I think she'll know

When logic and proportion have fallen sloppy dead
And the white knight is talking backwards
And the red queen's off with her head
Remember what the dormouse said
Feed your head, feed your head K"""

pocetk = 0
lyrics = lyrics.lower()


for i in range(len(lyrics)):
    if lyrics[i] == "k":
        pocetk = pocetk + 1
print(pocetk)
