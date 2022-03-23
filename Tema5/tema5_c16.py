"""
16. Functie in care sa dai un nume romanesc si sa iti printeze pe ecran
‘Numele este de baiat’ sau ‘Numele este de fata’
"""

# Rezolvare:
# Lists have been copied from Wikipedia.
def boy_or_girl(name):
	# A function that receives a romanian name and returns if it's a boy's name or a girl's.
	# Define the 2 lists(male and female names.)	
	male_names = ['Abel', 'Achim', 'Adam', 'Adelin', 'Adi', 'Adonis', 'Adrian', 'Agnos', 'Albert', 'Aleodor', 'Alex', 'Alexandru', 'Alexe', 'Alin', 'Alistar', 
				'Amedeu', 'Amza', 'Anatolie', 'Andrei', 'Andrian', 'Angel', 'Anghel', 'Antim', 'Anton', 'Antonie', 'Antoniu', 'Arcadian', 'Arian', 'Aristide', 'Arsenie', 
				'Atanasio', 'Augustin', 'Aurel', 'Aurelian', 'Avram', 'Axinte', 'Barbu', 'Bartolomeu', 'Basarab', 'Banel', 'Bebe', 'Beniamin', 'Benone', 'Bernard', 
				'Bogdan', 'Bradut', 'Bucur', 'Caius', 'Camil', 'Cantemir', 'Carol', 'Casian', 'Cazimir', 'Calin', 'Catalin', 'Cecil', 'Cedrin', 'Cezar', 'Ciprian', 'Claudiu', 
				'Codin', 'Codrin', 'Codrut', 'Constantin', 'Cornel', 'Corneliu', 'Corvin', 'Cosmin', 'Costache', 'Costica', 'Costel', 'Costin', 'Crin', 'Cristea', 'Cristian', 
				'Cristinel', 'Cristobal', 'Cristofor', 'Dacian', 'Damian', 'Dan', 'Daniel', 'Darius', 'David', 'Decebal', 'Denis', 'Dinu', 'Dionisie', 'Dominic', 'Dorel', 'Dorian', 
				'Dorin', 'Dorinel', 'Doru', 'Dragomir', 'Dragoș', 'Ducu', 'Dumitru', 'Edgar', 'Edmond', 'Eduard', 'Eftimie', 'Emanoil', 'Emanuel', 'Emanuil', 'Emil', 'Emilian', 
				'Eremia', 'Eric', 'Ernest', 'Eugen', 'Eusebiu', 'Eustatiu', 'Fabian', 'Faust', 'Felix', 'Filip', 'Fiodor', 'Flaviu', 'Florea', 'Florentin', 'Florian', 'Florin', 
				'Francisc', 'Gabi', 'Gabriel', 'Gelu', 'George', 'Georgel', 'Georgian', 'Ghenadie', 'Gheorghe', 'Gheorghita', 'Gherasim', 'Ghita', 'Gica', 'Gicu', 'Giorgian', 
				'Gratian', 'Gregorian', 'Grigoraș', 'Grigore', 'Haralamb', 'Haralambie', 'Horatiu', 'Horea', 'Horia', 'Horica', 'Iacob', 'Iacov', 'Iancu', 'Ianis', 'Ieremia', 
				'Ilarie', 'Ilarion', 'Ilie', 'Iliuta', 'Inocentiu', 'Ioan', 'Ion', 'Ionel', 'Ionica', 'Ionita', 'Ionut', 'Iorgu', 'Iosif', 'Irinel', 'Isidor', 'Iulian', 'Iuliu', 
				'Iurie', 'Iustin', 'Iustinian', 'Ivan', 'Jan', 'Jean', 'Jenel', 'Ladislau', 'Lascar', 'Laurentiu', 'Laurian', 'Lazar', 'Leonard', 'Leontin', 'Leordean', 'Lica', 
				'Liviu', 'Lorin', 'Luca', 'Lucentiu', 'Lucian', 'Lucretiu', 'Ludovic', 'Manole', 'Marcel', 'Marcu', 'Marian', 'Marin', 'Marinel', 'Marius', 'Martin', 'Matei', 
				'Maxim', 'Maximilian', 'Madalin', 'Marin', 'Mihai', 'Mihail', 'Mihaita', 'Mihnea', 'Mina', 'Mircea', 'Miron', 'Mitica', 'Mitrofan', 'Mitrut', 'Moise', 'Mugur', 
				'Mugurel', 'Nae', 'Narcis', 'Nechifor', 'Nelu', 'Nichifor', 'Nicoara', 'Nicodim', 'Nicolae', 'Nicolaie', 'Nicu', 'Niculita', 'Nicușor', 'Nicuta', 'Norbert', 
				'Noris', 'Norman', 'Octav', 'Octavian', 'Octaviu', 'Olimpian', 'Olimpiu', 'Oliver', 'Oliviu', 'Ovidiu', 'Pamfil', 'Panagachie', 'Panait', 'Paul', 'Pavel', 
				'Patru', 'Petre', 'Petrica', 'Petrișor', 'Petru', 'Petrut', 'Pintiliu', 'Pleșu', 'Pompiliu', 'Radu', 'Rafael', 'Rareș', 'Raul', 'Raducu', 'Razvan', 'Relu', 
				'Remus', 'Robert', 'Romeo', 'Romi', 'Romica', 'Romulus', 'Sabin', 'Sandu', 'Sandu', 'Sava', 'Sebastian', 'Septimiu', 'Sergiu', 'Sever', 'Severin', 'Silvian', 
				'Silviu', 'Simi', 'Simion', 'Sinica', 'Sorin', 'Stan', 'Stancu', 'Stelian', 'Serban', 'Stefan', 'Teodor', 'Teofil', 'Teohari', 'Theodor', 'Tiberiu', 'Timotei', 
				'Titus', 'Todor', 'Toma', 'Traian', 'Trandafir', 'Tudor', 'Valentin', 'Valer', 'Valeriu', 'Valter', 'Vasile', 'Veniamin', 'Vicentiu', 'Victor', 
				'Vincentiu', 'Viorel', 'Visarion', 'Virgil', 'Vlad', 'Vladimir', 'Vlaicu', 'Voicu', 'Zamfir', 'Zeno', 'Zaharie']
	female_names = ['Ada', 'Adela', 'Adelaida', 'Adelina', 'Adina', 'Adriana', 'Adnana', 'Agata', 'Aglaia', 'Agripina', 'Aida', 'Alberta', 'Albertina', 
					'Alexandra', 'Alexandrina', 'Alexia', 'Alice', 'Alida', 'Alina', 'Alis', 'Alma', 'Amalia', 'Amanda', 'Amelia', 'Ana', 'Anabela', 'Anaida', 
					'Anamaria', 'Anastasia', 'Anca', 'Ancuta', 'Anda', 'Andra', 'Andrada', 'Andreea', 'Anemona', 'Aneta', 'Angela', 'Angelica', 'Anghelina', 'Anica', 
					'Anișoara', 'Antoaneta', 'Antonela', 'Antonia', 'Anuta', 'Ariadna', 'Ariana', 'Arina', 'Aristita', 'Artemisa', 'Astrid', 'Atena', 'Augusta', 
					'Augustina', 'Aura', 'Aurelia', 'Aureliana', 'Aurica', 'Aurora', 'Axenia', 'Beatrice', 'Betina', 'Bianca', 'Blanduzia', 'Bogdana', 'Brândușa', 
					'Camelia', 'Carina', 'Carla', 'Carmen', 'Carmina', 'Carolina', 'Casandra', 'Casiana', 'Caterina', 'Catinca', 'Catrina', 'Catrinel', 
					'Catalina', 'Cecilia', 'Celia', 'Cerasela', 'Cezara', 'Chira', 'Cipriana', 'Clara', 'Clarisa', 'Claudia', 'Clementina', 'Cleopatra', 'Codrina', 
					'Codruta', 'Constanta', 'Constantina', 'Consuela', 'Coralia', 'Corina', 'Cornelia', 'Cosmina', 'Crenguta', 'Crina', 'Cristina', 'Daciana', 'Dafina', 
					'Daiana', 'Dalia', 'Dana', 'Daniela', 'Daria', 'Dariana', 'Delia', 'Demetra', 'Denisa', 'Despina', 'Diana', 'Dida', 'Didina', 'Dimitrina', 'Dina', 
					'Dochia', 'Doina', 'Domnica', 'Dora', 'Doriana', 'Dorina', 'Dorli', 'Draga', 'Dumbravita', 'Dumitra', 'Dumitrana', 'Ecaterina', 'Eftimia', 'Elena', 
					'Eleonora', 'Eliana', 'Elisabeta', 'Elisaveta', 'Eliza', 'Elodia', 'Elvira', 'Emanuela', 'Emilia', 'Erica', 'Estera', 'Eufrosina', 'Eugenia', 'Eusebia', 
					'Eva', 'Evanghelina', 'Evelina', 'Fabia', 'Fabiana', 'Felicia', 'Fausta', 'Filofteia', 'Filomela', 'Fiona', 'Flavia', 'Floare', 'Floarea', 'Flora', 
					'Florenta', 'Florentina', 'Floriana', 'Florica', 'Florina', 'Francesca', 'Frusina', 'Gabriela', 'Geanina', 'Gentiana', 'Georgeta', 'Georgia', 
					'Georgiana', 'Geta', 'Gherghina', 'Gianina', 'Gina', 'Giorgiana', 'Gloria', 'Glorita', 'Gratiana', 'Gratiela', 'Henrieta', 'Heracleea', 'Hortensia', 
					'Iasmina', 'Ica', 'Ilaria', 'Ileana', 'Ilinca', 'Ilona', 'Ina', 'Ioana', 'Ioanina', 'Iolanda', 'Ionela', 'Ionelia', 'Ionuta', 'Iosefina', 'Iridenta', 
					'Irina', 'Iris', 'Irma', 'Isabela', 'Isaura', 'Iulia', 'Iuliana', 'Iustina', 'Ivana', 'Ivona', 'Izabela', 'Izaura', 'Jana', 'Janeta', 'Janina', 
					'Jasmina', 'Jeana', 'Joita', 'Julia', 'Julieta', 'Larisa', 'Laura', 'Laurentia', 'Lavinia', 'Lacramioara', 'Leana', 'Lelia', 'Leontina', 'Leopoldina', 
					'Letitia', 'Lenuta', 'Lia', 'Liana', 'Lidia', 'Ligia', 'Lili', 'Liliana', 'Lioara', 'Livia', 'Loredana', 'Lorelei', 'Lorena', 'Luana', 'Lucia', 
					'Luciana', 'Lucretia', 'Ludmila', 'Ludovica', 'Luiza', 'Luminita', 'Magdalena', 'Maia', 'Malvina', 'Manuela', 'Mara', 'Marcela', 'Marcheta', 'Marga', 
					'Margareta', 'Maria', 'Mariana', 'Maricica', 'Marieta', 'Marilena', 'Marina', 'Marinela', 'Marioara', 'Marta', 'Martina', 'Marusia', 'Matilda', 
					'Madalina', 'Malina', 'Marioara', 'Mariuca', 'Melania', 'Melina', 'Melinda', 'Melisa', 'Mia', 'Mihaela', 'Milena', 'Minodora', 'Mioara', 'Mirabela', 
					'Miranda', 'Mirela', 'Mirona', 'Miuta', 'Miruna', 'Mona', 'Monalisa', 'Monica', 'Nadia', 'Naomi', 'Narcisa', 'Natalia', 'Natașa', 'Nicoleta', 'Niculina', 
					'Nidia', 'Nina', 'Noemi', 'Nora', 'Norica', 'Oana', 'Octavia', 'Octaviana', 'Ofelia', 'Olga', 'Olimpia', 'Olivia', 'Ortansa', 'Otilia', 'Ozana', 'Pamela', 
					'Paraschiva', 'Patricia', 'Paula', 'Paulica', 'Paulina', 'Petria', 'Petrina', 'Petronela', 'Petruta', 'Pompilia', 'Profira', 'Rada', 'Rafila', 'Raluca', 
					'Ramona', 'Rebeca', 'Reghina', 'Renata', 'Rica', 'Rita', 'Roberta', 'Robertina', 'Rodica', 'Romana', 'Romanita', 'Romina', 'Roxana', 'Roxelana', 'Roza', 
					'Rozalia', 'Ruxanda', 'Ruxandra', 'Sabina', 'Sabrina', 'Safina', 'Safta', 'Salomea', 'Sanda', 'Sandra', 'Saveta', 'Savina', 'Sandica', 'Sânziana', 'Selina', 
					'Semenica', 'Smeralda', 'Serafina', 'Severina', 'Sidonia', 'Silvana', 'Silvia', 'Silviana', 'Simina', 'Simona', 'Smaranda', 'Sodica', 'Sofia', 'Sofica', 
					'Sonia', 'Sorana', 'Sorina', 'Speranta', 'Stana', 'Stanca', 'Stela', 'Steliana', 'Steluta', 'Susana', 'Suzana', 'Svetlana', 'Stefana', 'Stefania', 'Tamara', 
					'Tania', 'Tatiana', 'Teea', 'Teodora', 'Teodosia', 'Teona', 'Teresa', 'Tereza', 'Tiberia', 'Timea', 'Tinca', 'Tincuta', 'Tudora', 'Tudorica', 'Tudorita', 
					'Tudosia', 'Valentina', 'Valeria', 'Vanesa', 'Varvara', 'Vasilica', 'Vasilichia', 'Venera', 'Vera', 'Veronica', 'Veta', 'Vicentia', 'Victoria', 'Violeta', 
					'Viorela', 'Viorica', 'Virginia', 'Viviana', 'Vladelina', 'Voichita', 'Zaharia', 'Zamfira', 'Zaraza', 'Zenaida', 'Zenobia', 'Zenovia', 'Zina', 'Zita', 'Zoe']	
	# Verify if the name we're searching for is in male_names.						
	if name in male_names:
		print(f"'{name}' is a boy's name.")
	# If the name we're searching for isn't in male_names, it's a girl name.	
	else:
		print(f"'{name}' is a girl's name.")

boy_or_girl("Stefan")
boy_or_girl("Stefania")
boy_or_girl("Zaharie")
boy_or_girl("Mihaela")