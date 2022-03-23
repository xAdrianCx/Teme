"""
c. Optionale (may need google)
16.
Ne imaginam o echipa de fotbal pt teren sintetic.
3 Schimbari maxime admise

Declara o Lista cu 5 jucatori
Schimbari_efectuate = va jucati voi cu valori diferite
Schimbari_max = 3

Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
Efectuam schimbarea 
Stergem jucatorul scos din lista
Adaugam jucatorul intrat
Afisam a intra x, a iesit y, mai aveti z schimbari
Daca jucatorul nu e in teren:
Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
Afisati ‘mai aveti z schimbari’

Testati codul cu diferite valori

Google search hint
“how to check if item is in list python”
"""

# Rezolvare:
# Presupunem ca schimbarile pe care le efectuam sunt post-pe-post si sunt 
# diferite de " "(spatiu liber). 
# Mergeau un while si-un for "ca unse" aici. :)

# Define a list of 5 players that are already on the field.
players_on_field = ["Alin", "Claudiu", "Dani", "Lucian", "Laurentiu"]
# Define a list to verify who was on the field already.
was_on_field = []
# Set a maximum number of changes.
schimbari_max = 3
# Verify how many changes has been done.
schimbari_efectuate = 0
number_of_changes = int(input("You can do 3 changes max." + 
	"\nHow many changes do you want to do, coach? "))
