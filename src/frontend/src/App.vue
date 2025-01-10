<template>
  <div class="bg-gray-900 text-white font-sans">
    <div class="container mx-auto px-4 py-10">
      <!-- Flex container to align Header and Image/Button -->
      <div class="flex flex-col md:flex-row items-start justify-between">
        <!-- Header and About Me -->
        <div class="w-full md:w-2/3">
          <HeaderSection />
          <AboutMe />
        </div>

        <!-- Profile Image and CTA Button -->
        <div class="w-full md:w-1/3">
          <ProfileCTA />
        </div>
      </div>

      <!-- How This Site Was Built -->
      <HowBuilt />

      <!-- Closing Section -->
      <ClosingSection />
    </div>

    <!-- Footer -->
    <AppFooter />
  </div>
</template>

<script>
import HeaderSection from './components/HeaderSection.vue'
import AboutMe from './components/AboutMe.vue'
import ProfileCTA from './components/ProfileCTA.vue'
import HowBuilt from './components/HowBuilt.vue'
import ClosingSection from './components/ClosingSection.vue'
import AppFooter from './components/AppFooter.vue'

export default {
  name: 'App',
  components: {
    HeaderSection,
    AboutMe,
    ProfileCTA,
    HowBuilt,
    ClosingSection,
    AppFooter
  }
}
</script>
