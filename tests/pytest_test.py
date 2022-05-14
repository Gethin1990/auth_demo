import os,sys                                     
sys.path.append(os.getcwd()) 

import inc_dec    # The code to test

def test_increment():
    print('abc')
    assert inc_dec.increment(3) == 4

def test_decrement():
    print('abc')
    assert inc_dec.decrement(3) == 2