if number_of_changes <= 3 and number_of_changes >= 1:
	# At tis time we want to make only 1 change.
	if number_of_changes == 1:
		player_1_out = input("Enter the name of the player you want out: ")
		player_1_in = input("Enter the name of the player you want in: ")
		# If the player is on the field.
		if player_1_out.title() in players_on_field:
			# If player_1_in is not on the field.
			if player_1_in.title() not in players_on_field:	
				# Substract a change.
				schimbari_max -= 1
				# Add a change.
				schimbari_efectuate += 1
				# Show the switch.
				print(f"Change: {player_1_out.title()} OUT, {player_1_in.title()} IN." + 
					f" Changes left: {schimbari_max}. Changes made: {schimbari_efectuate}.")
				# Add the new player on the field.
				players_on_field.append(player_1_in.title())
				# Show the players on the field after the change.
				print(f"Players on the field after the change: {players_on_field}.")			
			# If player_1_in was already on the field we can't make the switch.	
			elif player_1_in.title() in players_on_field:
				print(f"Can't make the swap because {player_1_in.title()} is on the field already.")
		# If the player is not on the field. (coach might be high if he tries this) :)	
		elif player_1_out.title() not in players_on_field:
			# Tell the coach that the player he wants to send out is not on the field.
			print(f"{player_1_out.title()} is not of the field. We cannot make that change.") 
	# Now we want to make two changes at the same time.		
	elif number_of_changes == 2:
		player_1_out = input("Enter the name of the 1st player you want out: ")
		player_2_out = input("Enter the name of the 2nd player you want out: ")
		player_1_in = input("Enter the name of the 1st player you want in: ")
		player_2_in = input("Enter the name of the 2nd player you want in: ")
		# If 1st player isn't on the field.
		if ((player_1_out.title() not in players_on_field) and (player_2_out.title() in players_on_field)):
			# Tell the coach that the 1st player isn't on the field.
			print(f"{player_1_out.title()} isn't on the field. We can't make that change.") 
			# If player_2_in is on the field we can't make the change.	
			if player_2_in.title() in players_on_field:	
				print(f"{player_2_in.title()} is already on the field. Can't make the change.")
			else:	
				# Make the change for the 2nd player.
				# Substract a change.
				schimbari_max -= 1
				# Add a change.
				schimbari_efectuate += 1
				# Show the 2nd swap.
				print(f"Change: {player_2_out.title()} OUT, {player_2_in.title()} IN." + 
					f" Changes left: {schimbari_max}. Changes made: {schimbari_efectuate}.")
				# Take the 2nd changed player out of the list.
				players_on_field.remove(player_2_out.title())
				# Add the 2nd new player to the list.
				players_on_field.append(player_2_in.title())
				# Show the players on the field after the change.
				print(f"Players on the field after the change: {players_on_field}.")
		# If the 2nd player isn't on the field.
		elif ((player_1_out.title() in players_on_field) and (player_2_out.title() not in players_on_field)):
			# If player_1_in is on field, can't make the change.	
			if player_1_in.title() in players_on_field:
				print(f"{player_1_in.title()} is already on the field. Can't make the change.")
			elif player_1_in.title() not in players_on_field:
				# Substract a change.
				schimbari_max -= 1
				# Add a change.
				schimbari_efectuate += 1
				# Take the 1st changed player out of the list.
				players_on_field.remove(player_1_out.title())
				# Add the 1st new player to the list.
				players_on_field.append(player_1_in.title())
				# Show the 1st switch.
				print(f"Change: {player_1_out.title()} OUT, {player_1_in.title()} IN." + 
					f" Changes left: {schimbari_max}. Changes made: {schimbari_efectuate}")
				# Show the players on the field after the change.
				print(f"Players on the field after the change: {players_on_field}.")
			# Tell the coach that the 2nd player isn't on the field.
			print(f"{player_2_out.title()} isn't on the field. We can't make that change.")		
		# If both are on the field.
		elif player_1_out.title() and player_2_out.title() in players_on_field:
			# If the players we want in are not on the field already.
			if ((player_1_in.title() not in players_on_field) and (player_2_in.title() not in players_on_field)):	
				# Remove the 1st player from the players_on_field.
				players_on_field.remove(player_1_out.title())
				# Remove 2nd player from players_on_field.
				players_on_field.remove(player_2_out.title())
				#Add the 2 players to players_on_field.
				players_on_field.append(player_1_in.title())
				players_on_field.append(player_2_in.title())
				# Substract changes.
				schimbari_max -= 2
				# Add changes.
				schimbari_efectuate += 2
				# Show the swap.
				print(f"Change: {player_1_out.title()} and {player_2_out.title()} OUT, {player_1_in.title()} and {player_2_in.title()} IN." + 
					f" Changes left: {schimbari_max}. Changes made: {schimbari_efectuate}.")
				# Show the players on the field after the change.
				print(f"Players on the field after the change: {players_on_field}.")
			# If player_1_in just got send out.	
			elif player_1_in.title() in players_on_field and player_2_in.title() not in players_on_field:	
				# Substract changes.
				schimbari_max -= 1
				# Add changes.
				schimbari_efectuate += 1
				# Remove player_2_out from players_on_field.
				players_on_field.remove(player_2_out.title())
				# Add player_2_in to players_on_field.
				players_on_field.append(player_2_in.title())
				# Show changes.
				print(f"Change: {player_2_out.title()} OUT, {player_2_in.title()} IN." + 
					f" Changes left: {schimbari_max}. Changes made: {schimbari_efectuate}.")
				# If we want to swap the same player.
				if player_1_in.title() == player_1_out.title():
					# Tell the coach that the player he wants to send in is already on the field.
					print(f"{player_1_in.title()} is already on the field. Can't make the change.")
				# Show the players on the field after the change.
				print(f"Players on the field after the change: {players_on_field}.")
			# If player_2_in just got send out.			
			elif player_1_in.title() not in players_on_field and player_2_in.title() in players_on_field:
				# Substract changes.
				schimbari_max -= 1
				# Add changes.
				schimbari_efectuate += 1
				# Remove player_2_out from players_on_field.
				players_on_field.remove(player_1_out.title())
				# Add player_2_in to players_on_field.
				players_on_field.append(player_1_in.title())
				# Show changes.
				print(f"Change: {player_1_out.title()} OUT, {player_1_in.title()} IN." + 
					f" Changes left: {schimbari_max}. Changes made: {schimbari_efectuate}.")	
				# If we want to swap the same player.
				if player_2_in.title() == player_2_out.title():
					# Tell the coach that the player he wants to send in is already on the field.
					print(f"{player_2_in.title()} is already on the field. Can't make the change.")
				# Show the players on the field after the change.
				print(f"Players on the field after the change: {players_on_field}.") 
			# If both players you want IN are on field.
			elif player_1_in.title() and player_2_in.title() in players_on_field:
				print(f"Both players you want IN are already on the field. Can't make any changes.")										
		# If both players are not on the field. (coach might be high if he tries this) :)	
		elif player_1_out.title() and player_2_out.title() not in players_on_field:
			# Tell the coach that the player he wants to send out is not on the field.
			print(f"{player_1_out.title()} and {player_2_out.title()} are not of the field. We can't make any changes.")
	# We want to make all 3 changes at once.		
	elif number_of_changes == 3:
		player_1_out = input("Enter the name of the 1st player you want out: ")
		player_2_out = input("Enter the name of the 2nd player you want out: ")
		player_3_out = input("Enter the name of the 3rd player you want out: ")
		player_1_in = input("Enter the name of the 1st player you want in: ")
		player_2_in = input("Enter the name of the 2nd player you want in: ")
		player_3_in = input("Enter the name of the 3rd player you want in: ")
		# If player 1 and 2 are on the field, but player 3 isn't on the field.
		if ((player_1_out.title() and player_2_out.title() in players_on_field) and (player_3_out.title() not in players_on_field)):
			# If 2 players we want in are not on the field already.
			if ((player_1_in.title() not in players_on_field) and (player_2_in.title() not in players_on_field)):
				# Remove the 1st player from the players_on_field.
				players_on_field.remove(player_1_out.title())
				# Remove 2nd player from players_on_field.
				players_on_field.remove(player_2_out.title())
				# Add 2nd player to was_on_field.
				players_on_field.append(player_1_in.title())
				players_on_field.append(player_2_in.title())
				# Substract changes.
				schimbari_max -= 2
				# Add changes.
				schimbari_efectuate += 2
				# Show the swap.
				print(f"Change: {player_1_out.title()} and {player_2_out.title()} OUT, {player_1_in.title()} and {player_2_in.title()} IN." + 
					f"  Changes left: {schimbari_max}. Changes made: {schimbari_efectuate}.")
				# player_3_out is not on the field, so cannot be exchanged.
				print(f"{player_3_out.title()} is not on the field. Can't make the change.")
				# Show the players on the field after the change.
				print(f"Players on the field after the change: {players_on_field}.")
			# If player_1_in just got send out.	
			elif player_1_in.title() in players_on_field and player_2_in.title() not in players_on_field:
				# Substract changes.
				schimbari_max -= 1
				# Add changes.
				schimbari_efectuate += 1
				# Remove player_2_out from players_on_field.
				players_on_field.remove(player_2_out.title())
				# Add player_2_in to players_on_field.
				players_on_field.append(player_2_in.title())
				# Show changes.
				print(f"Change: {player_2_out.title()} OUT, {player_2_in.title()} IN." + 
					f" Changes left: {schimbari_max}. Changes made: {schimbari_efectuate}.")
				# player_3_out is not on the field, so cannot be exchanged.
				print(f"{player_3_out.title()} is not on the field. Can't make the change.")
			# If player_2_in just got send out.			
			elif player_1_in.title() not in players_on_field and player_2_in.title() in players_on_field:
				# Substract changes.
				schimbari_max -= 1
				# Add changes.
				schimbari_efectuate += 1
				# Remove player_1_out from players_on_field.
				players_on_field.remove(player_1_out.title())
				# Add player_1_in to players_on_field.
				players_on_field.append(player_1_in.title())
				# Show changes.
				print(f"Change: {player_1_out.title()} OUT, {player_1_in.title()} IN." + 
					f" Changes left: {schimbari_max}. Changes made: {schimbari_efectuate}.")
				# player_3_out is not on the field, so cannot be exchanged.
				print(f"{player_3_out.title()} is not on the field. Can't make the change.")
			# If both players you want IN are on field.
			elif player_1_in.title() and player_2_in.title() in players_on_field:
				print(f"2 of the players you want IN are already on the field. Can't make the change.")					
				# player_3_out is not on the field, so cannot be exchanged.
				print(f"3rd player, '{player_3_out.title()}' is not on the field. Can't make the change.")
				# Done here.
		# If player 1 is on the field, but player 2 and 3 are not on the field.
		elif ((player_1_out.title() in players_on_field) and (player_2_out.title() and player_3_out.title()	not in players_on_field)):
			# If player_1_in is not on the field.
			if player_1_in.title() not in players_on_field:	
				# Substract a change.
				schimbari_max -= 1
				# Add a change.
				schimbari_efectuate += 1
				# Remove a player from players_on_field.
				players_on_field.remove(player_1_out.title())
				# Add the new player to the list.
				players_on_field.append(player_1_in.title())
				# Show the switch.
				print(f"Change: {player_1_out.title()} OUT, {player_1_in.title()} IN." + 
					f" Changes left: {schimbari_max}. Changes made: {schimbari_efectuate}.")
				# player_2_out is not on the field, so cannot be exchanged.
				print(f"2nd player, '{player_2_out.title()}' is not on the field. Can't make the change.")
				# player_3_out is not on the field, so cannot be exchanged.
				print(f"3rd player, '{player_3_out.title()}' is not on the field. Can't make the change.")	
				# Show the players on the field after the change.
				print(f"Players on the field after the change: {players_on_field}.")
			# If player_1_in was already on the field we can't make the switch.	
			elif player_1_in.title() in players_on_field:
				print(f"Can't make the swap because {player_1_in.title()} is on the field already.")
				# Take the changed player out of the list.
				# player_2_out is not on the field, so cannot be exchanged.
				print(f"2nd player, '{player_2_out.title()}' is not on the field. Can't make the change.")
				# player_3_out is not on the field, so cannot be exchanged.
				print(f"3rd player, '{player_3_out.title()}' is not on the field. Can't make the change.")
				print(f"No changes occured. Players on the field are the same: {players_on_field}.")
		# If player 1 and 2 are not on the field, but player 3 is on the field.
		elif ((player_1_out.title() and player_2_out.title() not in players_on_field) and (player_3_out.title() in players_on_field)):
			# If player_3_in is not on the field.
			if player_3_in.title() not in players_on_field:	
				# Substract a change.
				schimbari_max -= 1
				# Add a change.
				schimbari_efectuate += 1
				# Remove a player from players_on_field.
				players_on_field.remove(player_3_out.title())
				# Add the new player to the list.
				players_on_field.append(player_3_in.title())
				# player_1_out is not on the field, so cannot be exchanged.
				print(f"1st player, '{player_1_out.title()}' is not on the field. Can't make the change.")
				# player_2_out is not on the field, so cannot be exchanged.
				print(f"2nd player, '{player_2_out.title()}' is not on the field. Can't make the change.")
				# Show the switch.
				print(f"Change: {player_3_out.title()} OUT, {player_3_in.title()} IN." + 
					f" Changes left: {schimbari_max}. Changes made: {schimbari_efectuate}.")	
				# Show the players on the field after the change.
				print(f"Players on the field after the change: {players_on_field}.")
			# If player_3_in was already on the field we can't make the switch.	
			elif player_3_in.title() in players_on_field:
				print(f"Can't make the swap because {player_3_in.title()} is on the field already.")
				# Take the changed player out of the list.
				# player_1_out is not on the field, so cannot be exchanged.
				print(f"1st player, '{player_1_out.title()}' is not on the field. Can't make the change.")
				# player_2_out is not on the field, so cannot be exchanged.
				print(f"2nd player, '{player_2_out.title()}' is not on the field. Can't make the change.")
				print(f"No changes occured. Players on the field are the same: {players_on_field}.")
		# If player 1 is not on the field, but player 2 and 3 are on the field.
		elif ((player_1_out.title() not in players_on_field) and (player_2_out.title() and player_3_out.title() in players_on_field)):
			# If 2 players we want in are not on the field.
			if ((player_2_in.title() not in players_on_field) and (player_3_in.title() not in players_on_field)):
				# Remove the 2nd player from the players_on_field.
				players_on_field.remove(player_2_out.title())
				# Remove 3rd player from players_on_field.
				players_on_field.remove(player_3_out.title())
				#Add the 2 players to players_on_field.
				players_on_field.append(player_2_in.title())
				players_on_field.append(player_3_in.title())
				# Substract changes.
				schimbari_max -= 2
				# Add changes.
				schimbari_efectuate += 2
				# player_1_out is not on the field, so cannot be exchanged.
				print(f"{player_1_out.title()} is not on the field. Can't make the change.")
				# Show the swap.
				print(f"Change: {player_2_out.title()} and {player_3_out.title()} OUT, {player_2_in.title()} and {player_3_in.title()} IN." + 
					f"  Changes left: {schimbari_max}. Changes made: {schimbari_efectuate}.")
				# Show the players on the field after the change.
				print(f"Players on the field after the change: {players_on_field}.")
			# If player_2_in just got send out.	
			elif player_2_in.title() in players_on_field and player_3_in.title() not in players_on_field:
				# Substract changes.
				schimbari_max -= 1
				# Add changes.
				schimbari_efectuate += 1
				# Remove player_2_out from players_on_field.
				players_on_field.remove(player_3_out.title())
				# Add player_2_in to players_on_field.
				players_on_field.append(player_3_in.title())
				# player_1_out is not on the field, so cannot be exchanged.
				print(f"{player_1_out.title()} is not on the field. Can't make the change.")
				# Show changes.
				print(f"Change: {player_3_out.title()} OUT, {player_3_in.title()} IN." + 
					f" Changes left: {schimbari_max}. Changes made: {schimbari_efectuate}.")
				print(f"Players on the field after the change: {players_on_field}.")
			# If player_3_in just got send out.			
			elif player_2_in.title() not in players_on_field and player_3_in.title() in players_on_field:
				# Substract changes.
				schimbari_max -= 1
				# Add changes.
				schimbari_efectuate += 1
				# Remove player_2_out from players_on_field.
				players_on_field.remove(player_2_out.title())
				# Add player_2_in to players_on_field.
				players_on_field.append(player_2_in.title())
				# player_1_out is not on the field, so cannot be exchanged.
				print(f"{player_1_out.title()} is not on the field. Can't make the change.")
				# Show changes.
				print(f"Change: {player_2_out.title()} OUT, {player_2_in.title()} IN." + 
					f" Changes left: {schimbari_max}. Changes made: {schimbari_efectuate}.")
				# Show the players on the field after the change.
				print(f"Players on the field after the change: {players_on_field}.") 
			# If 2 players you want IN are on field.
			elif player_2_in.title() and player_3_in.title() in players_on_field:
				# player_1_out is not on the field, so cannot be exchanged.
				print(f"1st player, '{player_1_out.title()}' is not on the field. Can't make the change.")
				# 2 Players are on the field.
				print(f"2 of the players you want IN are already on the field. Can't make the change.")		
				# No changes.			
				print(f"No changes occured. Players on the field are the same: {players_on_field}.")
		# If all 3 players we want to change are on the field.
		elif player_1_out.title() and player_2_out.title() and player_3_out.title() in players_on_field:
			# If 2 players we want in are not on the field.
			if ((player_1_in.title() not in players_on_field) and (player_2_in.title() not in players_on_field) and (player_3_in.title() in players_on_field)):
				# Remove the 1st player from the players_on_field.
				players_on_field.remove(player_1_out.title())
				# Remove 2nd player from players_on_field.
				players_on_field.remove(player_2_out.title())
				# Add the two players to was_on_field.
				was_on_field.append(player_1_out.title())
				was_on_field.append(player_2_out.title())
				#Add the 2 players to players_on_field.
				players_on_field.append(player_1_in.title())
				players_on_field.append(player_2_in.title())
				# Substract changes.
				schimbari_max -= 2
				# Add changes.
				schimbari_efectuate += 2
				# Show the swap.
				print(f"Change: {player_1_out.title()} and {player_2_out.title()} OUT, {player_1_in.title()} and {player_2_in.title()} IN." + 
					f" Changes left: {schimbari_max}. Changes made: {schimbari_efectuate}.")
				# Show that a player has just been called out and can't get right back in.
				if player_3_in.title() in was_on_field:
					print(f"{player_3_in.title()} has been replaced already. You can't send him back on the field.")
				else:
					print(f"{player_3_in.title()} is already on the field. He'll stay on.")	
				# Show the players on the field after the change.
				print(f"Players on the field after the change: {players_on_field}.") 
			# If 2 players we want in are not on the field.
			elif (player_1_in.title() in players_on_field) and (player_2_in.title() not in players_on_field) and (player_3_in.title() not in players_on_field):
				# Remove the 2nd player from the players_on_field.
				players_on_field.remove(player_2_out.title())
				# Remove 3rd player from players_on_field.
				players_on_field.remove(player_3_out.title())
				# Add the two players to was_on_field.
				was_on_field.append(player_2_out.title())
				was_on_field.append(player_3_out.title())
				#Add the 2 players to players_on_field.
				players_on_field.append(player_2_in.title())
				players_on_field.append(player_3_in.title())
				# Substract changes.
				schimbari_max -= 2
				# Add changes.
				schimbari_efectuate += 2
				# Show the swap.
				print(f"Change: {player_2_out.title()} and {player_3_out.title()} OUT, {player_2_in.title()} and {player_3_in.title()} IN." + 
					f" Changes left: {schimbari_max}. Changes made: {schimbari_efectuate}.")
				# Show that a player has just been called out and can't get right back in.
				if player_1_in.title() in was_on_field:
					print(f"{player_1_in.title()} has been replaced already. You can't send him back on the field.")
				else:
					print(f"{player_1_in.title()} is already on the field. He'll stay on.")	
				# Show the players on the field after the change.
				print(f"Players on the field after the change: {players_on_field}.") 
			# If 1 player we want in is not on the field.
			elif ((player_1_in.title() not in players_on_field) and (player_2_in.title() in players_on_field) and (player_3_in.title() in players_on_field)):
				# Remove the 1st player from the players_on_field.
				players_on_field.remove(player_1_out.title())
				# Add the changed player to was_on_field.
				was_on_field.append(player_1_out.title())
				#Add 1st player to players_on_field.
				players_on_field.append(player_1_in.title())
				# Show the swap.
				print(f"Change: {player_1_out.title()} OUT, {player_1_in.title()} IN." + 
					f" Changes left: {schimbari_max}. Changes made: {schimbari_efectuate}.")
				# Show that a player has just been called out and can't get right back in.
				if player_2_in.title() in was_on_field:
					print(f"{player_2_in.title()} has been replaced already. You can't send him back on the field.")
				else:
					print(f"{player_2_in.title()} is already on the field. He'll stay on.")	
				# Show that a player has just been called out and can't get right back in.
				if player_3_in.title() in was_on_field:
					print(f"{player_3_in.title()} has been replaced already. You can't send him back on the field.")
				else:
					print(f"{player_3_in.title()} is already on the field. He'll stay on.")	
				# Show the players on the field after the change.
				print(f"Players on the field after the change: {players_on_field}.") 
			# If player_3_in isn't on field.	
			elif ((player_1_in.title() in players_on_field) and (player_2_in.title() in players_on_field) and (player_3_in.title() not in players_on_field)):
				# Remove the 3rd player from the players_on_field.
				players_on_field.remove(player_3_out.title())
				# Add the changed player to was_on_field.
				was_on_field.append(player_3_out.title())
				#Add 1st player to players_on_field.
				players_on_field.append(player_3_in.title())
				# Show the swap.
				print(f"Change: {player_3_out.title()} OUT, {player_3_in.title()} IN." + 
					f" Changes left: {schimbari_max}. Changes made: {schimbari_efectuate}.")
				# Show that a player has just been called out and can't get right back in.
				if player_1_in.title() in was_on_field:
					print(f"{player_1_in.title()} has been replaced already. You can't send him back on the field.")
				else:
					print(f"{player_1_in.title()} is already on the field. He'll stay on.")	
				# Show that a player has just been called out and can't get right back in.
				if player_2_in.title() in was_on_field:
					print(f"{player_2_in.title()} has been replaced already. You can't send him back on the field.")
				else:
					print(f"{player_2_in.title()} is already on the field. He'll stay on.")	
				# Show the players on the field after the change.	
				print(f"Players on the field after the change: {players_on_field}.") 
			# If all 3 players that we want in are not on the field.
			elif ((player_1_in.title() not in players_on_field) and (player_2_in.title() not in players_on_field) and (player_3_in.title() not in players_on_field)):
				# Remove the 1st player from the players_on_field.
				players_on_field.remove(player_1_out.title())
				# Remove the 2nd player from the players_on_field.
				players_on_field.remove(player_2_out.title())
				# Remove the 3rd player from the players_on_field.
				players_on_field.remove(player_3_out.title())
				# Add the changed player to was_on_field.
				was_on_field.append(player_1_out.title())
				# Add the changed player to was_on_field.
				was_on_field.append(player_2_out.title())
				# Add the changed player to was_on_field.
				was_on_field.append(player_3_out.title())
				#Add 1st player to players_on_field.
				players_on_field.append(player_1_in.title())
				#Add 2nd player to players_on_field.
				players_on_field.append(player_2_in.title())
				#Add 3rd player to players_on_field.
				players_on_field.append(player_3_in.title())
				print(f"Change: {player_1_out.title()}, {player_2_out.title()} and {player_3_out.title()} OUT," +
					f"\n {player_1_in.title()}, {player_2_in.title()} and {player_3_in.title()} IN." + 
					f"\n Changes left: {schimbari_max}. Changes made: {schimbari_efectuate}.")	
				# Show the players on the field after the change.	
				print(f"Players on the field after the change: {players_on_field}.")
			# If all 3 players that we want to send in are already on the field.	
			elif ((player_1_in.title() in players_on_field) and (player_2_in.title() in players_on_field) and (player_3_in.title() in players_on_field)): 	
				print(f"{player_1_out.title()}, {player_2_out.title()} and {player_3_out.title()} are already on the field." + 
					f"\n Can't do any changes. Changes left: {schimbari_max}. Changes made: {schimbari_efectuate}.") 

		# If all 3 players are not on the field. (drunk coach again)  :)
		elif player_1_out.title() and player_2_out.title() and player_3_out.title() not in players_on_field:
			# Substract changes.
			schimbari_max -= 0
			# Add changes.
			schimbari_efectuate += 0
			# Show the swap.		
			print(f"Change: {player_1_out.title()}, {player_2_out.title()} and {player_3_out.title()} " +
				f"are not on the field, can't make any changes." 
				f" Changes left: {schimbari_max}. Changes made: {schimbari_efectuate}.")
			# Show the players on the field after the change.
			print(f"Players on the field after the change: {players_on_field}.")
else:
	print("You can't make that number of changes.")

print(was_on_field)	