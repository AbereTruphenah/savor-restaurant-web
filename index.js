document.addEventListener('DOMContentLoaded', () => {
    const slideshowContainer = document.querySelector('.slideshow');
    const slides = slideshowContainer.querySelectorAll('.slide'); // Select all elements with the 'slide' class
    let currentSlideIndex = 0;
    const slideInterval = 3000;

    function showSlide(index) {
        // Hide all slides
        slides.forEach((slide) => {
            slide.classList.remove('opacity-100');
            slide.classList.add('opacity-0');
        });

        // Show the current slide
        slides[index].classList.remove('opacity-0');
        slides[index].classList.add('opacity-100');
    }

    function nextSlide() {
        currentSlideIndex = (currentSlideIndex + 1) % slides.length;
        showSlide(currentSlideIndex);
    }

    // Start the automatic slideshow
    setInterval(nextSlide, slideInterval);
});