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
    project_skills = int(project_line[1])
    for j in range(project_skills):
        project_skill = inp_file.readline().split()
        project_skill_name = project_skill[0]
        project_skill_level = int(project_skill[1])
        skills_level[project_skill_name] = project_skill_level
    project = Project(project_name, skills_level, int(project_line[1]), int(project_line[2]), int(project_line[3]),int(project_line[4]))
    #(name , skill , duration{time} , score , best_before , no. of contributors)
    projects.append(project)

## Nubs First


# find minimum skill required of all projects
min_skill_required = {}
for project in projects:
        for skill in project.skills_level:
            if skill not in min_skill_required:
                min_skill_required[skill] = project.skills_level[skill,project]
            else:
                if min_skill_required[skill] > project.skills_level[skill][0]:
                    min_skill_required[skill] = [project.skills_level[skill],project]
        # project order by skill
        project_order_by_skill = []
        for skill in min_skill_required:
            project_order_by_skill.append(min_skill_required[skill])
        project_order_by_skill.sort(key=lambda x: x[0])
stop = False
ans = []
while not stop:
    # allot contributers to projects
    stop = True
    for project in project_order_by_skill:
        is_valid_project = True
        min_contributer = None
        for contributer in contributers:
            if contributer.available == 0:
                if min_contributer == None:
                    min_contributer = contributer
                if min_contributer.skills_level[project[1]] > contributer.skills_level[project[1]]:
                    min_contributer = contributer
        
        if min_contributer:
            # check project's skill level required
            contri_to_project = [min_contributer]
            for skill in project[1].skills_level:
                if is_valid_project:
                    for con in contributers:
                        found = False
                        if con not in contri_to_project:
                            if con.skills_level[skill] >= project[1].skills_level[skill]:
                                contri_to_project.append(con)
                        if not found:
                            is_valid_project = False
                            break
            if is_valid_project:
                ans.append(project[1],contri_to_project)
                stop = False
                for con in contri_to_project:
                    con.make_contribute(project[1].time)
    con.update_round()
    if stop:
        break
# print answer
print(len(ans))
for a in ans:
    print(a[0].name)
    for con in a[1]:
        print(con.name,end=" ")
    print()         
