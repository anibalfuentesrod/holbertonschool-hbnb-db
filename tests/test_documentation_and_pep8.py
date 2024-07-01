"""
This module contains tests for checking documentation and PEP8 compliance.
"""

import unittest
import pycodestyle
import os
import ast

class TestDocumentation(unittest.TestCase):
    """
    This class represents the test case for documentation and PEP8 compliance.
    """

    def test_documentation(self):
        """
        Test if all modules, classes, functions, and methods have docstrings.
        """
        for root, _, files in os.walk('src'):
            for file in files:
                if file.endswith('.py'):
                    with open(os.path.join(root, file)) as f:
                        tree = ast.parse(f.read())
                        self.check_docstrings(tree, os.path.join(root, file))

    def check_docstrings(self, tree, file_path):
        """
        Check if the given tree has docstrings.

        Args:
            tree (AST): The AST of the file.
            file_path (str): The path to the file.
        """
        self.assertIsNotNone(
            ast.get_docstring(tree),
            f'Module {file_path} is missing a docstring'
        )
        for node in tree.body:
            if isinstance(node, (ast.ClassDef, ast.FunctionDef)):
                self.assertIsNotNone(
                    ast.get_docstring(node),
                    f'{node.name} in {file_path} is missing a docstring'
                )

    def test_pep8_compliance(self):
        """
        Test if the codebase is PEP8 compliant.
        """
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(['src'])
        self.assertEqual(
            result.total_errors, 0,
            f"Found PEP8 errors and warnings: {result.total_errors}"
        )
