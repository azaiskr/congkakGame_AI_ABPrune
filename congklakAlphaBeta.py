class Papan_congklak:
    def __init__(self, lubCongklak):
        if lubCongklak != None:
            self.isi = lubCongklak[:]
        else:
            self.isi = [0 for i in range(16)]
            for i in range(0,7):
                self.isi[i] = 7
            for i in range(8,15):
                self.isi[i] = 7

    def player_move(self, i):
        j = i
        repeat_turn = False
        add = self.isi[j]
        self.isi[j] = 0
        if i > 7:
            stones = add
            while stones > 0:
                i += 1
                i = i % 16
                if i == 6:
                    continue
                else:
                    self.isi[i % 16] += 1
                stones -= 1
            if i > 7 and self.isi[i] == 1 and i != 15 and self.isi[6-(i-8)] != 0:
                self.isi[15] += 1 + self.isi[6-(i-8)]
                self.isi[i] = 0
                self.isi[6-(i-8)] = 0
            if i == 15:
                repeat_turn = True
        else:
            stones = add
            while (stones > 0):
                i += 1
                i = i % 16
                if i == 15:
                    continue
                else:
                    self.isi[i%16] += 1
                stones -= 1
            if i < 7 and self.isi[i] == 1 and i != 7 and self.isi[-i + 14]!=0:
                self.isi[7] += 1 + self.isi[-i + 14]
                self.isi[i] = 0
                self.isi[-i + 14] = 0
            if i == 7:
                repeat_turn = True
        return repeat_turn

    def isEnd(self):
        if sum(self.isi[0:6])==0 :
            self.isi[15]+=sum(self.isi[8:15])
            for i in range(16):
                if  (i != 15 and i != 7):
                    self.isi[i] = 0

            return True
        elif sum(self.isi[8:15])==0:
            self.isi[7] += sum(self.isi[0:7])
            for i in range(16):
                if  (i != 15 and i != 7):
                    self.isi[i] = 0
            return True

        return False

    def print_congklak(self):
        for i in range(14,7,-1):
            print('    ', self.isi[i], ' ', end = '')
        print('  ')
        print(self.isi[15],'                                                       ',self.isi[7])

        for i in range(0,7,1):
            print('    ', self.isi[i], ' ', end='')
        print('  ')

    def husVal(self):
        if self.isEnd():
            if self.isi[15]>self.isi[7]:
                return 100
            elif self.isi[15]==self.isi[7]:
                return 0
            else :
                 return -100
        else:
            return self.isi[15]- self.isi[7]

def alphabeta(lubCongklak, depth, alpha, beta , MinorMax):
    if depth == 0 or lubCongklak.isEnd(): #3 
        return lubCongklak.husVal(),-1 #2
    if MinorMax:
        v = -1000000 #1
        player_move = -1 #1
        for i in range(8,15,1): #116
            if lubCongklak.isi[i]==0: #2
                continue 
            a = Papan_congklak(lubCongklak.isi[:]) #1
            minormax = a.player_move(i) #1
            newv,_ =  alphabeta(a, depth-1, alpha, beta, minormax) #1
            if v < newv: #3
                player_move = i
                v = newv
            alpha = max(alpha, v) #1
            if alpha >= beta : #2
                break
        return v, player_move #2
    else:
        v = 1000000 #1
        player_move = -1 #1
        for i in range(0, 7, 1):#116
            if lubCongklak.isi[i] == 0: #2
                continue
            a = Papan_congklak(lubCongklak.isi[:]) #1
            minormax = a.player_move(i) #1
            newv,_ = alphabeta(a, depth - 1, alpha, beta, not  minormax) #1
            if v > newv: #3
                player_move = i
                v = newv
            beta = min(beta, v) #1
            if alpha >= beta: #2
                break
        return v, player_move #2

def player_player():
    j = Papan_congklak(None)
    j.print_congklak()
    while True:
        if j.isEnd():
            break
        while True:
            if j.isEnd():
                break
            print("\n")
            h = int(input("PLAYER 1 >>> "))
            if h < 8 or h > 14 or j.isi[h] == 0:
                print("Lubang kosong tidak dapat dipilih. Pilih lubang lain!")
                continue

            t = j.player_move(h)
            j.print_congklak()
            if not t:
                break
        while True:
            if j.isEnd():
                break
            print("\n")
            h = int(input("PLAYER 2 >>> "))
            if h > 6 or j.isi[h] == 0:
                print("Lubang kosong tidak dapat dipilih. Pilih lubang lain!")
                continue

            t = j.player_move(h)
            j.print_congklak()
            if not t:
                break

    if j.isi[7] < j.isi[15]:
        print("\n")
        print("WINNER : Player 1")
    else:
        print("\n")
        print("WINNER : Player 2")
    print('Game Selesai')
    j.print_congklak()

def player_aibot():
    j = Papan_congklak(None)
    j.print_congklak()
    while True:
        if j.isEnd():
            break
        while True:
            if j.isEnd():
                break
            h = int(input("YOUR TURN >>> "))
            if h > 6 or j.isi[h] == 0:
                print("Lubang kosong tidak dapat dipilih. Pilih lubang lain!")
                continue
            t = j.player_move(h)
            print("\n")
            j.print_congklak()
            if not t:
                break
        while True:
            if j.isEnd():
                break
            print("AI-BOT >>> ", end = "")
            j != 7
            _,k = alphabeta(j, 10, -100000, 100000, True) #depth 10
            print(k)
            t = j.player_move(k)
            print("\n")
            j.print_congklak()
            if not t:
                break
    if j.isi[7] < j.isi[15]:
        print("\n")
        print("NiceTry!! AI-BOT menang.")
    else:
        print("\n")
        print("Congrats!! You beat us!.")
    print('Game Selesai')
    j.print_congklak()

print("\n\t\t:::: CONGKLAK BOARD GAME ::::")
print("\t!!! Selamat Datang di Congklak Game !!!")
while True:
    print("\nPilih tipe Gameplay yang kamu inginkan : ")
    print("(1) Player-1 vs Player-2")
    print("(2) Player vs AI-Bot")
    type = int(input(">>> "))
    print("\n")
    if type == 1:
        player_player()
        break
    elif type == 2:
        player_aibot()
        break
    else:
        print("Tipe Gameplay tidak ditemukan, pilih ulang!")
        continue