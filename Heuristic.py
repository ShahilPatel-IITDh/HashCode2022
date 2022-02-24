import sys

inp_file = open(sys.argv[1], 'r')

class Contributer:
    def __init__(self, name, skills_level: dict):
        self.name = name
        self.skills_level = skills_level
        self.available = 0
    def make_contribute(self,time:int):
        self.available = time
    def update_round(self):
        self.available -= 1


class Project:
    def __init__(self, name, skills_level: dict, time:int, score:int, best_before:int, no_of_contributers:int):
        self.name = name
        self.skills_level = skills_level
        self.time = time
        self.best_before = best_before
        self.no_of_contributers = no_of_contributers
    

no_of_contributers, no_of_projects = map(int, inp_file.readline().split())

contributers = []
for i in range(no_of_contributers):
    contributer_line = inp_file.readline().split()
    contributer_name = contributer_line[0]
    skills_level = {}
    contributer_skills = int(contributer_line[1])
    for j in range(contributer_skills):
        contributer_skill = inp_file.readline().split()
        contributer_skill_name = contributer_skill[0]
        contributer_skill_level = int(contributer_skill[1])
        skills_level[contributer_skill_name] = contributer_skill_level
    contributer = Contributer(contributer_name, skills_level)
    contributers.append(contributer)

projects = []
for i in range(no_of_projects):
    project_line = inp_file.readline().split()
    project_name = project_line[0]
    skills_level = {} #{skill,level}
    project_skills = int(project_line[-1])
    #print(project_line)
    for j in range(project_skills):
        project_skill = inp_file.readline().split()
        project_skill_name = project_skill[0]
        project_skill_level = int(project_skill[1])
        skills_level[project_skill_name] = project_skill_level
    project = Project(project_name, skills_level, int(project_line[1]), int(project_line[2]), int(project_line[3]),int(project_line[4]))
    #(name , skill , duration{time} , score , best_before , no. of contributors)
    projects.append(project)

heuristic=[]
for i in projects:
    sum=0
    #print(i.name)
    for s in i.skills_level:
        sum+=i.skills_level[s]
    h=i.time*i.best_before*sum
    heuristic.append([i,i.time*i.best_before*sum])

def criteria(e):
    return e[1]

heuristic.sort(key=criteria)
for i in heuristic:
    print(i)