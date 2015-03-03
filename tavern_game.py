def TheEnd():
	print "----------"
	print "Congratultions! You made it all the way to the end without dying"
	print "and you discovered Trench's true motives!"
	print "Play again to see some of the other fantastic endings,"
	print "try getting yourself killed,"
	print "or try typing jibberish when asked to make a choice!"
	print "Would you like to play AGAIN? or EXIT?"
	choice = raw_input("> ")
	
	if choice == "AGAIN":
		tavern()
	
	elif choice == "EXIT":
		exit(0)

	else:
		print "You fumble on the keyboard, breaking your fingers,"
		print "getting an infection, and dying."
		start()

def Trench_Retreated():
	print "----------"
	print "Trench has most certainly been defeated but is not dead."
	print "You can go home, or wherever else you like, if you LEAVE."
	print "Or, to make sure the job is finished, you can PURSUE him."
	print "This is a much more dangerous choice."
	print "LEAVE or PURSUE?"
	choice = raw_input("> ")

	if choice == "LEAVE":
		print "----------"
		print "You decide to leave well enough alone. Trench has surely"
		print "learned not to mess with you."
		print "It gets late before you get back to town,"
		print "so you set up camp for the night."
		print "You make a dinner of salted meat and beer and lay down"
		print "beside the camp fire."
		print "You wake in the night to hear the rumbling of many heavy feet."
		print "Do you OPEN your eyes and see what awaits?"
		print "Or keep them CLOSED and hope it just goes away?"
		choiceL = raw_input("> ")
		
		if choiceL == "OPEN":
			print "----------"
			print "You open your eyes to see Trench standing over you, surrounded"
			print "by dozens of trolls."
			print "Trench - Thank you for giving me the time to gather my strength"
			print "and allies. Apologies for this."
			print "Trench pulls out a small bone whistle and gives it a blow."
			print "The trolls swarm around you"
			print "and pound you into a pile of red goo."
			start()

		elif choiceL == "CLOSED":
			print "----------"
			print "You keep your eyes closed and pretend to stay asleep."
			print "You hear a familiar voice whisper to you."
			print "Trench - A worthy adversary, but foolish and naive."
			print "There is a rustle of pockets, a heavy footstep,"
			print "and instant death."
			start()

		else:
			print "Your body is trampled by the smelly feet of a hundred trolls."
			start()

	elif  choice == "PURSUE":
		print "----------"
		print "You head into the direction you suspect Trench fled in,"
		print "keeping to the shadows."
		print "Dusk falls before you find him,"
		print "licking his wounds near a rotted tree trunk."
		print "He pulls out a small bone whistle and blows it; there is no sound from"
		print "the whistle, but suddenly a hundred torches light up in the trees"
		print "all around you."
		print "A hundred trolls walk towards him, he points in the direction of town,"
		print "and they start marching."
		print "You take this opportunity to assassinate Trench;"
		print "he doesn't even know what hit him. You take his whistle."
		print "By blowing this whistle you can become the KING of trolls, a tyrant lord."
		print "Or you can force the trolls to commit SUICIDE and save the town forever."
		print "Or you can SMASH the whistle into pieces and leave the trolls"
		print "to their own devices."
		print "Will you become KING? Cause mass troll SUICIDE? or SMASH the whistle?"
		choiceP = raw_input("> ")

		if choiceP == "KING":
			print "----------"
			print "You blow the whistle and command the trolls to become"
			print "your minions."
			print "They raise you on high and bring you to their empire"
			print "in the mountain."
			print "From this seat of power, you have the trolls ransack villages,"
			print "pillage their treasures, and hoard them at your feet."
			print "It's good to be king."
			TheEnd()

		elif choiceP == "SUICIDE":
			print "----------"
			print "You call the trolls back and convince them that suicide is the"
			print "only way their alien machine god will accept them."
			print "They all drink the Kool-Aid and die."
			print "A hundred troll spirits rise up to meet their great machine god"
			print "where they feast on apple pie for all eternity."
			print "The town thanks you for your benevolence in saving them forever;"
			print "they raise you to the status of king and all pay homage."
			print "It's good to be king."
			TheEnd()

		elif choiceP == "SMASH":
			print "----------"
			print "You smash the whistle into pieces."
			print "The trolls all snap out of the trance the whistle put them in."
			print "They come back to you and the troll chieftan approaches."
			print "Chief - Oy, was you da one wot smashed da wissle? DAT'S GREAT!"
			print "YOU GONNA BE DA NEW TROLL KING!"
			print "The troll chief pats you on the back."
			print "Unfortunately he hits you way too hard"
			print "and you cough out your heart and lungs."
			print "Maybe it's not so good to be king."
			start()		

		else:
			print "You accidentally swallow the whistle, choke on it, and die."
			start()

	else:
		print "Think hard..."
		Trench_Retreated()

