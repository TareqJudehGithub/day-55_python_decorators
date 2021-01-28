# Create the logging_decorator() function 👇
class User:
  def __init__(self, name):
    self.name = name
    self.is_logged_in = False


def is_authenticated_decorator(function):
  def wrapper(*args):
    if args[0].is_logged_in:
      function(args[0])
  return wrapper


@is_authenticated_decorator
def create_blog_post(user):
  print(f"This is {user.name}'s blog post.") 

new_user = User("Ali")
new_user.is_logged_in = True

create_blog_post(new_user)


# ================================================================================


def decorator_function(function):
    def wrapper_function():
        function()
    return wrapper_function


def say_hello():
    print("Hello")


say_hello()


def some_func(*args, **kwargs):
    # *args and **kwargs:
    age, height, weight, lucky_number = args
    print(age, height, weight, lucky_number)
    print(args[2])
    print(f"My name is {kwargs['fname']} {kwargs['lname'] }")


some_func(1, 2, 3, 4, fname="Tareq", lname="Joudeh")