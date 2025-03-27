using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class ExceptionClass
{
    public void Execute()
    {
        try
        {
            int a = 10;
            int b = 0;
            int c = a / b;
        }
        catch (Exception ex)
        {
            Console.WriteLine("Exception: " + ex.Message);
        }
        finally
        {
            Console.WriteLine("Finally block is executed");
        }
    }

    public static void Main(string[] args)
    {
        ExceptionClass ec = new ExceptionClass();
        ec.Execute();
    }
}
