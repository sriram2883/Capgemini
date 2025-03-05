using Microsoft.AspNetCore.Mvc;
using System.Security.Cryptography.X509Certificates;
using WebApplication1.model;
using static WebApplication1.model.Classes;

namespace WebApplication1.Controllers
{
    [ApiController]
    [Route("student")]

    public class StudentController : Controller
    {
        public static List<StudentAccount> studentlist = new List<StudentAccount>();
        [HttpGet(Name = "studentdata")]
        public IActionResult GetStudent()
        {
            for (int i = 0; i < 10; i++)
            {
                StudentAccount account = new StudentAccount();
                account.student = new Classes();
                account.student.Id = i;
                account.student.Name = "Student" + i;
                account.account = new Account();
                account.account.AccountId = i;
                account.account.AccountType = "savingsOf" + i;
                account.account.Balance = 1000 + i;
                studentlist.Add(account);

            }
            return Ok(studentlist);
        }

        [HttpGet("hey/{id}", Name = "GetStudentById")]
        public IActionResult GetStudentById(int id)
        {
            if (StudentController.studentlist.Count>0 && id >= 0 && id < studentlist.Count)
            {
                return Ok(studentlist[id]);
            }
            else
                return BadRequest("No record found");
        }

    }
}
