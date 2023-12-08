
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Car:
    car_count = 0

    def __init__(self, brand, model, color, transmission, drive):
        Car.car_count += 1
        self.car_number = Car.car_count
        self.brand = brand
        self.model = model
        self.color = color
        self.transmission = transmission
        self.drive = drive
        self.features = {
            "Двери": "закрыты",
            "Фары": "выключены",
            "Двигатель": "заглушен",
            "Багажник": "закрыт"
        }

    def toggle_feature(self, feature):
        if feature in self.features:
            if feature == "Двери":
                if self.features[feature] == "закрыты":
                    self.features[feature] = "открыты"
                else:
                    self.features[feature] = "закрыты"
            elif feature == "Фары":
                if self.features[feature] == "выключены":
                    self.features[feature] = "включены"
                else:
                    self.features[feature] = "выключены"
            elif feature == "Двигатель":
                if self.features[feature] == "заглушен":
                    self.features[feature] = "заведен"
                else:
                    self.features[feature] = "заглушен"
            elif feature == "Багажник":
                if self.features[feature] == "закрыт":
                    self.features[feature] = "открыт"
                else:
                    self.features[feature] = "закрыт"

    def get_status(self):
        status = f"Машина #{self.car_number}: {self.brand} {self.model}\n"
        status += f"Цвет: {self.color}\n"
        status += f"Коробка передач: {self.transmission}\n"
        status += f"Привод: {self.drive}\n"
        for feature, feature_status in self.features.items():
            status += f"{feature}: {feature_status}\n"
        return status

def add_car():
    brand = brand_var.get()
    model = model_var.get()
    color = color_var.get()
    transmission = transmission_var.get()
    drive = drive_var.get()
    car = Car(brand, model, color, transmission, drive)
    cars.append(car)
    update_car_listbox()

def delete_car():
    index = car_listbox.curselection()
    if index:
        car_index = int(index[0])
        cars.pop(car_index)
        for i in range(car_index, len(cars)):
            cars[i].car_number -= 1
        update_car_listbox()

def delete_all_cars():
    global cars
    cars = []
    update_car_listbox()

def select_car(event):
    index = car_listbox.curselection()[0]
    car_index = int(index)
    selected_car = cars[car_index]
    status_label.config(text=selected_car.get_status())

def toggle_feature(feature):
    index = car_listbox.curselection()[0]
    car_index = int(index)
    selected_car = cars[car_index]
    selected_car.toggle_feature(feature)
    status_label.config(text=selected_car.get_status())

def sort_by_color():
    cars.sort(key=lambda car: car.color)
    update_car_listbox()

def sort_by_transmission():
    cars.sort(key=lambda car: car.transmission)
    update_car_listbox()

def sort_by_drive():
    cars.sort(key=lambda car: car.drive)
    update_car_listbox()

def update_car_listbox():
    car_listbox.delete(0, tk.END)
    for car in cars:
        car_listbox.insert(tk.END, f"{car.car_number}: {car.brand} {car.model}")

brands = ["Audi", "BMW", "Mercedes-Benz", "Volkswagen", "Toyota", "Honda", "Ford", "Chevrolet", "Nissan", "Hyundai", "Kia", "Mazda", "Volvo", "Subaru", "Lexus", "Jaguar", "Land Rover", "Porsche", "Ferrari"]
models = {
    "Audi": ["A3", "A4", "A6", "Q5", "Q7"],
    "BMW": ["X3", "X5", "3 Series", "5 Series", "7 Series"],
    "Mercedes-Benz": ["C-Class", "E-Class", "S-Class", "GLC", "GLE"],
    "Volkswagen": ["Golf", "Passat", "Jetta", "Tiguan", "Atlas"],
    "Toyota": ["Corolla", "Camry", "RAV4", "Highlander", "Sienna"],
    "Honda": ["Civic", "Accord", "CR-V", "Pilot", "Odyssey"],
    "Ford": ["F-150", "Escape", "Focus", "Explorer", "Mustang"],
    "Chevrolet": ["Silverado", "Equinox", "Malibu", "Traverse", "Camaro"],
    "Nissan": ["Altima", "Rogue", "Sentra", "Murano", "Pathfinder"],
    "Hyundai": ["Elantra", "Sonata", "Tucson", "Santa Fe", "Kona"],
    "Kia": ["Forte", "Optima", "Sportage", "Sorento", "Telluride"],
    "Mazda": ["Mazda3", "Mazda6", "CX-5", "CX-9", "MX-5 Miata"],
    "Volvo": ["S60", "S90", "XC40", "XC60", "XC90"],
    "Subaru": ["Impreza", "Legacy", "Outback", "Crosstrek", "Ascent"],
    "Lexus": ["ES", "LS", "NX", "RX", "GX"],
    "Jaguar": ["XE", "XF", "F-PACE", "E-PACE", "I-PACE"],
    "Land Rover": ["Range Rover", "Discovery", "Evoque", "Velar", "Defender"],
    "Porsche": ["911", "Cayenne", "Panamera", "Macan", "Taycan"],
    "Ferrari": ["F8 Tributo", "Portofino", "Roma", "812 Superfast", "SF90 Stradale"]
}

