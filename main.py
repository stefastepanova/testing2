import tkinter as tk
from tkinter import messagebox


class Calculator:
    def calculate_bmi(weight, height):
        height_in_meters = height / 100
        bmi = weight / (height_in_meters ** 2)
        return round(bmi, 2)

        
    def calculate_calories(weight, height, age, gender, activity_level):
        if gender == "Мужской":
            bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
        else:
            bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)
        return round(bmr * activity_level, 2)


    def calculate_water(weight):
        return round(weight * 0.03, 2)


    def calculate_activity_level(days, intensity):
        base_activity = 1.2
        intensity_multipliers = {
            "Легкие": 0.05,
            "Умеренные": 0.1,
            "Интенсивные": 0.15
        }
        extra_activity = days * intensity_multipliers[intensity]
        return round(base_activity + extra_activity, 2)


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор здоровья")
        self.create_widgets()

    
    def create_widgets(self):
        tk.Label(self.root, text="Вес (кг):").grid(row=0, column=0, sticky="w")
        tk.Label(self.root, text="Рост (см):").grid(row=1, column=0, sticky="w")
        tk.Label(self.root, text="Возраст:").grid(row=2, column=0, sticky="w")
        tk.Label(self.root, text="Пол:").grid(row=3, column=0, sticky="w")
        tk.Label(self.root, text="Количество тренировок в неделю:").grid(row=4, column=0, sticky="w")
        tk.Label(self.root, text="Интенсивность тренировок:").grid(row=5, column=0, sticky="w")

        self.weight_entry = tk.Entry(self.root)
        self.height_entry = tk.Entry(self.root)
        self.age_entry = tk.Entry(self.root)
        self.days_entry = tk.Entry(self.root)

        self.weight_entry.grid(row=0, column=1)
        self.height_entry.grid(row=1, column=1)
        self.age_entry.grid(row=2, column=1)
        self.days_entry.grid(row=4, column=1)

        self.gender_var = tk.StringVar(value="Мужской")
        tk.OptionMenu(self.root, self.gender_var, "Мужской", "Женский").grid(row=3, column=1)

        self.intensity_var = tk.StringVar(value="Легкие")
        tk.OptionMenu(self.root, self.intensity_var, "Легкие", "Умеренные", "Интенсивные").grid(row=5, column=1)

        tk.Button(self.root, text="Рассчитать", command=self.calculate).grid(row=6, column=0, columnspan=2)

    
    def validate_weight(self, weight):
        if not weight.strip():
            raise ValueError("Поле 'Вес' не может быть пустым.")
        try:
            weight = float(weight)
        except ValueError:
            raise ValueError("Вес должен быть числом.")
        if weight <= 0:
            raise ValueError("Вес должен быть положительным числом.")
        return weight


    def validate_height(self, height):
        if not height.strip():
            raise ValueError("Поле 'Рост' не может быть пустым.")
        try:
            height = float(height)
        except ValueError:
            raise ValueError("Рост должен быть числом.")
        if height <= 0:
            raise ValueError("Рост должен быть положительным числом.")
        return height


    def validate_age(self, age):
        if not age.strip():
            raise ValueError("Поле 'Возраст' не может быть пустым.")
        try:
            age = int(age)
        except ValueError:
            raise ValueError("Возраст должен быть числом.")
        if age <= 0:
            raise ValueError("Возраст должен быть положительным числом.")
        return age


    def validate_days(self, days):
        if not days.strip():
            raise ValueError("Поле 'Количество тренировок в неделю' не может быть пустым.")
        try:
            days = int(days)
        except ValueError:
            raise ValueError("Количество тренировок должны быть числом.")
        if days < 0:
            raise ValueError("Количество тренировок не может быть отрицательным.")
        return days


    def calculate(self):
        try:
            weight = self.validate_weight(self.weight_entry.get())
            height = self.validate_height(self.height_entry.get())
            age = self.validate_age(self.age_entry.get())
            days = self.validate_days(self.days_entry.get())
            gender = self.gender_var.get()
            intensity = self.intensity_var.get()

            activity_level = Calculator.calculate_activity_level(days, intensity)
            bmi = Calculator.calculate_bmi(weight, height)
            calories = Calculator.calculate_calories(weight, height, age, gender, activity_level)
            water = Calculator.calculate_water(weight)

            result = (
                f"Ваш ИМТ: {bmi}\n"
                f"Рекомендуемая норма калорий: {calories} ккал\n"
                f"Рекомендуемая норма воды: {water} л\n"
            )
            messagebox.showinfo("Результаты", result)
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.withdraw() 
