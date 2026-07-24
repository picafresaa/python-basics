def main():
    baconFile = open("bacon.txt", "w")
    baconFile.write("Hello World!\n")
    baconFile.close()
    
    baconFile = open("bacon.txt", "a")
    baconFile.write("Bacon is not a vegetable.")
    baconFile.close()
    print(baconFile)
    
main()