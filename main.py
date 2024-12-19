import random
import google.generativeai as genai
import PIL.Image
import os
import glob
import drawer
import time


class Authentication:
    def __init__(self):
        genai.configure(api_key="YOUR_OWN_GEMINI_API_KEY")
        self.model = genai.GenerativeModel(model_name="gemini-1.5-flash")

        self.randomNumber = random.randint(0, 100)

        print("\n\n\n", "To verify you are not a robot draw the number: ", self.randomNumber, "\n\n\n")

        time.sleep(3)

        drawer.DrawingWindow()

        self.analyzeImage()

        self.showResponse()

    @staticmethod
    def getMostRecentFile():
        filesList = glob.glob('./*') # * means all if need specific format then *.csv
        newestFile = max(filesList, key=os.path.getctime)
        
        return str(newestFile)

    def analyzeImage(self):
        image1Path = "./" + Authentication.getMostRecentFile()
        image1 = PIL.Image.open(image1Path)

        promt = "Write the number you see in the photo"
        response = self.model.generate_content([promt, image1]).text

        return response

    def showResponse(self):
        if int(self.analyzeImage()) == self.randomNumber:
            print("\n\n\n", "Drawed number: ", self.randomNumber)
            print(" Drawn number matches random number")
            print(" Test successful, not a robot", "\n\n\n")
        else:
            print("\n\n\n", "test failed, retry.")

    
Authentication()
