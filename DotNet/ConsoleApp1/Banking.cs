using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Banking
    {
        private string _accountNumber;

        public string AccountNumber
        {
            get { return _accountNumber; }
            set
            {
                if (value.Length == 10)
                {
                    _accountNumber = value;
                }
                else
                {
                    Console.WriteLine("Account number must be 10 characters long");
                }
            }
        }
    }
}
