from creature import Creature
from item import Item
from location import Location

def test_creatures_1():
    """
    A student who enrolled in INFO1110 needs to write a program in python. 
    He is terror rating of 5 at the start.
    However, he find pycharm is very helpful to debug the code.
    The terror rating of pycharm is 100
    So the student will get a total terror rating of 105, if he uses pycharm to write programs.
    """
    USYD = Location("USYD")
    me = Creature("Me", 5, USYD, "INFO1110 student")
    USYD.add_creature(me)
    pycharm = Item("pycharm", "powerful pycharm", "A powerful tool such as pycharm can help you debug", 100)
    USYD.add_item(pycharm)
    me.get_location().remove_item(pycharm)
    me.take(pycharm)
    assert me.get_terror_rating() == 105, "Test 1 failed."
    print("Test 1 passed!")

def test_creatures_2():
    """
    This student is taught to use terminal with atom to write code.
    But after he uses terminal with atom, he find the interface is not very good.
    Cannot compare with pycharm. 
    So that he decide not to listen to teachers, but keep using pycharm. 
    Therefore, the student should still have a terror rating of 105 after he decides not to use terminal.
    """
    USYD = Location("USYD")
    me = Creature("Me", 5, USYD, "INFO1110 student")
    USYD.add_creature(me)
    pycharm = Item("pycharm", "powerful pycharm","A powerful tool such as pycharm can help you debug", 100)
    USYD.add_item(pycharm)
    me.get_location().remove_item(pycharm)
    me.take(pycharm)
    terminal = Item("terminal","Mac terminal","A console to execute commands directly", 1)
    USYD.add_item(terminal)
    me.take(terminal)
    me.get_location().remove_item(terminal)
    me.drop(terminal)
    me.get_location().add_item(pycharm)
    assert me.get_terror_rating() == 105, "Test 2 failed."
    print("Test 2 passed!")
    
def test_creatures_3():
    '''
    The student keep using pycharm during lab, and it was caught by the tutor at school.
    The tutor ask student not using pycharm anymore, but tutor has lower terror rating than student.
    So that tutor is trying to make student not to use pycharm, but he can do nothing to abandon. 
    The student is still not being caught, and he is still able to use pycharm. 
    So that the times that tutor catch student about not using pycharm is only once.
    '''
    USYD = Location("USYD")
    me = Creature("Me", 5, USYD, "INFO1110 student")
    USYD.add_creature(me)
    pycharm = Item("pycharm","powerful pycharm","A powerful tool such as pycharm can help you debug", 100)
    USYD.add_item(pycharm)
    me.get_location().remove_item(pycharm)
    me.take(pycharm)
    tutor = Creature("Tutor", 2, USYD, "INFO1110 tutor")
    USYD.add_creature(tutor)
    tutor.catch()
    assert me.get_terror_rating() == 105 and tutor.get_catch_time() == 1, "Test 3 failed."
    print("Test 3 passed!")
    
def test_creatures_4():
    '''
    The school provide a powerful online software, edstem, to help student learn INFO1110.
    This item is located on the location, online. 
    Student at the location, online, is able to access this item to enhance their studies.
    Thus, the student will gain a total terror rating of 15. 
    '''
    online = Location("online")
    me = Creature("Me", 5, online, "INFO1110 student")
    online.add_creature(me)
    edstem = Item("edstem","school management software","A powerful online software to discuss and submit homework", 10)
    online.add_item(edstem)
    me.get_location().remove_item(edstem)
    me.take(edstem)
    assert me.get_terror_rating() == 15, "Test 4 failed."
    print("Test 4 passed!")
    
def test_creatures_5():
    '''
    Online is on the north of USYD, so that there exits a path between them. 
    The student is originally at the USYD, but he moves north to online.
    Make sure the current location of the student is online 
    '''
    online = Location("online")
    USYD = Location("USYD")
    USYD.add_path("north", online)
    me = Creature("Me", 5, USYD, "INFO1110 student")
    USYD.add_creature(me)
    me.get_location().remove_creature(me)
    paths = me.get_location().get_paths()
    me.set_location(paths.get("north"))
    me.get_location().add_creature(me)
    assert me.get_location() == online, "Test 5 failed."
    print("Test 5 passed!")
    
test_creatures_1()
test_creatures_2()
test_creatures_3()
test_creatures_4()
test_creatures_5()

