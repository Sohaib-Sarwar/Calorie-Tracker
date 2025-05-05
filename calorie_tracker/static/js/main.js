// Theme switcher
document.addEventListener('DOMContentLoaded', function() {
  // Check for saved theme preference or use preferred color scheme
  const currentTheme = localStorage.getItem('theme') || 
    (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  
  // Apply the theme
  if (currentTheme === 'dark') {
    document.documentElement.setAttribute('data-theme', 'dark');
    document.getElementById('theme-switch').checked = true;
  }
  
  // Handle theme switch changes
  const themeSwitch = document.getElementById('theme-switch');
  if (themeSwitch) {
    themeSwitch.addEventListener('change', function(e) {
      if (e.target.checked) {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
      } else {
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('theme', 'light');
      }
    });
  }
  
  // Add animation classes to elements on page load
  const animatedElements = document.querySelectorAll('.animate-on-load');
  animatedElements.forEach(element => {
    element.classList.add('fade-in');
  });
  
  // Add animation to cards when they become visible
  if ('IntersectionObserver' in window) {
    const cards = document.querySelectorAll('.card');
    const cardObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('slide-up');
          cardObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
    
    cards.forEach(card => {
      cardObserver.observe(card);
    });
  }
  
  // Initialize tooltips
  const tooltips = document.querySelectorAll('[data-toggle="tooltip"]');
  tooltips.forEach(tooltip => {
    new bootstrap.Tooltip(tooltip);
  });
  
  // Initialize popovers
  const popovers = document.querySelectorAll('[data-toggle="popover"]');
  popovers.forEach(popover => {
    new bootstrap.Popover(popover);
  });
  
  // Chart.js initialization for stats (if available)
  if (document.getElementById('calorieChart')) {
    initCalorieChart();
  }
});

// Initialize calorie chart
function initCalorieChart() {
  const ctx = document.getElementById('calorieChart').getContext('2d');
  
  // Extract data from the data attributes
  const chartLabels = JSON.parse(document.getElementById('calorieChart').dataset.labels);
  const chartData = JSON.parse(document.getElementById('calorieChart').dataset.values);
  
  const chart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: chartLabels,
      datasets: [{
        label: 'Calories Consumed',
        data: chartData,
        backgroundColor: 'rgba(76, 175, 80, 0.2)',
        borderColor: '#4CAF50',
        borderWidth: 2,
        pointBackgroundColor: '#388E3C',
        pointBorderColor: '#fff',
        pointHoverBackgroundColor: '#fff',
        pointHoverBorderColor: '#4CAF50',
        tension: 0.4
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          beginAtZero: true,
          grid: {
            color: 'rgba(0, 0, 0, 0.05)'
          }
        },
        x: {
          grid: {
            display: false
          }
        }
      },
      plugins: {
        legend: {
          display: true,
          position: 'top'
        },
        tooltip: {
          mode: 'index',
          intersect: false,
          backgroundColor: 'rgba(0, 0, 0, 0.7)'
        }
      },
      interaction: {
        mode: 'nearest',
        axis: 'x',
        intersect: false
      },
      animation: {
        duration: 1000,
        easing: 'easeInOutQuart'
      }
    }
  });
  
  // Update chart when theme changes
  document.getElementById('theme-switch').addEventListener('change', function() {
    updateChartTheme(chart);
  });
}

// Update chart theme based on current theme
function updateChartTheme(chart) {
  const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
  
  chart.options.scales.y.grid.color = isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.05)';
  chart.options.scales.y.ticks.color = isDark ? '#E0E0E0' : '#666';
  chart.options.scales.x.ticks.color = isDark ? '#E0E0E0' : '#666';
  chart.options.plugins.tooltip.backgroundColor = isDark ? 'rgba(30, 30, 30, 0.8)' : 'rgba(0, 0, 0, 0.7)';
  
  chart.update();
}
