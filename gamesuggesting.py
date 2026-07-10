def main ():
    
    
    while True: 
        difficulty = input("difficult or casual? ").strip().lower()
        if difficulty in ["difficult", "casual"]:
         break
        else:
         print("invalid difficulty")

    players = input("multiplayer or singleplayer? ").strip().lower()
    
    while True: 
        players = input("multiplayer or singleplayer? ").strip().lower()

        if players in ["multiplayer", "singleplayer"]:
           break
        else:
         print("invalid players")


    
        if difficulty == "difficult" and players == "multiplayer":
         recommend("poker")
        elif difficulty == "difficult" and players == "singleplayer":
         recommend("blackjack")
        elif difficulty == "casual" and players == "singleplayer":
         recommend("solitaire")
        else:
         recommend("chess")
        

        
def recommend(game):
    print(f"i recommend you play {game}")

main()