"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[(1234, 2, 2)]],
            "answer": [1243, 1324, 1432, 2134, 3214, 4231],
        },
        {
            "input": [[(8765, 1, 0), (1234, 2, 1)]],
            "answer": [1245, 1263, 1364, 1435, 1724, 1732, 
2734, 3264, 4235, 8134, 8214, 8231],
        },
                {
            "input": [[(1234, 2, 2), (4321, 1, 3)]],
            "answer": [],
        },
    ],
    "Extra": [
        {
            "input": [[(3127, 0, 1), (5723, 1, 0), 
(7361, 0, 2), (1236, 1, 0)]],
            "answer": [4786, 4796, 8746, 8796, 9746, 9786],
        },
    ]
}
