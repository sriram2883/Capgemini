using System;
using System.Linq;
using System.Threading;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Support.UI;
using NUnit.Framework;

[TestFixture]
public class Test1Test
{
    private IWebDriver driver;
    private IJavaScriptExecutor js;

    [SetUp]
    public void SetUp()
    {
        driver = new ChromeDriver();
        js = (IJavaScriptExecutor)driver;
        driver.Manage().Window.Maximize();
    }

    [TearDown]
    public void TearDown()
    {
        driver.Dispose();
        driver.Quit();
    }

    [Test]
    public void TestPythonCompiler()
    {
        driver.Navigate().GoToUrl("https://www.programiz.com/python-programming/online-compiler");

        WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(10));

        var editor = wait.Until(d => d.FindElement(By.CssSelector("#editor .ace_text-input")));

        editor.SendKeys(Keys.Control + "a");
        editor.SendKeys(Keys.Backspace);

        editor.SendKeys("a = 5\nb = 10\nprint(a + b)");

        var runButton = driver.FindElement(By.CssSelector(".run-text"));
        runButton.Click();

        Thread.Sleep(3000);

        string terminalContent = (string)js.ExecuteScript(@"
            return document.querySelector('#terminal').innerText.trim();
        ");

        Console.WriteLine("Extracted Terminal Content:\n" + terminalContent);
        string firstLine = terminalContent.Split('\n')[0].Trim();

        Assert.AreEqual("15", firstLine, "Unexpected output from compiler!");
    }
}
