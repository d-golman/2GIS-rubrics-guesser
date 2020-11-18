import json

I = input

def findInDB(query):    #поиск совпадений в ДБ
    with open("rubrics.json", "r",encoding="utf-8") as read_file:
        rubrics = json.load(read_file)
    result = []
    for rubric in rubrics.items(): # занесение в список групп с совпадением ключевого слова
        for keyword in rubric[1]:
            if query.lower() in keyword:
                result.append(rubric)
    selectRubric(result)

def selectRubric(rubrics):    # выдача и выбор рубрики
    with open("preferences.json", "r",encoding="utf-8") as read_file:
        preferences = json.load(read_file)    
    prefered = getPrefs(rubrics,preferences) # формирование выдачи
    print('Результаты:')
    for i,rubric in enumerate(prefered): # выдача рубрик
        print('{}: {}'.format(i,rubric))
    index = I('Выберите результат \n') # выбор рубрики
    choose = prefered[int(index)]
    setPrefs(choose,preferences,prefered) 


def setPrefs(choose,preferences,prefered): # изменение предпочтений пользователя
    if choose in list(preferences['user1'].keys()):# изменение веса предпочтений
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
    for rubric in rubrics: # занесение значений у которых есть вес
        for preferense in preferences['user1'].items():
            if rubric[0] == preferense[0]:
                values.update({preferense[0]:preferense[1]})                    
    for rubric in rubrics: # занесение значений без веса
        if rubric[0] not in list(values.keys()):
            values.update({rubric[0]:0})    
    values = {k: v for k, v in sorted(values.items(), key=lambda item: -item[1])} # сортировка по уменьшению веса
    result = list(values.keys())
    return(result)

    

def main():   
    query = I() #запрос пользователя
    findInDB(query) 

if __name__ == "__main__":
    main()