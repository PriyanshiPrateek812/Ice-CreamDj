document.addEventListener("DOMContentLoaded", function () {
    let currentSlide = 0;
    const slides = document.querySelectorAll(".quiz-slide");
    const circles = document.querySelectorAll(".circle");
    const submitButton = document.querySelector(".submit-btn");
    const form = document.getElementById("quiz-form");

    // Show the current slide
    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.classList.toggle("active", i === index);
        });
        circles.forEach((circle, i) => {
            circle.classList.toggle("active", i === index);
        });
        // Show submit button only on the last slide
        submitButton.style.display = index === slides.length - 1 ? "block" : "none";
    }

    // Go to a specific slide
    function goToSlide(index) {
        currentSlide = index;
        showSlide(currentSlide);
    }

    // Add event listeners for options
    document.querySelectorAll(".option").forEach((option) => {
        option.addEventListener("click", function () {
            const value = this.dataset.value;
            const questionIndex = Array.from(slides).findIndex(slide => slide.contains(this));
            document.getElementById(`q${questionIndex + 1}`).value = value;
            if (currentSlide < slides.length - 1) {
                goToSlide(currentSlide + 1);
            } else {
                submitButton.style.display = "block"; // Show submit button on the last question
            }
        });
    });

    // Submit the quiz
    function submitQuiz() {
        if (form.checkValidity()) {
            form.submit();
        } else {
            alert("Please answer all questions before submitting!");
        }
    }

    // Initialize
    showSlide(currentSlide);
    window.goToSlide = goToSlide;
    window.submitQuiz = submitQuiz;
});
