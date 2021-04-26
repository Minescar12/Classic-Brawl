from Utils.Reader import BSMessageReader
from Logic.Player import Players
from Packets.Messages.Server.Battle.BattleResultMessage import BattleResultMessage
from Packets.Messages.Server.KeepAliveOkMessage import KeepAliveOkMessage

import time

class ClientInputMessage(BSMessageReader):
    def __init__(self, client player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.player = player

    def decode(self):
        self.read_Vint() #0
        self.read_Vint() #unknown 16, 33, 34
        self.read_Vint() #Count
        v3 = self.read_Vint()
        result = self.sub_3A9EC(v3, 0, 30)
        print(str(result))
        #("ClientInput: Tick: ", self.tick)
    
    def sub_3A9EC(self, a1, a2, a3):
        if a1 < a3:
            a3 = a1
        if a1 <= a2:
            a3 = a2
        return a3

    def process(self):
        pass
        '''ticking = 0
        while True:
            if ticking >= 4:
                self.player.battleTick += 1
                KeepAliveServerMessage(self.client, self.player).send()
                ticking = 0
            
            
            VisionUpdateMessage(self.client, self.player).send()
            time.sleep(0.03)
            ticking += 1'''