skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala', 'NodeJS'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}

#print(job_skills.intersection(skills))

print(list(skills & job_skills)[0])
print(skills & job_skills)
print(list(skills & job_skills))
