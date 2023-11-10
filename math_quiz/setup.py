from setuptools import setup, find_packages

setup(
    name='math_quiz',  # Change 'math_quiz' to the name of your package
    version='1.0',  # Specify the version number
    packages=find_packages(),  # Automatically include all packages
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:math_quiz'  # Replace with your actual entry point
        ]
    },
)
