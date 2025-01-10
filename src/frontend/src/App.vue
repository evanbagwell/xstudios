<template>
  <div class="bg-gray-900 text-white font-sans">
    <div class="container mx-auto px-4 py-10 pb-32">
      <!-- Flex container to align Header and Image/Button -->
      <div class="flex flex-col md:flex-row items-start justify-between">
        <!-- Header and About Me -->
        <div class="w-full md:w-2/3">
          <HeaderSection />
          <AboutMe />
        </div>

        <!-- Sudoku Puzzle: Fixed for Desktop + Centered on Mobile -->
        <!-- <div class="self-start md:-mt-8 md:ml-12 flex justify-center md:justify-start mt-4">
          <SudokuPuzzle />
        </div> -->
        <div class="self-start md:-mt-8 md:ml-12 md:mr-14 flex justify-center md:justify-start mt-4">
          <SudokuPuzzle />
        </div>

        <!-- Profile Image and CTA Button: Fixed for Desktop + Centered on Mobile -->
        <div class="w-full md:w-1/3 flex justify-center md:justify-start mt-4 md:mt-0">
          <ProfileCTA />
        </div>
      </div>

      <!-- How This Site Was Built -->
      <HowBuilt />

      <!-- Closing Section -->
      <ClosingSection />
      
      <!-- Contact Icons -->
      <ContactIcons />
    </div>

    <!-- Footer -->
    <AppFooter />
  </div>
</template>


<script>
import ContactIcons from './components/ContactIcons.vue';
import SudokuPuzzle from './components/SudokuPuzzle.vue';
import HeaderSection from './components/HeaderSection.vue'
import AboutMe from './components/AboutMe.vue'
import ProfileCTA from './components/ProfileCTA.vue'
import HowBuilt from './components/HowBuilt.vue'
import ClosingSection from './components/ClosingSection.vue'
import AppFooter from './components/AppFooter.vue'

export default {
  name: 'App',
  components: {
    ContactIcons,
    SudokuPuzzle,
    HeaderSection,
    AboutMe,
    ProfileCTA,
    HowBuilt,
    ClosingSection,
    AppFooter
  }
}
</script>
