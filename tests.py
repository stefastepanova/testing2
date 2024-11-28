import unittest
from main import Calculator
from main import App
import tkinter as tk

class TestHealthCalculator(unittest.TestCase):
    
    def setUp(self):
        self.root = tk.Tk()
        self.app = App(self.root)

    def test_bmi_calculation(self):
        weight = 70
        height = 170
        bmi = Calculator.calculate_bmi(weight, height)
        self.assertEqual(bmi, 24.22)

    def test_calories_calculation(self):
        weight = 70
        height = 170
        age = 30
        gender = "Мужской"
        activity_level = 1.35
        calories = Calculator.calculate_calories(weight, height, age, gender, activity_level)
        self.assertAlmostEqual(calories, 2256.34, places=1)
        
        gender = "Женский"
        calories = Calculator.calculate_calories(weight, height, age, gender, activity_level)
        self.assertAlmostEqual(calories, 2010.96, places=1) 

    def test_water_calculation(self):
        weight = 70
        water = Calculator.calculate_water(weight)
        self.assertEqual(water, 2.1)

    def test_activity_level_calculation(self):
        days = 3
        intensity = "Легкие"
        activity_level = Calculator.calculate_activity_level(days, intensity)
        self.assertEqual(activity_level, 1.35)
        
        intensity = "Умеренные"
        activity_level = Calculator.calculate_activity_level(days, intensity)
        self.assertEqual(activity_level, 1.5)
        
        intensity = "Интенсивные"
        activity_level = Calculator.calculate_activity_level(days, intensity)
        self.assertEqual(activity_level, 1.65)
        
        days = 0
        intensity = "Умеренные"
        activity_level = Calculator.calculate_activity_level(days, intensity)
        self.assertEqual(activity_level, 1.2)

    def test_validate_weight(self):
        weight = "70"
        self.assertEqual(self.app.validate_weight(weight), 70.0)

        with self.assertRaises(ValueError) as context:
            self.app.validate_weight("")
        self.assertEqual(str(context.exception), "Поле 'Вес' не может быть пустым.")

        with self.assertRaises(ValueError) as context:
            self.app.validate_weight("abc")
        self.assertEqual(str(context.exception), "Вес должен быть числом.")

        with self.assertRaises(ValueError) as context:
            self.app.validate_weight("-5")
        self.assertEqual(str(context.exception), "Вес должен быть положительным числом.")

    def test_validate_height(self):
        height = "170"
        self.assertEqual(self.app.validate_height(height), 170.0)

        with self.assertRaises(ValueError) as context:
            self.app.validate_height("")
        self.assertEqual(str(context.exception), "Поле 'Рост' не может быть пустым.")

        with self.assertRaises(ValueError) as context:
            self.app.validate_height("xyz")
        self.assertEqual(str(context.exception), "Рост должен быть числом.")

        with self.assertRaises(ValueError) as context:
            self.app.validate_height("-150")
        self.assertEqual(str(context.exception), "Рост должен быть положительным числом.")

    def test_validate_age(self):
        age = "25"
        self.assertEqual(self.app.validate_age(age), 25)

        with self.assertRaises(ValueError) as context:
            self.app.validate_age("")
        self.assertEqual(str(context.exception), "Поле 'Возраст' не может быть пустым.")

        with self.assertRaises(ValueError) as context:
            self.app.validate_age("twenty")
        self.assertEqual(str(context.exception), "Возраст должен быть числом.")

        with self.assertRaises(ValueError) as context:
            self.app.validate_age("-10")
        self.assertEqual(str(context.exception), "Возраст должен быть положительным числом.")

    def test_validate_days(self):
        days = "3"
        self.assertEqual(self.app.validate_days(days), 3)

        with self.assertRaises(ValueError) as context:
            self.app.validate_days("")
        self.assertEqual(str(context.exception), "Поле 'Количество тренировок в неделю' не может быть пустым.")

        with self.assertRaises(ValueError) as context:
            self.app.validate_days("abc")
        self.assertEqual(str(context.exception), "Количество тренировок должны быть числом.")

        with self.assertRaises(ValueError) as context:
            self.app.validate_days("-1")
        self.assertEqual(str(context.exception), "Количество тренировок не может быть отрицательным.")


if __name__ == "__main__":
    unittest.main()
