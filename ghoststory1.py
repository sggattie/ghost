print("""
Well, that's it, you're dead. You lived a good life, probably. Ask not for whom the bell tolls. It tolls for thee, at least right now. We are at the hour of judgement. More specifically, yours. Yet there is no booming voice of authority. The clouds have not parted. You merely float above your corpse, your shell. ...You float. This is the end, but... it is not the end. You can see. You can move. No sound, smell, or touch. But there is something. Religion, or lack thereof, as you know it has crashed out the window. Perhaps, though... perhaps there is something out there. You just have to find it. Do you want to? The world, the universe, is yours to explore. So with that, the real question is...
""")
#looking to prompt multiple inputs from user at different points. Previous inputs affect subsequent inputs.
#inputone = the first input from the user. prompted after the prologue.
inputone = input("Where do you go now? ")


chapterone_home = """
Even being deprived of your sense can't stop homesickness. Where else are you to really go, but the one place you can truly call home? Even without the sense of smell... you can feel the aroma, imagine those senses of home. Fresh baked chocolate chip on a cooling rack. The pitter-patter of puppy paws. The glowing hearth of the family television. It's not glowing right now, though. Nobody's home. Wonder where they could be...
"""

if inputone = home
	print(chapterone_home)
elif inputone = ocean
	print(chapterone_ocean)
elif inputone = space
	print(chapterone_space) 

#end of each chapter, prompts a sort of "ok, where to next? open ended like the old text adventures like Zork. 

#Hopefully down the line adding a GUI to make it more of an interactive ebook. Not so much choose your own adventure, but make your own adventure.
#Ideally GUI has a world map, user can touch to general area they want to travel to. Map changes as user has progressed through story.
#https://gamefaqs.akamaized.net/screens/1/c/e/gfs_39540_2_2_mid.jpg
inputtwo = input("Where to now? ")
#inputtwo = the second input from the user. And so on.
#Variables would represent sections on the map with specific collision boxes. Before that, a list could give a few different words something could be. Ocean = sea, water, underwater, etc.
if inputone = home and inputtwo = ocean
	print("home to ocean chapter")
elif inputtwo = space
	print("home to space chapter")
break
if inputone = ocean and inputtwo = home
	print("ocean to home chapter")
elif inputtwo = space
	print("ocean to space chapter")
break
if inputone = space and inputtwo = home or ocean
	print("lost in space chapter")
end


