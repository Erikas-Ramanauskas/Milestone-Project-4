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

  for (let ul of ulList) {
    const li = ul.querySelectorAll("li");
    const topPosition = 80; // procentage number for top position of drop down menu
    const windowHeight = window.innerHeight;
  
    const totalHeight = windowHeight - topPosition
    const totalNumberOfItems = Math.ceil(totalHeight / 40);
  
    const numberOfColumns = Math.ceil(li.length / totalNumberOfItems);
    ul.style.width = `${numberOfColumns * 200}px`;
  }
});
