#Import classes from other module 
from todolist import TodoList, TodoItem


class ToDoListApp(object):

	
	def show_banner(self):
		print "This is Cliff's probably not working to do list app"
	
	def delete_command(self): 
	
	
	def add_command(self)
	#collect all to do item from user
	#create a toDoItem and populate it with data
	
	#store it to do list
		todo_list.add(??)
	
	
	
	def command_loop(self):
		self.show_banner()
		
		tdlist = TodoList()

		command = ""
		
		while command != "quit"
			comman = raw_input("What can I To Do List app for you?").strip().lower()
			if not command:
				continue

			if command == 'quit':
				break

			if command == 'add':
				self.add_command(tdlist)
			
			elif command == 'delete':
				self.delete_command(tdlist)
				
			elif command 