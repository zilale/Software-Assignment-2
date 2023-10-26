##
# 2WF90 Algebra for Security -- Software Assignment 2
# Polynomial and Finite Field Arithmetic
# solve.py
#
#
# Group number:
# group_number 
#
# Author names and student IDs:
# Žilvinas Aleksa 1703749
# Ainius Sinickas 1704919
# Jonas Mieliauskas 1719408g
# Gustas Šimkus 1704917
##

# Import built-in json library for handling input/output 
import json

from operations.polynomial_arithmetic.polynomial_addition import polynomial_addition
from operations.polynomial_arithmetic.polynomial_subtraction import polynomial_subtraction
from operations.polynomial_arithmetic.polynomial_multiplication import polynomial_multiplication
from operations.polynomial_arithmetic.polynomial_longdivision import polynomial_long_division

from operations.finite_fields.addition import finiteFieldsAddition
from operations.finite_fields.subtraction import finiteFieldsSubtraction
from operations.finite_fields.multiplication import finiteFieldsMultiplication
from operations.finite_fields.division import finiteFieldsDivision
from operations.finite_fields.inverse import finiteFieldsInversion


def solve_exercise(exercise_location : str, answer_location : str):
    """
    solves an exercise specified in the file located at exercise_location and
    writes the answer to a file at answer_location. Note: the file at
    answer_location might not exist yet and, hence, might still need to be created.
    """
    
    # Open file at exercise_location for reading.
    with open(exercise_location, "r") as exercise_file:
        # Deserialize JSON exercise data present in exercise_file to corresponding Python exercise data 
        exercise = json.load(exercise_file)
        

    ### Parse and solve ###

    # Check type of exercise
    if exercise["type"] == "polynomial_arithmetic":
        # Check what task within the polynomial arithmetic tasks we need to perform
        if exercise["task"] == "addition":
            answer = polynomial_addition(exercise["f"], exercise["g"], exercise["p"])
            
        elif exercise["task"] == "subtraction":
            answer = polynomial_subtraction(exercise["f"], exercise["g"], exercise["p"])
        
        elif exercise["task"] == "multiplication":
            answer = polynomial_multiplication(exercise["f"], exercise["g"], exercise["p"])
        
        elif exercise["task"] == "division":
            answer = polynomial_long_division(exercise["f"], exercise["g"], exercise["p"])
            
        # et cetera
    elif  exercise["type"] == "finite_field_arithmetic":
        # Check what task within the finite field arithmetic tasks we need to perform
        if exercise["task"] == "addition":
            answer = finiteFieldsAddition(exercise["f"], exercise["g"], exercise["m"], exercise["h"])
            
        elif exercise["task"] == "subtraction":
            answer = finiteFieldsSubtraction(exercise["f"], exercise["g"], exercise["m"], exercise["h"])
            
        elif exercise["task"] == "multiplication":
            answer = finiteFieldsMultiplication(exercise["f"], exercise["g"], exercise["m"], exercise["h"])
            
        elif exercise["task"] == "division":
            answer = finiteFieldsDivision(exercise["f"], exercise["g"], exercise["m"], exercise["h"])
        
        elif exercise["task"] == "inversion":
            answer = finiteFieldsInversion(exercise["f"], exercise["m"], exercise["h"])
            
        # et cetera


    # Open file at answer_location for writing, creating the file if it does not exist yet
    # (and overwriting it if it does already exist).
    with open(answer_location, "w") as answer_file:
        # Serialize Python answer data (stored in answer) to JSON answer data and write it to answer_file
        json.dump(answer, answer_file, indent=4)
    