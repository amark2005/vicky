document.addEventListener('DOMContentLoaded', () => {
    const btn = document.getElementById('cta-btn');
    
    btn.addEventListener('click', () => {
        const projectSection = document.getElementById('projects');
        projectSection.scrollIntoView({ behavior: 'smooth' });
    });

    console.log("Portfolio loaded successfully.");
});