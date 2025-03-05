using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    public class Polymorphism
    {
        public Polymorphism()
        {
            Console.WriteLine("Constructor without parameters");
        }

        public virtual void Display()
        {
            Console.WriteLine("Method without parameters");
        }
    }

    public class Child : Polymorphism
    {
        public override void Display()
        {
            Console.WriteLine("Overridden method in Child class");
        }
    }

}
