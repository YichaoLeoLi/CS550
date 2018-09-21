def start():
    result = input('\n\nYou are here to save the princess! \n\nShe has been kidnapped by Bowser and Bowser Jr. \nYou are at a fork in the road, and you can either \n\n1)Go ahead and save the Princess or \n\n2)Turn back in shame and dishonor.\n\n>>')
    if result == '1':
    	savePrincess()
    elif result == '2':
    	shame()
    else:
    	print("I don't know what "+result+" means. \nPlease type 1 or 2.")
    	start()
def savePrincess():
	result2 = input("\n\nYou wonder where the princess is right now. Now you can either ask \n\n1)your best friend or \n\n2)some random people on the street.\n\n>>")

def shame():
	print('fefe')




start()