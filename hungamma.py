import random


class game:
    def gussed_word(self, word_list):
        self.gussed = random.choice(word_list)
        return self.gussed

    def game_start(self):
        i = 5
        while i != 0:
            print("you got {} chances left ".format(i))
            i -= 1
            user = input("Please Gusse Your Letter: ")

            if user == self.gussed:
                print("Congrates, You Got Correct in {} chance".format(i+1))
                break
            else:
                print("Not Correct!!")
                continue
                return "Thanku For Participating"

word_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


g = game()
print(g.gussed_word(word_list))
g.game_start()