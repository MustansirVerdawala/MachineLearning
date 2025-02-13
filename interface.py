import os
from json import load
from time import sleep#, time
import socket

class interface:
    
    def __init__(self):
        pass

    def fetchInput(self):
        #start=time()
        #rn=time()
        #while (rn-start)<5:
        while True:
            try:
                f = open(r'C:\Users\mbverdaw\AppData\LocalLow\DefaultCompany\Vampire Survivors Like Game\frames.json')
                data=load(f)
                
                frames=data['frameByteData']
                
                while len(frames)<4:
                    frames.append(frames[-1])
                    
                if len(frames)>4:
                    frames=frames[(len(frames)-5):(len(frames)-1)]
                    
                
                break
            except:
                pass
        #else:
        #    return 0, 0, 0, 0
        
        health=data['health']
        
        
        try:
            cEnemyDist=data['cEnemyDist']
        except:
            cEnemyDist=512*512

        try:
            pScore=data['pScore']
        except:
            pScore=0
            
        try:
            velocity=data['velocity']
        except:
            velocity=10
        
        timeAlive=data['timeAlive']
                
        return frames, health, timeAlive, pScore, cEnemyDist, velocity

    def keyPress(self, moves):
        host = '127.0.0.1'  # Since both are on the same machine
        port = 8052  # This should match the port Unity is listening on
    
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((host, port))
                s.sendall(moves.encode())  # Sending moves as a string
                # print("Moves sent to Unity:", moves)
        except Exception as e:
            print(f"Error sending moves: {e}")

    def reset(self):
        self.keyPress('r')
        sleep(1)
        self.keyPress('r')
        
# =============================================================================
#         _, health, __, ___=self.fetchInput()
#         while health!=100:
#             kc.press_key('space')
#             sleep(1)
#             kc.unpress_key('space')
#             _, health, __, ___=self.fetchInput()
# =============================================================================

    def initialize(self):
        os.startfile(r"C:\Users\mbverdaw\Downloads\build_2\Vampire Survivors Like Game.exe")
        sleep(5)
