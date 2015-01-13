import json 
		
file_name = "./contact_info.json" 		
		
		
def load_file(book):
	 
	f = open(file_name, 'r')
	#try:	
	book.update(json.load(f))	
	#except ValueError:
		#print "Invalid Data"
		#return
	f.close()		
		
		
		
def delete_contact(book):

	delete = raw_input("Enter name to be deleted")
	try:
		del book[delete] 
	except KeyError:
		print "No name in system"
		return 
		
	
	
	
	
	
def add_to_list(book):
	
	contact = raw_input("Type out Name and phone number seperated by a comma: ")
	contact_split = contact.split(",")
	if len(contact_split) != 2:
		print "Entered bad info"
		return
	book[contact_split[0]] = contact_split[1]
	
	
def save_list(book):

	f = open(file_name, 'w')
	json.dump(book, f)
	f.close()
	


def main():

	address_book = {}
	
	while True:
	
		choice = raw_input("Enter address book command. Add, list, del, load and save :")
		if choice == 'quit':
			print "Thanks for using the address book. Goodbye!"
			break
			
		elif choice == 'add':
			print "Add entry to address book: "
			
			add_to_list(address_book)
			
		
		elif choice == 'delete':
			print "Delete entry from address book"
			
			delete_contact(address_book)
			
		elif choice == 'list':
			print "Listing entries from address book"
			print address_book
			
		elif choice == "Save":
			print "Save list"
			save_list(address_book)
			
		elif choice == "load":
			print "Load list"
			load_file(address_book)	
				
		else: 
			print "I'm sorry I don't know that command"
			
main()
	


	