def Trench_Defeated():
	print "----------"
	print "Using one of the swords that Trench so graciously provided for you,"
	print "you hack his head off."
	print "Surely someone will pay for this thing; Trundy must have gone after him"
	print "for something more than JUST troll-loving."
	print "Upon searching his person for anything of value"
	print "(not like he's going to use it, right?), you discover a small bone whistle."
	print "Recognizing this as a traditional troll-whistle, you realize he must have had"
	print "some serious plans; these whistles are very rare."
	print "Making sure nothing ever comes of it, you smash the whistle to pieces. On your"
	print "way back to town, you search Trundy's corpse for some sort of contract."
	print "Sure enough, you find one: a contract for five thousand gold pieces, payable by"
	print "the League of Extraordinary Knights upon receipt of Trench's head."
	print "You return to town, turn in Trench's head to the League, get your five thousand"
	print "gold pieces, and live happily ever after."
	print "I'm sure smashing that bone whistle was enough...right?!"

def WaUn1():
	print "----------"
	print "Deciding against close combat, Trench casually gathers three"
	print "throwing daggers into each hand."
	print "Whip-like arms send the daggers flying frighteningly fast at you."
	print "Will you DODGE the daggers or CATCH them?"
	choice = raw_input("> ")

	if choice == "DODGE":
		print "----------"
		print "You gracefully weave your way through the daggers with"
		print "seemingly time-bending reactions."
		print "Trench finds an opening and closes the distance for another"
		print "melee attack. Will you DISARM or KILL?"
		choiceD = raw_input("> ")
		
		if choiceD == "DISARM":
			print "----------"
			print "Trench approaches with two daggers drawn."
			print "Unfortunately for Trench, he was not expecting your"
			print "seemingly unnatural reaction speed."
			print "You drop to the ground and grab his left arm, twisting and"
			print "pushing it back towards his advance, snapping it at the elbow."
			print "Trench's other arm comes around with the dagger, which you"
			print "stop with the palm of your hand on his wrist."
			print "You tighten your grip and rip the tendons out of his wrist,"
			print "forcing him to drop the dagger."
			print "Trench falls to the ground in agony, rolls onto his side,"
			print "and vanishes in a puff of smoke."
			Trench_Retreated()

		elif choiceD == "KILL":
			print "----------"
			print "Trench approaches with two daggers drawn."
			print "Unfortunately for Trench, the opening he saw"
			print "was not an opening at all."
			print "You drop to your back."
			print "Trench attempts to adjust his trajectory, but you grab"
			print "his hands with yours, forcing him to fall over you."
			print "Rolling on top of him, you bury the daggers into his neck,"
			print "watching every last bit of life drain from his eyes."
			Trench_Defeated()

		else:
			print "You catch a poisoned dagger in your eye. You leap onto"
			print "Trench and bite his throat out before the poison"
			print "takes hold and you die."
			start()

	elif choice == "CATCH":
		print "----------"
		print "You catch three of the daggers and let the other three pass by."
		print "Time to go on the offensive. Will you THROW the daggers back"
		print "or WIELD them?"
		choiceC = raw_input("> ")

		if choiceC == "THROW":
			print "----------"
			print "You send one of the daggers back at him through the air."
			print "He dodges low."
			print "You read the dodge and throw the next dagger to his left,"
			print "deliberately giving him enough time to read the throw"
			print "and dodge right."
			print "The third dagger is thrown without waiting for his dodge,"
			print "so as not to give him time to react."
			print "Trench falls directly into the path of the third dagger,"
			print "which catches him in the ribcage."
			Trench_Defeated()

		elif choiceC == "WIELD":
			print "----------"
			print "The daggers are small enough for you to wield"
			print "two in your right hand and one in your left."
			print "Not expecting this turn of events,"
			print "Trench takes half a step backwards."
			print "This is the exact opening you needed."
			print "You close the distance quickly and swing your right hand"
			print "from high to low across his face."
			print "One dagger cuts clean across his face,"
			print "cutting his right eye and mouth."
			print "The other dagger gets lodged into his left eye socket."
			print "He raises his hands to his face, and you stick the left handed"
			print "dagger under his right arm."
			Trench_Defeated()

		else:
			print "Unfortunately you caught a poisoned dagger by the blade and die."

	else:
		print "The daggers find their mark, two in the eyes, two in the chest,"
		print "and two in the ... you know what, you don't want to know."

