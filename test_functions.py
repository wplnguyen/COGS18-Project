import functions as functions
import os
 
def specificFiles():
    path = os.getcwd()
    f = open("[COGS100] Assignment 1.txt", "w+")
    f.write("COGS 100: Cyborgs Now and in the Future")
    f.close()
    print("[COGS100] Assignment 1.txt created in " + path)
    f = open("[COGS1] Assignment 1.txt", "w+")
    f.write("COGS 1: Intro to Cognition")
    f.close()
    print("[COGS1] Assignment 1.txt created in " + path)
    f = open("[COGS18] Assignment 1.txt", "w+")
    f.write("COGS 18: Python")
    f.close()
    print("[COGS18] Assignment 1.txt created in " + path)
    f = open("[COGS10] Assignment 1.txt", "w+")
    f.write("COGS 10: Cognition")
    f.close()
    print("[COGS10] Assignment 1.txt created in " + path)

def testFunction1():
    specificFiles()
    functions.bracketSort()
    files = os.listdir()
    count = 0
    for item in files:
        if os.path.isdir(item):
            try:
                assert item == 'COGS1'
                count += 1
            except AssertionError:
                next
            try:
                assert item == 'COGS10'
                count += 1
            except AssertionError:
                next
            try:
                assert item == 'COGS100'
                count += 1
            except AssertionError:
                next
            try:
                assert item == 'COGS18'
                count += 1
            except AssertionError:
                next
    assert count == 4
    
def testFunction2():
    specificFiles()
    functions.inTextSort()
    files = os.listdir()
    count = 0
    for item in files:
        if os.path.isdir(item):
            try:
                assert item == 'COGS1'
                count += 1
            except AssertionError:
                next
            try:
                assert item == 'COGS10'
                count += 1
            except AssertionError:
                next
            try:
                assert item == 'COGS100'
                count += 1
            except AssertionError:
                next
            try:
                assert item == 'COGS18'
                count += 1
            except AssertionError:
                next
    assert count == 4
    
def testFunction3():
    specificFiles()
    functions.bracketSort()
    files = os.listdir()
    count = 0
    for item in files:
        if os.path.isdir(item):
            try:
                assert item == 'COGS1'
                count += 1
            except AssertionError:
                next
            try:
                assert item == 'COGS10'
                count += 1
            except AssertionError:
                next
            try:
                assert item == 'COGS100'
                count += 1
            except AssertionError:
                next
            try:
                assert item == 'COGS18'
                count += 1
            except AssertionError:
                next
    assert count == 4    
        
testFunction1()
testFunction2()
testFunction3()