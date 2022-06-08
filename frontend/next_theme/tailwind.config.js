const color = require('tailwindcss/colors')

module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    screen:{
      'table':'640px',
      'laptop':'1024px',
      'desctop':"1280px"
    },
    spacing:{
      '0':'0px',
      '1':'4px',
      '2':'8px',
      '3':'16px',
      '4':'24px',
      'sm':'100px',
      'md':'200px',
      'lg':'300px',
      'xl':'400px'
    },  
    extend: {
    colors:{
      l1: '#264653',
      l2: '#2a9d8f',
      l3: '#e9c46a',
      l4: '#f4a261',
      l5: '#e76f51',
    },
    },
  },
  plugins: [
    require('tailwind-scrollbar'),
  ],
  variants: {
    scrollbar: ['dark']
}
}
