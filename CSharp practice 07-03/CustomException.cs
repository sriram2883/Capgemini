using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharp_practice_07_03
{
    class CustomException : Exception
    {
        public CustomException(string message) : base(message)
        {
        }
    }
}
