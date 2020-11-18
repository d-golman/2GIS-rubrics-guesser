import json

I = input

def findInDB(query):    
    with open("rubrics.json", "r",encoding="utf-8") as read_file:
        rubrics = json.load(read_file)
    result = []
    for rubric in rubrics.items():
        for keyword in rubric[1]:
            if query.lower() in keyword:
                result.append(rubric)
    selectRubric(result)

def selectRubric(rubrics):    
    with open("preferences.json", "r",encoding="utf-8") as read_file:
        preferences = json.load(read_file)    
    prefered = getPrefs(rubrics,preferences)
    print('Результаты:')
    for i,rubric in enumerate(prefered):
        print('{}: {}'.format(i,rubric))
    index = I('Выберите результат \n')
    choose = prefered[int(index)]
    setPrefs(choose,preferences,prefered)


def setPrefs(choose,preferences,prefered):
    if choose in list(preferences['user1'].keys()):
        for i in prefered:
            for j in preferences['user1'].items():
                if i ==j[0]:
                    if j[0] == choose:
                        if preferences['user1'][i] <= 4:
                            preferences['user1'][i] +=1
                    else:
                        if preferences['user1'][i] >= 1:
                            preferences['user1'][i] -=1
    else:
        preferences['user1'].update({choose:1})
    with open("preferences.json", "w", encoding="utf-8") as write_file:
        json.dump(preferences, write_file,ensure_ascii=False)

def getPrefs(rubrics,preferences):
    values = {}
    for rubric in rubrics:
        for preferense in preferences['user1'].items():
            if rubric[0] == preferense[0]:
                values.update({preferense[0]:preferense[1]})                    
    for rubric in rubrics:
        if rubric[0] not in list(values.keys()):
            values.update({rubric[0]:0})    
    values = {k: v for k, v in sorted(values.items(), key=lambda item: -item[1])} 
    result = list(values.keys())
    return(result)

    

def main():   
    query = I()
    findInDB(query)

if __name__ == "__main__":
    main()