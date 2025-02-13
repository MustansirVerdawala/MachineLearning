import pyautogui
# import time
#import keyboard

class KeyboardController():
    def __init__(self):
        self._charsequence = []
        self._prevcharsequence = []

    def press_key(self, charkey):
        pyautogui.keyDown(charkey)

    def unpress_key(self, charkey):
        pyautogui.keyUp(charkey)

    #only method that should be called publically normally
    def set_current_key_sequence(self, input: str): #characters to press should be seperated by commas
        inputlist = input.split(",")
        self._charsequence = inputlist

        self.stop_key_sequence()
        
        self.restart_key_sequence()

        self._prevcharsequence = self._charsequence

    #call if key presses should be halted 
    def stop_key_sequence(self):
        if len(self._prevcharsequence) != 0:
            for i in range(len(self._prevcharsequence)):
                self.unpress_key(self._prevcharsequence[i])
    
    #call if key presses should be resumed
    def restart_key_sequence(self):
        for i in range(len(self._charsequence)):
            self.press_key(self._charsequence[i])





'''
#testing purposes, comment out when using in normal circumstances
if __name__ == '__main__':
    ktestobj = KeyboardController()

    ktestobj.set_current_key_sequence("w,d")
    time.sleep(2.5)
    ktestobj.set_current_key_sequence("a,s")
    time.sleep(2.5)
    ktestobj.set_current_key_sequence("w,d")
    time.sleep(2.5)
    ktestobj.set_current_key_sequence("a,s")
    time.sleep(2.5)
    ktestobj.set_current_key_sequence("w,d")
    time.sleep(2.5)
    ktestobj.set_current_key_sequence("a,s")


    
'''
