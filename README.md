# Basic Data Structures Operations in Python

This Python program demonstrates basic operations on three fundamental data structures in Python: a list, a dictionary, and a set. It includes creating these data structures and performing basic operations such as adding, removing, and modifying elements.

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Usage](#usage)
4. [Code Explanation](#code-explanation)
    - [List Operations](#list-operations)
    - [Dictionary Operations](#dictionary-operations)
    - [Set Operations](#set-operations)
5. [Running the Program](#running-the-program)



## Introduction

This program is a simple demonstration of how to work with lists, dictionaries, and sets in Python. It covers:
- Creating a list, dictionary, and set.
- Adding elements.
- Removing elements.
- Modifying elements.

## Prerequisites

- Python 3.x installed on your system.
- Jupyter Notebook

## Usage

Clone this repository or download the script to your local machine. Run the script using Python to see the output of various operations on the list, dictionary, and set.

## Code Explanation

### List Operations

1. *Creating a list*:
    python
    my_list = [1, 2, 3, 4, 5]
    
2. *Adding an element to the list*:
    python
    my_list.append(6)
    
3. *Removing an element from the list*:
    python
    my_list.remove(3)
    
4. *Modifying an element in the list*:
    python
    my_list[2] = 10
    

### Dictionary Operations

1. *Creating a dictionary*:
    python
    my_dict = {'sateesh': 201, 'sudheer': 202, 'mohan': 203}
    
2. *Adding an element to the dictionary*:
    python
    my_dict['basha'] = 204
    
3. *Removing an element from the dictionary*:
    python
    del my_dict['sudheer']
    
4. *Modifying an element in the dictionary*:
    python
    my_dict['sateesh'] = 205
    

### Set Operations

1. *Creating a set*:
    python
    my_set = {1, 2, 3, 4, 5}
    
2. *Adding an element to the set*:
    python
    my_set.add(6)
    
3. *Removing an element from the set*:
    python
    my_set.discard(3)
    
4. *Modifying an element in the set* (by removing an element and adding a new one):
    python
    my_set.discard(4)
    my_set.add(10)


## Running the Program in Jupyter Notebook

To run the program in a Jupyter notebook, follow these steps:

1. **Open Jupyter Notebook:**
   - If you have Anaconda installed, you can open the Jupyter Notebook from the Anaconda Navigator.
   - Alternatively, you can open it by running the following command in your terminal or command prompt:
     bash
     jupyter notebook
     

2. **Create a New Notebook:**
   - Once Jupyter Notebook is open in your browser, click on "New" and select "Python 3" to create a new notebook.

3. **Copy and Paste the Code:**
   - Copy the provided code and paste it into the first cell of the new notebook.
4. **Run the Cell:**
   - Click on the cell containing the code and press `Shift + Enter` to run the cell. The output will be displayed below the cell.

