def test_function():
    def inner_function():
        print("Я в области видмости test_function")

    inner_function()

test_function()

try:
   inner_function()
except NameError as a:
  print(f"Ошибка:{a}")




