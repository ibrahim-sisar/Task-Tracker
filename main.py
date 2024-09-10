import json

def add_task(task):
    the_task_name=task

    with open('task.json','r') as id_number:
        data2=json.load(id_number)
        id_number2=len(data2)+1


    dict={
        'task':the_task_name,
        'in-progress':False,
        'done':False,
        'id':id_number2
    }
    with open('task.json','r') as git_data:
        data=json.load(git_data)
        data[id_number2]=dict
        
    
    with open('task.json','w') as save:
        json.dump(data,save)
        print(f'Task added successfully (ID: {id_number2})')  
def list():
    with open('task.json','r') as git_data:
        data=json.load(git_data)
        for task in data:
            print(data[task]['task'])
def list_done():
    with open('task.json','r') as git_data:
        data=json.load(git_data)
        for task in data:
            if data[task]['done'] == True:
                print(data[task]['task'])
def list_in_progress():
    with open('task.json','r') as git_data:
        data=json.load(git_data)
        for task in data:
            if data[task]['in-progress'] == True:
                print(data[task]['task'])
def list_todo():
    with open('task.json','r') as git_data:
        data=json.load(git_data)
        for task in data:
            if data[task]['done'] == False and data[task]['in-progress'] == False:
                print(data[task]['task'])
def delet_task(task):
    no=task
    with open('task.json','r') as git_data:
        data=json.load(git_data)
       
        if no in data:
            data.pop(no)
            with open('task.json','w') as delete:
                json.dump(data,delete)
                print(f'Task deleted successfully')  
        
def updata_task(task,new_task):
    the_task_name=task
    
    

    with open('task.json','r') as git_data:
        data=json.load(git_data)
        task_name=data[task]['task']
        task_done=data["1"]['done']
        task_in_progress=data[task]['in-progress']
        if the_task_name in data:
            the_new_task_name=new_task
            dict={
                'task':the_new_task_name,
                'in-progress':task_in_progress,
                'done':task_done,
                'id':the_task_name
            }
            data[the_task_name]=dict
            print(data)
            
    
    
            with open('task.json','w') as save:
                json.dump(data,save)
                print(f'Task updata successfully') 
def mark_in_progress(id):
    the_task_name=id
    
    with open('task.json','r') as id_number:
        data2=json.load(id_number)

    with open('task.json','r') as git_data:
        data=json.load(git_data)
        task_name=data[id]['task']
        task_done=data[id]['done']
        if the_task_name in data:
            
            dict={
                'task':task_name,
                'in-progress':True,
                'done':False,
                'id':the_task_name
            }
            data[the_task_name]=dict
     
            
    
    
            with open('task.json','w') as save:
                json.dump(data,save)
                print(f'Task marked successfully')
def mark_done(id):
    the_task_name=id
    
    with open('task.json','r') as id_number:
        data2=json.load(id_number)

    with open('task.json','r') as git_data:
        data=json.load(git_data)
        task_name=data[id]['task']
        task_in_progress=data[id]['in-progress']
        if the_task_name in data:
            
            dict={
                'task':task_name,
                'in-progress':False,
                'done':True,
                'id':the_task_name
            }
            data[the_task_name]=dict
           
            
    
    
            with open('task.json','w') as save:
                json.dump(data,save)
                print(f'Task marked successfully') 


while True:
    task=input('task-cli ')
    if task.startswith('add'):
        task2=task[4:]
        task3=task2.strip("'")
        task3=task3.strip('"')
        add_task(task3)
    elif task.startswith('delete'):
        task2=task[7:]
        delet_task(task3)
    elif task.startswith('updata'):
        print('updata')
        task2=task[7:]
        if task2.find('"') != -1:
            text = task2.split('"')
        elif task2.find("'") != -1:
            text = task2.split("'")
        old_task=text[0].strip()
        new_task=text[1].strip()
        updata_task(old_task,new_task)
    elif task.startswith('mark-in-progress'):
        task2=task[17:]
        mark_in_progress(task2)
    elif task.startswith('mark-done'):
        task2=task[10:]
        mark_done(task2)
    elif task.startswith('list done'):
        list_done()
    elif task.startswith('list todo'):
        list_todo()   
    elif task.startswith('list in-progress'):
        list_in_progress() 
    elif task.startswith('list'):
        list()
    else:
        print('Unknown input')
    




