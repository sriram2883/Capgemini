using Microsoft.EntityFrameworkCore;
using System;

var builder = WebApplication.CreateBuilder(args);
string connectionString = "Data Source=(localdb)\\MSSQLLocalDB;Initial Catalog=TestDb;Integrated Security=True;Pooling=False;Encrypt=True;Trust Server Certificate=True";

// Add services to the container.
//builder.Services.AddDbContext<AppDbContext>(options =>
//    options.UseSqlServer(connectionString));

builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();
app.UseAuthorization();
app.MapControllers();
app.Run();
