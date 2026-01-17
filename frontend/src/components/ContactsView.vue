<script setup lang="ts">
  import { onMounted, ref } from 'vue';

  const contacts = ref<Array<{ id: number; name: string; email: string }>>([]);

  onMounted(async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/contacts');
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      console.log(data);
      contacts.value = data.map((user: any) => ({
        id: user.id,
        name: user.name,
        email: user.email,
      }));
    } catch (error) {
      console.error('Error fetching contacts:', error);
    }
  });
</script>

<template>
  <div>
    <h1>Contact List</h1>
    <ul>
      <li v-for="contact in contacts" :key="contact.id">
        <strong>{{ contact.name }}</strong> - {{ contact.email }}
      </li>
    </ul>
  </div>
</template>
