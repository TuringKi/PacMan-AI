# testClasses.py
# --------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and Pieter 
# Abbeel in Spring 2013.
# For more info, see http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html

# import modules from python standard library
import inspect
import re
import sys

# Class which models a question in a project.  Note that questions have a
# maximum number of points they are worth, and are composed of a series of
# test cases
class Question(object):

    def raiseNotDefined(self):
        print 'Method not implemented: %s' % inspect.stack()[1][3]
        sys.exit(1)

    def __init__(self, questionDict):
        self.maxPoints = int(questionDict['max_points'])
        self.testCases = []

    def getMaxPoints(self):
        return self.maxPoints

    # Note that 'thunk' must be a function which accepts a single argument,
    # namely a 'grading' object
    def addTestCase(self, testCase, thunk):        
        self.testCases.append((testCase, thunk))

    def execute(self, grades):
        self.raiseNotDefined()

# Question in which all test cases must be passed in order to receive credit
class PassAllTestsQuestion(Question):

    def execute(self, grades):
        # TODO: is this the right way to use grades?  The autograder doesn't seem to use it.            
        testsFailed = False
        grades.assignZeroCredit()
        for _, f in self.testCases:
            if not f(grades):
                testsFailed = True
        if testsFailed:
            grades.fail("Tests failed.")
        else:
            grades.assignFullCredit()
            

# Question in which predict credit is given for test cases with a ``points'' property.
# All other tests are mandatory and must be passed.
class HackedPartialCreditQuestion(Question):

    def execute(self, grades):
        # TODO: is this the right way to use grades?  The autograder doesn't seem to use it.            
        grades.assignZeroCredit()
        
        points = 0
        passed = True
        for testCase, f in self.testCases:
            testResult = f(grades)
            if "points" in testCase.testDict:
                if testResult: points += float(testCase.testDict["points"])                
            else:
                passed = passed and testResult        
        
        ## FIXME: Below terrible hack to match q3's logic
        if int(points) == self.maxPoints and not passed:
            grades.assignZeroCredit()
        else:
            grades.addPoints(int(points))


class Q6PartialCreditQuestion(Question):
    """Fails any test which returns False, otherwise doesn't effect the grades object.
    Partial credit tests will add the required points."""

    def execute(self, grades):
        grades.assignZeroCredit()

        results = []
        for _, f in self.testCases:
            results.append(f(grades))
        if False in results:
            grades.assignZeroCredit()
            
class PartialCreditQuestion(Question):
    """Fails any test which returns False, otherwise doesn't effect the grades object.
    Partial credit tests will add the required points."""

    def execute(self, grades):
        grades.assignZeroCredit()
        
        for _, f in self.testCases:
            if not f(grades):
                grades.assignZeroCredit()
                grades.fail("Tests failed.")
                return False
            


# Template modeling a generic test case 
class TestCase(object):
    
    def raiseNotDefined(self):
        print 'Method not implemented: %s' % inspect.stack()[1][3]
        sys.exit(1)

    def getPath(self):
        return self.path

    def __init__(self, testDict):
        self.testDict = testDict
        self.path = testDict['path']

    def __str__(self):
        self.raiseNotDefined()
        
    def execute(self, grades, moduleDict, solutionDict):
        self.raiseNotDefined()

    def writeSolution(self, moduleDict, filePath):
        self.raiseNotDefined()
        return True

