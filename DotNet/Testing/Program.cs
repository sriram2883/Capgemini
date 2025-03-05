using System;
namespace Testing
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var calculator = new Calculator();
            var result = calculator.Add(1, 2);
            Console.WriteLine(result);
        }


    }
}