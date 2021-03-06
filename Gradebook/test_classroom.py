from classroom import Classroom


def setup_for_test():
    classroom = Classroom("Music")
    return classroom

def test_init_class():
    classroom = Classroom("Music")
    assert classroom.name == "Music"

def test_eroll_student():
    classroom = setup_for_test()
    classroom.enroll_student("Will", 1)
    assert classroom.roster["Will"] == 1
    classroom.enroll_student("Bill", 2)
    assert classroom.roster["Bill"] == 2
    assert len(classroom.roster) == 2

def test_give_assignment():
    classroom = setup_for_test()
    classroom.enroll_student("Will", 1)
    classroom.give_assignment(1, "Brew")
    assert classroom.assignments[1] == "Brew"

def test_edit_grade():
    classroom = setup_for_test()
    classroom.enroll_student("Will", 1)
    classroom.give_assignment(1, "Brew")
    classroom.edit_grade(1, 90)

def test_add_course():
    classroom = setup_for_test()
    classroom.add_course("Violin", "1-3pm")
    classroom.add_course("Piano", "4-7pm")
    assert classroom.courses['Violin'] == "1-3pm"
    assert classroom.courses['Piano'] == "4-7pm"
    assert len(classroom.courses) == 2

def test_delete_course():
    classroom = setup_for_test()
    classroom.add_course("Violin", "1-3pm")
    classroom.add_course("Piano", "4-7pm")
    classroom.delete_course("Violin")
    assert len(classroom.courses) == 1
    classroom.delete_course("Piano")
    assert len(classroom.courses) == 0

def test_update_course_time():
    classroom = setup_for_test()
    classroom.add_course("Violin", "1-3pm")
    classroom.add_course("Piano", "4-7pm")
    classroom.update_course_time("Violin", "8-10am")
    assert classroom.courses["Violin"] == "8-10am"



test_init_class()
# test_add_course()
# test_delete_course()
# test_eroll_student()
# test_give_assignment()
test_edit_grade()