def WaDua1():
	print "----------"
	print "Trench's voice seems to be coming from behind you, to the left."
	print "Do you ATTACK or RETREAT?"
	choice = raw_input("> ")
	
	if choice == "ATTACK":
		print "----------"
		print "Will you step and SPIN towards Trench's direction"
		print "or will you turn and LUNGE?"
		choiceA = raw_input("> ")
		
		if choiceA == "SPIN":
			print "----------"
			print "Assuming Trench is indeed behind you to your left, you spin"
			print "in his direction, swords at shoulder level."
			print "Apparently catching Trench off guard, you feel your first sword"
			print "find something hard, hearing a clang of steel on steel"
			print "You feel the sword bounce slightly and the rustle of pieces of"
			print "metal falling on the grass."
			print "The second sword hits something much softer and you feel"
			print "resistance as you come about-face to see your foe."
			print "There are broken daggers on the ground. You can see where your"
			print "first sword landed on his chest, breaking daggers and"
			print "knocking them free of his vest."
			print "You can also see a large gash on his face and one of his arms,"
			print "prizes of the second sword's strike."
			print "There is fury in his eyes, a puff of smoke, and he is gone."
			Trench_Retreated()

		elif choiceA == "LUNGE":
			print "----------"
			print "You turn to find your foe indeed where you suspected."
			print "Unfortunately he reads your turn, and when you lunge"
			print "he avoids the attack."
			print "In his evasion, he digs two daggers deep into your"
			print "right sword arm."
			print "You drop the sword and attempt to slash with the left hand."
			print "Trench avoids this attack as well, tossing a dagger"
			print "into your throat."
			print "Assuming your imminent death, Trench drops his guard slightly."
			print "You take this chance to throw your sword at him."
			print "Not expecting such a ridiculous move, Trench is caught in awe"
			print "as the sword catches him in the ribcage."
			print "You then drown in your own blood."
			start()

		else:
			print "A dagger finds its way into your back and another into your neck."

	elif choice == "RETREAT":
		print "----------"
		print "Fearing an imminent follow-up dagger, you decide to put distance"
		print "between you and your foe."
		print "Will you attempt to BLIND Trench by throwing dirt to cover your escape?"
		print "Or will you SPRINT?"
		choiceR = raw_input("> ")

		if choiceR == "BLIND":
			print "----------"
			print "You grab a handfull of dirt and toss it in his direction"
			print "as you roll away."
			print "The disctraction works; as you roll, you see Trench"
			print "shielding his eyes."
			print "You flee into the tree line, only to find yourself face to"
			print "face with a troll and his twenty troll-friends."
			print "Before you have a chance to react, the troll nails you into"
			print "the dirt like a tent stake."
			start()
		
		elif choiceR == "SPRINT":
			print "----------"
			print "You attempt to simply sprint away from Trench, heading towards"
			print "the tree line as fast as possible."
			print "You hear a crack behind you, and a puff of smoke materializes"
			print "in front of you."
			print "At the very last second, you see Trench appear from the smoke,"
			print "crouched, with two daggers pointed upwards."
			print "There isn't enough time to slow down. You impale yourself upon"
			print "the daggers, skewering your lungs and heart."
			start()

		else:
			print "A dagger is drawn across your throat and another implanted down"
			print "through your collarbone. Instant death."

	else:
		print "The soft sound of footsteps retreating through grass, the faint whistle"
		print "of metal through the air, three flying daggers bury themselves"
		print "into vital organs."
		start()
#EDITING STOPPED HERE
def WaSin1():
	print "----------"
	print "Trench - I will give you one chance. Walk away now, and you live. You have"
	print "no reason to fight me"
	print "Will you FIGHT or LEAVE?"
	choice = raw_input("> ")

	if choice == "LEAVE":
		print "----------"
		print "You turn to leave, Trench keeps his guard up until you are past the"
		print "tree line."
		print "Will you WAIT in the tree line to watch Trench? Or will you CONTINUE"
		print "back to town?"
		choiceL = raw_input("> ")

		if choiceL == "CONTINUE":
			print "----------"
			print "You head back towards town."
			print "Night approaches, and you camp for the night."
			print "You wake in the night to find yourself surrounded by trolls"
			print "wielding torches and clubs."
			print "Trench steps through the crowd of trolls."
			print "Trench - Can't have you warning the townsfolk"
			print "Before you can reach for your sword, a troll smashes your"
			print "skull in with his club."
			start()

		elif choiceL == "WAIT":
			print "----------"
			print "Once past the tree line, you hide in the shadows."
			print "Trench waits for a long time looking at the tree line,"
			print "scanning for movement."
			print "Once he is sufficiently convinced that you have moved on,"
			print "he pulls a small bone whistle out of his vest."
			print "He blows into it, there is no audible sound, but suddenly the"
			print "ground trembles ever so slightly."
			print "Trolls emerge from the treeline, hundreds of them, holding"
			print "unlit torches and clubs."
			print "They march towards the town, lighting the torches as dusk falls."
			print "You decide it might be best to seek your fortunes elsewhere"
			print "in this world, and head the opposite direction."
			start()
	
		else:
			print "A troll rushes out of the woods and screams"
			print "'FOR DA TROLL EMPIRE' and smashes your face"
			print "before you can react."
			start()

	elif choice == "FIGHT":
		print "----------"
		print "You ready your sword, taking a posture that is"
		print "equally defensive and offensive."
		print "Trench - Very well, have it your way."
		print "Will you attack HIGH or LOW?"
		choiceF = raw_input("> ")

		if choiceF == "LOW":
			print "----------"
			print "You sidestep towards Trench, who instantly countersteps."
			print "With the mobility provided by a single blade, you are"
			print "able to make a low sweeping attack during his counterstep."
			print "Trench performes a backflip to avoid the slash, throwing"
			print "three daggers on his landing."
			print "Crouching to avoid the daggers, you return with an upward"
			print "thrust that catches Trench in the belly"
			print "Trench's mouth fills with blood and he slumps over, dead"
			Trench_Defeated()

		elif choiceF == "HIGH":
			print "----------"
			print "You come down upon Trench with an overhead swing."
			print "Trench dodges low to avoid it and returns with a"
			print "dagger to your side."
			print "You gracefully return your sword towards his arm,"
			print "slicing deep into elbow pit."
			print "Trench drops the dagger and springs backwards."
			print "You pick up the dagger, and throw it at him. While he dodges"
			print "the dagger, you catch his hamstring with your sword."
			print "Trench lets out a pained and angry cry as there is a puff of"
			print "smoke, and he is gone."
			Trench_Retreated()

		else:
			print "Before you can act, Trench vanishes in smoke, a dagger flies"
			print "from the tree line, you attempt to dodge but it grazes your"
			print "cheek. You die instantly."
			start()

	else:
		print "Suddenly the forest erupts in flames, terrified trolls run screaming"
		print "from the trees into the clearing, tampling both you and Trench."
		start()

