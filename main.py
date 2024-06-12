import django_setup

from myapp.models import User, Status, Task

user1 = User.objects.create(name = "Ivan")
user2 = User.objects.create(name = "Max")

status1 = Status.objects.create(status = "success")
status2 = Status.objects.create(status = "not a success")

task1 = Task.objects.create(name = "Biology", description = "This is interesting lesson", status = status1, assigned_to = user1)
task2 = Task.objects.create(name = "Chemistry", description = "This is beautiful lesson", status = status2, assigned_to = user2)

task1.status = status2
task1.save()

task1.assigned_to = user2
task1.save()

'''not_need = Status.objects.get(id=4)
not_need.delete()
'''