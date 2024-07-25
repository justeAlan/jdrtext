from random import randint

#Variables principales
HP_PLAYER = 50
HP_OPPONENT = 50
POTIONS = 3
ACTION_MENU = "Souhaitez-vous attaquer (1) ou vous soigner (2) ? "
ACTION_CHOICE = ["1", "2"]

#Boucle principale
main_game = True
while main_game == True:
    player_choice = ""
    while player_choice not in ACTION_CHOICE:
        player_choice = input(ACTION_MENU)
        if player_choice not in ACTION_CHOICE:
            print("Veuillez choisir une action valide.")
    
    if player_choice == "1": #boucle d'attaque joueur
        attack_player = randint(5, 10)
        HP_OPPONENT = HP_OPPONENT - attack_player

        if attack_player <= 9: #print critique si coup 10
            print(f"""Vous infligez {attack_player} de dégats à l'ennemi.
        Il reste {HP_OPPONENT} points de vie à l'ennemi.""")
        else:
            print(f"""
        WOW ! Tu as infligé un coup critique !
                  
Vous infligez {attack_player} de dégats à l'ennemi.
        Il reste {HP_OPPONENT} points de vie à l'ennemi.""")
            
        if HP_OPPONENT <= 0: # Condition pour gagner
            print("Vous avez vaincu votre ennemi ! GG")
            break
        else: #boucle attaque ennemi
            attack_opponent = randint(5, 15)
            HP_PLAYER = HP_PLAYER - attack_opponent
            if attack_opponent <= 13:
                print(f"""
Votre ennemi vous inflige {attack_opponent} point de dégats.
        Il vous reste {HP_PLAYER} points de vie.""")
            else:
                print(f"""
        Aie... Coup critique !
                      
Votre ennemi vous inflige {attack_opponent} point de dégats.
        Il vous reste {HP_PLAYER} points de vie.""")
            if HP_PLAYER <= 0: # condition pour perdre
                print("NOOB T'AS PERDU LOL")
                break

    elif player_choice == "2": #boucle de potion
        if POTIONS > 0:
            POTIONS -= 1
            potion_hp = randint(15, 50)
            HP_PLAYER = HP_PLAYER + potion_hp

            if HP_PLAYER > 50:
                HP_PLAYER = 50
                print("Votre nombre de points de vie ne peut excéder 50.")
            elif potion_hp >= 40:
                print("\nVous sentez que la potion fait plus d'effet qu'à son habitude !\n")
            print(f"Vous passez votre tour pour vous soigner de {potion_hp}. Il vous reste : {HP_PLAYER}.")

            #Retour à l'attaque de l'attaque de l'ennemi
            attack_opponent = randint(5, 15)
            HP_PLAYER = HP_PLAYER - attack_opponent
            if attack_opponent <= 13:
                print(f"""Votre ennemi vous inflige {attack_opponent} point de dégats.
        Il vous reste {HP_PLAYER} points de vie.""")
            else:
                print(f"""
        Aie... Coup critique !
Votre ennemi vous inflige {attack_opponent} point de dégats.
        Il vous reste {HP_PLAYER} points de vie.""")
            
            if HP_PLAYER == 0: #Condition de défaite
                print("NOOB T'AS PERDU LOL")
                break
        else: # Plus de potion
            print("Vous n'avez plus de potion...")
            continue

    print("-" * 50)
        
        

