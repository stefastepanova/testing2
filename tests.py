import unittest
from main import Calculator
from main import App
import tkinter as tk

class TestHealthCalculator(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = App(self.root)

    # Тест расчёта BMI
    def test_bmi_calculation_correct(self):
        weight = 70
        height = 170
        bmi = Calculator.calculate_bmi(weight, height)
        self.assertEqual(bmi, 24.22)

    # Тест расчёта калорий для мужчины
    def test_calories_calculation_male(self):
        weight = 70
        height = 170
        age = 30
        gender = "Мужской"
        activity_level = 1.35
        calories = Calculator.calculate_calories(weight, height, age, gender, activity_level)
        self.assertAlmostEqual(calories, 2256.34, places=1)

    # Тест расчёта калорий для женщины
    def test_calories_calculation_female(self):
        weight = 70
        height = 170
        age = 30
        gender = "Женский"
        activity_level = 1.35
        calories = Calculator.calculate_calories(weight, height, age, gender, activity_level)
        self.assertAlmostEqual(calories, 2010.96, places=1)

    # Тест расчёта воды
    def test_water_calculation_correct(self):
        weight = 70
        water = Calculator.calculate_water(weight)
        self.assertEqual(water, 2.1)

    # Тесты уровня активности
    def test_activity_level_light(self):
        days = 3
        intensity = "Легкие"
        activity_level = Calculator.calculate_activity_level(days, intensity)
        self.assertEqual(activity_level, 1.35)

    def test_activity_level_moderate(self):
        days = 3
        intensity = "Умеренные"
        activity_level = Calculator.calculate_activity_level(days, intensity)
        self.assertEqual(activity_level, 1.5)

    def test_activity_level_intense(self):
        days = 3
        intensity = "Интенсивные"
        activity_level = Calculator.calculate_activity_level(days, intensity)
        self.assertEqual(activity_level, 1.65)

    def test_activity_level_zero_days(self):
        days = 0
        intensity = "Умеренные"
        activity_level = Calculator.calculate_activity_level(days, intensity)
        self.assertEqual(activity_level, 1.2)

    # Тесты проверки веса
    def test_validate_weight_valid(self):
        weight = "70"
        self.assertEqual(self.app.validate_weight(weight), 70.0)

    def test_validate_weight_empty(self):
        with self.assertRaises(ValueError) as context:
            self.app.validate_weight("")
        self.assertEqual(str(context.exception), "Поле 'Вес' не может быть пустым.")

    def test_validate_weight_non_numeric(self):
        with self.assertRaises(ValueError) as context:
            self.app.validate_weight("abc")
        self.assertEqual(str(context.exception), "Вес должен быть числом.")

    def test_validate_weight_negative(self):
        with self.assertRaises(ValueError) as context:
            self.app.validate_weight("-5")
        self.assertEqual(str(context.exception), "Вес должен быть положительным числом.")

    # Тесты проверки роста
    def test_validate_height_valid(self):
        height = "170"
        self.assertEqual(self.app.validate_height(height), 170.0)

    def test_validate_height_empty(self):
        with self.assertRaises(ValueError) as context:
            self.app.validate_height("")
        self.assertEqual(str(context.exception), "Поле 'Рост' не может быть пустым.")

    def test_validate_height_non_numeric(self):
        with self.assertRaises(ValueError) as context:
            self.app.validate_height("xyz")
        self.assertEqual(str(context.exception), "Рост должен быть числом.")

    def test_validate_height_negative(self):
        with self.assertRaises(ValueError) as context:
            self.app.validate_height("-150")
        self.assertEqual(str(context.exception), "Рост должен быть положительным числом.")

    # Тесты проверки возраста
    def test_validate_age_valid(self):
        age = "25"
        self.assertEqual(self.app.validate_age(age), 25)

    def test_validate_age_empty(self):
        with self.assertRaises(ValueError) as context:
            self.app.validate_age("")
        self.assertEqual(str(context.exception), "Поле 'Возраст' не может быть пустым.")

    def test_validate_age_non_numeric(self):
        with self.assertRaises(ValueError) as context:
            self.app.validate_age("twenty")
        self.assertEqual(str(context.exception), "Возраст должен быть числом.")

    def test_validate_age_negative(self):
        with self.assertRaises(ValueError) as context:
            self.app.validate_age("-10")
        self.assertEqual(str(context.exception), "Возраст должен быть положительным числом.")

    # Тесты проверки количества тренировок
    def test_validate_days_valid(self):
        days = "3"
        self.assertEqual(self.app.validate_days(days), 3)

    def test_validate_days_empty(self):
        with self.assertRaises(ValueError) as context:
            self.app.validate_days("")
        self.assertEqual(str(context.exception), "Поле 'Количество тренировок в неделю' не может быть пустым.")

    def test_validate_days_non_numeric(self):
        with self.assertRaises(ValueError) as context:
            self.app.validate_days("abc")
        self.assertEqual(str(context.exception), "Количество тренировок должны быть числом.")

    def test_validate_days_negative(self):
        with self.assertRaises(ValueError) as context:
            self.app.validate_days("-1")
        self.assertEqual(str(context.exception), "Количество тренировок не может быть отрицательным.")

if __name__ == "__main__":
    unittest.main()
