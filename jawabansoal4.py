#Nama       : Umar Hilmi
#NIM        : 221402077
#Number     : 4

class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def bmi_value(self):
        height_m = self.height * 0.3048
        weight_kg = self.weight * 0.453592
        bmi = weight_kg / (height_m ** 2)
        return bmi

    def __eq__(self, other):
        return self.weight == other.weight and self.height == other.height

person1 = BMI(70, 5.8)
person2 = BMI(80, 6.0)

print("BMI person 1:", person1.bmi_value())
print("BMI person 2:", person2.bmi_value())
print("Are both persons equal in weight and height?", person1 == person2)