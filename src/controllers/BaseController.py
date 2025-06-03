from helpers.config import Settings, get_settings
import os
import random
import string

class BaseController:
    """
    Base controller class that initializes settings.
    This class can be extended by other controllers to inherit the settings.
    """
    def __init__(self):
        self.settings = get_settings()

        self.base_path = os.path.dirname(os.path.dirname(__file__))
        self.files_path = os.path.join(self.base_path, 'assets/files')

    def generate_random_string(self, length: int = 10) -> str:
        """
        Generate a random string of fixed length.
        
        Args:
            length (int): The length of the random string to generate. Default is 10.
        Returns:
            str: A random string consisting of letters and digits.
        """
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))
    