<template>
  <div class="flex flex-col items-end text-right">
    <!-- Profile Image -->
    <img src="/Evan_Bagwell_Business_Photo.jpeg" 
         alt="Evan Bagwell Avatar" 
         class="rounded-lg border-2 border-gray-700 w-64 md:w-72 h-auto object-cover mb-4">

    <!-- CTA Button -->
    <button @click="hireEvan" 
            :class="buttonClass"
            class="w-64 md:w-72 px-4 py-2 font-semibold rounded transition duration-300 text-white whitespace-nowrap">
      {{ buttonText }}
    </button>
  </div>
</template>

<script>
export default {
  name: 'ProfileCTA',
  data() {
    return {
      buttonText: 'Add Evan to Your Dev Team',
      buttonClass: 'bg-blue-600 hover:bg-blue-700'
    };
  },
  methods: {
    hireEvan() {
      this.buttonText = '✔️ Evan Added!';
      this.buttonClass = 'bg-green-600 hover:bg-green-700'; // FIXED: Button turns green
    }
  }
}
</script>
