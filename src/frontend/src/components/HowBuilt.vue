<template>
    <div class="mt-16 bg-gray-800 p-6 rounded-lg shadow-md">
      <h2 class="text-2xl font-semibold">How this site was built</h2>
      <p class="mt-4 text-gray-400">
        This project showcases my backend development expertise. Built with Django for backend logic and Vue.js for the frontend, deployed with NGINX and Gunicorn.
      </p>
      <div class="mt-4 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        <div v-for="(category, index) in techStack" :key="index">
          <h3 class="font-semibold text-lg">{{ category.title }}</h3>
          <ul class="text-gray-400">
            <li v-for="(item, idx) in category.items" :key="idx">{{ item }}</li>
          </ul>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'HowBuilt',
    data() {
      return {
        techStack: [
          { title: 'Frontend', items: ['Vue.js', 'Tailwind CSS'] },
          { title: 'Backend', items: ['Python & Django', 'Gunicorn & NGINX'] },
          { title: 'Deployment', items: ['DigitalOcean Droplet'] }
        ]
      };
    }
  }
  </script>
  