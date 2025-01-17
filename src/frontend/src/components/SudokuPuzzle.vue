<template>
  <div class="mt-8 p-4 pr-8 bg-gray-800 text-white rounded-lg shadow-md flex flex-col items-center">
    <h2 class="text-2xl font-semibold mb-6 text-center">🧩 Play Sudoku!</h2>

    <div class="mb-4 flex space-x-4">
  <button @click="fetchPuzzle('easy')" class="px-4 py-2 bg-green-500 hover:bg-green-600 text-white rounded">
    Easy
  </button>
  <button @click="fetchPuzzle('medium')" class="px-4 py-2 bg-yellow-500 hover:bg-yellow-600 text-white rounded">
    Medium
  </button>
  <button @click="fetchPuzzle('hard')" class="px-4 py-2 bg-red-500 hover:bg-red-600 text-white rounded">
    Hard
  </button>
</div>

    <div class="grid grid-cols-9 gap-0 justify-center">
      <input
        v-for="(cell, index) in puzzle"
        :key="index"
        :value="cell === 0 ? '' : cell"
        :readonly="originalPuzzle[index] !== 0"
        @input="updateCell(index, $event.target.value)"
        :class="[
          originalPuzzle[index] !== 0 ? 'prefilled' : 'user-input',
          'cell',
          getBorderClass(index)
        ]"
      />
    </div>

    <button @click="validatePuzzle" class="mt-6 px-6 py-2 bg-blue-600 hover:bg-blue-700 rounded text-white">
      ✅ Check Solution
    </button>

    <p v-if="result !== null" :class="result ? 'text-green-400' : 'text-red-400'">
      {{ result ? 'Correct! 🎉' : 'Incorrect. Try Again! ❌' }}
    </p>
  </div>
</template>

<script>
export default {
  name: 'SudokuPuzzle',
  data() {
    return {
      puzzle: Array(81).fill(0),
      originalPuzzle: Array(81).fill(0),
      result: null
    };
  },
  mounted() {
    this.fetchPuzzle();
  },
  methods: {
    fetchPuzzle(difficulty = 'medium') {
  const baseUrl = window.location.hostname === 'localhost'
    ? 'http://localhost:8080'
    : 'https://whyiwanttoworkatxstudios.com';

  fetch(`${baseUrl}/api/sudoku/generate/?difficulty=${difficulty}`)
    .then(response => response.json())
    .then(data => {
      this.puzzle = data.puzzle.flat();
      this.originalPuzzle = [...this.puzzle];
      this.result = null;  // Reset result when a new puzzle is loaded
    })
    .catch(error => {
      console.error("Failed to fetch puzzle:", error);
    });
},
    updateCell(index, value) {
      if (this.originalPuzzle[index] === 0) {
        this.puzzle.splice(index, 1, parseInt(value) || 0);
      }
    },
    validatePuzzle() {
      const baseUrl = window.location.hostname === 'localhost'
        ? 'http://localhost:8080'
        : 'https://whyiwanttoworkatxstudios.com';

      fetch(`${baseUrl}/api/sudoku/validate/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ solution: this.chunkArray(this.puzzle, 9) })
      })
        .then(response => response.json())
        .then(data => {
          this.result = data.valid;
        })
        .catch(error => {
          console.error("Failed to validate puzzle:", error);
        });
    },
    chunkArray(arr, size) {
      return Array.from({ length: size }, (_, i) => arr.slice(i * size, i * size + size));
    },
    getBorderClass(index) {
      const row = Math.floor(index / 9);
      const col = index % 9;
      return {
        'border-top-bold': row % 3 === 0 && row !== 0,
        'border-left-bold': col % 3 === 0 && col !== 0
      };
    }
  }
}
</script>

<style scoped>
/* General cell styling */
.cell {
  width: 40px;
  height: 40px;
  text-align: center;
  font-size: 18px;
  border: 1px solid #555;
  margin: 0;
}

/* Pre-filled numbers */
.prefilled {
  background-color: #333;
  color: white;
  font-weight: bold;
}

/* User input numbers */
.user-input {
  background-color: #444;
  color: #00ff00;
}

.border-top-bold {
  border-top: 3px solid #ffffff !important;
}

.border-left-bold {
  border-left: 3px solid #ffffff !important;
}

/* Ensure the grid has complete borders on the right and bottom edges */
.border-right-bold {
  border-right: 3px solid #ffffff !important;
}

.border-bottom-bold {
  border-bottom: 3px solid #ffffff !important;
}

/* Adjust the right padding only */
.mt-8 {
  padding-right: 1.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.cell {
  width: 100%;                 /* Full width of the grid column */
  aspect-ratio: 1 / 1;         /* Forces the height to match the width */
  text-align: center;
  font-size: 18px;
  font-weight: bold;
  border: 1px solid #555;
  box-sizing: border-box;      /* Includes border in width/height */
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
  margin: 0;
}
</style>
