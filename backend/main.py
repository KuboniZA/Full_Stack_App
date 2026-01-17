from flask import request, jsonify
from config import app, db
from models import Contact

# TODO 2: Read: all contacts, single contact by id
@app.route('/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_dict(), contacts)) # Convert each contact to a dictionary: to_dict() is being provided in models.py
                                                            # Then convert the map to a list, then convert the list of dictionaries to JSON using jsonify.
    return jsonify({"contacts": json_contacts})

# @app.route('/contacts/<int:id>', methods=['GET'])
# def get_contact(id):
#     contact = Contact.query.get(id)
#     return jsonify(contact.to_dict())

# TODO 1: Create: name, surname, email, phone
@app.route('/create-contacts', methods=['POST'])
def create_contact():
    name = request.json.get('name')
    surname = request.json.get('surname')
    email = request.json.get('email')
    phone = request.json.get('phone')

    if not name or not surname or not email: # Basic validation to ensure required fields are provided
        return jsonify({"error": "Name, surname, and email are required fields."}), 400

    new_contact = Contact(
        name=name,
        surname=surname,
        email=email,
        phone=phone
    )
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
    #return jsonify(new_contact.to_dict()), 201. <-- Returning the created contact details may not be necessary.
    return jsonify({"message": "Contact created successfully!"}), 201

# TODO 3: Update: contact by id
@app.route('/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    contact = Contact.query.get(id)

    if not contact:
        return jsonify({"error": "Contact not found."}), 404
    
    data = request.json
    contact.name = data.get('name', contact.name)
    contact.surname = data.get('surname', contact.surname)
    contact.email = data.get('email', contact.email)
    contact.phone = data.get('phone', contact.phone)
    db.session.commit()
    #return jsonify(contact.to_dict()) <-- Returning the updated contact details may not be necessary.
    return jsonify({"message": "Contact updated successfully!"}), 200

# TODO 4: Delete: contact by id
@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    contact = Contact.query.get(id)
    
    if not contact:
        return jsonify({"error": "Contact not found."}), 404
    
    db.session.delete(contact)
    db.session.commit()
    return jsonify({"message": "Contact deleted successfully!"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)