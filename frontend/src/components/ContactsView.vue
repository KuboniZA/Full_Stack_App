<script setup lang="ts">
  import ContactForm from './ContactForm.vue';
  import { onMounted, ref } from 'vue';

  const contactForm = ref<InstanceType<typeof ContactForm> | null>(null);
  const contacts = ref<Array<{ id: number; name: string; surname: string; email: string; phone: number }>>([]);

  onMounted(async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/contacts');
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      console.log(data);
      contacts.value = data.contacts; // Adjust according to your API response structure and ensure 'contacts' key exists
    } catch (error) {
      console.error('Error fetching contacts:', error);
    }
  });

  const deleteContact = async (id: number) => {
    const confirmDelete = confirm('Are you sure you want to delete this contact?');
    if (!confirmDelete) return;

    try {
      const response = await fetch(`http://127.0.0.1:5000/contacts/${id}`, {
        method: 'DELETE',
      });
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      // Remove the deleted contact from the local state
      contacts.value = contacts.value.filter(contact => contact.id !== id);
    } catch (error) {
      console.error('Error deleting contact:', error);
    }
  };

  const editContact = (contact: { id: number; name: string; surname: string; email: string; phone: number }) => {
    contactForm.value?.setContact(contact);
    contactForm.value?.makeFormVisible();
  };
</script>

<template>
  <div>
    <ContactForm ref="contactForm" />
    <h1>Contact List</h1>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Surname</th>
          <th>Phone</th>
          <th>Email</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="contact in contacts" :key="contact.id">
          <td>{{ contact.name }}</td>
          <td>{{ contact.surname }}</td>
          <td>{{ contact.phone }}</td>
          <td>{{ contact.email }}</td>
          <td>
            <button @click="editContact(contact)">Edit</button>
            <button @click="deleteContact(contact.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
  table {
    width: 95%;
    border-collapse: collapse;
    position: relative;
    left: 2.5%;
  }

  th, td {
    border: 1px solid #ddd;
    padding: 8px;
  }

  th {
    background-color: #f2f2f2;
    text-align: left;
  }

  button {
    margin-right: 5px;
  }
</style>
