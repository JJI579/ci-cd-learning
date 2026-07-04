<script setup lang="ts">
import { onMounted, ref } from 'vue';


const text = ref("Waiting...");
async function fetchName() {
  const resp = await fetch("http://localhost:8000")
  text.value = (await resp.json()).text
}

onMounted(() => {
  fetchName()
})

</script>

<template>
  
  <div class="center">
    <h1>Who do you want to say hello to!</h1>
    <p>
      {{ text }}
    </p>
    <button @click="fetchName">New person!</button>
  </div>
  
</template>

<style scoped>

</style>
