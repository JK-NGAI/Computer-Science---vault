# Catering Company Invoice Management System

import datetime
import os

def display_menu():
    """Display the main menu options"""
    print("\n" + "="*60)
    print("     CATERING COMPANY INVOICE MANAGEMENT SYSTEM")
    print("="*60)
    print("1. Create New Invoice")
    print("2. View Existing Invoice")
    print("3. Update Invoice")
    print("4. List All Invoices")
    print("5. Delete Invoice")
    print("6. Exit")
    print("="*60)

def generate_invoice_number():
    """Generate a unique invoice number"""
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    return f"INV-{timestamp}"

def get_current_date():
    """Get current date in readable format"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_customer_name():
    """Get and validate customer name"""
    while True:
        name = input("Enter customer name: ").strip()
        if name:
            # Remove invalid characters for filename
            valid_name = "".join(c for c in name if c.isalnum() or c in (' ', '-', '_')).rstrip()
            if valid_name:
                return valid_name
            else:
                print("❌ Invalid name. Please use letters, numbers, spaces, hyphens, or underscores.")
        else:
            print("❌ Customer name cannot be empty.")

def add_items():
    """Add items to the invoice"""
    items = []
    print("\n--- ADD ITEMS (Enter 'done' when finished) ---")
    
    while True:
        item_name = input("Item name: ").strip()
        if item_name.lower() == 'done':
            break
        
        if not item_name:
            print("❌ Item name cannot be empty.")
            continue
        
        try:
            quantity = int(input("Quantity: "))
            if quantity <= 0:
                print("❌ Quantity must be positive.")
                continue
                
            price = float(input("Price per unit (KSh): "))
            if price <= 0:
                print("❌ Price must be positive.")
                continue
                
            # Calculate item total
            item_total = quantity * price
            
            # Create item dictionary
            item = {
                'name': item_name,
                'quantity': quantity,
                'price': price,
                'total': item_total
            }
            
            items.append(item)
            print(f"✅ Added: {item_name} x{quantity} @ KSh{price:.2f} each = KSh{item_total:.2f}")
            print("-" * 40)
            
        except ValueError:
            print("❌ Invalid input. Quantity must be integer, price must be number.")
    
    return items

def calculate_totals(items):
    """Calculate subtotal, tax, and grand total"""
    subtotal = sum(item['total'] for item in items)
    tax = subtotal * 0.16  # 16% VAT
    grand_total = subtotal + tax
    
    return subtotal, tax, grand_total

def create_invoice():
    """Create a new invoice"""
    print("\n" + "="*60)
    print("              CREATE NEW INVOICE")
    print("="*60)
    
    # Get customer name
    customer_name = get_customer_name()
    
    # Check if invoice already exists
    filename = f"{customer_name}.txt"
    if os.path.exists(filename):
        print(f"\n❌ Invoice for {customer_name} already exists.")
        overwrite = input("Do you want to overwrite? (yes/no): ").lower()
        if overwrite not in ['yes', 'y']:
            print("Invoice creation cancelled.")
            return
    
    # Generate invoice details
    invoice_number = generate_invoice_number()
    invoice_date = get_current_date()
    
    print(f"\nInvoice Number: {invoice_number}")
    print(f"Date: {invoice_date}")
    
    # Add items
    items = add_items()
    
    if not items:
        print("❌ No items added. Invoice not created.")
        return
    
    # Calculate totals
    subtotal, tax, grand_total = calculate_totals(items)
    
    # Save invoice to file
    save_invoice(filename, {
        'invoice_number': invoice_number,
        'invoice_date': invoice_date,
        'customer_name': customer_name,
        'items': items,
        'subtotal': subtotal,
        'tax': tax,
        'grand_total': grand_total
    })
    
    print(f"\n✅ Invoice created successfully!")
    print(f"📁 Saved as: {filename}")
    
    # Display invoice preview
    display_invoice_preview(customer_name)

def save_invoice(filename, invoice_data):
    """Save invoice data to file"""
    with open(filename, 'w') as file:
        # Write invoice header
        file.write("="*80 + "\n")
        file.write("                    CATERING COMPANY INVOICE\n")
        file.write("="*80 + "\n\n")
        
        file.write(f"Invoice Number: {invoice_data['invoice_number']}\n")
        file.write(f"Date: {invoice_data['invoice_date']}\n")
        file.write(f"Customer: {invoice_data['customer_name']}\n\n")
        
        file.write("-"*80 + "\n")
        file.write(f"{'Item':<30} {'Quantity':>10} {'Price':>12} {'Total':>12}\n")
        file.write("-"*80 + "\n")
        
        # Write items
        for item in invoice_data['items']:
            file.write(f"{item['name']:<30} {item['quantity']:>10} KSh{item['price']:>9.2f} KSh{item['total']:>9.2f}\n")
        
        file.write("-"*80 + "\n\n")
        
        # Write totals
        file.write(f"{'Subtotal:':>62} KSh{invoice_data['subtotal']:>9.2f}\n")
        file.write(f"{'VAT (16%):':>62} KSh{invoice_data['tax']:>9.2f}\n")
        file.write(f"{'GRAND TOTAL:':>62} KSh{invoice_data['grand_total']:>9.2f}\n\n")
        
        file.write("="*80 + "\n")
        file.write("           Thank you for choosing our catering services!\n")
        file.write("="*80 + "\n")

def display_invoice_preview(customer_name):
    """Display invoice preview on screen"""
    filename = f"{customer_name}.txt"
    
    try:
        with open(filename, 'r') as file:
            print("\n" + "="*80)
            print("                    INVOICE PREVIEW")
            print("="*80)
            print(file.read())
    except FileNotFoundError:
        print(f"❌ Invoice for {customer_name} not found.")
    except Exception as e:
        print(f"❌ Error displaying invoice: {e}")

def view_invoice():
    """View an existing invoice"""
    print("\n" + "="*60)
    print("                VIEW INVOICE")
    print("="*60)
    
    customer_name = input("Enter customer name to view invoice: ").strip()
    
    if not customer_name:
        print("❌ Customer name cannot be empty.")
        return
    
    filename = f"{customer_name}.txt"
    
    try:
        with open(filename, 'r') as file:
            print("\n" + "="*80)
            print(f"              INVOICE FOR: {customer_name}")
            print("="*80)
            print(file.read())
    except FileNotFoundError:
        print(f"❌ No invoice found for customer: {customer_name}")
    except Exception as e:
        print(f"❌ Error reading invoice: {e}")

def update_invoice():
    """Update an existing invoice"""
    print("\n" + "="*60)
    print("                UPDATE INVOICE")
    print("="*60)
    
    customer_name = input("Enter customer name to update invoice: ").strip()
    
    if not customer_name:
        print("❌ Customer name cannot be empty.")
        return
    
    filename = f"{customer_name}.txt"
    
    if not os.path.exists(filename):
        print(f"❌ No invoice found for customer: {customer_name}")
        return
    
    # Display current invoice
    print(f"\nCurrent invoice for {customer_name}:")
    view_invoice()
    
    print("\n--- UPDATE OPTIONS ---")
    print("1. Add new items")
    print("2. Clear all items and start over")
    print("3. Cancel update")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        # Add new items to existing invoice
        try:
            # Read existing invoice data
            with open(filename, 'r') as file:
                lines = file.readlines()
            
            # Extract items section (simplified approach - in production, parse properly)
            print("\n--- ADD NEW ITEMS ---")
            new_items = add_items()
            
            if new_items:
                # Recreate invoice with new items
                print("Updating invoice with new items...")
                
                # For simplicity, we'll recreate the invoice
                print("Please re-enter the updated order details:")
                items = add_items()
                
                if items:
                    # Generate new invoice data
                    invoice_number = generate_invoice_number()
                    invoice_date = get_current_date()
                    subtotal, tax, grand_total = calculate_totals(items)
                    
                    # Save updated invoice
                    save_invoice(filename, {
                        'invoice_number': invoice_number,
                        'invoice_date': invoice_date,
                        'customer_name': customer_name,
                        'items': items,
                        'subtotal': subtotal,
                        'tax': tax,
                        'grand_total': grand_total
                    })
                    
                    print(f"\n✅ Invoice updated successfully!")
                    display_invoice_preview(customer_name)
                else:
                    print("❌ No items added. Invoice not updated.")
            else:
                print("No new items added.")
                
        except Exception as e:
            print(f"❌ Error updating invoice: {e}")
    
    elif choice == '2':
        # Clear and start over
        print("\n--- CREATE NEW INVOICE (Replace existing) ---")
        create_invoice()
    
    elif choice == '3':
        print("Update cancelled.")
    
    else:
        print("❌ Invalid choice.")

def list_all_invoices():
    """List all invoice files"""
    print("\n" + "="*60)
    print("                ALL INVOICES")
    print("="*60)
    
    invoice_files = [f for f in os.listdir('.') if f.endswith('.txt') and f != 'ouk_students.txt']
    
    if not invoice_files:
        print("📁 No invoices found.")
        return
    
    print(f"\nFound {len(invoice_files)} invoice(s):\n")
    
    for i, filename in enumerate(invoice_files, 1):
        customer_name = filename[:-4]  # Remove .txt extension
        try:
            # Get file modification time
            mod_time = os.path.getmtime(filename)
            mod_date = datetime.datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d %H:%M")
            
            # Get invoice number from file
            with open(filename, 'r') as file:
                first_line = file.readline()  # Skip header
                second_line = file.readline()  # Skip header
                third_line = file.readline()  # Invoice number line
                if "Invoice Number:" in third_line:
                    inv_num = third_line.strip().replace("Invoice Number:", "").strip()
                else:
                    inv_num = "N/A"
            
            print(f"{i}. Customer: {customer_name}")
            print(f"   Invoice #: {inv_num}")
            print(f"   Last modified: {mod_date}")
            print()
            
        except Exception as e:
            print(f"{i}. {filename} (Error reading details)")

def delete_invoice():
    """Delete an invoice"""
    print("\n" + "="*60)
    print("                DELETE INVOICE")
    print("="*60)
    
    customer_name = input("Enter customer name to delete invoice: ").strip()
    
    if not customer_name:
        print("❌ Customer name cannot be empty.")
        return
    
    filename = f"{customer_name}.txt"
    
    if not os.path.exists(filename):
        print(f"❌ No invoice found for customer: {customer_name}")
        return
    
    # Show invoice preview before deletion
    print(f"\nInvoice to delete:")
    view_invoice()
    
    confirm = input(f"\nAre you sure you want to delete invoice for {customer_name}? (yes/no): ").lower()
    
    if confirm in ['yes', 'y']:
        try:
            os.remove(filename)
            print(f"✅ Invoice for {customer_name} deleted successfully!")
        except Exception as e:
            print(f"❌ Error deleting invoice: {e}")
    else:
        print("Deletion cancelled.")

def main():
    """Main program loop"""
    print("\n" + "="*60)
    print("  WELCOME TO CATERING COMPANY INVOICE SYSTEM")
    print("="*60)
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            create_invoice()
        elif choice == '2':
            view_invoice()
        elif choice == '3':
            update_invoice()
        elif choice == '4':
            list_all_invoices()
        elif choice == '5':
            delete_invoice()
        elif choice == '6':
            print("\n✅ Thank you for using Catering Company Invoice System!")
            print("   Goodbye!")
            break
        else:
            print("\n❌ Invalid choice. Please enter a number between 1 and 6.")

# Run the program
if __name__ == "__main__":
    main()