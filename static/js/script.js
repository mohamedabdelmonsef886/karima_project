(function () {
    // Animate Skill Bars
    window.addEventListener("load", function () {
        const fills = document.querySelectorAll(".skill-fill");
        fills.forEach(fill => {
            const percent = fill.dataset.percent;
            if (percent) {
                fill.style.width = percent + "%";
            }
        });
    });

    // Mobile Menu Toggle
    const toggleBtn = document.querySelector(".menu-toggle");
    const tLinks = document.querySelector(".nav-links");

    if (!toggleBtn || !tLinks) return; // Safety check

    toggleBtn.addEventListener("click", function (e) {
        e.stopPropagation();
        toggleBtn.classList.toggle("menu-active");
        tLinks.classList.toggle("open");
    });

    // Prevent closing when clicking inside the menu
    tLinks.addEventListener("click", function (e) {
        e.stopPropagation();
    });

    // Close menu when clicking outside
    document.addEventListener("click", function (e) {
        if (!toggleBtn.contains(e.target) && !tLinks.contains(e.target)) {
            toggleBtn.classList.remove("menu-active");
            tLinks.classList.remove("open");
        }
    });
})();