def AtUn1():
	print "----------"
	print "You notice that the particular dagger you took from him"
	print "appears to be coated in poison."
	print "The dagger is large enough for you to WIELD it,"
	print "but also light enough for you to THROW it."
	choice = raw_input("WIELD or THROW?> ")

	if choice == "WIELD":
		print "----------"
		print "ATTACK or WAIT?"
		choiceW = raw_input("> ")
		
		if choiceW == "ATTACK":
			print "----------"
			print "Not wasting a single moment, you rush Trench with the dagger"
			print "Your speed takes him by surprise, but he has become wary of you."
			print "Trench redirects your dagger arm, and breaks your wrist, knowing"
			print "all too well what poison is on the dagger."
			print "But his tunnel vision on the poisoned dagger leaves your"
			print "other arm free. You manage to grab another dagger from his vest."
			print "Before he can react, you draw the dagger across his throat."
			Trench_Defeated()

		elif choiceW == "WAIT":
			print "----------"
			print "Waiting to see Trench's reaction, you notice just a hint of"
			print "worry in his eye as he realizes which dagger you took."
			print "There is a puff of smoke and Trench disappears"
			print "You notice a subtle shift of the smoke to the left and make"
			print "a low slash toward it"
			print "As Trench's back foot was indeed the last thing to leave the"
			print "smoke, you catch his achille\'s heel with the blade"
			print "There is no sound other than the thud of grass cushioning a"
			print "body hitting the soil"
			print "The small cut you made through his boot was enough to get the"
			print "poison into his bloodstream, killing Trench instantly"
			Trench_Defeated()
	
		else:
			print "You taste the poison on the dagger, just to see what it tastes"
			print "like, and fall down dead."	

	if choice == "THROW":
		print "----------"
		print "Will you FOLLOW up on the throw? Or will you RETREAT after throwing?"
		choiceT = raw_input("FOLLOW or RETREAT?> ")
		
		if choiceT == "FOLLOW":
			print "----------"
			print "You hurl the dagger at Trench. Knowing full-well what poison"
			print "is on the dagger, Trench makes all efforts to evade the."
			print "flying dagger. Trench leaves an opening while evading the"
			print "dagger, you move to his side, pull another dagger from"
			print "his vest, and stick it in his neck."
			print "Trench falls to the ground grabbing for the dagger in his neck."
			print "Leaving nothing to chance, you pull another dagger from his vest,"
			print "hold one of Trench's arms down and cut the subclavial artery,"
			print "then the femoral artery."
			Trench_Defeated()

		elif choiceT == "RETREAT":
			print "----------"
			print "You hurl the dagger at Trench. Knowing full-well what poison is"
			print "on the blade, Trench makes all efforts to evade the"
			print "flying steel."
			print "You take a step back to see the result and give yourself room"
			print "to breathe."
			print "Trench avoids the flying dagger, but leaves an opening that you"
			print "are unable to capitalize on due to your distance from him"
			print "Once Trench recovers, there is a cloud of smoke, and he is gone."
			Trench_Retreated()

		else:
			print "You fumble the throw and drop the dagger. You attempt to catch"
			print "it but unfortunately grab the poisoned blade. The end."
			start()

