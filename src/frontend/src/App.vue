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
    fetch('https://whyiwanttoworkatxstudios.com/api/number/')
      .then(response => response.json())
      .then(data => {
        this.number = data.value;
      })
      .catch(error => console.error(error));
  }
}
</script>
