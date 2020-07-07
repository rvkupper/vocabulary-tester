"""This file contains the backend of vocabulary-tester.

Author: rvkupper
Date of production: 7-7-2020
"""


def check(d: dict, key: str, ans: str, case_sensitive: bool = True) -> bool:
    """Check whether given answer ans is the correct value of key in 
    dictionary d with case sensitivity option. 
    
    :param:
    d: dictionary with words to be tested
    key: current word on trial
    ans: given answer by user
    
    :return:
    Returns boolean whether answer was correct.
    
    :exceptions:
    Raises assertion error if d is empty.
    Raises assertion error if key not in d.
    
    >>> check({'geel': 'yellow', 'rood': 'red'}, 'geel', 'yellow')
    True
    >>> check({'Nederland': 'Netherlands', 'Duitsland': 'Germany'}, 'Nederland', 'netherlands')
    False
    >>> check({'Nederland': 'Netherlands'}, 'Nederland', 'netherlands', case_sensitive=False)
    True
    >>> check({}, 'a', 'b')
    Traceback (most recent call last):
    ...
    AssertionError: d is empty, should contain dictionary object.
    """
    assert d, "d is empty, should contain dictionary object."
    assert key in d, "key not in d."
    
    if case_sensitive:
        return ans == d[key]
    else:
        ans_upper = ans.upper()
        correct_upper = d[key].upper()
        return ans_upper == correct_upper


# For doctesting
if __name__ == "__main__":
    import doctest
    doctest.testmod()