def AtDua1():
	print "----------"
	print "Do you LEAVE the dagger in or REMOVE it?"
	choice = raw_input("LEAVE or REMOVE?> ")

	if choice == "LEAVE":
		print "----------"
		print "You don't bother wasting time removing the dagger,"
		print "do you ATTACK or RETREAT?"
		choiceL = raw_input("> ")
	
		if choiceL == "ATTACK":
			print "----------"
			print "The pain of the dagger in your side sends you into overdrive."
			print "You attack again, in a flurry of swords, desperation giving"
			print "you clarity on your target."
			print "The attack comes so furiously and the attacks so deliberate"
			print "that Trench is caught off guard."
			print "He avoids the first three swings, but your attacks continue"
			print "unabated until one finds its mark."
			print "Trench's leg is caught with your left sword, which slows him"
			print "down for just an instant."
			print "Seeing the opening, your right sword is inserted into his"
			print "abdomen. The left sword comes up to remove his head."
			print "Before continuing, you remove the dagger carefully and bandage"
			print "it up before you bleed out."
			Trench_Defeated()
	
		elif choiceL == "RETREAT":
			print "----------"
			print "Thinking it better not to get another dagger in the side,"
			print "you take a step back."
			print "There is a glint in Trench's eyes, he seems to vanish"
			print "There is another sharp pain in your other side as Trench"
			print "reappears next to you, burying a dagger into you"
			print "You flail at him but the damage is done."
			print "A dagger finds your neck, and Trench stands over you."
			print "Trench - Sssh*GLCK*"
			print "Just before your eyes shut forever, you shove your sword"
			print "into his mouth."
			start()
		else:
			print "You adjust the wrong way, the dagger cuts into something"
			print "serious, and you die before you can move."
			start()

	elif choice == "REMOVE":
		print "----------"
		print "You quickly, perhaps too quickly, remove the dagger from your side,"
		print "there is a sudden gush of blood. Do you ATTACK or RETREAT?"
		choiceR = raw_input("> ")

		if choiceR == "ATTACK":
			print "----------"
			print "Knowing that you have precious little time before you bleed out,"
			print "you decide to make a last ditch attack."
			print "With literally nothing left to lose, you throw caution to the"
			print "wind and attack in a flurry of strikes."
			print "Your reckless strikes leave an opening which Trench takes"
			print "advantage of, sticking a dagger into your shoulder."
			print "When you swing in his direction, he weaves and slices the artery"
			print "in your leg."
			print "You fall to your knees, quickly losing all strength."
			print "Trench stands over you, preparing to cut your throat and end it."
			print "Unfortunately for him he gets a little too close."
			print "Just before you fall for the last time, you summon your last"
			print "bit of strength to raise your sword into his manhood."
			start()

		elif choiceR == "RETREAT":
			print "----------"
			print "You step back, looking at the wound, realizing that removing"
			print "the dagger has sealed your fate"
			print "You look up to see where Trench is, and where the next blow"
			print "may come from."
			print "Having seen the severity of the bleed, Trench has vanished"
			print "knowing your fate."
			print "You attempt to staunch the bleeding and bandage the wound,"
			print "but the hasty removal of the dagger in the middle of combat"
			print "did too much damage. You calmly sit down, and close your eyes."
			start()

	else:
		print "You adjust the wrong way, the dagger cuts into something serious,"
		print "and you die before youc an move."
		start()
	
def AtSin1():
	print "----------"
	print "There is a small flash to your LEFT and a soft thud to your RIGHT"
	print "Do you move LEFT or RIGHT?"
	move = raw_input("> ")

	if move == "RIGHT":
		print "----------"
		print "Do you ATTACK or DEFEND?"
		moveR = raw_input("> ")

		if moveR == "ATTACK":
			print "----------"
			print "You blindly attack what you suspect to be the true"
			print "location of Trench"
			print "You feel the unmistakable bite of steel into flesh as your"
			print "sword finds a mark"
			print "There is a grunt and you see Trench laying on the ground,"
			print "his shoulder severly wounded"
			print "Trench - I admit defeat. I have to wonder why a warrior" 
			print "with such prowess with a blade was following that miserable"
			print "drunk Trundy. Unless...do you know?!"
			Trench_Defeated()

		elif moveR == "DEFEND":
			print "----------"
			print "You move where you suspect the attack to come from and"
			print "prepare yourself"
			print "There is the unmistakable clash of steel on steel as a dagger"
			print "bounces off your sword."
			print "The second blow comes, a manual dagger thrust at the throat"
			print "This blow, too, is knocked away by you."
			print "A voice comes from the shadow - Very well. We shall call it a"
			print "draw. Pray we never meet again."
			Trench_Retreated()
		
		else:
			print "A dagger finds its way between your ribs. You try to scream"
			print "but another dagger finds your throat."
			print "Trench - Sshhh..."
			start()	

	elif move == "LEFT":
		print "----------"
		print "Do you DEFEND or RETREAT?"
		moveL = raw_input("> ")

		if moveL == "DEFEND":
			print "----------"
			print "You step in the direction of Trench's distraction and prepare"
			print "yourself for the coming attack"
			print "There is a cloud of smoke where the thud sounded from"
			print "You just catch a glimpse of two daggers, held by gloved hands,"
			print "materializing from the smoke."
			print "Avoiding the attack altogether, Trench again disappears."
			print "A voice comes from the shadows - Very well. We shall call it a"
			print "draw. Pray we never meet again."
			Trench_Retreated()

		elif moveL == "Retreat":
			print "----------"
			print "You move towards Trench's distraction flash, then roll"
			print "backwards to safety."
			print "There is a cloud of smoke where the thud sounded from."
			print "The smoke dissipates, the clearing is now completely empty,"
			print "save for the sword you did not take."
			print "A voice comes from the shadows at the tree line - Very well."
			print "I see you are no fool. We shall meet again."
			Trench_Retreated()

		else:
			print "A dagger finds its way between your ribs. You try to scream but"
			print "another dagger finds your throat."
			print "Trench - Sshh..."
			start()
	else:
		print "A pang of pain in your side, soft warmth, tired...so tired..."
		start()

