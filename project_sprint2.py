from typing import Type, Dict, List

class Training:
    """Родительский класс Training содержит базовые методы и свойства 
    фитнес-трекера."""
    
    M_IN_KM: int = 1000
    len_step: float = 0.65
    
    def __init__(self, action: int, duration: float, weight: float) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight    

    def get_distance(self) -> float:
        distance = self.action * self.len_step / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        mean_speed = self.get_distance()/self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        pass

    def show_training_info(self):
        return InfoMessage(self.__class__.__name__, self.duration, 
        self.get_distance(), self.get_mean_speed(), self.get_spent_calories())


class Running(Training):
    """Дочерний класс содержит метод расчета калорий для бега."""

    def get_spent_calories(self)-> float:
        coeff_calorie_1: float = 18
        coeff_calorie_2: float = 20
        running_spent_calories = ((coeff_calorie_1 * self.get_mean_speed() 
        - coeff_calorie_2) * self.weight / self.M_IN_KM * self.duration * 60)
        return running_spent_calories


class SportsWalking(Training):
    """Дочерний класс содержит дополнительный параметр и метод расчета калорий 
    для ходьбы."""

    def __init__(self, action, duration, weight, height) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        coeff_calorie_3: float = 0.035
        coeff_calorie_4: float = 0.029
        walking_spent_calories = ((coeff_calorie_3 * self.weight 
        + (self.get_mean_speed() ** 2 // self.height) * coeff_calorie_4 * self.weight) 
        * self.duration * 60)
        return walking_spent_calories


class Swimming(Training):
    """Дочерний класс содержит дополнительные параметры и методы расчета калорий, 
    средней скорости дистанции для ходьбы."""

    def __init__(self, action, duration, weight, length_pool: int, 
    count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_spent_calories(self) -> float:
        coeff_calorie_5: float = 1.1
        coeff_calorie_6: float = 2
        swimming_spent_calories = ((self.get_mean_speed() + coeff_calorie_5) 
        * coeff_calorie_6 * self.weight)
        return swimming_spent_calories

    def get_mean_speed(self) -> float:
        mean_speed = (self.length_pool * self.count_pool / self.M_IN_KM 
        / self.duration)
        return mean_speed

    def get_distance(self) -> float:
        len_step: float = 1.38
        distance = self.action * len_step / self.M_IN_KM
        return distance

class InfoMessage:
    """Самостоятельный класс для создания объектов сообщений."""

    def __init__(self, training_type: str, duration: float, distance: float, 
        speed: float, calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def info_message (self):
        return (f'Тип тренировки: {self.training_type}; Длительность: ' 
               f'{self.duration:.3f} ч.; Дистанция: {self.distance:.3f}'
               f' км; Ср. скорость: {self.speed:.3f} км/ч; '
               f'Потрачено ккал: {self.calories:.3f}.')

def read_package(workout_type: str, data: List [int]) -> Training:
    """Функция распаковки пакета данных для тестов."""
    workout: Dict[str, Type[Training]] = {'SWM': Swimming,'RUN': Running, 
    'WLK': SportsWalking,}
    return workout[workout_type](*data)

def main(training_enter: Training) -> InfoMessage:
    """Функция вывода экземпляра класса Training."""
    info = training_enter.show_training_info()
    print (info.info_message())

if __name__ == '__main__':
    """Имитация получения данных от блока датчиков фитнес-трекера"""
    packages = [        
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
