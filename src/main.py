
from datetime import date
from utils import add, subtract

print("Name: Faria Tasnim Era")
print("Today's Date:", date.today())

print("10 + 5 =", add(10, 5))
print("10 - 5 =", subtract(10, 5))

from utils import add, subtract, multiply, divide

print("10 / 5 =", divide(10, 5))
print("10 / 0 =", divide(10, 0))