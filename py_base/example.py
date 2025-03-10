"""Example module to demonstrate package functionality.

This module provides example functions and classes to show how to structure
Python package code with proper documentation and type hints.
"""
from typing import List, Optional


def add_numbers(a: float, b: float) -> float:
    """Add two numbers together.

    Args:
        a: The first number
        b: The second number

    Returns:
        The sum of the two numbers

    Examples:
        >>> add_numbers(1.0, 2.0)
        3.0
    """
    return a + b


class ExampleClass:
    """A simple example class to demonstrate class documentation.

    This class shows how to structure a Python class with proper documentation,
    type hints, and best practices.

    Attributes:
        name: A string representing the name of the instance
        value: An optional numeric value associated with the instance
    """

    def __init__(self, name: str, value: Optional[float] = None) -> None:
        """Initialize an ExampleClass instance.

        Args:
            name: The name of the instance
            value: An optional numeric value (default: None)
        """
        self.name = name
        self.value = value

    def get_info(self) -> dict:
        """Get information about the instance.

        Returns:
            A dictionary containing the instance's name and value
        """
        return {
            "name": self.name,
            "value": self.value
        }

    @staticmethod
    def list_items(items: List[str]) -> List[str]:
        """Process a list of items.

        Args:
            items: A list of strings to process

        Returns:
            The processed list of strings
        """
        return [item.strip().lower() for item in items]