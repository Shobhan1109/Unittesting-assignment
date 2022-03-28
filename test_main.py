import unittest
import sqlite3
class employee(unittest.TestCase):
    def setUp(self):
        self.connection=sqlite3.connect("employee.db")
        self.empcode = "1102"
        self.empname = "John"

    def tearDown(self):
        self.empcode = "0"
        self.empname = ""

    def test_case_employee(self):
        r = self.connection.execute("SELECT empname from employee where empcode = "+self.empcode)
        for i in r:
            namefetch = i[0]
        self.assertEqual(namefetch, self.empname)

if __name__=="__main__":
    unittest.main()