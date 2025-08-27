from abc import ABC , abstractmethod
from enum import Enum
# WHEN NOT TO USE THE STATE PATTERN : NOT TO DO OVER ENGINEERING
class Stopwatch:
    def __init__(self):
        self._is_running = False
    
    def click (self):
        if self._is_running == True:
            self._is_running = False
            print("The clock has been stopped")
        elif self._is_running == False:
            self._is_running = True
            print("The clock has been Started")

watch =Stopwatch()
watch.click()
watch.click()
watch.click()
watch.click()