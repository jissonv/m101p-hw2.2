
from pymongo import MongoClient

# Write a program in the language of your choice that will remove the grade of
# type "homework" with the lowest score for each student from the dataset in
# the handout. Since each document is one grade, it should remove one document
# per student. This will use the same data set as the last problem, but if you
#  don't have it, you can download and re-import.

# grades.json
# There are two homework scores for each student and have data of 200 students
# { "_id" : ObjectId("50906d7fa3c412bb040eb57a"), "student_id" : 0, "type" : "homework", "score" : 63.98402553675503 }
# { "_id" : ObjectId("50906d7fa3c412bb040eb578"), "student_id" : 0, "type" : "quiz", "score" : 31.95004496742112 }
# { "_id" : ObjectId("50906d7fa3c412bb040eb579"), "student_id" : 0, "type" : "homework", "score" : 14.8504576811645 }
# { "_id" : ObjectId("50906d7fa3c412bb040eb577"), "student_id" : 0, "type" : "exam", "score" : 54.6535436362647 }
# { "_id" : ObjectId("50906d7fa3c412bb040eb57b"), "student_id" : 1, "type" : "exam", "score" : 74.20010837299897 }
# { "_id" : ObjectId("50906d7fa3c412bb040eb57c"), "student_id" : 1, "type" : "quiz", "score" : 96.76851542258362 }
# { "_id" : ObjectId("50906d7fa3c412bb040eb57d"), "student_id" : 1, "type" : "homework", "score" : 21.33260810416115 }
# { "_id" : ObjectId("50906d7fa3c412bb040eb57e"), "student_id" : 1, "type" : "homework", "score" : 44.31667452616328 }
# .....

# our aim is to remove the lowest homework score of each user

con = MongoClient('localhost')
db = con.students
try:

    homework_data = db.grades.find({'type': 'homework'}).sort([('student_id', 1), ('score', 1)])
    # The above query fetch all the homework data sorted in ascending order of first student_id and then in score

    # {u'student_id': 0, u'_id': ObjectId('50906d7fa3c412bb040eb579'), u'type': u'homework', u'score': 14.8504576811645}
    # {u'student_id': 0, u'_id': ObjectId('50906d7fa3c412bb040eb57a'), u'type': u'homework', u'score': 63.98402553675503}
    # {u'student_id': 1, u'_id': ObjectId('50906d7fa3c412bb040eb57d'), u'type': u'homework', u'score': 21.33260810416115}
    # {u'student_id': 1, u'_id': ObjectId('50906d7fa3c412bb040eb57e'), u'type': u'homework', u'score': 44.31667452616328}
    # Now all the student's minimum homework score in even index
    for index, item in enumerate(homework_data):
        print item
        if index % 2 == 0:
            print 'removing item', item
            db.grades.remove(item)

except Exception as e:
    print e





