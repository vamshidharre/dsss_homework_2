from setuptools import setup, find_packages

setup(
    name='math-quiz',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz:math_quiz',  # Adjust this line based on your actual entry point
        ],
    },
)
