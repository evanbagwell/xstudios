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
    fetch('http://127.0.0.1:8000/api/number/')
      .then(response => response.json())
      .then(data => {
        this.number = data.value;
      })
      .catch(error => console.error(error));
  }
}
</script>