def trench_fight():
	single = False
	dual = False
	unarmed = False
	print "----------"
	print "Trench - So, troll-killer, how will you arm yourself? ONE sword?"
	print "TWO swords? Or NONE?"
	
	armed = raw_input("How many swords will you take? ONE? TWO? Or NONE?\n> ")
	
	if armed == "ONE":
		print "----------"
		print "You grab the stronger-looking of the two swords. One will make you agile"
		print "while still dangerous"
		print "Trench - A wise choice, but it will not save you"
		single = True

	elif armed == "TWO":
		print "----------"
		print "You grab both swords. Maximum destruction. You know how to"
		print "use two swords at once right?"
		print "Trench - A bold choice, somehow I doubt you know how to use"
		print "those though..."
		dual = True

	elif armed == "NONE":
		print "----------"
		print "WEAPONS ARE FOR COWARDS!!"
		print "Trench - Interesting choice, I may have underestimated you..."
		unarmed = True

	else:
		print "Trench - Poor choice"
		print "Trench seems to vanish, there is a sharp sting in your side,"
		print "then your back, then your neck, and everything goes dark"
		start()
	
	print "----------" 
	print "Trench - Shall we begin then? Would you like to make the first move or shall I?"

	move1 = raw_input("ATTACK or WAIT?\n> ")

	if move1 == "ATTACK" and single:
		print "----------"
		print "You perform an elegant quick strike with the sword,"
		print "dashing towards Trench."
		print "He avoids the attack with relative ease, during his feint he draws"
		print "one of his daggers."
		print "You see the drawn dagger and manage to avoid his counter strike"
		print "Trench - Very good."
		AtSin1()
	
	elif move1 == "ATTACK" and dual:
		print "----------"
		print "You perform a furious barrage of (clumsy) strikes with your swords."
		print "Trench manages to wheel away from your flurry and in his feint sticks a dagger in your side."
		print "Trench - As I thought..."
		AtDua1()

	elif move1 == "ATTACK" and unarmed:
		print "----------"
		print "You lunge at Trench, faster than he expected. He attempts to spin out"
		print "of the way."
		print "He escapes your attack, but you catch his arm for a brief moment and"
		print "grab one of the daggers from his vest with your left hand."
		print "*muttering* Trench - indeed..."
		AtUn1()

	elif move1 == "WAIT" and single:
		print "----------"
		print "You stand there staring at eachother, neither making the first move."
		WaSin1()

	elif move1 == "WAIT" and dual:
		print "----------"
		print "Trench sends two daggers hurtling towards you."
		print "With your left handed sword you block the incoming daggers and at the"
		print "last moment notice that Trench is suddenly beside you."
		print "He attempts to bury a dagger into your kidney but you deflect the blow"
		print "with your right handed sword."
		print "With neither party dealing damage, Trench seems to vanish before you"
		print "can strike a blow."
		print "Trench - Hmmm..."
		WaDua1()

	elif move1 == "WAIT" and unarmed:
		print "----------"
		print "You can see uncertainty in Trench's eyes"
		print "Trench approaches, rather quickly, seeming to pass by your right side."
		print "At the last moment, he feints to your left and attempts to stick a"
		print "dagger in your heart."
		print "You push his dagger arm out of the way enough that it only grazes"
		print "your chest."
		print "With one fluid motion, you disarm the heart-seeking dagger from him and"
		print "insert it into his thigh."
		print "Trench's eyes fill with fury and doubt as he unflinchingly removes"
		print "the dagger from his leg."
		WaUn1()
	else:
		print "Trench - Too slow"
		print "There is a puff of smoke, a flash of blood, and then darkness."
		start()

