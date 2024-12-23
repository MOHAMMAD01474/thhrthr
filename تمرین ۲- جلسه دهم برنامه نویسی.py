
class Footbalist:

    def __init__(self, first_name, last_name, weight ,  height , number ):
        
        self.first_name = first_name

        self.last_name = last_name

        self.number = number

        self.height = height

        self.weight = weight


    def player_first_number(self):
        return('The player first name: '+ self.first_name)
    
   
class Goalkeeper(Footbalist):
    pass


class Defenders(Footbalist):
    pass


player1 = Footbalist('Behnam' , 'Sabzali' , 81 , 173 , 1)

player2 = Goalkeeper('Saber' , 'Talebi' , 77 , 169 , 2)

player3 = Defenders('Mahdi' , 'Baboly' , 84 , 184 , 3)

player4 = Defenders('Babak' , 'jalali' , 90 , 190 , 4)

print(player1.player_first_number())
