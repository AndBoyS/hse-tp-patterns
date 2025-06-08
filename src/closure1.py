from typing import Any


# Базовый пример
def outer_function(msg) -> Any:
    def inner_function() -> Any:
        print(f"Message: {msg}")

    return inner_function


greet = outer_function("Hello, World!")
greet()
