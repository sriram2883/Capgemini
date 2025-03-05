using Microsoft.VisualStudio.TestTools.UnitTesting;
using Testing.Program;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;
namespace Testing.Program.Tests
{
    [TestClass()]
    public class CalculatorTests
    {
        Calculator calculator = new Calculator();
        [TestMethod()]
        public void AddTest()
        {
            int expected = 3;
            int actual = calculator.Add(1, 2);
            Debug.WriteLine($"Expected: {expected}, Actual: {actual}");
            Assert.AreEqual(expected, actual, "The Add method did not return the expected result.");
        }
    }
}
