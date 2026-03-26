// URBAN CRUISE JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Registration Form Close/Reopen Functionality
    const closeRegistrationBtn = document.getElementById('closeRegistrationBtn');
    const reopenRegistrationBtn = document.getElementById('reopenRegistrationBtn');
    const registrationSection = document.getElementById('registrationSection');
    const registrationFormBody = document.getElementById('registrationFormBody');

    // Close registration form
    if (closeRegistrationBtn) {
        closeRegistrationBtn.addEventListener('click', function() {
            registrationSection.style.display = 'none';
            reopenRegistrationBtn.style.display = 'inline-block';
            
            // Save preference to localStorage
            localStorage.setItem('registrationFormClosed', 'true');
        });
    }

    // Reopen registration form
    if (reopenRegistrationBtn) {
        reopenRegistrationBtn.addEventListener('click', function() {
            registrationSection.style.display = 'block';
            reopenRegistrationBtn.style.display = 'none';
            
            // Remove preference from localStorage
            localStorage.removeItem('registrationFormClosed');
            
            // Smooth scroll to registration section
            registrationSection.scrollIntoView({ behavior: 'smooth' });
        });
    }

    // Check if form was previously closed
    if (localStorage.getItem('registrationFormClosed') === 'true') {
        registrationSection.style.display = 'none';
        reopenRegistrationBtn.style.display = 'inline-block';
    }

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Navbar scroll effect
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            navbar.classList.add('navbar-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled');
        }
    });

    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Form validation enhancements
    const forms = document.querySelectorAll('.needs-validation');
    forms.forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });

    // Lazy loading for images
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver(function(entries, observer) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });

        document.querySelectorAll('img[data-src]').forEach(function(img) {
            imageObserver.observe(img);
        });
    }

    // Search functionality
    const searchInputs = document.querySelectorAll('[data-search]');
    searchInputs.forEach(function(input) {
        input.addEventListener('input', function() {
            const query = this.value.toLowerCase();
            const target = document.querySelector(this.dataset.search);
            const items = target.querySelectorAll('.searchable-item');
            
            items.forEach(function(item) {
                const text = item.textContent.toLowerCase();
                if (text.includes(query)) {
                    item.style.display = '';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });

    // Price range slider
    const priceRange = document.getElementById('priceRange');
    const priceValue = document.getElementById('priceValue');
    
    if (priceRange && priceValue) {
        priceRange.addEventListener('input', function() {
            priceValue.textContent = '$' + this.value;
        });
    }

    // Date picker initialization
    const datePickers = document.querySelectorAll('.date-picker');
    datePickers.forEach(function(picker) {
        picker.addEventListener('change', function() {
            const selectedDate = new Date(this.value);
            const today = new Date();
            
            if (selectedDate < today) {
                this.setCustomValidity('Please select a future date');
            } else {
                this.setCustomValidity('');
            }
        });
    });

    // Loading states for buttons
    const loadingButtons = document.querySelectorAll('[data-loading]');
    loadingButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const originalText = this.innerHTML;
            this.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>Loading...';
            this.disabled = true;
            
            // Simulate loading (remove this in production)
            setTimeout(function() {
                button.innerHTML = originalText;
                button.disabled = false;
            }, 2000);
        });
    });

    // Counter animation for stats
    function animateCounter(element, target, duration = 2000) {
        let start = 0;
        const increment = target / (duration / 16);
        
        function updateCounter() {
            start += increment;
            if (start < target) {
                element.textContent = Math.floor(start).toLocaleString();
                requestAnimationFrame(updateCounter);
            } else {
                element.textContent = target.toLocaleString();
            }
        }
        
        updateCounter();
    }

    // Trigger counter animation when stats come into view
    const stats = document.querySelectorAll('.stat-counter');
    if (stats.length > 0) {
        const statsObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    const target = parseInt(entry.target.dataset.target);
                    animateCounter(entry.target, target);
                    statsObserver.unobserve(entry.target);
                }
            });
        });

        stats.forEach(function(stat) {
            statsObserver.observe(stat);
        });
    }

    // Gallery lightbox
    const galleryImages = document.querySelectorAll('.gallery-image');
    galleryImages.forEach(function(img) {
        img.addEventListener('click', function() {
            const modal = document.createElement('div');
            modal.className = 'modal fade';
            modal.innerHTML = `
                <div class="modal-dialog modal-lg modal-dialog-centered">
                    <div class="modal-content">
                        <div class="modal-body p-0">
                            <img src="${this.src}" class="img-fluid" alt="${this.alt}">
                        </div>
                    </div>
                </div>
            `;
            
            document.body.appendChild(modal);
            const bsModal = new bootstrap.Modal(modal);
            bsModal.show();
            
            modal.addEventListener('hidden.bs.modal', function() {
                document.body.removeChild(modal);
            });
        });
    });

    // Print functionality
    const printButtons = document.querySelectorAll('[data-print]');
    printButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const target = this.dataset.print;
            const element = document.querySelector(target);
            
            if (element) {
                const printWindow = window.open('', '_blank');
                printWindow.document.write(`
                    <html>
                        <head>
                            <title>Print</title>
                            <style>
                                body { font-family: Arial, sans-serif; margin: 20px; }
                                img { max-width: 100%; height: auto; }
                                .no-print { display: none; }
                            </style>
                        </head>
                        <body>
                            ${element.innerHTML}
                        </body>
                    </html>
                `);
                printWindow.document.close();
                printWindow.print();
            }
        });
    });

    // Copy to clipboard functionality
    const copyButtons = document.querySelectorAll('[data-copy]');
    copyButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const text = this.dataset.copy;
            navigator.clipboard.writeText(text).then(function() {
                const originalTitle = button.getAttribute('title');
                button.setAttribute('title', 'Copied!');
                button.innerHTML = '<i class="fas fa-check"></i>';
                
                setTimeout(function() {
                    button.setAttribute('title', originalTitle);
                    button.innerHTML = '<i class="fas fa-copy"></i>';
                }, 2000);
            });
        });
    });

    // Back to top button
    const backToTopButton = document.getElementById('backToTop');
    if (backToTopButton) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 300) {
                backToTopButton.style.display = 'block';
            } else {
                backToTopButton.style.display = 'none';
            }
        });

        backToTopButton.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    console.log('URBAN CRUISE JavaScript initialized successfully!');
});

// Utility functions
function formatPrice(price) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(price);
}

function formatDate(date) {
    return new Intl.DateTimeFormat('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    }).format(new Date(date));
}

function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// API helpers
async function fetchWithErrorHandling(url, options = {}) {
    try {
        const response = await fetch(url, options);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error('Fetch error:', error);
        throw error;
    }
}

// Form validation helper
function validateForm(formElement) {
    const inputs = formElement.querySelectorAll('input, textarea, select');
    let isValid = true;
    
    inputs.forEach(function(input) {
        if (!input.checkValidity()) {
            isValid = false;
            input.classList.add('is-invalid');
        } else {
            input.classList.remove('is-invalid');
        }
    });
    
    return isValid;
}
