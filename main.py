from tkinter import Button, Entry, Label, Listbox, Tk, Variable
from apartment import Apartment


if __name__ == '__main__':
    root = Tk() # создаем корневой объект - окно
    root.title("аренда квартир") # устанавливаем заголовок окна
    root.geometry("1000x800") # устанавливаем размеры окна

    label_address = Label(text="Введите адрес") # создаем текстовую метку
    label_address.pack() # размещаем метку в окне
    # поле ввода для адреса
    entry_address = Entry() #создаем поле ввода
    entry_address.pack() # размещаем поле ввода в окно

    label_square = Label(text="Площадь") # создаем текстовую метку
    label_square.pack() # размещаем метку в окне
    # поле ввода для площади
    entry_square = Entry() #создаем поле ввода
    entry_square.pack() # размещаем поле ввода в окно

    label_number_of_rooms = Label(text="Количество комнат") # создаем текстовую метку
    label_number_of_rooms.pack() # размещаем метку в окне
    # поле ввода для количества комнат
    entry_number_of_rooms = Entry() #создаем поле ввода
    entry_number_of_rooms.pack() # размещаем поле ввода в окно

    label_rent_price = Label(text="Cтоимость аренды за сутки") # создаем текстовую метку
    label_rent_price.pack() # размещаем метку в окне
    # поле ввода для стоимости аренды
    entry_rent_price = Entry() #создаем поле ввода
    entry_rent_price.pack() # размещаем поле ввода в окно

    label_description = Label(text="Описание") # создаем текстовую метку
    label_description.pack() # размещаем метку в окне
    # поле ввода для описания
    entry_description = Entry() #создаем поле ввода
    entry_description.pack() # размещаем поле ввода в окно
    
    def add_apartment():
        address = entry_address.get() # get - метод для считывания данных из поля
        square = entry_square.get() 
        number_of_rooms = entry_number_of_rooms.get() 
        rent_price = entry_rent_price.get() 
        description = entry_description.get() 
        apartment = Apartment(address, square, number_of_rooms, rent_price, description) # создается объект
        list_flat.append(apartment) # добавление объекта в список
        list_flat_var.set(list_flat) # обновление Listbox

    # кнопка для добавления квартиры
    btn_add_apartment = Button(text="Добавить квартиру", command=add_apartment)
    btn_add_apartment.pack()

    def delete(): # 
        index = apartment_listbox.curselection() # получить индекс выбранного элемента
        list_flat.remove(list_flat[index[0]]) # удалить элемент
        list_flat_var.set(list_flat) # переопределяем Listbox


    list_flat = [] # список для хранения квартир
    apartment = Apartment("Дубна, Университетская, 19", 300, 5, 4000, "Отличный ремонт и удобное расположение!")
    list_flat.append(apartment) # добавление объекта в список
    list_flat_var = Variable(master=None, value=list_flat, name=None) # сохранить созданный и заполненный список в переменную типа Variable
    apartment_listbox = Listbox(width=100, listvariable=list_flat_var) # создать листбокс, в котором будет отображаться список list_flat_var
    apartment_listbox.pack() # добавляем листбокс на форму

    def to_rent(self):
        self.status = "сдана"
        
    def cancel_rental(self):
        self.status = "свободна"

    def rental():
        index = apartment_listbox.curselection()
        list_flat[index[0]].to_rent()
        list_flat_var(list_flat)

    def cancel():
        index = apartment_listbox.curselection()
        list_flat[index[0]].cancel_rental()
        list_flat_var.set(list_flat)

    # кнопка для удаления квартиры из списка
    btn_del_apartment = Button(text="Удалить", command=delete)
    btn_del_apartment.pack()

    # кнопка для сдачи квартиры в аренду
    btn_rent_apartment = Button(text="Сдать квартиру", command=rental)
    btn_rent_apartment.pack()

    # кнопка для освобождения квартиры
    btn_change_rent_apartment = Button(text="Освободить квартиру", command=cancel)
    btn_change_rent_apartment.pack()

    root.mainloop()

