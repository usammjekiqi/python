from typing import Optional1
from typing import Union
from typing import Any
from typing import List

def greet(name: Optional1[str] = None) -> str:
    if name:
        return  name
    else:
        return " Anonymous"
    

print(greet())

def process_value(value: Union[int, str]) -> str:
    if isinstance(value, int):
        return f" Number: {value}"
    return f" String: {value}"

print(process_value("Digital school"))

def process_anything(value: Any) -> str:
    return f" processed: {value}"

print(process_anything(("any string")))

def sum_list(numbers: List[int]) -> int:
    return sum(numbers)

numbers = list[int] = [1, 2, 3]
result:int = sum_list(numbers)