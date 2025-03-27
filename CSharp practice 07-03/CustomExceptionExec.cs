using CSharp_practice_07_03;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class CustomExceptionExec
{
    public static void Main(string[] args)
    {
        try
        {
            int a = 10;
            int b = 0;
            if (b == 0)
            {
                throw new CustomException("Divide by zero error");
            }
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
}