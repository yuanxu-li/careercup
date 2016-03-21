# Design Grade Database: Imagine a simple database storing information for students'
# grades. Design what this databse might look like and provide a SQL query to return
# a list of the honor roll students (top 10%), sorted by their grade point average.

Students:
StudentID
StudentName

Courses:
CourseID
CourseName

CourseStudent:
CourseID
StudentID
Grade

select top 10 percent StudentID, StudentName, avg(Grade)
from Students left join CourseStudent on Students.StudentID = CourseStudent.StudentID
group by StudentID, StudentName
order by avg(Grade) desc