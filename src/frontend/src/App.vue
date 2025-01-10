<template>
  <div>
    <h1>Number from Django: {{ number }}</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
      number: null
    }
  },
  mounted() {
  const baseUrl = window.location.hostname === 'localhost'
    ? 'http://localhost:8080'
    : 'https://whyiwanttoworkatxstudios.com';

  fetch(`${baseUrl}/api/number/`)
    .then(response => response.json())
    .then(data => {
      this.number = data.value;
    })
    .catch(error => console.error(error));
}
}
</script>
