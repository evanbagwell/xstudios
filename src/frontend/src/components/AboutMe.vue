<template>
    <div class="mt-6">
      <h2 class="text-2xl font-semibold mb-2">About Me</h2>
      <ul class="space-y-3">
        <li v-for="(item, index) in skills" :key="index" class="flex items-start">
          <span class="text-blue-400 mr-2">&#9679;</span>
          <div class="text-gray-400 break-words whitespace-normal overflow-visible text-clip">
            <strong>{{ item.title }}</strong>
            <p>{{ item.description }}</p>
          </div>
        </li>
      </ul>
    </div>
  </template>
  
  
  <script>
  export default {
    name: 'AboutMe',
    data() {
      return {
        skills: [
          {
            title: 'Backend Development Expertise',
            description: 'Over 4 years of experience building scalable systems using Python, Django, and PostgreSQL, with a strong focus on API integration and server deployment.'
          },
          {
            title: 'Full-Stack Project Deployment',
            description: 'End-to-end development and deployment of complex applications, integrating frontend frameworks like Vue and ReactJS with secure, high-performance backends.'
          },
          {
            title: 'Algorithmic Trading Systems',
            description: 'Designed and implemented complex custom trading algorithms, processed real-time market data, and optimized strategies through historical statistical analysis across diverse asset classes.'
          }
        ]
      };
    }
  }
  </script>
  