class AIAgent:
    def __init__(self):
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)

    def get_skills(self):
        return self.skills