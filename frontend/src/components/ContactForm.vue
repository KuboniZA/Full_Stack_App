<script setup lang="ts">
import { ref } from 'vue';

const emittedEvent = defineEmits(['contact-updated']);

const name = ref('');
const surname = ref('');
const email = ref('');
const phone = ref('');

function handleSubmit() {
  // Handle form submission logic here
  console.log('Form submitted:', {
    name: name.value,
    surname: surname.value,
    email: email.value,
    phone: phone.value,
  });
  const newContact = {
    name: name.value,
    surname: surname.value,
    email: email.value,
    phone: phone.value,
  };
  // You can send newContact to your backend API here
  const apiUrl = editingContactId.value
    ? `http://127.0.0.1:5000/contacts/${editingContactId.value}`
    : 'http://127.0.0.1:5000/create-contacts';

    const requestOptions = {
    method: editingContactId.value ? 'PUT' : 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(newContact),
  };
  fetch(apiUrl, requestOptions)
    .then((response) => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then((data) => {
      console.log('Contact created successfully:', data);

      editingContactId.value = null; // Reset editing state after successful submission
      name.value = '';
      surname.value = '';
      email.value = '';
      phone.value = '';
      emittedEvent('contact-updated'); // Notify parent component to refresh contact list
      hideForm();
    })
    .catch((error) => {
      console.error('Error creating contact:', error);
    });
  // Reset form fields after submission
  const resetForm = () => {
    name.value = '';
    surname.value = '';
    email.value = '';
    phone.value = '';
  };
  resetForm();
  hideForm();
}

// Form visibility management
const formVisible = ref(false);
const modalVisible = ref(false);

const makeFormVisible = () => {
  formVisible.value = true;
  modalVisible.value = true;
};

const hideForm = () => {
  formVisible.value = false;
  modalVisible.value = false;
};

// Add editing functionality

const editingContactId = ref<number | null>(null);

const setContact = (contact: { id: number; name: string; surname: string; email: string; phone: number }) => {
  editingContactId.value = contact.id;

  name.value = contact.name;
  surname.value = contact.surname;
  email.value = contact.email;
  phone.value = String(contact.phone);
};

// Expose methods to parent component

defineExpose({
  makeFormVisible,
  hideForm,
  setContact
});
</script>

 <template>
   <div>
     <button class="add-contact-btn" @click="makeFormVisible">Add New Contact</button>
     <div class="modal-overlay" v-show="modalVisible"></div>
     <form @submit.prevent="handleSubmit" v-show="formVisible" class="form">
      <span @click="hideForm" class="hide-form-btn">&times;</span>
       <div>
         <label for="name">Name:</label>
         <input type="text" id="name" v-model="name" name="name" required placeholder="First Name" />
       </div>
       <div>
         <label for="surname">Surname:</label>
         <input class="surname-input" type="text" id="surname" v-model="surname"  name="surname" required placeholder="Last Name" />
       </div>
       <div>
         <label for="email">Email:</label>
         <input type="email" id="email" v-model="email" name="email" required placeholder="Email Address" />
       </div>
       <div>
         <label for="phone">Phone:</label>
         <input type="tel" id="phone" v-model="phone" name="phone" required placeholder="Phone Number" />
       </div>
       <button class="submit-btn" type="submit">Submit</button>
     </form>
   </div>
 </template>

 <style scoped>

   .form {
     display: flex;
     flex-direction: column;
     width: 300px;
     position: fixed;
     z-index: 2;
     top: 25%;
     left: 25%;
     width: 50%;
     height: auto;
     overflow: auto;
     background-color: #ddd;
     padding: 20px;
     border-radius: 15px;
     box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
   }
   .modal-overlay {
    /* Position it fixed relative to the browser window */
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.6); /* 60% opacity black */
    z-index: 1;
}


   div {
     margin-bottom: 10px;
   }

   label {
     margin-bottom: 5px;
   }

   input {
     padding: 8px;
     font-size: 14px;
     border-radius: 5px;
      border: none;
   }
   input:focus {
     outline: none;
     border: 2px solid #4CAF50;
   }

   .submit-btn {
     padding: 10px;
     font-size: 16px;
     background-color: #4CAF50;
     color: white;
     border: none;
     cursor: pointer;
     border-radius: 1000px;
     width: 100px;
     position: relative;
     left: 50%;
     transform: translateX(-50%);
   }

   .submit-btn:hover {
     background-color: #45a049;
   }

   .add-contact-btn {
     padding: 5px;
     font-size: 16px;
     border: none;
     cursor: pointer;
     border-radius: 25px;
   }
   .hide-form-btn {
     font-size: 28px;
     font-weight: bold;
     position: absolute;
     top: 10px;
     right: 20px;
     cursor: pointer;
   }
   .hide-form-btn:hover {
     color: red;
     cursor: pointer;
   }
   input {
     width: 80%;
     position: relative;
     left: 2.5rem;
   }
    .surname-input {
      position: relative;
      left: 1.4rem;
    }
 </style>
