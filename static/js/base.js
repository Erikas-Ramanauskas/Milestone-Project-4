// Wait for the document to be ready
document.addEventListener("DOMContentLoaded", function () {
  // Get all elements with class 'toast'
  const toastElements = document.querySelectorAll(".toast");

  // Initialize Bootstrap Toast for each element
  toastElements.forEach(function (toastElement) {
    const bootstrapToast = new bootstrap.Toast(toastElement);
    bootstrapToast.show();
  });

  // Eddit meniu
  const ulList = document.querySelectorAll(".product-list ul");
  const windowHeight = window.innerHeight;

  for (let ul of ulList) {
    const li = ul.querySelectorAll("li");

    const numberOfColumns = Math.ceil(li.length / 16);
    ul.style.width = `${numberOfColumns * 200}px`;
  }
});
