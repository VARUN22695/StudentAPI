namespace StudentApi.Models
{
    public class Student
    {
        public int Id { get; set; }          // Primary key
        public string Name { get; set; }     // Student name
        public int Age { get; set; }         // Student age
        public string Course { get; set; }   // Enrolled course
    }
}
