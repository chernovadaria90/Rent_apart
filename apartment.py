class Apartment:
    #конструктор
     def __init__(self, address, square, number_of_rooms, rent_price, description):
         # статус
          self.status = "свободна"
          self.address = address #  адрес
          self.square = square #  площадь
          self.number_of_rooms = number_of_rooms #количество комнат
          self.rent_price = rent_price #стоимость аренды за сутки
          self.description = description #текстовое описание

     def __str__(self):
         return self.status + " -- адрес: " + self.address + ", площадь: " +  str(self.square) + ", количество комнат: " + str(self.number_of_rooms) + ", стоимость аренды за сутки: " + str(self.rent_price) + ". " + self.description
              

