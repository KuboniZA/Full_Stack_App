<script setup lang="ts">
import { ref } from 'vue';

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
  const apiUrl = 'http://127.0.0.1:5000/create-contacts';
  const requestOptions = {
    method: 'POST',
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
}

const formVisible = ref(false);

const toggleFormVisible = () => {
  formVisible.value = !formVisible.value;
};

</script>

 <template>
   <div>
     <button class="add-contact-btn" @click="toggleFormVisible"><h2>Add Contact</h2></button>
     <form @submit.prevent="handleSubmit" v-show="formVisible">
       <div>
         <label for="name">Name:</label>
         <input type="text" id="name" v-model="name" name="name" required />
       </div>
       <div>
         <label for="surname">Surname:</label>
         <input type="text" id="surname" v-model="surname"  name="surname" required />
       </div>
       <div>
         <label for="email">Email:</label>
         <input type="email" id="email" v-model="email" name="email" required />
       </div>
       <div>
         <label for="phone">Phone:</label>
         <input type="tel" id="phone" v-model="phone" name="phone" required />
       </div>
       <button class="submit-btn" type="submit">Submit</button>
     </form>
   </div>
 </template>

 <style scoped>
   form {
     display: flex;
     flex-direction: column;
     width: 300px;
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
   }

   .submit-btn {
     padding: 10px;
     font-size: 16px;
     background-color: #4CAF50;
     color: white;
     border: none;
     cursor: pointer;
     border-radius: 1000px;
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
 </style>