def forest_continue():
	print "----------"
	print "One troll down, which you suspect is probably one more troll than that"
	print "bloody drunk Trundy ever defeated."
	print "How hard could it be to take down this Trench fellow?"
	print "After continuing on in the woods for a few hours, you come to the edge of a"
	print "clearing. Do you INSPECT or CONTINUE?"

	choice1 = raw_input("> ")

	if choice1 == "INSPECT":
		print "----------"
		print "You notice two crossed swords in the centre of the clearing"
		print "On the far side of the clearing you can just barely make out a cloaked,"
		print "shadowy figure standing in the trees"
		print "Trench - Ah I see you've noticed me. Well that will ruin"
		print "my plan to surprise you."

	elif choice2 == "CONTINUE":
		print "----------"
		print "Boldly striding into the clearing, you pay no heed to your"
		print "surroundings."
		print "What threat could anything possibly pose to someone who can defeat"
		print "a troll so handily?"
		print "There is a sharp sting in the side of your neck. Just before your"
		print "eyes close forever a cloaked man walks up to you"
		print "Trench - It would have been wiser to talk to me in the Tavern"
		print "you fool. Who follows a beligerent drunk like that anyways?!"
		start()

	else:
		print "You stumble out of the tree line, slip on a pile of leaves, break your neck, and die."
		start()

	print "----------"
	print "Trench - I must confess however, I am surprised to see that Trundy did"
	print "not make it. Seems like all her grandeur was hot air?"
	print "Trench - Why did you continue? You don\'t have the contract, you don\'t"
	print "know who I am, what could possibly be your motive?"
	print "What is your motive?"
	motive = raw_input("> ")
	
	print "Trench - %s? Really? You didn't strike me as that type in the tavern." % motive
	print "Trench - I suppose it can't be helped though, you are here to die in"
	print "Trundy's place."
	print "Trench - As you noticed, I have brought two swords. They are both for you."
	print "You will see I don't need one."
	print "Trench removes his cloak, revealing a large number of daggers, some for"
	print "throwing and some for manual handling"
	trench_fight()

def knight_quest():
	print "----------"
	print "You have decided to help Trundy kill a troll-lover. Truly a noble task." 
	print "You have left the Tavern and headed North into the woods as instructed." 
	print "You forgot to bring any weapons with you, but surely Trundy remembered"
	print "a spare for you."
 	print "You aren't walking for long before you hear a familiar drunken voice"
	print "shouting through the trees."
	print "---"
	print "Trundy - Oh you think yer so scary ye big ugly troll!"
	print "Troll - Yer that wretched little metal lady wot took my gold when"
	print "I was havin a sleep! The same one wot kicked me bruver in the shin"
	print "an ran away wif his gold too!!"
	print "Trundy - Quick! Distract this troll so I can kill him again! Musta"
	print "somehow survived me killin blow last time we fought!"
	print "Troll - Listen lady we aint neva fought or I woulda squamshed ya!"
	distraction = raw_input("DISTRACT THE TROLL!\n> ")
	print "----------"
	print "You %s, which actually distracts Trundy more than the troll. In her" % distraction
	print "distraction, Trundy momentarily drops her guard and the troll knocks"
	print "her head clean off her shoulders."
	troll_fight1()

def troll_fight1():
	armed = False
	print "----------"
	print "The troll slowly lumbers towards you, awkwardly and slowly"
	print "Troll - Oy wot on erf are you doin? Did you just try a kill me?!"
	print "Troll - You was wif dat stupid metal lady, which means you stole my"
	print "gold too! I HATE PEOPLE WHO STEAL MY GOLD!!"
	print "The troll winds up for a swing. The blow will kill you if it lands,"
	print "but the attack is easily read and avoidable. Do you DODGE or ATTACK?"
	
	choice1 = raw_input("> ")
	
	if choice1 == "DODGE":
		print "----------"
		print "You easily roll out of the way of the slow dumb troll and find"
		print "yourself next to Trundy's Dead body."
		print "Seeing as you weren't equipped with any weapons to start with,"
		print "you decide to pick up Trundy's broadsword"
		print "(sure hope you know how to use that)"
		armed = True

	elif choice1 == "ATTACK":
		print "----------"
		print "You don't actually have a weapon, but that doesn't stop you from"
		print "jumping onto the troll's face and pulling out one of his eyeballs."

	else:
		print "The troll smashes you and grinds you into a pulp. No one remembers you."
		print "Your story is never told. You accomplished nothing."
		start()

	print "The troll is furious now, he reels and winds up for a wild sweeping attack."
	print "Do you ATTACK or DODGE?"

	choice2 = raw_input("> ")

	if choice2 == "ATTACK" and armed:
		print "----------"
		print "Before the troll can execute his attack, you bury your sword into"
		print "its belly. You heave upwards with all your might until the sword"
		print "catches on the bottom of the troll's ribcage"
		print "The sword snaps at the hilt, the trolls guts spill all over you,"
		print "and you revel in your newfound troll-killing glory."
		print "You decide to continue Trundy's quest alone, since you are the"
		print "new troll-killer in town"
		forest_continue()

	elif choice2 ==  "ATTACK" and not armed:
		print "----------"
		print "Emboldened by your previous maiming of the troll, you decide that"
		print "weapons are for cowards anyways. You prepare to leap at the troll"
		print "again and remove his other stinking eye"
		print "You leap at the troll again, which causes the troll to drop his"
		print "club, turn, and flee in sheer terror at the prospect of losing"
		print "his only remaining good eye."
		forest_continue()

	elif choice2 ==  "DODGE" and armed:
		print "----------"
		print "The troll has caught on to your rolling tactic. The blow comes so"
		print "wildly that it catches you in the middle of your attempted evasion."
		print "You are tossed 10 feet in the air, when you land the troll stomps"
		print "on you, then smashes your body, then eats your guts. He turns your"
		print "skull into a fancy candy dish for house parties."
		start()

	elif choice2 == "DODGE" and not armed:
		print "----------"
		print "He may only have one good eye, but he is mad now and swinging like"
		print "a maniac. You avoid the first swing with your roll"
		print "(thank goodness for poor depth perception)."
		print "You find yourself lying next to Trundy's dead body and notice her"
		print "broadsword on the ground. You go to pick it up but before you manage"
		print "to grab it the next wild blow comes at you."
		print "Unfortunately you have no time to react to this blow, the troll"
		print "smashes you to pieces. The troll then uses your hide as a fancy"
		print "throw rug and becomes the envy of all the trolls in northern hillshire."
		start()

	else:
		print "The troll pounds your face in, opens you up, and uses your bladder"
		print "as a baseball catcher's mitt."
		start()

