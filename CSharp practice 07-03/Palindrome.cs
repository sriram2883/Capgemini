using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

    class PalinConverter
    {
        public string ProcessInput(string input)
        {
            string processed = input.ToLower().TrimStart().TrimEnd().Replace("  ", " ");
            //while(processed.Contains("  "))
            //{
            //    processed = processed.Replace("  ", " ");
            //}
            string[] chars = processed.Split(' ');
            for (int i = 0; i < chars.Length; i++)
            {
                chars[i] = chars[i].TrimStart().TrimEnd();
                if (chars[i].Length > 2) { 
                    Console.Write(chars[i]);
                    Console.WriteLine(IsPalindrome(chars[i]) ? "  Yes" : "  No");
                }
            }
            return "";
    }
    public string Reverse(string input)
        {
            string reversed = "";
            for (int i = input.Length - 1; i >= 0; i--)
            {
                reversed += input[i];
            }
            return reversed;
        }

        public bool IsPalindrome(string input)
        {
            string reversed = Reverse(input);
            if (input == reversed)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
    }
    class Palindrome
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter a string to check if it is a palindrome: ");
            string input = Console.ReadLine();
            string inputLower = input.ToLower();
            PalinConverter pc = new PalinConverter();
            pc.ProcessInput(inputLower);
        //if (pc.IsPalindrome(inputLower))
        //{
        //    Console.WriteLine("The string is a palindrome.");
        //}
        //else
        //{
        //    Console.WriteLine("The string is not a palindrome.");
        //}
    }
    }

