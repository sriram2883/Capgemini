using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Student
    {
        public string name;
        public int age;
    }
    class Dualmain
    {
        static void Main(string[] args)
        {
            List<Student> list = new List<Student>();

            list.Add(new Student() { name = "sriram", age = 10 });
            list.Add(new Student() { name="hari",age = 20 });
            list.Add(new Student() { name = "ddn" ,age = 22 });
            var filterednames = from student in list
                                where student.age > 20
                                orderby student.name descending
                                select student.name;

            foreach (var item in filterednames)
            {
                Console.WriteLine(item);
            }
        }
    }
}
