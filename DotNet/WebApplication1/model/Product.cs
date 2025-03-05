using System.ComponentModel.DataAnnotations;

namespace WebApplication1.model
{
    public class Product
    {
        [Key]
        public int ProductId { get; set; }
        public string Name { get; set; }
        public int Price { get; set; }
    }
}
