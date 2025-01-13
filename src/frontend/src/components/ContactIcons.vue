<template>
  <div class="mt-8 mb-0 pb-0 flex justify-center space-x-6">
    <!-- LinkedIn -->
    <a href="https://www.linkedin.com/in/evan-bagwell-458396137/" target="_blank" 
       class="tooltip text-gray-400 hover:text-white text-2xl">
      <i class="fab fa-linkedin"></i>
      <span class="tooltip-text">Connect on LinkedIn</span>
    </a>

    <!-- Email -->
    <a href="mailto:evan@quantyle.io" 
       class="tooltip text-gray-400 hover:text-white text-2xl">
      <i class="fas fa-envelope"></i>
      <span class="tooltip-text">Send me an email</span>
    </a>

    <!-- Resume -->
    <a href="/Evan_Bagwell_Resume_2025.pdf" target="_blank" 
       class="tooltip text-gray-400 hover:text-white text-2xl">
      <i class="fas fa-file-alt"></i>
      <span class="tooltip-text">View my resume</span>
    </a>
  </div>
</template>

<script>
export default {
  name: 'ClosingSection'
}
</script>