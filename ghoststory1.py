inputone = input("Well, you're dead. What is there to do now? ")

#looking to prompt multiple inputs from user at different points. Previous inputs affect subsequent inputs.
#inputone = the first input from the user. prompted after the prologue.
if inputone = home
	print("home chapter")
elif inputone = ocean
	print("ocean chapter")
elif inputone = space
	print("space chapter") 

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


