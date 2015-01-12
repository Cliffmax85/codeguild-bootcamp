
		
		
		
		
		
		
address_book = []		
		
def delete_contact():
	print address_book
	
	#delete contains name to delete
	delete = raw_input("Enter name to be deleted: ")
	#find entry name in list address_book
	#that may succeed or fail. If don't find name print error
	for delete in address_book:
		if delete == 'quit':
			
		
	
	
	
	
def add_to_list():
	
	contact = raw_input("Enter name first a comma and then your number ")
	parts = {'contact_info' : contact}
	parts = contact.split(',')
	print parts
	return parts 


def main():
	
	while True:
	
		choice = raw_input("Enter address book command. Add, list, delete or quit:")
		if choice == 'quit':
			print "Thanks for using the address book. Goodbye!"
			break
			
		elif choice == 'add':
			print "Add entry to address book"
			
			new_contact = add_to_list()
			address_book.append(new_contact)
			print "added"
			
		elif choice == 'delete':
			print "Delete entry from address book"
			#contact_to_delete = delete_contact()
			#address_book.remove(contact_to_delete)
			
			
		elif choice == 'list':
			print "Listing entries from address book"
			print address_book
			
			
		else: 
			print "I'm sorry I don't know that command"
			
main()
	


	
