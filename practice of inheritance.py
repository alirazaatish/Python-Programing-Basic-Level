class student:
    def __init__(self,name,roll_no,grade):
        self.name=name
        self.roll_no=roll_no
        self.grade=grade


class primary_section(student):
    def __init__(self,play_games):
        super().__init__( )
        self.play_games=play_games

class midlle_section(student):
    pass

primary_section_obj1=primary_section("Atish",5,"A","toys")
print(primary_section_obj1.name)
print(primary_section_obj1.roll_no)
print(primary_section_obj1.grade)
print(primary_section_obj1.play_games("toys"))

midlle_section_obj1=midlle_section("AIMEN",7,'B')
print(midlle_section_obj1.name)
print(midlle_section_obj1.roll_no)
print(midlle_section_obj1.grade)
