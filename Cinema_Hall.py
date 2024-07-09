class Star_Cinema:
    
    _hall_list = []
    
    @classmethod
    def entry_hall(self,hall):
        self._hall_list.append(hall)
    
class Hall(Star_Cinema):
    def __init__(self,row,col, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = row
        self.__cols = col
        self.__hall_no = hall_no
        super().entry_hall(self)

# Toofan = Hall(5,5,'nana')

    def entry_show(self,id, movie_name, time):
        self.__show_list.append((id,movie_name, time))
        self.__seats[id] = [[0 for x in range(self.__cols)] for y in range(self.__rows)]
            
    def book_seats(self):
        self.view_show_list()
        sid = input("ENTER SHOW ID : ")
        t = int(input("Number of Tickets ? : "))
        if sid not in [show[0] for show in self.__show_list]:
            print("No such Show found")
        else:
            for i in range(t):
                x = int(input("ENTER ROW : "))
                y = int(input("ENTER COLUMN : "))
                if x >= self.__rows or x < 0 or y >= self.__cols or y < 0:
                    print("Invalid Seat No")
                elif self.__seats[sid][x][y] == 1:
                    print("Seat Already Booked")
                else:
                    self.__seats[sid][x][y] = 1
                    print(f"Seat ({x},{y}) booked for show {sid}")
            
                    
    def view_show_list(self):
        print('-'*8)
        for i in self.__show_list:
            print(f"MOVIE NAME : {i[1]}({i[0]}) \tSHOW ID:{i[0]} \tTIME:{i[2]}")
        print('-'*8)
        
    def view_available_seats(self):
        self.view_show_list()
        x = input("ENTER SHOW ID:")
        
        if x in self.__seats:   
            seats = self.__seats[x]
            for row in seats:
                print(" ".join(map(str, row)))
        else :
            print("Invalid Show Id \n")
            

Savar_cinema_hall = Hall(5,5,"1")
Dhaka_cinema_hall = Hall(5,5,"2")
Rajshahi_cinema_hall = Hall(5,5,"3")
Star_Cinema.entry_hall(Savar_cinema_hall)
Star_Cinema.entry_hall(Dhaka_cinema_hall)
Star_Cinema.entry_hall(Rajshahi_cinema_hall)


Savar_cinema_hall.entry_show('110','Toofan', '15/10/2024 10:00 AM')
Savar_cinema_hall.entry_show('111','Dhaka Attack', '16/10/2024 11:00 AM')
Savar_cinema_hall.entry_show('112','Aynabaji', '17/10/2024 12:00 AM')


a = True
while(a):
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. EXIT")
    x = int(input("ENTER OPTION : "))
    if x == 1:
        Savar_cinema_hall.view_show_list()
    elif x==2:
        Savar_cinema_hall.view_available_seats()
    elif x == 3:
        Savar_cinema_hall.book_seats()
    elif x == 4:
        a = False
    else :
        print("INVALID CHOICE, WANNA TRY AGAIN? ")
        
    