transmissions = ["МКПП", "АКПП"]
drives = ["Задний", "Передний", "4WD"]
colors = ["Красный", "Синий", "Белый", "Черный", "Серый", "Зеленый", "Серебристый", "Желтый"]

cars = []

app = tk.Tk()
app.title("Car Control App")
app.geometry("800x800")  # Установите размер окна
app.resizable(False, False)


# Добавьте фоновое изображение автомобиля
image = Image.open("car.png")  # Замените "car_background.jpg" на путь к вашему изображению
photo = ImageTk.PhotoImage(image)
background_label = tk.Label(app, image=photo)
background_label.place(relwidth=1, relheight=1)


brand_label = tk.Label(app, text="Марка машины:")
brand_label.pack()

brand_var = tk.StringVar()
brand_combobox = ttk.Combobox(app, textvariable=brand_var, values=brands)
brand_combobox.pack()

model_label = tk.Label(app, text="Модель машины:")
model_label.pack()

model_var = tk.StringVar()
model_combobox = ttk.Combobox(app, textvariable=model_var, values=[""])
model_combobox.pack()

color_label = tk.Label(app, text="Цвет:")
color_label.pack()

color_var = tk.StringVar()
color_combobox = ttk.Combobox(app, textvariable=color_var, values=colors)
color_combobox.pack()

transmission_label = tk.Label(app, text="Коробка передач:")
transmission_label.pack()

transmission_var = tk.StringVar()
transmission_combobox = ttk.Combobox(app, textvariable=transmission_var, values=transmissions)
transmission_combobox.pack()

drive_label = tk.Label(app, text="Привод:")
drive_label.pack()

drive_var = tk.StringVar()
drive_combobox = ttk.Combobox(app, textvariable=drive_var, values=drives)
drive_combobox.pack()

add_button = tk.Button(app, text="Добавить машину", command=add_car)
add_button.pack()

delete_button = tk.Button(app, text="Удалить машину", command=delete_car)
delete_button.pack()

delete_all_button = tk.Button(app, text = "Удалить все машины", command = delete_all_cars)
delete_all_button.pack()

car_listbox = tk.Listbox(app)
car_listbox.pack()
car_listbox.bind("<<ListboxSelect>>", select_car)

status_label = tk.Label(app, text="", justify="left")
status_label.pack()

feature_buttons = []
features = ["Двери", "Фары", "Двигатель", "Багажник"]

for feature in features:
    button = tk.Button(app, text=feature, command=lambda f=feature: toggle_feature(f))
    button.pack()
    feature_buttons.append(button)

sort_color_button = tk.Button(app, text="Сортировка по цвету", command=sort_by_color)
sort_color_button.pack()

sort_transmission_button = tk.Button(app, text="Сортировка по коробке передач", command=sort_by_transmission)
sort_transmission_button.pack()

sort_drive_button = tk.Button(app, text="Сортировка по приводу", command=sort_by_drive)
sort_drive_button.pack()

def update_models(event):
    selected_brand = brand_var.get()
    models_for_brand = models.get(selected_brand, [""])
    model_combobox['values'] = models_for_brand
    model_combobox.set(models_for_brand[0])

brand_combobox.bind("<<ComboboxSelected>>", update_models)

app.mainloop()