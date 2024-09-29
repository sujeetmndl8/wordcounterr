function showSection(sectionId) {
    // Hide all sections first
    document.querySelectorAll('.section').forEach(section => {
        section.classList.add('hidden');
    });

    // Show the selected section
    document.getElementById(sectionId).classList.remove('hidden');
    
    // Scroll smoothly to the section
    document.getElementById(sectionId).scrollIntoView({
        behavior: 'smooth'
    });
}

function countWordsAndCharacters() {
    const text = document.getElementById('text-input').value;

    // Show loading ripple animation
    document.getElementById('loading-bar').style.display = 'block';

    // Simulate word counting process (replace this with actual backend API call)
    setTimeout(() => {
        const wordCount = text.trim().split(/\s+/).length;
        const charCount = text.length;

        // Hide loading ripple animation after the process
        document.getElementById('loading-bar').style.display = 'none';

        // Update the results
        document.getElementById('word-count').textContent = wordCount;
        document.getElementById('char-count').textContent = charCount;
    }, 3000);  // Simulate 3-second delay for loading
}