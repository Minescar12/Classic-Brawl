from Utils.Writer import Writer

class FriendListMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20105
        self.player = player

    def encode(self):
        self.indexOfPlayer = 1
        
        self.writeVint(len(self.players)) # Playera Count
        for player in self.players:
            if player["lowID"] == self.player.low_id:
                self.indexOfPlayer = self.players.index(player) + 1
        
            self.writeVint(0) # Games Played Together Recently

            self.writeInt(0)  # HighID
            self.writeInt(player["lowID"])  # LowID

            self.writeString()
            self.writeString()
            self.writeString()
            self.writeString()
            self.writeString()


            self.writeInt(player['trophies'])  # Friend state 0 = friend, 1 = not friend, 2 = request sent, 3 = you have an invite from him??, 4 = friend list
            self.writeInt(4)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
        
            if player["clubID"] != 0:
                DataBase.loadClub(self, player["clubID"])

                self.writeBoolean(True)  # Is in club
           
                self.writeInt(0)
                self.writeInt(0)
                self.writeInt(0)
                self.writeString(self.clubName)
                self.writeInt(0)
                self.writeInt(0)    
            else:
                self.writeBoolean(False)  # Is in club
            
            self.writeString()
            self.writeInt(0)
            
            self.writeBoolean(True)  # ?? is a player?
        
            self.writeString("Friendly bot")
            self.writeVint(100)
            self.writeVint(28000005)
            self.writeVint(43000002)
            self.writeVint(0)
