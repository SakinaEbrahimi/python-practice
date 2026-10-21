def show_todo_list(todo_list):
    if(len(todo_list) == 0):
        print("You do not have any todo yet.")
        return

    for index in range(len(todo_list)):
        print(f"{index + 1}: {todo_list[index]}")

def todo():
    is_continue = True
    print("Welcome to ToDo creator.")
    todos = []
    while(is_continue):
        userRequest = int(input(" 1 for create todo list \n 2 for see your todo list \n 3 for delete todo list \n 4 for exit \n Please Enter an number "))
        if( userRequest == 1):
            new_todo = input("Enter your todo ")
            if(len(new_todo) == 0):
                continue
            todos.append(new_todo)
        elif( userRequest == 2):
            show_todo_list(todos)
        elif( userRequest == 3):
            show_todo_list(todos)  
            if(len(todos) == 0):
                continue          
            remove_index = int(input("Please Enter number of todo."))

            if(0 < remove_index <= len(todos)):
                todos.pop(remove_index - 1)
            else:
                print("Invalid index.") 
        elif( userRequest == 4):
            print("You exited from program.")
            is_continue = False
        else:
            print("Invalid value please enter valid number")
        


todo()
