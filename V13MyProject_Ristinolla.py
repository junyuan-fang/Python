#TIE-02101 Ohjelmointi 1: Johdanto
#Junyuan Fang, junyuan.fang@tuni.fi, opiskelijanumero: 292042
#Tehtävä 13.9.1 Graafisen käyttöliittymän suunnitteleminen ja toteuttaminen
#Ohjelman tehtävä on ristinollan toteutus graafisella käyttöliittymällä
#Ohjelma vaihtaa pelaajan vuoronsa klikkauksen jälkeen.
#Ohjelma päättä voittaja pelin lopussa
#Peli voi pelata useita kertoja

from tkinter import *
import random
PELAAJA=2
KOKO=3
#Toteutetaan luokka "ristinolla", jolla 2 pelaajat voivat vuorovaikuttaa pelin kanssa
class ristinolla:
    def __init__(self):
        self.__mainw=Tk()
        self.__mainw.title(f"Ristinolla")
        self.__mainw.option_add("*Font", "Verdana 66")
        self.__mainw.option_add("*Label.Font", "Verdana 22")

        self.initialize_game()
        self.__mainw=mainloop()

    def initialize_game(self):
        """
        Nollaa/luodaan tarvittavat arvot oletukseksi
        Ikkuna, jolla on kaikki valmiit napit, tai Label:t oletetussa muodossa.
        :return: None
        """
        self.__turn = 0
        self.__Button_ls = []
        self.__koordinaatisto_ls = []
        for i in range(KOKO):
            self.__Button_ls.append([None] * KOKO)
            self.__koordinaatisto_ls.append([None] * KOKO)
        # Luodaan nappeja, näyttää napit GUI ikkunalle ja tallennetaan listaan.
        # Luodaan samalla koordinaatistot matriisina, myöhämmin tunnistamista varten
        # y=rivi, x=column
        for y in range(KOKO):
            for x in range(KOKO):
                new_button = Button(self.__mainw, text=" ",height = 1, width = 3,
                                    command=lambda x=x,y=y : self.press_button(y,x))  # command

                self.__Button_ls[y][x] = new_button
                new_button.grid(row=y, column=x)

                self.__koordinaatisto_ls[y][x] = True

        #Yleinen huomautus näytölle
        self.__info=Label(self.__mainw,text="Replay can be pressed since somebody wins")
        self.__info.grid(row=0, column=KOKO, sticky=EW)

        #Tämä Label käytetään pelin vuoroa ja ilmoitusta varten
        self.__info_Label = Label(self.__mainw)
        self.__info_Label.grid(row=1, column=KOKO, sticky=EW)

        #Tämä button käytetään pelin nollamista varten
        self.__initialize_button = Button(self.__mainw, relief="raised", text="REPLAY",
                                          command=self.initialize_game)                 # command
        self.__initialize_button.grid(row=KOKO - 1, column=KOKO, sticky=EW+S)
        self.__initialize_button["state"]=DISABLED

        self.info_update()


    def press_button(self,y,x):
        """Muuttaa napin tilaa klikauksella(sekä text että state)

        :param y: size, joka on 3 tässä
        :param x: size, joka on 3 tässä
        :return: None
        """
        self.__Button_ls[y][x]["text"]=self.mark_x_or_o()
        self.__Button_ls[y][x]["state"]=DISABLED
        self.__koordinaatisto_ls[y][x]=not(self.__koordinaatisto_ls[y][x])

        #Tarkistaan voittaja ja onnitellaan voittaja
        if self.who_win(self.mark_x_or_o()):
            self.buttons_state_after_win()
            #vuottaja esiintyy, ja vuorolla tiedetään kuka on voittanut
            self.Label_winner_congrat(self.__turn)
            return
        self.next_turn()
        self.info_update()

    def mark_x_or_o(self):
        #palauttaa teksti"X" tai "O" napin tekstin muuttamista varten
        if self.__turn%PELAAJA==0:
            return "X"
        else:
            return "O"

    def info_update(self):
        self.__gamesituationtext = "X=1, O=2 .Player " + str(self.__turn%PELAAJA + 1) + " turn"
        self.__info_Label["text"]=self.__gamesituationtext


    def who_win(self,mark):
        """
        Merkin avulla, tutkitaan mahdollista voittajaa.

        :param mark: täällä hetkellä vuorossa olevan pelaajan merkki
        :return Ture:  jos täyttää voittamisen vaatimuksen
        :return False: jos ei täyttää
        """
        for i in range(KOKO):
            if self.__Button_ls[i][0]["text"] == self.__Button_ls[i][1]["text"] == self.__Button_ls[i][2]["text"] == mark:
                return True
            elif self.__Button_ls[0][i]["text"]== self.__Button_ls[1][i]["text"]== self.__Button_ls[2][i]["text"] == mark:
                return True
        if self.__Button_ls[0][0]["text"] == self.__Button_ls[1][1]["text"] == self.__Button_ls[2][2]["text"] == mark:
            return True
        elif self.__Button_ls[0][2]["text"] == self.__Button_ls[1][1]["text"] == self.__Button_ls[2][0]["text"] == mark:
            return True

        return False

    def next_turn(self):
        self.__turn+=1

    def buttons_state_after_win(self):
        #nollataan napin state oletukseksi
        for y in range(KOKO):
            for x in range(KOKO):
                self.__Button_ls[y][x]["state"] = DISABLED
        self.__initialize_button["state"] = NORMAL

    def Label_winner_congrat(self,turn):
        self.__info_Label["text"]="Congrtulation player {:d}, you won!".format(turn%PELAAJA+1)
        self.__info_Label.configure(foreground="red")

def main():
    #Aloitetaan
    Play=ristinolla()

main()