/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './*.html',
    './calculator/*.html',
    './articles/*.html',
  ],
  theme: {
    extend: {
      fontFamily: {
        display: ['Clash Display', 'sans-serif'],
        sans:    ['Satoshi', 'sans-serif'],
        mono:    ['JetBrains Mono', 'monospace'],
      },
      colors: {
        ink:     { DEFAULT: '#0d1117', 50: '#f5f7fa', 100: '#e8ecf2', 200: '#c9d2de', 300: '#9aaabb', 400: '#637b93', 500: '#3d5a72', 600: '#284560', 700: '#1a3249', 800: '#112338', 900: '#0d1117' },
        leaf:    { DEFAULT: '#16a34a', 50: '#f0fdf4', 100: '#dcfce7', 200: '#bbf7d0', 300: '#86efac', 400: '#4ade80', 500: '#22c55e', 600: '#16a34a', 700: '#15803d', 800: '#166534', 900: '#14532d' },
        saffron: { DEFAULT: '#ea580c', 50: '#fff7ed', 100: '#ffedd5', 200: '#fed7aa', 300: '#fdba74', 400: '#fb923c', 500: '#f97316', 600: '#ea580c', 700: '#c2410c' },
      },
    },
  },
  plugins: [],
}
