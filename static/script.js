// Customisable Title Bar Functionality
function setSiteTitle(newTitle) {
    document.getElementById("siteTitle").textContent = newTitle;
}

// Example interactive behaviour
document.getElementById("ctaButton").addEventListener("click", () => {
    alert("Thanks for getting started!");
});

document.getElementById("contactButton").addEventListener("click", () => {
    alert("Contact form coming soon!");
});
