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
# Ainius Sinickas 1820516
# Jonas Mieliauskas 1719408g
# Gustas Šimkus 1704917
##

# Import built-in json library for handling input/output 
import json

from operations.polynomial_arithmetic.polynomial_addition import polynomial_addition
from operations.polynomial_arithmetic.polynomial_subtraction import polynomial_subtraction
from operations.polynomial_arithmetic.polynomial_multiplication import polynomial_multiplication
from operations.polynomial_arithmetic.polynomial_longdivision import remove_leading_zeros
from operations.polynomial_arithmetic.euclidean_algo import extended_euclidefn_flgo

from operations.finite_fields_arithmetic.addition import finite_fields_addition
from operations.finite_fields_arithmetic.subtraction import finite_fields_subtraction
from operations.finite_fields_arithmetic.multiplication import finite_fields_multiplication
from operations.finite_fields_arithmetic.division import finite_fields_division
from operations.finite_fields_arithmetic.inverse import finite_fields_inversion
from operations.finite_fields_arithmetic.primitivity_check import primitivity_checking


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
        
        elif exercise["task"] == "long_division":
            answer = remove_leading_zeros(exercise["f"], exercise["g"], exercise["p"])
        
        elif exercise["task"] == "extended_euclidean_algorithm":
            answer = extended_euclidefn_flgo(exercise["f"], exercise["g"], exercise["p"])
            
        # et cetera
    elif  exercise["type"] == "finite_field_arithmetic":
        # Check what task within the finite field arithmetic tasks we need to perform
        if exercise["task"] == "addition":
            answer = finite_fields_addition(exercise["f"], exercise["g"], exercise["m"], exercise["h"])
            
        elif exercise["task"] == "subtraction":
            answer = finite_fields_subtraction(exercise["f"], exercise["g"], exercise["m"], exercise["h"])
            
        elif exercise["task"] == "multiplication":
            answer = finite_fields_multiplication(exercise["f"], exercise["g"], exercise["m"], exercise["h"])
            
        elif exercise["task"] == "division":
            answer = finite_fields_division(exercise["f"], exercise["g"], exercise["m"], exercise["h"])
        
        elif exercise["task"] == "inversion":
            answer = finite_fields_inversion(exercise["f"], exercise["m"], exercise["h"])
        
        elif exercise["task"] == "primitivity_check":
            answer = primitivity_checking(exercise["f"], exercise["m"], exercise["h"])
            
        # et cetera


    # Open file at answer_location for writing, creating the file if it does not exist yet
    # (and overwriting it if it does already exist).
    with open(answer_location, "w") as answer_file:
        # Serialize Python answer data (stored in answer) to JSON answer data and write it to answer_file
        json.dump(answer, answer_file, indent=4)
