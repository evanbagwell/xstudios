<template>
    <footer class="bg-gray-900 text-gray-400 py-4 shadow-inner">
      <div class="container mx-auto text-center">
        <p>&copy; {{ currentYear }} Evan Bagwell. All rights reserved.</p>
        <p>Designed and developed by Evan Bagwell.</p>
      </div>
    </footer>
  </template>
  
  <script>
  export default {
    name: 'AppFooter',
    data() {
      return {
        currentYear: new Date().getFullYear()
      };
    }
  }
  </script>
  