def knight():
	print "----------"
	print "Knight - I earn me my as a bounty hunter of shorts."
	print "Knight - This one time *hic* I trolled a kill and took all his gold HA!"
	print "HAHA! *HURRP*Aahhh"
	print "Knight - I am pretty much the most famous troll-killer in history."
	print "Knight - They call me Troll-Kill Trundy, but me real name is Brenda."
	print "Trundy -  waddya think o that?!" 

	Thoughts = raw_input("Well,what do you think?!\n> ")

	print "----------"
	print "Completely oblivious to anything you had said or done, Trundy continues."
	print "Trundy - Ash it happens, I'm acshully hunting a person right now."
	print "Trundy - Some miserable troll-lover name Trench. Say, you wanna come with me?"
	print "Trundy - you can see the mighty troller-kill in action!"
	print "Trundy - I tell you what, we can shplit the bounty 70/70, I need someone to" 
	print "spread the word of my greatnesssssshhhh anyways. WADYA SAY?!"
	
	knight_choice = raw_input("YES or NO?\n> ")

	if knight_choice == "NO":
		print "----------"
		print "Trundy - Well I cannae blame yeh. Trollsh are some scary beasts."
		print "I can't even imagine what I'd do if I saw one in real life!"
		tavern()
	elif knight_choice == "YES":
		print "----------"
		print "Trundy - ahHA! I'm just going to have a drink little more then you can "
		print "meet me up north! Just LEAVE TAVERN and HEAD NORTH!"
		knight_quest()
	else:
		print "Trundy-I couldnae understand ye, was that a YES or a NO?"
	
def tavern():
	print "----------"
	print "You are in a tavern. The smell of pipe smoke, cheap beer, and blood hang in the"
	print "air. Despite the large tavern, there are only 3 patrons present, and the"
	print "TAVERNKEEP himself. The first person you see is a KNIGHT, sitting alone at the"
	print "largest and most central table. The table itself is littered with empty beer"
	print "mugs. The second person you see is a CLOAKED MAN smoking a pipe by the window." 
	print "It is clear by his table that he has not ordered anything."
	print "The last patron you see is a pair of CHILDREN who are far too young to be here."
	print "And of course there is the TAVERNKEEP himself here as well."
	print "Will you talk to the KNIGHT? The TAVERNKEEP? The CLOAKED MAN? Or the CHILDREN?"
	print "Or will you LEAVE TAVERN?"
	
	talk_choice = raw_input ("> ")
	
	if talk_choice == "KNIGHT":
		knight()
	
	elif talk_choice == "TAVERNKEEP":
		tavernkeep()
	
	elif talk_choice == "CLOAKED MAN":
		cloaked_man()
	
	elif talk_choice == "CHILDREN":
		children()
	
	elif talk_choice == "LEAVE TAVERN":
		start()
	
	else:
		print "Maybe you should think about your choices a little more..."
		tavern()
		
def start():
	print "----------"
	print "You stand infront of a tavern."
	print "You may choose to ENTER to get a drink and maybe an adventure."
	print "Or you may choose to LEAVE and vanish into the void."
	print "ENTER or LEAVE?"
	choice = raw_input("> ")

	if choice == "ENTER":
		"You enter the tavern..."
		tavern()

	elif choice == "LEAVE":
		"You vanish into absolute nothingness"
		exit(0)	

	else:
		print "You should probably ENTER or LEAVE"
		start()
	
start()
