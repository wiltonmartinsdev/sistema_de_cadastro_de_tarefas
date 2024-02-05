class Task:
    def __init__(self, Id, Title, Description, Completed=False) -> None:
        self.Id = Id
        self.Title = Title
        self.Description = Description
        self.Completed = Completed

    def to_dict(self):
        return {
            "Id": self.Id,
            "Title": self.Title,
            "Description": self.Description,
            "Completed": self.Completed 
        }