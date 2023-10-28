Volume = 1.44
Numbers_of_pages = 100
Number_of_lines = 50
Number_of_characters = 25
One_characters = 4
Volume_b = Volume*1024*1024
Number_of_books = round((Volume_b / (Numbers_of_pages * Number_of_lines * Number_of_characters * One_characters)
                   ),)
print("Количество книг, помещающихся на дискету:", Number_of_books)
