using Microsoft.EntityFrameworkCore;
using WebApplication2.model;

namespace WebApplication2
{
    public class ApplicationDbContext:DbContext
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options) { }

        public DbSet<Product> Products { get; set; }

    }
}
